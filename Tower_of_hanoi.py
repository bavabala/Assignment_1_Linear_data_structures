def TowerHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerHanoi(n-1, aux_rod, to_rod, from_rod)
N = 3
TowerHanoi(N, 'A', 'C', 'B')