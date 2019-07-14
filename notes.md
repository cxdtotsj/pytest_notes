# 测试规则

## 测试点

1. 测试默认值
2. 测试各字段赋值（属性名）

## pytest相关

1. pytest discover 规则

    * 文件命名为 `test_<something>.py` 或者 `<something>_test.py`
    * 测试函数、测试类方法应命名为 `test_<something>`
    * 测试类应当命名为 `Test<something>`

2. 命令行选项

    * --collect-only    显示会被运行的测试用例  <br>
        `pytest --collect-only`
    * -k    刷选    <br>
        ```
        pytest -k "asdict or defaults" --collect-only
        pytest -k "asdict or defaults"
        ``` 
    * -m    标记
        ```
        @pytest.mark.run_these_please
        def test_mumber_access():
        ...

        pytest -v -m run_these_access

        # 同时存在mark1和mark2标记的用例
        pytest -v -m "mark1 and mark2"

        # 包含mark1，不包含mark2
        pytest -v -m "mark1 and not mark2"

        # 包含mark1，或者包含mark2
        pytest -v -m "mark1 or mark2"
        ```
    * -x    错误异常后退出
    * --maxfail=num    指定失败次数后，停止运行
    * -s    输出打印信息
    * --lf  重新运行做好一个错误的用例
    * --ff  重第一个失败的测试用例开始，全部运行用例
    * -v    详细输出
    * -q    简化输出    <br>
        `pytest -q --tb=line`
    * -l    用例失败后，显示局部变量
    * --tb=style    用例失败时，输出信息的显示方式 
        1. short    相对比较详细
        2. line     只显示一行
        3. no       不显示错误信息
        4. long     输出最详细的回溯信息
        5. auto     默认值，只显示第一个和最后一个用例的信息回溯，格式与 long 一致
        6. native   只显示Python标准库的回溯信息
    * --duration=N  显示N个耗时最长的阶段