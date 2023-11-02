import os
import pandas as pd
import numpy as np
#i was here
jjjjjjjjjjjjjjjjjjj
uhg9uyg7yg97yg
uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
oooooooooooooooooooooooooooooooooooo
uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu
blah  hu8goutgyigf79

iugoyugfuivu
oi0joij08uh
input_path = r"D:\PRZM_state_centroid_method"
weather_grid = os.path.join(input_path,"StateCentroid_WeaGrid.txt")
df_wg = pd.read_csv(weather_grid, header=0)
print(df_wg.columns)

sce_all = r"D:\DB\RawScenarios_082023\all_remove_duplicate_MaxRD.csv"
df_sec_all = pd.read_csv(sce_all, low_memory= False)
# df_sec_all = df_sec_all[df_sec_all["gen_class"] == 10] # Use this syntax to select crop type
print(df_sec_all.shape)

df = df_sec_all[df_sec_all["weather_grid"].isin(df_wg["stationID"])] # Select scenarios based on weather grid list.
print(df.shape)
# Sort the scenarios based on weather_grid and area from the largest area to the least (ascending = False).
sorted_df = df.sort_values(by=["weather_grid","area"], ascending= [True, False])
sorted_df["wg"] = sorted_df["weather_grid"]
print(sorted_df.shape)
# Keep the scenarios with largest area for each weather grid
result_df = sorted_df.groupby("wg").first()

print(result_df.shape)

out_csv = os.path.join(input_path,"StaCtroid_sce_allcrop.csv")
result_df.to_csv(out_csv, index = None)

# input_txt = r"D:\PRZM_state_centroid_method\Scenarios_from_StateCentroids\tbl_Scenarios_from_StateCentroids.txt"
# df_txt = pd.read_csv(input_txt, header = 0)
# # print(df_txt.head(), df_txt.shape)
#
# df_txt = df_txt[df_txt["gen_class"] == 10]
# # print(df_txt.shape)
# df_txt["key"] = df_txt["scenario_id"].astype(str) + df_txt["cdl_alias"].astype(str) + df_txt["cokey"].astype(str) \
#                 + df_txt["gen_class"].astype(str)+ \
#                 df_txt["plant_date"].astype(str) + df_txt["region"].astype(str)
# df_txt = df_txt["key"]
# print(df_txt)
#
#
# sce_all = r"D:\DB\RawScenarios_082023\all_remove_duplicate_MaxRD.csv"
# df_sec_all = pd.read_csv(sce_all, low_memory= False)
# df_sec_all["key"] = df_sec_all["scenario_id"].astype(str) + df_sec_all["cdl_alias"].astype(str) + df_sec_all["cokey"].astype(str) \
#                 + df_sec_all["gen_class"].astype(str)+ df_sec_all["plant_date"].astype(str) + df_sec_all["region"].astype(str)
# df_sec_all=df_sec_all[df_sec_all["key",'scenario_id']]
# select_df = df_sec_all[df_sec_all["key"].isin(df_txt)]
# print(select_df.shape)

