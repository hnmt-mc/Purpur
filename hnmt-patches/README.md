# 日ノ本鯖のPurpurパッチ

Paperweightの `rebuildPatches` がこの環境では編集を拾わなかったため、
`applyAllPatches` 後のソースへPythonスクリプトで当てる方式にしています。

- `getplayers-cache.py`
  - `CraftWorld.getPlayers()` をワールドごとにキャッシュし、参加・退出の変更番号でのみ再構築する。
  - `ServerLevel` に `hnmtPlayerListVersion` を追加し、`addPlayer` / `removePlayerImmediately` で増やす。
  - 呼び出し元にはコピーを返すので、Bukkit APIの可変リスト契約は維持。

ビルド: `./hnmt-build.sh`
