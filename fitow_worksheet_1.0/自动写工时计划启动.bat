@echo off 
echo 工时脚本,仅供娱乐,切勿当真
set /p month=请输入日期(202211):
set /p name=请输入名字:

::本月的起始时间,会自动获取工作日
::start_time = datetime.date(2022, 11, 1)
::end_time = datetime.date(2022, 11, 30)
::已两个项目号举例，可进行适当的修改
::work_time = [4,4]
::project = ["项目号1","项目号2"]
::work_item = ["模型训练及调优","集成调试（算法及应用层测试）"]
::work_item_plus = ["实际检出测试、跟踪及分析","算法及应用层测试"]
::leader_plan = ["项目点检","整理数据以及模型训练"]

envs\python.exe src\fitow_worksheet.py %month% %name%
pause