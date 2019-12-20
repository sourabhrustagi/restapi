from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppy_model import Base, Puppy

app = Flask(__name__)

engine = create_engine('sqlite:///puppies.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/readHello')
def getRequestHello():
    return "Hi, I got your GET Request!"


@app.route('/createHello', methods=['post'])
def postRequestHello():
    return "I see you sent a POST message :-)"


@app.route('/updateHello', methods=['PUT'])
def updateRequestHello():
    return "Sending Hello on an PUT request!"


@app.route('/deleteHello', methods=['DELETE'])
def deleteRequestHello():
    return "Deleting your hard drive..... haha just kidding! I received a DELETE request!"


@app.route('/testJson')
def testJson():
    return jsonify(username="admin", email="sourabhrustagi1@gmail.com", id="1")


@app.route('/')
def entryPoint():
    return "Welcome to rest api"


@app.route("/")
@app.route('/puppies', methods=['GET', 'POST'])
def puppiesFunction():
    if request.method == 'GET':
        return getAllPuppies()
    elif request.method == 'POST':
        print("Making a New puppy")
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        print(name)
        print(description)
        return makeANewPuppy(name, description)


@app.route('/puppiesdemo', methods=['POST'])
def puppiesDemoFunction():
    if request.method == 'POST':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        print(name)
        print(description)
        return jsonify(name=name, description=description)


# Make another app.route() decorator here that takes in an integer named 'id' for when the client visits a URI like
# "/puppies/5"
@app.route('/puppies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def puppiesFunctionId(id):
    if request.method == 'GET':
        return getPuppy(id)
    if request.method == 'PUT':
        name = request.args.get('name', '')
        description = request.args.get('description', '')
        return updatePuppy(id, name, description)
    elif request.method == 'DELETE':
        return deletePuppy(id)


def makeANewPuppy(name, description):
    puppy = Puppy(name=name, description=description)
    session.add(puppy)
    session.commit()
    return jsonify(Puppy=puppy.serialize)


def getAllPuppies():
    return "Getting All the puppies!"


def getPuppy(id):
    puppy = session.query(Puppy).filter_by(id=id).one()
    return jsonify(puppy=puppy.serialize)


def updatePuppy(id, name, description):
    puppy = session.query(Puppy).filter_by(id=id).one()
    if not name:
        puppy.name = name
    if not description:
        puppy.description = description
    session.add(puppy)
    session.commit()
    return "Updated a Puppy with id %s" % id


def deletePuppy(id):
    puppy = session.query(Puppy).filter_by(id=id).one()
    session.delete(puppy)
    session.commit()
    return "Removed Puppy with id %s" % id


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# Try Running
# http://0.0.0.0:5000/readHello
