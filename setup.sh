#!/bin/bash

# 패키지 업데이트 및 git-flow 설치
sudo apt-get update && sudo apt-get install -y git-flow

# PATH 설정
echo 'export PATH=$PATH:/usr/lib/git-core' >> ~/.bashrc
source ~/.bashrc
