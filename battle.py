def battle(player, monster):
    print(f"\nA battle begins between {player.name.title()} and {monster.name.title()}! Who will win?\n")
    
    turn = 0
    while player.is_alive() and monster.is_alive():
        if turn % 2 == 0:
            player.attack(monster)
        else:
            monster.attack(player)
        turn += 1
        print("")

    if player.is_alive():
        print(f"\nVictory! {player.name.title()} has defeated {monster.name.title()}!")
        if hasattr(monster, "drop_loot"):
            loot = monster.drop_loot()
            if hasattr(player, "collect_loot"):
                player.collect_loot(loot)
    else:
        print(f"\n{player.name.title()} was defeated by {monster.name.title()}... Good luck next time!\n")
