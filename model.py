import numpy as np
import pandas as pd
import pickle
import os

BASE_DIR = "content"

startups = pickle.load(open(os.path.join(BASE_DIR, "startups"), "rb"))
startups["First name"] = startups["First name"].fillna("")
startups["Surname"] = startups["Surname"].fillna("")


cosine_sim = pickle.load(open(os.path.join(BASE_DIR, "cosine_sim"), "rb"))

indices = pickle.load(open(os.path.join(BASE_DIR, "indices"), "rb"))

def getStartup(Investor_name):
    try:
        id_num = indices[Investor_name]
        sim_scores = list(enumerate(cosine_sim[id_num]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        startup_indices = [i[0] for i in sim_scores if i[0] <= 203]
        startup_indices = startup_indices[:10]
        output = []
        for i in startup_indices:
            output_dict = {}
            output_dict["startup_name"] = startups["Startup name"][i]
            output_dict["applicant_name"] = startups["First name"][i] + " " + startups["Surname"][i]
            output_dict["email"] = startups["Email"][i]
            output_dict["country"] = startups["Location"][i]
            output_dict["stage"] = startups["Stage"][i]
            output.append(output_dict)
        return output, True
    except Exception as ex:
        return [], False

if __name__ == "__main__":
    _, _ = getStartup("Chris")
