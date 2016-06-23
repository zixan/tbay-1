from tbay import User, Item, Bid, session

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "crazyinlove"

sylvester = User()
sylvester.username = "sylvester"
sylvester.password = "meow453"

jayz = User()
jane.username = "jayznyc"
jane.password = "hovahova"

Base.metadata.create_all(engine)

session.add_all([beyonce, sylvester, jayz])
session.commit()

baseball = Item()
headphones.name = "baseball"
headphones.description = "Who wants to play ball? Get your baseball here!"
session.add(baseball)
session.commit()
