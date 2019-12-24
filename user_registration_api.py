from flask import Flask
from flask import jsonify, request, url_for, abort, g
from flask_httpauth import HTTPBasicAuth
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from user_model import Base, User, Bagel

auth = HTTPBasicAuth()

engine = create_engine('sqlite:///bagelShop.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@auth.verify_password
def verify_password(username, password):
    print("Looking for user %s" % username)
    user = session.query(User).filter_by(username=username).first()
    if not user:
        print("User not found")
        return False
    elif not user.verify_password(password):
        print("Unable to verify password")
        return False
    else:
        g.user = user
        return True


@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        print("missing arguments")
        abort(400)
    user = session.query(User).filter_by(username=username).first()
    if user is not None:
        print("existing user")
        return jsonify({'message': 'user already exists'}), 200

    user = User(username=username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return jsonify(
        {'username': user.username}), 201  # , {'Location': url_for('get_user', id=user.id, _external=True)}


@app.route('/readHello')
def getRequestHello():
    return "Hi, I got your GET Request!"


@app.route('/api/users/<int:id>')
def get_user(id):
    user = session.query(User).filter_by(id=id).one()
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@app.route('/api/resource')
@auth.login_required
def get_resource():
    return jsonify({'data', 'Hello, %s!' % g.user.username})


@app.route('/bagels', methods=['GET', 'POST'])
@auth.login_required
def showAllBagels():
    if request.method == 'GET':
        bagels = session.query(Bagel).all()
        return jsonify(bagels=[bagel.serialize for bagel in bagels])
    elif request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        picture = request.json.get('picture')
        price = request.json.get('price')
        newBagel = Bagel(name=name, description=description, picture=picture, price=price)
        session.add(newBagel)
        session.commit()
        return jsonify(newBagel.serialize)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# Create a user
# curl -i -X POST -H "Content-Type: application/json" -d '{"username":"Lorenzo", "password":"Udacity"}'
# http://localhost:5000/api/users

# Test resource without login
# curl -u Lorenzo:Yoodac//localhost:5000/api/resource
