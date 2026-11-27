
import numpy as np
import pandas as pd
import string 
from config import Config #removed leading '.' for package relative issue

# seed 
rng = np.random.default_rng(42)  

# simplified MBIs based on uppercase alphabet (excluding S, L, O, B, I, Z for similarity to other numerics)
# and all numerics, but cannot start with zero - total of 11 characters - 4, 7, 10, and 11th space is numeric only
numerics_list = list("ACDEFGHJKMNPQRTUVWXY") 
alpha_list = list(string.digits)
both_list = numerics_list + alpha_list 
id_strings_pools = [list("123456789"),
                     alpha_list, 
                     both_list, 
                     numerics_list, 
                     alpha_list, 
                     both_list, 
                     numerics_list, 
                     alpha_list, 
                     alpha_list, 
                     numerics_list, 
                     numerics_list] 

# test random MBI 
rand = "".join(str([rng.choice(p) for p in id_strings_pools])) 
print(rand)

# create a new mbi randomly, only incldue if not in list already 
mbi_list = [] 
def new_mbi(): 
    for i in range(10): #Config.n_members
        rand = "".join(str([rng.choice(p) for p in id_strings_pools]))

        if rand not in mbi_list: 
            mbi_list.append(rand)

# call new mbi function to create 
def build_members(cfg:Config, rng:np.random.Generator) -> pd.DataFrame: 
    n = cfg.n_members 
    disabled = rng.random(n) < 0.10 # 10% chance of disability 
    age0 = np.where(disabled, rng.integers(30, 65, n), 
                    np.clip(rng.normal(74, 7, n), 65, 99).astype(int)) # disabled will have age pre-65, random for older citizen aligned 
    align_year = np.where(rng.random(n) < 0.50, 
                          "2025", "2026") # 50% chance original mkt_from_dt is 2025, 2026