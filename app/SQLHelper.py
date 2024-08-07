import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, func

import pandas as pd
import numpy as np


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

    def get_bar(self, min_attempts, region):

        return None

    def get_pie(self, min_attempts, region):

        return None

    def get_table(self, min_attempts, region):

        return None

    def get_map(self, min_attempts, region):

        return None
