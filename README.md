# Bert-predict

## 1.更换模型
将bert_pretrain文件夹下存放下述百度云链接中的文件。

链接：https://pan.baidu.com/s/1KHlQHJ1S68HV2HLlMabKwA?pwd=rcwk 
提取码：rcwk


若想使用百度的ERNIE模型，将预训练模型存放在ERNIE_pretrain文件下下即可


链接：https://pan.baidu.com/s/1wLbvE2mjriXZDjQBzjtOzw?pwd=461n 
提取码：461n 



## 2.更换数据
数据存放在THUCNews/data文件夹下，分为train,test,dev,class,predict五个文件，其中class文件存放的是所预测的y的类别，根据其他文件的更改调整即可。其他文件要做修改或者更新时请注意将格式调整为"title\ttopic"的形式。

项目数据来源于清华大学自然语言处理与社会人文计算实验室（http://thuctc.thunlp.org/），感谢他们在中文NLP领域的贡献

## 3.运行方式
（1）基础的bert

python run.py --model bert

（2）bert + 其它（eg bert_CNN）

python run.py --model bert_CNN

（3）ERNIE

python run.py --model ERNIE

## 3.模型保存与预测结果
训练好的模型保存在THUCNews/save_dict文件夹下，预测结果存放在主目录下的predict.txt文件内


## 4.参考的运行版本
pandas == 1.5.2


torch == 1.13.0


numpy == 1.20.3
