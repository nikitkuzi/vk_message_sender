import vk_api
if __name__=="__main__":
    # logpass
    vk_session = vk_api.VkApi("+79780000000", "pass")
    vk_session.auth()
    
    vk = vk_session.get_api()
    msg = """message"""
    myId = vk.users.get()[0]['id']
    
    # group_id - short name
    # Example: https://vk.com/repetitorysimferopolya
    groupsId_to_send = [
        vk.groups.getById(group_id="repetitorysimferopolya")[0]['id'],
        vk.groups.getById(group_id="repetitorsimf")[0]['id'],
        vk.groups.getById(group_id="repetitorysimferopol")[0]['id']
    ]
    
    # find your photo id
    # where the first photo in the list
    # is the last you added to your albums

    # for photoes in vk.photos.getAll(owner_id=myId)['items']:
        # print("id:", photoes['id'], "url:", photoes['sizes'][0]['url'])
    photoesId_to_send = [
        "457241095"
    ]

    for groups in groupsId_to_send:
        vk.wall.post(owner_id=groups*-1, message=msg, attachments="photo"+str(myId)+"_"+str(photoesId_to_send[0]))


