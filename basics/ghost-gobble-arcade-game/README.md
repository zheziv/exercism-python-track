# Test result

/Users/zhe.chen/PycharmProjects/exercism-python-track/.venv/bin/python -X pycache_prefix=/Users/zhe.chen/Library/Caches/JetBrains/PyCharm2025.1/cpython-cache /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 58532 --file /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/zhe.chen/PycharmProjects/exercism-python-track/basics/ghost-gobble-arcade-game/arcade_game_test.py 
Testing started at 13:41 ...
Connected to pydev debugger (build 251.26927.90)
Launching pytest with arguments /Users/zhe.chen/PycharmProjects/exercism-python-track/basics/ghost-gobble-arcade-game/arcade_game_test.py --no-header --no-summary -q in /Users/zhe.chen/PycharmProjects/exercism-python-track/basics/ghost-gobble-arcade-game

============================= test session starts ==============================
collecting ... collected 13 items

arcade_game_test.py::GhostGobbleGameTest::test_dont_lose_if_not_touching_a_ghost PASSED [  7%]
arcade_game_test.py::GhostGobbleGameTest::test_dont_lose_if_touching_a_ghost_with_a_power_pellet_active PASSED [ 15%]
arcade_game_test.py::GhostGobbleGameTest::test_dont_win_if_all_dots_eaten_but_touching_a_ghost PASSED [ 23%]
arcade_game_test.py::GhostGobbleGameTest::test_dont_win_if_not_all_dots_eaten PASSED [ 30%]
arcade_game_test.py::GhostGobbleGameTest::test_ghost_does_not_get_eaten_because_no_power_pellet_active PASSED [ 38%]
arcade_game_test.py::GhostGobbleGameTest::test_ghost_does_not_get_eaten_because_not_touching_ghost PASSED [ 46%]
arcade_game_test.py::GhostGobbleGameTest::test_ghost_gets_eaten PASSED   [ 53%]
arcade_game_test.py::GhostGobbleGameTest::test_lose_if_touching_a_ghost_without_a_power_pellet_active PASSED [ 61%]
arcade_game_test.py::GhostGobbleGameTest::test_no_score_when_nothing_eaten PASSED [ 69%]
arcade_game_test.py::GhostGobbleGameTest::test_score_when_eating_dot PASSED [ 76%]
arcade_game_test.py::GhostGobbleGameTest::test_score_when_eating_power_pellet PASSED [ 84%]
arcade_game_test.py::GhostGobbleGameTest::test_win_if_all_dots_eaten PASSED [ 92%]
arcade_game_test.py::GhostGobbleGameTest::test_win_if_all_dots_eaten_and_touching_a_ghost_with_a_power_pellet_active PASSED [100%]

======================= 13 passed, 13 warnings in 0.03s ========================

Process finished with exit code 0

