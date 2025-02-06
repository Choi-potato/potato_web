import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import argparse

parser = argparse.ArgumentParser(description='Pedigree drawing')
parser.add_argument('--clone', '-c', type=str, required=True, help='Clone name')
args = parser.parse_args()

# 1️⃣ 수량(Yield) 데이터 리스트 (예시)
yield_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # 실제 데이터 사용 가능
target_yield = 45  # 분석하고 싶은 품종의 수량
standard_yield = 60

# 2️⃣ 정규분포의 평균과 표준편차 계산
mean_yield = np.mean(yield_data)
std_yield = np.std(yield_data)

# 3️⃣ 상위 몇 %인지 계산
percentile = stats.percentileofscore(yield_data, target_yield, kind="rank")

# 4️⃣ 정규분포 그래프 생성
x = np.linspace(min(yield_data), max(yield_data), 100)
y = stats.norm.pdf(x, mean_yield, std_yield)

# 5️⃣ 그래프 설정
plt.figure(figsize=(8, 5))

# 정규분포 곡선 그리기
plt.plot(x, y, color='blue')

# 목표 지점 표시 (빨간 점 & 선)
plt.axvline(target_yield, color='red', linestyle="--")
plt.axvline(standard_yield, color='black', linestyle="-")
#plt.scatter([target_yield], [stats.norm.pdf(target_yield, mean_yield, std_yield)], color='red', s=100, zorder=3)

# 6️⃣ 불필요한 요소 제거
plt.yticks([])  # Y축 눈금 제거
plt.gca().spines['top'].set_visible(False)     # 위쪽 테두리 제거
plt.gca().spines['right'].set_visible(False)   # 오른쪽 테두리 제거
plt.gca().spines['left'].set_visible(False)    # 왼쪽 테두리 제거
#plt.gca().spines['bottom'].set_visible(False)  # 아래쪽 테두리 제거
plt.grid(False)  # 회색 배경 격자 제거

# 7️⃣ 그래프 저장
save_path = 'static/graph/' + args.clone + '_lw.png'
plt.savefig(save_path, dpi=600, bbox_inches='tight', transparent=True)  # 투명 배경 저장
plt.close()
