import vk_api
import time
if __name__=="__main__":
    with open("token.txt", 'r') as f:
    # read token
        vk_session = vk_api.VkApi(token=f.read())
    
    vk = vk_session.get_api()
    msg = """Репетитор по математике и информатике
- ОГЭ\ЕГЭ Математика
- ОГЭ\ЕГЭ Информатика
- Повторение и изучение школьного материала, а так же выполнение домашнего задания.
- Выполнение лабораторных работ, контрольных работ, Excel и Word.
- Написание программ на Java  Python.
К каждому ученику индивидуальный подход, который будет завлекать его к учебе и давать качественный результат
Занятия онлайн. По всем вопросам обращаться в лс и по тел. +79787283681 (Viber, WhatsApp)"""
    myId = vk.users.get()[0]['id']
    
    # group_ids - short name
    # Example: https://vk.com/repetitorovnet
    group_ids = ["repetitorovnet", "club12150271", "repetitorysimferopol", "my.tutors", "home_tutor", "my.tutor", "club153005273", "tvoyprepod", "repetitor_moscow_77", "club23026278", "repetitory_rus"]
    groupsId_to_send = []

    # Create array of groups to send post to
    for ids in group_ids:
        groupsId_to_send.append(vk.groups.getById(group_id=ids)[0]['id'])
    
    # find photo id to send, where the first photo in the list is the last you added to your albums
    # for photoes in vk.photos.getAll(owner_id=myId)['items']:
        # print("id:", photoes['id'], "url:", photoes['sizes'][0]['url'])
    photoesId_to_send = ["457241095"]

    # send post
    for groups in groupsId_to_send:
        try:
            vk.wall.post(owner_id=groups*-1, message=msg, attachments="photo"+str(myId)+"_"+str(photoesId_to_send[0]))
            time.sleep(0.5)
        except e:
            print(e)