import graphene
from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)
class Book(graphene.ObjectType):
    title = graphene.String()
    author = graphene.String()

class Query(graphene.ObjectType):
    book = graphene.Field(Book)
    books = graphene.List(Book)

    def resolve_book(self, info):
        return Book(title="Hello World", author="Me")
    
    def resolve_books(self, info):
        return [
            Book(title="The Author of the Rings", author="J.R.R. Tolkien"),
            Book(title="The Catcher in the Rye", author="J.D. Salinger"),
            Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
        ]
    
schema = graphene.Schema(query=Query)

q = '''
{
    book {
        title
        author
    }
} 
'''

#     "result = schema.execute(q)\n",
#     "print(result.data)"

# results = schema.execute(q)
# print(results.data)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
