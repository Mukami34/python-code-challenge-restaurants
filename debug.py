#!/usr/bin/env python3
import random
import ipdb;

from lib.models import Review, Restaurant, Customer
from lib.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



if __name__ == '__main__':

    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    Base.metadata.create_all(engine)

    
    # Create instances of Restaurant, Customer, and Review
    restaurant1 = Restaurant(name="Restaurant 1", price=2)
    restaurant2 = Restaurant(name="Restaurant 2", price=3)

    customer1 = Customer(first_name="John", last_name="Doe")
    customer2 = Customer(first_name="Jane", last_name="Smith")

    # Create reviews
    review1 = Review(customer=customer1, restaurant=restaurant1, star_rating=4)
    review2 = Review(customer=customer1, restaurant=restaurant2, star_rating=5)
    review3 = Review(customer=customer2, restaurant=restaurant1, star_rating=3)

    # Add the instances to the session and commit to the database
    session.add(restaurant1)
    session.add(restaurant2)
    session.add(customer1)
    session.add(customer2)
    session.add(review1)
    session.add(review2)
    session.add(review3)
    session.commit()


    ipdb.set_trace()
