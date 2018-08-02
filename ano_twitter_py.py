from pyculiarity import detect_ts, detect_vec
import pandas as pd
import time

def run(period = None, longterm_period = None, link_data = None):


    if period is None:
        period = 24
        longterm_period = period * 30 + 1

    twitter_example_data = pd.read_csv(link_data)

    data = twitter_example_data[twitter_example_data.columns[1]]
    results = detect_vec(data, max_anoms=0.02, \
                         direction='both', period=period, longterm_period=longterm_period)

    res_table = results['anoms']
    index_ano = res_table[res_table.columns[1]].tolist()

    res = []
    for i in range(len(data)):
        if i in index_ano:
            res.append(1)
        else:
            res.append(0)

    res = pd.DataFrame(res)
    res.columns = ['ano']

    result_table = pd.concat([twitter_example_data.reset_index(drop=True), res], axis=1)
    return result_table

if __name__ == '__main__':
    link_data = "C:\\Users\\CPU10902-local\\Desktop\\data_test\\data_hourly_2cols.csv"
    start_time = time.time()
    res = run(24, (24 *30+ 1), link_data)
    res.to_csv("C:\\Users\\CPU10902-local\\Desktop\\ano_twitter_python.csv", sep=',', index=False)
    print("--- Done.  Total run time: %s seconds ---" % (time.time() - start_time))

