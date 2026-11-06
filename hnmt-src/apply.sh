#!/bin/bash
# Paperweight の適用後ソースに、hnmt の変更を戻す。
# 使い方: ./gradlew applyAllPatches のあと、リポジトリ直下で ./hnmt-src/apply.sh
# 理由: これらの変更は minecraft-patches に入っていない（rebuildMinecraftPatches が拾わない）。
# 消えると再ビルドで失われるため、ここに原本を置いて上書きする。
set -euo pipefail
cd "$(dirname "$0")/.."
DEST=purpur-server/src/minecraft/java
[ -d "$DEST" ] || { echo "先に ./gradlew applyAllPatches を実行してください: $DEST がありません"; exit 1; }
(cd hnmt-src/tree && find . -name '*.java' -print0) | while IFS= read -r -d '' f; do
  install -D -m 644 "hnmt-src/tree/$f" "$DEST/${f#./}"
  echo "applied ${f#./}"
done
