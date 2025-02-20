import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import argparse
import statistics

parser = argparse.ArgumentParser(description='Pedigree drawing')
parser.add_argument('--clone', '-c', type=str, required=True, help='Clone name')
parser.add_argument('--target', '-t', type=str, required=True, help='target')
args = parser.parse_args()

standard_yield = 1.08

try:
    target_yield = float(args.target)
    yield_data = [1.1,0.97,1.23,1.15,1.12,1.08,1.18,1.21,1.01,1.22,1.18,1.3,1.17,0.97,1.1,1.02,1.08,1.18,1.16,1.11,1.39,1.1,1.23,1.31,1.4,1.13,1.04,1.23,1.25,1.06,1.59,1.84,1.11,1.09,1.34,1.3,1.48,1.42,1.47,1.37,1.45,1.14,1.17,1.23,1.14,1.4,1.52,1.12,1.44,1.1,1.27,1.1,1.32,1.5,1.25,1.18,1.06,1.67,1.15,1.03,1.15,1.2,1.15,1.1,1.47,1.54,1.31,1.37,1.79,1.76,2.01,1.5,1.07,1.05,0.98,1.74,1.86,1.36,1.76,1.13,1.19,1.26,1.19,1.66,1.15,1.46,1.66,1.54,1.16,1.1,1.4,1.08,1.27,1.06,1.47,1.04,1.07,1.26,1.7,1.08,1.27,1.1,1.14,"-","-",1.08,1.44,1.11,1.25,1.43,1.26,1.03,1.21,1.27,1.44,1.06,1.18,1.01,1.11,1.01,1.06,1.09,1.09,1.23,1,1.08,0.79,1.04,1.19,1.16,1.09,1.25,1.08,1.4,1.16,1.03]
    yield_data = [float(y) for y in yield_data if isinstance(y, (int, float))]
    median_value = statistics.median(yield_data)
    average_value = round(statistics.mean(yield_data),2)

    mean_yield = np.mean(yield_data)
    std_yield = np.std(yield_data)

    x = np.linspace(min(yield_data), max(yield_data), 100)
    y = stats.norm.pdf(x, mean_yield, std_yield)


    target_yield_height = stats.norm.pdf(target_yield, mean_yield, std_yield)
    standard_yield_height = stats.norm.pdf(standard_yield, mean_yield, std_yield)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue')

    plt.vlines(standard_yield, 0, standard_yield_height, color='black', linestyle="-", label=f"Sumi = {standard_yield}")
    plt.vlines(target_yield, 0, target_yield_height, color='red', linestyle="--", label=f"{args.clone} = {target_yield}")
    plt.vlines(target_yield, 0, 0, color='white', linestyle="--", label=f"Median = {median_value}")
    plt.vlines(target_yield, 0, 0, color='white', linestyle="--", label=f"Average = {average_value}")
    #plt.scatter([target_yield], [stats.norm.pdf(target_yield, mean_yield, std_yield)], color='red', s=100, zorder=3)

    plt.yticks([])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    #plt.gca().spines['bottom'].set_visible(False)
    plt.grid(False)
    plt.legend(loc='upper right', fontsize=10, frameon=False)

    save_path = 'static/graph/' + args.clone + '_lw.png'
    plt.savefig(save_path, dpi=600, bbox_inches='tight', transparent=True)
    plt.close()
except ValueError:
    target_yield = args.target
    yield_data = [1.1,0.97,1.23,1.15,1.12,1.08,1.18,1.21,1.01,1.22,1.18,1.3,1.17,0.97,1.1,1.02,1.08,1.18,1.16,1.11,1.39,1.1,1.23,1.31,1.4,1.13,1.04,1.23,1.25,1.06,1.59,1.84,1.11,1.09,1.34,1.3,1.48,1.42,1.47,1.37,1.45,1.14,1.17,1.23,1.14,1.4,1.52,1.12,1.44,1.1,1.27,1.1,1.32,1.5,1.25,1.18,1.06,1.67,1.15,1.03,1.15,1.2,1.15,1.1,1.47,1.54,1.31,1.37,1.79,1.76,2.01,1.5,1.07,1.05,0.98,1.74,1.86,1.36,1.76,1.13,1.19,1.26,1.19,1.66,1.15,1.46,1.66,1.54,1.16,1.1,1.4,1.08,1.27,1.06,1.47,1.04,1.07,1.26,1.7,1.08,1.27,1.1,1.14,"-","-",1.08,1.44,1.11,1.25,1.43,1.26,1.03,1.21,1.27,1.44,1.06,1.18,1.01,1.11,1.01,1.06,1.09,1.09,1.23,1,1.08,0.79,1.04,1.19,1.16,1.09,1.25,1.08,1.4,1.16,1.03]
    yield_data = [float(y) for y in yield_data if isinstance(y, (int, float))]
    median_value = statistics.median(yield_data)
    average_value = round(statistics.mean(yield_data),2)


    mean_yield = np.mean(yield_data)
    std_yield = np.std(yield_data)

    x = np.linspace(min(yield_data), max(yield_data), 100)
    y = stats.norm.pdf(x, mean_yield, std_yield)

#    target_yield_height = stats.norm.pdf(target_yield, mean_yield, std_yield)
    standard_yield_height = stats.norm.pdf(standard_yield, mean_yield, std_yield)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, color='blue')

    plt.vlines(standard_yield, 0, standard_yield_height, color='black', linestyle="-", label=f"Sumi = {standard_yield}")
    plt.vlines(standard_yield, 0, 0, color='white', linestyle="--", label=f"{args.clone} = Not examined")
    plt.vlines(standard_yield, 0, 0, color='white', linestyle="--", label=f"Median = {median_value}")
    plt.vlines(standard_yield, 0, 0, color='white', linestyle="--", label=f"Average = {average_value}")
    #plt.scatter([target_yield], [stats.norm.pdf(target_yield, mean_yield, std_yield)], color='red', s=100, zorder=3)

    plt.yticks([])
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    #plt.gca().spines['bottom'].set_visible(False)
    plt.grid(False)
    plt.legend(loc='upper right', fontsize=10, frameon=False)

    save_path = 'static/graph/' + args.clone + '_lw.png'
    plt.savefig(save_path, dpi=600, bbox_inches='tight', transparent=True)
    plt.close()
