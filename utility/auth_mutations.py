import graphene
import graphql_jwt


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()
    delete_token_cookie = graphql_jwt.relay.DeleteJSONWebTokenCookie.Field()

    # Long running refresh tokens
    revoke_token = graphql_jwt.relay.Revoke.Field()

    delete_refresh_token_cookie = \
        graphql_jwt.relay.DeleteRefreshTokenCookie.Field()
