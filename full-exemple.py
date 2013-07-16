from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.superadmin import Admin
from flask.ext.mongorest import MongoRest
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods

from mongoengine import (
    Document, EmbeddedDocument, EmbeddedDocumentField,
    StringField, ListField, EmailField)

class Author(EmbeddedDocument):
    name = StringField(required=True, max_length=160)
    email = EmailField()

class Comment(EmbeddedDocument):
    name = StringField(max_length=60)
    comment = StringField(required=True)

class Blog(Document):
    titre = StringField(required=True, max_length=60)
    tags = ListField(StringField(max_length=30))
    auteur = EmbeddedDocumentField(Author)
    comments = ListField(EmbeddedDocumentField(Comment))

class BlogResource(Resource):
    document = Blog

app = Flask("Presentation Python")

app.config['MONGODB_SETTINGS'] = {'DB': 'presentation_python'}
app.config['SECRET_KEY'] = "12345"
db = MongoEngine(app)

admin = Admin(app)
admin.register(Blog)


@api.register(name='blogs', url='/blog/')
class BlogView(ResourceView):
    resource = PostResource
    methods = [methods.Create, methods.Update, methods.Fetch, methods.List]

if __name__ == "__main__":
    app.run()
