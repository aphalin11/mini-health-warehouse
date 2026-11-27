from dataclasses import dataclass 
import pandas as pd 

@dataclass 
class Config: 
    n_members: int = 2000 # total members in demo roster 
