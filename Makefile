m01:
	time python -m src.main01
m02:
	time python -m src.main02
m03:
	time python -m src.main03
m04:
	time python -m src.main04
m05:
	time python -m src.main05
m06:
	time python -m src.main06
m07:
	time python -m src.main07
m08:
	time python -m src.main08
m09:
	time python -m src.main09
m10:
	time python -m src.main10
m11:
	time python -m src.main11
m12:
	time python -m src.main12
m13:
	time python -m src.main13
m14:
	time python -m src.main14
m15:
	time python -m src.main15
m17:
	time python -m src.main17
m19:
	time python -m src.main19
task:
	time celery -A src.task.app worker --loglevel=info
m18:
	time python -m src.main18
all:
	time python -m src.main01
	time python -m src.main02
	time python -m src.main03
	time python -m src.main04
	time python -m src.main05
	time python -m src.main06
	time python -m src.main07
	time python -m src.main08
	time python -m src.main09
	time python -m src.main10
	time python -m src.main11
	time python -m src.main12