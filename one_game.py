def adventure_game():
    game_running = True
    current_location = "城堡大门"

    locations = {
        "城堡大门": {
            "description": "你站在一个古老的城堡前。城堡的大门紧闭。",
            "options": {
                "进入城堡": "中央大厅",
                "离开": "游戏结束"
            }
        },
        "中央大厅": {
            "description": "你来到了城堡的中央大厅，四周陈列着古老的装饰品。",
            "options": {
                "探索图书馆": "图书馆",
                "前往地牢": "地牢",
                "回到城堡大门": "城堡大门"
            }
        },
        "图书馆": {
            "description": "这里是城堡的图书馆，书架上摆满了各种古书。",
            "options": {
                "研究一本古老的魔法书": "发现魔法",
                "回到中央大厅": "中央大厅"
            }
        },
        "地牢": {
            "description": "你小心翼翼地走进了地牢，周围一片漆黑。",
            "options": {
                "继续前进": "遭遇怪物",
                "逃回中央大厅": "中央大厅"
            }
        },
        "发现魔法": {
            "description": "你发现了一个强大的魔法，可以帮助你在冒险中获胜。",
            "options": {
                "使用魔法": "游戏胜利",
                "回到中央大厅": "中央大厅"
            }
        },
        "遭遇怪物": {
            "description": "一个可怕的怪物出现了！你需要做出选择。",
            "options": {
                "战斗": "游戏失败",
                "逃跑": "中央大厅"
            }
        },
        "游戏胜利": {
            "description": "恭喜你！你成功地使用魔法，赢得了游戏。",
            "options": {
                "重新开始": "城堡大门"
            }
        },
        "游戏失败": {
            "description": "很不幸，你被怪物打败了。游戏结束。",
            "options": {
                "重新开始": "城堡大门"
            }
        },
        "游戏结束": {
            "description": "你决定结束这次冒险，希望下次再会。",
            "options": {}
        }
    }

    def display_location(location_key):
        location = locations[location_key]
        print("\n" + location["description"])
        for option in location["options"]:
            print(f"- {option}")
    
    def get_player_choice(location_key):
        location = locations[location_key]
        choice = input("\n你的选择是？ ").strip()
        return location["options"].get(choice, "无效选择")

    while game_running:
        display_location(current_location)
        if current_location == "游戏结束":
            print("感谢游玩！")
            break
        choice_result = get_player_choice(current_location)
        if choice_result == "无效选择":
            print("无效的选择，请重新选择。")
        else:
            current_location = choice_result

if __name__ == "__main__":
    adventure_game()
