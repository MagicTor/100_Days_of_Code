# Find out how many color of squirrels there are in the ...Squirrel_Data.csv file
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["grey","red","black"],
    "Count": [gray_count, red_count, black_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_color_counts.csv")
