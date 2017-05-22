# Quiz_day2

## 1. 리스트 컴프리헨션을 사용하여 홀수 단만 “{} * {} = {}” 형식으로 출력하는 make_gugu()함수를 만드세요

```
['{}x{}={}'.format(x,y,x*y)(x,y) for x in range(10) for y in range(10)]
```

## 2. Level은 어떤 숫자가 출력되고 왜 그 숫자가 출력되는지 설명하시오.level = 0def local1(): level = 20 def local2(): global level level += 3local1()print(level)

```
global 로 인해 0가 산출된다.
```

## 3. plus함수(1)를 이용해서 print_plus(a,b) 함수를 실행 하였을 때 (2) 결과처럼 작동하게 작성하시오. (1) def plus(a,b): return a + b(2) 함수 시작 (a와b를 더한 값이 나와야 함) ex: a=3, b=6 이면 9가 들어가야 함 함수 끝

```
def print_plus(*args):
	def main_plus(*args):
		return a+b
	def plus():
		print('함수 시작 \n {}\n함수 끝'.format(main_plus(*args)))
		return main_plus
	
```


## 4. 3번의 print_plus 사용하여 plus의 데코레이터로 동작하게끔 작성하시오. Ex) @print_plus def plus(a,b): return a + b plus(3,5) 결괏값) 함수 시작 8 함수 끝

```
def print_plus(main_plus):
    def plus(*args,**kwargs):
        print('함수 시작 \n {} \n함수 끝'.format(main_plus(*args, **kwargs)))
        return main_plus(*args, **kwargs)
    return plus

@print_plus
def main_plus(a,b):
    return a+b
```

## 5.
순차검색을 구현하시오. 1. 1~100 의 숫자를 가지는 리스트를 생성 후 무작위로 섞어주세요. 2. sequential(list, num) 함수를 생성해주세요 3. num이 list에 있으면 위치를 반환하고 없으면 “없습니다”. 반환해주세요

```
list_100=[x for x in range(100)]
def sequential(list,num):
    if num in list:
        return list_100.index(num)
    else:
        print('없습니다')

sequential(list_100,18)
```

>무작위로 추출하여 섞어야하지만 구현하지 못했다.