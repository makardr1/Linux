#!/bin/bash

algorithm_selection(){
	echo "Введите число для выбора сложности алгоритма"
	echo "1) O(n**2)"
	echo "2) O(n * log(n))"
	
	read var_1
	
	if [[ "$var_1" =~ ^[0-9]+$ ]]; then
		echo "Вы ввели число: $var_1"
		if [ "$var_1" == "1" ]; then
			echo "Сортировка пузырьком"
			cd ../Python
			python3 bubble_sort.py
		elif [ "$var_1" == "2" ]; then
			echo "Быстрая сортировка"
			cd ../Python
			python3 quick_sort.py
		else
			echo "Такого числа нет в списке"
			algorithm_selection
		fi
	else
		echo "Необходимо ввести число"
		algorithm_selection
	fi
	
}
algorithm_selection 
