from user import User
from settings import write_session, read_session


read_session = read_session()
users = read_session.query(User).all()

write_session = write_session()
for user in users:
    new_user = User()
    new_user.name = user.name
    write_session.add(new_user)
write_session.commit()
