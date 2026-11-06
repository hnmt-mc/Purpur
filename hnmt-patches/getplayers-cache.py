from pathlib import Path

home = Path.home()
# ServerLevel: プレイヤー一覧の変更番号
p = home / 'hnmt-purpur/purpur-server/src/minecraft/java/net/minecraft/server/level/ServerLevel.java'
s = p.read_text()
if 'hnmtPlayerListVersion' not in s:
    s = s.replace(
        '    final List<ServerPlayer> players = Lists.newArrayList();',
        '    final List<ServerPlayer> players = Lists.newArrayList();\n    public int hnmtPlayerListVersion;',
        1,
    )
    s = s.replace(
        '    private void addPlayer(ServerPlayer player) {\n',
        '    private void addPlayer(ServerPlayer player) {\n        ++this.hnmtPlayerListVersion;\n',
        1,
    )
    s = s.replace(
        '    public void removePlayerImmediately(ServerPlayer player, Entity.RemovalReason reason) {\n',
        '    public void removePlayerImmediately(ServerPlayer player, Entity.RemovalReason reason) {\n        ++this.hnmtPlayerListVersion;\n',
        1,
    )
    p.write_text(s)
    print('ServerLevel patched')

# CraftWorld: getPlayers のキャッシュ
p = home / 'hnmt-purpur/paper-server/src/main/java/org/bukkit/craftbukkit/CraftWorld.java'
s = p.read_text()
old = '''    @Override
    public List<Player> getPlayers() {
        List<Player> list = new ArrayList<Player>(this.world.players().size());

        for (net.minecraft.world.entity.player.Player human : this.world.players()) {
            HumanEntity bukkitEntity = human.getBukkitEntity();

            if ((bukkitEntity != null) && (bukkitEntity instanceof Player)) {
                list.add((Player) bukkitEntity);
            }
        }

        return list;
    }'''
new = '''    private List<Player> hnmtCachedPlayers;
    private int hnmtCachedPlayersVersion = -1;

    @Override
    public List<Player> getPlayers() {
        final int version = this.world.hnmtPlayerListVersion;
        if (this.hnmtCachedPlayers == null || this.hnmtCachedPlayersVersion != version) {
            List<Player> list = new ArrayList<Player>(this.world.players().size());
            for (net.minecraft.world.entity.player.Player human : this.world.players()) {
                HumanEntity bukkitEntity = human.getBukkitEntity();
                if ((bukkitEntity != null) && (bukkitEntity instanceof Player)) {
                    list.add((Player) bukkitEntity);
                }
            }
            this.hnmtCachedPlayers = list;
            this.hnmtCachedPlayersVersion = version;
        }
        return new ArrayList<>(this.hnmtCachedPlayers);
    }'''
if 'hnmtCachedPlayers' not in s:
    s = s.replace(old, new, 1)
    p.write_text(s)
    print('CraftWorld patched')
