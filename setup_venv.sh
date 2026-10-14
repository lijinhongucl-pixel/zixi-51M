#!/bin/bash
# 建本地环境: uv venv (py3.11) + 可编辑安装 zixi-51m
set -e
cd "$(dirname "$0")"
uv venv .venv --python 3.11
uv pip install --python .venv/bin/python -e .
echo "done. 激活: source .venv/bin/activate"
