import numpy as np

sample_data = np.load('sample_data.npy',allow_pickle=True)
# fruits = np.load('fruits_300.npy')
# If M is (32 x 32 x 3), then .reshape(1,-1) will produce a 2d array (not 1d), of shape (1, 32*32*3).
# That can be reshaped back to (32,32,3) with the same sort of reshape statement.
sample_data_2d = sample_data.reshape(-1, 100 * 100 )

print("sample_data의 shape 맞추기:", sample_data)
print("sample_data_2d의 shape 맞추기:", sample_data_2d)
# 여기에서 출력되는 차원의 숫자가 같아야 한다.
print("sample_data.shape:", sample_data.shape)
print("sample_data_2d.shape:", sample_data_2d.shape)

from sklearn.cluster import KMeans

# K값을 지정해 준다.random_state=항상 값은값이 랜덤하게 나온다.
km = KMeans(n_clusters=5)  # random_state=42 -> 항상 랜덤값이 같게 하기위해 쓴다.
# 사이킷 런의 철학은 nxd, 갯수x차원
km.fit(sample_data_2d)
# 할당된 레이블의 결과를 볼 수 있다.
print("km.labels_", km.labels_)
print("km.labels_.shape", km.labels_.shape)
print("첫번째:", km.labels_[0:])
# print("두번째:", km.labels_[10:20])
# print("세번째:", km.labels_[20:30])

print(np.unique(km.labels_, return_counts=True))
print(km.labels_)

import matplotlib.pyplot as plt



def draw_sample_data(arr, ratio=1):
    n = 30  # n은 샘플 개수입니다
    # 한 줄에 10개씩 이미지를 그립니다. 샘플 개수를 10으로 나누어 전체 행 개수를 계산합니다.
    print(n)
    rows = int(np.ceil(n / 10))
    # 행이 1개 이면 열 개수는 샘플 개수입니다. 그렇지 않으면 10개입니다.
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols * ratio, rows * ratio), squeeze=False)
    for i in range(rows):
        print(i)
        for j in range(cols):
            if i * 10 + j < n:  # n 개까지만 그립니다.
                print(i)
                axs[i, j].imshow(arr[i * 10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()


draw_sample_data(sample_data[km.labels_ == 0])
draw_sample_data(sample_data[km.labels_ == 1])
draw_sample_data(sample_data[km.labels_ == 2])
draw_sample_data(sample_data[km.labels_ == 3])
draw_sample_data(sample_data[km.labels_ == 4])