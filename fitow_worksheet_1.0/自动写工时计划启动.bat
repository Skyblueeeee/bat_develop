@echo off 
echo ��ʱ�ű�,��������,������
set /p month=����������(202211):
set /p name=����������:

::���µ���ʼʱ��,���Զ���ȡ������
::start_time = datetime.date(2022, 11, 1)
::end_time = datetime.date(2022, 11, 30)
::��������Ŀ�ž������ɽ����ʵ����޸�
::work_time = [4,4]
::project = ["��Ŀ��1","��Ŀ��2"]
::work_item = ["ģ��ѵ��������","���ɵ��ԣ��㷨��Ӧ�ò���ԣ�"]
::work_item_plus = ["ʵ�ʼ�����ԡ����ټ�����","�㷨��Ӧ�ò����"]
::leader_plan = ["��Ŀ���","���������Լ�ģ��ѵ��"]

envs\python.exe src\fitow_worksheet.py %month% %name%
pause