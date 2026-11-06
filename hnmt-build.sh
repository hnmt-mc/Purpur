#!/bin/sh
# 日ノ本鯖のPurpurフォークビルド。
# 上流パッチを適用してから、hnmt の変更（hnmt-src/tree）をソースへ戻してビルドする。
# Paperweight の rebuildMinecraftPatches は手編集を拾わないため、この順番が必須。
set -e
./gradlew applyAllPatches --no-daemon
./hnmt-src/apply.sh
./gradlew :purpur-server:createMojmapPaperclipJar -x test --no-daemon
