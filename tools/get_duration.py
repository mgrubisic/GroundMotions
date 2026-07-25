import numpy as np
from scipy.integrate import cumulative_trapezoid


def get_duration(ag: np.ndarray, dt: float) -> tuple[float, float]:
    """计算7-75%, 5-95%有效持时

    Args:
        ag (np.ndarray): 加速度序列
        dt (float): 时间步长
    """
    cumulative_energy = cumulative_trapezoid(ag ** 2, dx=dt, initial=0)
    total_energy = cumulative_energy[-1]
    energy_5 = 0.05 * total_energy
    energy_75 = 0.75 * total_energy
    energy_95 = 0.95 * total_energy
    idx_5 = np.where(cumulative_energy >= energy_5)[0][0]
    idx_75 = np.where(cumulative_energy >= energy_75)[0][0]
    idx_95 = np.where(cumulative_energy >= energy_95)[0][0]
    t_5 = idx_5 * dt
    t_75 = idx_75 * dt
    t_95 = idx_95 * dt
    d_5_75 = t_75 - t_5
    d_5_95 = t_95 - t_5
    
    return d_5_75, d_5_95
