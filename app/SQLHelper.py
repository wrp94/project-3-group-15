from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

import pandas as pd


# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///onlinefoods.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    # COMMENT BACK IN IF USING THE ORM

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def get_educational_bar(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        educational_bar_data = session.query(
            OnlineFoods.educational_qualifications).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).all()

        session.close()

        df = pd.DataFrame(educational_bar_data)

        return df.to_dict()

    def get_employment_donut(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        occupation_donut_data = session.query(OnlineFoods.occupation).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).all()

        session.close()

        df = pd.DataFrame(occupation_donut_data)

        return df.to_dict()

    def get_violin(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        violin_data = session.query(OnlineFoods.age).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).all()

        session.close()

        df = pd.DataFrame(violin_data)

        return df.to_dict()

    def get_map(self, occupation):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        map_data = session.query(OnlineFoods.latitude, OnlineFoods.longitude).\
            filter(OnlineFoods.occupation == occupation).all()

        session.close()

        df = pd.DataFrame(map_data)

        return df.to_dict()
