"""预训练权重定位。只读本仓库 pretrained/ 目录, 无网络下载。

pretrained/G.pth   生成器 (warm start; 移植产物见仓库根 build_warm_g.py)
pretrained/D.pth   判别器 (可选, 缺失则从零起步)
pretrained/DUR.pth 时长预测器 (可选, 同上)
"""
import os

import torch

LOCAL_PRETRAIN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pretrained")


def load_pretrain_model():
    """返回 (G, D, DUR) 权重文件路径; 缺失的部件为 None (从零起步)。"""
    paths = []
    for name in ("G.pth", "D.pth", "DUR.pth"):
        p = os.path.join(LOCAL_PRETRAIN_DIR, name)
        paths.append(p if os.path.isfile(p) else None)
    return paths


def load_or_download_config(language, use_hf=True, config_path=None, **kwargs):
    from . import utils
    assert config_path is not None and os.path.isfile(config_path), \
        f"config 不存在: {config_path}"
    return utils.get_hparams_from_file(config_path)


def load_or_download_model(language, device, use_hf=True, ckpt_path=None, **kwargs):
    assert ckpt_path is not None and os.path.isfile(ckpt_path), \
        f"checkpoint 不存在: {ckpt_path}"
    return torch.load(ckpt_path, map_location=device, weights_only=False)
