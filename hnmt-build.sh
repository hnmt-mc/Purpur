#!/bin/sh
# 日ノ本鯖のPurpurフォークビルド。上流パッチを適用してから、ここのパッチを当てる。
set -e
./gradlew applyAllPatches --no-daemon
python3 hnmt-patches/getplayers-cache.py
./gradlew :purpur-server:createMojmapPaperclipJar -x test --no-daemon
