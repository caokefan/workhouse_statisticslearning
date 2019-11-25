# -*- coding: utf-8 -*-

"""
数字字母识别
利用CNN对验证码的数据集进行多分类
"""

from VerifyCodeCNN import CNN
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelBinarizer

CSV_FILE_PATH = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/sample/data.csv'          # CSV 文件路径
df = pd.read_csv(CSV_FILE_PATH)       # 读取CSV文件

# 数据集的特征
features = ['v'+str(i+1) for i in range(16*20)]
labels = df['label'].unique()
# 对样本的真实标签进行标签二值化
lb = LabelBinarizer()
lb.fit(labels)
y_ture = pd.DataFrame(lb.transform(df['label']), columns=['y'+str(i) for i in range(26)])
y_bin_columns = list(y_ture.columns)

for col in y_bin_columns:
    df[col] = y_ture[col]

# 将数据集分为训练集和测试集，训练集70%, 测试集30%
x_train, x_test, y_train, y_test = train_test_split(df[features], df[y_bin_columns], \
                                                    train_size = 0.7, test_size=0.3, random_state=123)

# 使用CNN进行预测
# 构建CNN网络
# 模型保存地址
MODEL_SAVE_PATH = 'C:/Users/caokefan/PycharmProjects/workhouse_statisticslearning/machinelearningwork1/cnn/cnn_verifycode.ckpt'
# CNN初始化
cnn = CNN(1000, 0.0005, MODEL_SAVE_PATH)

# 训练CNN
cnn.train(x_train, y_train)
# 预测数据
y_pred = cnn.predict(x_test)

label = 'abcdefghijkLmnopqrstuvwxyz'
# 预测分类
prediction = []
for pred in y_pred:
    label = labels[list(pred).index(max(pred))]
    prediction.append(label)

# 计算预测的准确率
x_test['prediction'] = prediction
x_test['label'] = df['label'][y_test.index]
print(x_test.head())
accuracy = accuracy_score(x_test['prediction'], x_test['label'])
print('CNN的预测准确率为%.2f%%.'%(accuracy*100))