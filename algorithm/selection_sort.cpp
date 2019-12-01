#include <iostream>
using namespace std;
//#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable: 4996)
int main(void)
{
	int i, j, min, index, temp;
	int arr[10] = { 1,10,5 ,8,7,6,4,3,2,9 };
	for (i = 0; i < 10; i++)
	{
		min = 999;
		for (j = i; j < 10; j++)
		{
			if (min > arr[j])
			{
				min = arr[j];
				index = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[index];
		arr[index] = temp;
	}
	for (i = 0; i < 10; i++)
	{
		printf("%d ", arr[i]);
	}

	return 0;

}
