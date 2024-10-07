import graphene

# Define a Query class that will contain your "Hello World" resolver
class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="World"))

    # Resolver method for the 'hello' field
    def resolve_hello(self, info, name):
        return f'Hello, {name}!'

# Define a schema
schema = graphene.Schema(query=Query)

# Execute the query
query_string = '{ hello(name: "Ghulam") }'
result = schema.execute(query_string)

# Print the result
print(result.data['hello'])
