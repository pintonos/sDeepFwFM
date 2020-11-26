"""
Created on June 23, 2019
@author: Wei Deng
"""

import sys
import math
import argparse
import csv, math, os
import pandas as pd
import dask
import dask.dataframe as dd
import numpy as np
import utils.util

# criteo feature dimension starts from 0, total feature dimensions 39
# oath dataset starts from 1
def load_category_index(file_path, feature_dim_start=0, dim=39):
    f = open(file_path, 'r')
    cate_dict = []
    for i in range(dim):
        cate_dict.append({})
    for line in f:
        datas = line.strip().split(',')
        cate_dict[int(datas[0]) - feature_dim_start][datas[1]] = int(datas[2])
    return cate_dict


def read_data(file_path, emb_file, num_list, feature_dim_start=0, dim=39, parquet=False, twitter_category=None):
    result = {'label': [], 'value': [], 'index': [], 'feature_sizes': []}
    cate_dict = load_category_index(emb_file, feature_dim_start, dim)
    # the left part is numerical features and the right is categorical features
    result['feature_sizes'] = [1] * len(num_list)
    for num, item in enumerate(cate_dict):
        if num + 1 not in num_list:
            result['feature_sizes'].append(len(item) + 1)

    if parquet:
        data = pd.read_parquet(file_path)
        for label in ['reply', 'retweet', 'retweet_comment', 'like']:
            if label != twitter_category:
                data = data.drop(columns=[label])

        data = utils.util.save_memory(data)

        result['label'] = data[twitter_category].values.tolist()
        result['index'] = data.iloc[:, [i for i in range(len(num_list) + 1, len(data.columns))]].values.tolist()
        result['value'] = data.iloc[:, [i for i in range(1, len(num_list) + 1)]].values.tolist()

        del data

    else:
        f = open(file_path, 'r')
        for line_idx, line in enumerate(f):
            datas = line.strip().split(',')
            result['label'].append(int(datas[0]))

            indexs = [int(item) for i, item in enumerate(datas) if i not in num_list and i != 0]
            values = [float(item) for i, item in enumerate(datas) if i in num_list]
            result['index'].append(indexs)
            result['value'].append(values)
    return result

def get_feature_sizes(emb_file, num_list, feature_dim_start=0, dim=39, twitter=False):
    result = {'label': [], 'value': [], 'index': [], 'feature_sizes': []}
    cate_dict = load_category_index(emb_file, feature_dim_start, dim)
    # the left part is numerical features and the right is categorical features
    result['feature_sizes'] = [1] * len(num_list)
    for num, item in enumerate(cate_dict):
        if num + 1 not in num_list and not twitter:
            result['feature_sizes'].append(len(item) + 1)
        if twitter and len(item) > 0:
            result['feature_sizes'].append(len(item) + 1)

    return result
