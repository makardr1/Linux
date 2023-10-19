#!/bin/bash

while : 
do
	echo "Введите число для выбора сложности алгоритма"
	echo "1) O(n**2)"
	echo "2) O(n * log(n))"
	
	read var_1
	
	echo "Вы ввели цифру: $var_1. Уверены в выборе сложности алгоритма?"
	echo "Введите да/нет"
	
	read var_2
	
	if [ "$var_2" == "да" ]; then
		echo "Запускаем скрипт"
		break
	fi
done

