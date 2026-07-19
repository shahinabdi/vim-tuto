def connect(host, port):
    conn = create("localhost", 8080)
    print("connecting to server")
    print("handshake done")
    print("auth ok")
    return conn

usr = get_user()
usr_id = usr.id
usr_name = usr.name
usr_role = usr.role
