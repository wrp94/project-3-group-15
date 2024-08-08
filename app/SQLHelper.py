from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import pandas as pd
import numpy as np


# The Purpose of this Class is to separate out any Database logic
class SQLHelper():
    #################################################
    # Database Setup
    #################################################

    # define properties
    def __init__(self):
        self.engine = create_engine("sqlite:///app/onlinefoods.sqlite")
        self.Base = None

        # automap Base classes
        self.init_base()

    def init_base(self):
        # reflect an existing database into a new model
        self.Base = automap_base()
        # reflect the tables
        self.Base.prepare(autoload_with=self.engine)

    #################################################
    # Database Queries
    #################################################

    def get_bar(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        educational_bar_data = session.query(
            OnlineFoods.educational_qualifications,
            func.count(OnlineFoods.educational_qualifications)).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).group_by(
            OnlineFoods.educational_qualifications).all()

        session.close()

        return {education_level: count for education_level, count in educational_bar_data}

    def get_donut(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        occupation_donut_data = session.query(
            OnlineFoods.occupation,
            func.count(OnlineFoods.occupation)).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).group_by(
            OnlineFoods.occupation).all()

        session.close()

        return {occupation: count for occupation, count in occupation_donut_data}

    def get_violin(self, gender, marital_status):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        violin_data = session.query(
            OnlineFoods.age,
            func.count(OnlineFoods.age)).filter(
            OnlineFoods.gender == gender,
            OnlineFoods.marital_status == marital_status).group_by(
                OnlineFoods.age).all()

        session.close()

        return {age: count for age, count in violin_data}

    def get_dashboard(self, gender, marital_status):
        data = [self.get_bar(gender, marital_status),
                self.get_donut(gender, marital_status),
                self.get_violin(gender, marital_status)]

        return data

    def get_map(self, occupation):

        OnlineFoods = self.Base.classes.onlinefoods

        session = Session(bind=self.engine)

        map_data = session.query(
            OnlineFoods.latitude, 
            OnlineFoods.longitude,
            OnlineFoods.educational_qualifications).\
            filter(OnlineFoods.occupation == occupation).all()

        session.close()

        data = []

        for i in range(len(map_data)): 
            row = map_data[i]

            latitude = row[0]
            longitude = row[1]
            education = row[2]

            data.append(
                {
                    "latitude": latitude,
                    "longitude": longitude,
                    "education": education
                }
            )

        return data
