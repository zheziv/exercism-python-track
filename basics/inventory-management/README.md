Test result:

/Users/zhe.chen/PycharmProjects/exercism-python-track/.venv/bin/python -X pycache_prefix=/Users/zhe.chen/Library/Caches/JetBrains/PyCharm2025.2/cpython-cache /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pydev/pydevd.py --multiprocess --qt-support=auto --client 127.0.0.1 --port 53490 --file /Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm/_jb_pytest_runner.py --path /Users/zhe.chen/PycharmProjects/exercism-python-track/basics/inventory-management/dicts_test.py 
Testing started at 14:56 ...
Connected to: <socket.socket fd=3, family=2, type=1, proto=0, laddr=('127.0.0.1', 53491), raddr=('127.0.0.1', 53490)>.
Connected to pydev debugger (build 252.25557.178)
Launching pytest with arguments /Users/zhe.chen/PycharmProjects/exercism-python-track/basics/inventory-management/dicts_test.py --no-header --no-summary -q in /Users/zhe.chen/PycharmProjects/exercism-python-track

============================= test session starts ==============================
collecting ... collected 11 items

basics/inventory-management/dicts_test.py::InventoryTest::test_add_from_empty_dict PASSED [  9%]
basics/inventory-management/dicts_test.py::InventoryTest::test_add_multiple_items PASSED [ 18%]
basics/inventory-management/dicts_test.py::InventoryTest::test_add_new_item PASSED [ 27%]
basics/inventory-management/dicts_test.py::InventoryTest::test_add_one_item PASSED [ 36%]
basics/inventory-management/dicts_test.py::InventoryTest::test_create_inventory PASSED [ 45%]
basics/inventory-management/dicts_test.py::InventoryTest::test_decrement_items PASSED [ 54%]
basics/inventory-management/dicts_test.py::InventoryTest::test_decrement_items_not_in_inventory PASSED [ 63%]
basics/inventory-management/dicts_test.py::InventoryTest::test_list_inventory PASSED [ 72%]
basics/inventory-management/dicts_test.py::InventoryTest::test_not_below_zero PASSED [ 81%]
basics/inventory-management/dicts_test.py::InventoryTest::test_remove_item PASSED [ 90%]
basics/inventory-management/dicts_test.py::InventoryTest::test_remove_item_not_in_inventory PASSED [100%]

======================= 11 passed, 11 warnings in 0.03s ========================

Process finished with exit code 0
