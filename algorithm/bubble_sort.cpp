#include <iostream>
using namespace std;
//#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable: 4996)
int main(void)
{
	int i, j, temp;

	int arr[10] = { 10,3,7,5,4,9,1,8,2,6 };

	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 9 - i; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];	
				arr[j + 1] = temp;
				
			}
		}
	}
	for (i = 0; i < 10; i++)
	{
		printf("%d ", arr[i]);
	}
	return 0;

}
