import imp
import graphene
import graphql_jwt
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery


class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    verify_token = graphql_jwt.Verify.Field(),
    refresh_token = graphql_jwt.Refresh.Field()
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()


class Mutation(AuthMutation, graphene.ObjectType):
    pass


class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
