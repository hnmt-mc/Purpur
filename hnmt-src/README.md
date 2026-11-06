# hnmt のソース変更（Paperweight パッチ外）

`applyAllPatches` のあとに `./hnmt-src/apply.sh` を実行すると、下記の変更が入る。
`rebuildMinecraftPatches` は手編集を拾わないため、パッチ形式にせず原本を保持している。

| ファイル | 変更 |
|---|---|
| `ServerLevel.java` | `getWorldBorder()` をキャッシュ（`hnmtCachedWorldBorder`） |
| `ServerLevel.java` | プレイヤー一覧のバージョン（`hnmtPlayerListVersion`）※旧 `getplayers-cache.py` の内容 |
| `LivingEntity.java` | `canCollideWithBukkit` の高速路、`onClimbable` のタグ判定キャッシュ |
| `BlockBehaviour.java` | `hnmtIsClimbable()`（CLIMBABLEタグを1回だけ判定） |
| `ChunkMap.java` | チャンク近傍判定を5tickキャッシュ（`ChunkData` にフィールド） |
| `ChunkData.java` | 上記キャッシュ用のフィールド |

ビルド手順:
```sh
./gradlew applyAllPatches
./hnmt-src/apply.sh
./gradlew :purpur-server:createMojmapPaperclipJar
```

## 旧方式（廃止）

`hnmt-patches/getplayers-cache.py` は `getPlayers` の変更だけを当てる旧方式。
`hnmt-src/tree/ServerLevel.java` に同じ変更が含まれるため削除した。
両方当てると二重適用で壊れるので、必ず `hnmt-build.sh`（applyAllPatches → hnmt-src/apply.sh）を使う。
