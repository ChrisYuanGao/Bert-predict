# coding: UTF-8
import time
import torch
import numpy as np
import pandas as pd
from train_eval import train, init_network, predict
from importlib import import_module
import argparse
from utils import build_dataset, build_iterator, get_time_dif
import os

parser = argparse.ArgumentParser(description='Chinese Text Classification')
parser.add_argument('--model', type=str, required=True, help='choose a model: Bert, ERNIE')
args = parser.parse_args()


if __name__ == '__main__':
    dataset = 'THUCNews'  # 数据集

    model_name = args.model  # bert
    x = import_module('models.' + model_name)
    config = x.Config(dataset)
    np.random.seed(1)
    torch.manual_seed(1)
    torch.cuda.manual_seed_all(1)
    torch.backends.cudnn.deterministic = True  # 保证每次结果一样

    start_time = time.time()
    print("Loading data...")
    train_data, dev_data, test_data,predict_data = build_dataset(config)
    train_iter = build_iterator(train_data, config)
    dev_iter = build_iterator(dev_data, config)
    test_iter = build_iterator(test_data, config)
    predict_iter = build_iterator(predict_data, config)
    time_dif = get_time_dif(start_time)
    print("Time usage:", time_dif)

    if os.path.exists("finetune_model/v1.pkl"):
        print('fine-tuned model have exist, loading existing model:')
        model = torch.load("finetune_model/v1.pkl")
        print("successfully load the model")
    
    else:
        # train
        model = x.Model(config).to(config.device)
        train(config, model, train_iter, dev_iter, test_iter)
        print("Fine-tune finish! Now saving model...")
        torch.save(model,"finetune_model/v1.pkl")

    # predict
    print("start to predict")
    predict(config,model,predict_iter)
    pure_text = pd.read_csv("THUCNews/data/predict.txt",sep='\t',header=None)
    pure_text = pure_text.iloc[:,0]
    label = pd.read_csv("prediction_result.txt",dtype=int)
    result = pd.concat([pure_text,label.astype(int)],axis=1)
    result.to_csv("prediction_result.txt",index=False,header=None,sep='\t')
    print("finish!")