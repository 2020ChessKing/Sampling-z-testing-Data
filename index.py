#   imports
import  plotly.express as plotly, plotly.figure_factory as graphs, plotly.graph_objects as graphObjects
import pandas as panda, statistics as stats, random


#   code
# raw materals
data_frame = panda.read_csv('C:\Swarup\WhiteHat Jr\Python\Projects\Sampling_Data\medium_data.csv')
data = data_frame["claps"].tolist()
clap_data_mean_list = []

# functions
def setup():
    for i in range(0, 100):
        sample_data = sampleData()
        clap_data_mean_list.append(sample_data)

    mean_clap_sampled = stats.mean(clap_data_mean_list)
    stdev_clap_sampled = stats.stdev(clap_data_mean_list)
    stdev_clap_population = stats.stdev(data)
    mean_clap_population = stats.mean(data)
    zscore = (mean_clap_population - mean_clap_sampled)/stdev_clap_population
    print(zscore)
    print("The mean of the sample means is: ", mean_clap_sampled, "-- -- -- The mean of the population is: ", mean_clap_population)

    # Standard Deviations
    area_1_start, area_1_end = mean_clap_sampled - stdev_clap_sampled, mean_clap_sampled + stdev_clap_sampled
    area_2_start, area_2_end = mean_clap_sampled - 2*(stdev_clap_sampled), mean_clap_sampled + 2*(stdev_clap_sampled)
    area_3_start, area_3_end =  mean_clap_sampled - 3*(stdev_clap_sampled), mean_clap_sampled + 3*(stdev_clap_sampled)

    # Area Percentages (1rst, 2nd, 3rd)
    first_area_percentage = [result for result in data if result > area_1_start and result < area_1_end]
    second_area_percentage = [result for result in data if result > area_2_start and result < area_2_end]
    third_area_percentage = [result for result in  data if result > area_3_start and result < area_3_end]

    #Convert into Percentages
    area_1_coverage = len(first_area_percentage)*100/len(data)
    area_2_coverage = len(second_area_percentage)*100/len(data)
    area_3_coverage = len(third_area_percentage)*100/len(data)

    print(area_1_coverage, area_2_coverage, area_3_coverage)
    print(area_1_start)

    dist_plot = graphs.create_distplot([clap_data_mean_list], ["Claps"], show_hist=False)
    dist_plot.add_trace(graphObjects.Scatter(x=[mean_clap_sampled, mean_clap_sampled], y=[0, 0.004], mode="lines", line=dict(width=(area_1_coverage + area_2_coverage + area_3_coverage)), name="Area 3"))
    dist_plot.add_trace(graphObjects.Scatter(x=[mean_clap_sampled, mean_clap_sampled], y=[0, 0.004], mode="lines", line=dict(width=(area_1_coverage + area_2_coverage)), name="Area 2"))
    dist_plot.add_trace(graphObjects.Scatter(x=[mean_clap_sampled, mean_clap_sampled], y=[0, 0.004], mode="lines", line=dict(width=(area_1_coverage)), name="Area 1"))
    dist_plot.add_trace(graphObjects.Scatter(x=[mean_clap_sampled, mean_clap_sampled], y=[0, 0.004] , mode="lines"))

    dist_plot.show()

def sampleData():
    clap_data_list = []

    for i in range(0, 30):
        random_number = random.randint(1, len(data)-1)
        random_clap = round(data[random_number])
        clap_data_list.append(random_clap)

    clap_data_list_mean = stats.mean(clap_data_list)
    return round(clap_data_list_mean)



def showGraph():
    dist_plot = graphs.create_distplot([clap_data_mean_list], ["claps"], show_hist=False)
    dist_plot.show()



if __name__ == "__main__":
    setup()