/* Author: Simon Westphahl <westphahl@gmail.com>
 * Description: Quicksort algorithm with average vs. worst case comparison
 * License: Public Domain
 */

#include <iostream>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>

const unsigned int arraySize = 100000;

int partition(int a[], int first, int last)
{
  int x = a[first];
  int j = last + 1;
  int i = first - 1;
  int tmp;

  while (true) {
    do j--;
    while (a[j] > x);
    do i++;
    while (a[i] < x);
    if (i < j) {
      tmp = a[i];
      a[i] = a[j];
      a[j] = tmp;
    } else {
      return j;
    }
  }
}

void quicksort(int a[], int first, int last)
{
  int partLast = 0;

  if (first < last) {
    partLast = partition(a, first, last);
    quicksort(a, first, partLast);
    quicksort(a, partLast + 1, last);
  }
}

int main()
{
  int *a = new int [arraySize];
  clock_t prgstart, prgend;

  for (int i = 1; i < arraySize; i++) {
    a[i] = rand();
  }

  prgstart = clock();
  quicksort(a, 0, arraySize - 1);
  prgend = clock();

  std::cout << "Runtime (random): "
            << (float) (prgend - prgstart) / CLOCKS_PER_SEC
            << std::endl;

  prgstart = clock();
  quicksort(a, 0, arraySize - 1);
  prgend = clock();

  std::cout << "Runtime (presorted/worst case):" 
            << (float) (prgend - prgstart) / CLOCKS_PER_SEC
            << std::endl;
  exit(0);
}
