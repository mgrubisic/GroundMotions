from typing import Literal
import numpy as np


def scaling(
    ag: np.ndarray,
    dt: float,
    rule: Literal['a', 'b', 'c', 'd', 'e'],
    para: float | tuple,
    T: np.ndarray,
    Sa_targ: np.ndarray,
    Sa_ag: np.ndarray=None,
) -> tuple[float, np.ndarray]:
    """地震动缩放

    Args:
        ag (np.ndarray): 加速度时程
        dt (float): 时间步长
        rule (Literal['a', 'b', 'c', 'd', 'e']): 缩放规则
        para (float | tuple): 缩放参数，与`rule`的取值有关
        T (np.ndarray): 周期序列
        Sa_targ (np.ndarray): 目标谱Sa序列
        Sa_ag (np.ndarray, optional): 实际地震动反应谱Sa序列，有则采用，无则计算
    
    Note:
    -----
    缩放规则:
    * [a] 按Sa(0)(即PGA)匹配反应谱, para=None
    * [b] 按Sa(Ta)匹配反应谱, para=Ta
    * [c] 按Sa(Ta~Tb)匹配反应谱(几何平均数), 最小化RMSE, para=(Ta, Tb)
    * [d] 按Sa,avg(Ta~Tb)匹配反应谱, para=(Ta, Tb)
    * [e] 指定缩放系数, para=SF
    para (float | tuple): 缩放参数，与`approach`的取值有关

    Returns:
        float: 缩放系数
    """
    if Sa_ag is None:
        from .spectrum import spectrum
        Sa_ag, _, _ = spectrum(ag, dt, T)
    if rule == 'a':
        sf = Sa_targ[0] / Sa_ag[0]
    elif rule == 'b':
        Ta: float = para
        sf = np.interp(Ta, T, Sa_targ) / np.interp(Ta, T, Sa_ag)
    elif rule == 'c':
        Ta, Tb = para
        learning_rate = 0.01  # 学习率
        num_iterations = 1000  # 迭代次数
        Sa_ag_cut = Sa_ag[(Ta <= T) & (T <= Tb)]
        Sa_targ_cut = Sa_targ[(Ta <= T) & (T <= Tb)]
        init_sf = np.mean(Sa_targ_cut) / np.mean(Sa_ag_cut)  # 初始缩放系数
        sf = _gradient_descent(Sa_ag_cut, Sa_targ_cut, init_sf, learning_rate, num_iterations)
    elif rule == 'd':
        Ta, Tb = para
        Sa_targ_cut = Sa_targ[(Ta <= T) & (T <= Tb)]
        Sa_avg_targ = _geometric_mean(Sa_targ_cut)
        Sa_ag_cut = Sa_ag[(Ta <= T) & (T <= Tb)]
        Sa_avg_ag = _geometric_mean(Sa_ag_cut)
        sf = Sa_avg_targ / Sa_avg_ag
    elif rule == 'e':
        sf = para
    else:
        raise ValueError('【Error】参数approach错误')

    return sf, Sa_ag

def _gradient_descent(a, b, init_SF, learning_rate, num_iterations):
    """梯度下降"""
    f = init_SF
    for _ in range(num_iterations):
        error = a * f - b
        gradient = 2 * np.dot(error, a) / len(a)
        f -= learning_rate * gradient
    return f

def _geometric_mean(data):
    """计算几何平均数"""
    total = 1
    n = len(data)
    for i in data:
        total *= pow(i, 1 / n)
    return total