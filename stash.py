
def get_login_url():
    result = \
        "https://oauth.vk.com/authorize?" \
        "client_id={appid}&" \
        "display=page&" \
        "redirect_uri={redirect_uri}&" \
        "scope={scopes}&" \
        "response_type=token&" \
        "v=5.37".format(
            appid="5005266",
            redirect_uri="https://oauth.vk.com/blank.html",
            scopes="messages,friends,offline,audio,wall")
    print(result)
    exit(1)

get_login_url()

#def longpoll_test():
#    lp_data = vkapi.messages.getLongPollServer()
#    lp = LongPollManager(lp_data)
#    updates = lp.connect()
#   for upd in updates:
#        print(upd[0])
