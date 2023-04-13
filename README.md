# Bert-predict

##1.更换模型
将bert_pretrain文件夹下的所有文件替换为下述百度云链接中的文件。


链接：https://pan.baidu.com/s/1KHlQHJ1S68HV2HLlMabKwA?pwd=rcwk 
提取码：rcwk

##2.更换数据
数据存放在THUCNews/data文件夹下，分为train,test,dev,class,predict五个文件，其中class文件存放的是所预测的y的类别，根据其他文件的更改调整即可。其他文件要做修改或者更新时请注意将格式调整为"title\ttopic"的形式。

##3.模型保存与预测结果
训练好的模型保存在THUCNews/save_dict文件夹下，预测结果存放在主目录下的predict.txt文件内
