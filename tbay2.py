from tbay import User, Item, Bid, session

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
session.add(beyonce)
session.commit()

jayz = User()
jayz.username = "jayznyc"
jayz.password = "hovahova"
session.add(jayz)
session.commit()

headphones = Item()
headphones.name = "redbeats"
headphones.description = "Beats by Dre, Noise Cancelling"
session.add(headphones)
session.commit()

highheels = Item()
highheels.name = "stilettos"
highheels.description = "Lemonade Stilettos"
session.add(highheels)
session.commit()

session.query(User).all()