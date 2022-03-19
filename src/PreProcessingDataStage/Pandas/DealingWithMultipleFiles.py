# When working with multiple files we can use Glob.

# import glob
#
# files = glob.glob("file*.csv")
#
# df_list = []
# for filename in files:
#     data = pd.read_csv(filename)
#     df_list.append(data)
#
# df = pd.concat(df_list)
#
# print(files)