/* Author: Simon Westphahl <westphahl@gmail.com>
 * Description: Insertion sort with average vs. best case comparison
 * License: Public Domain
 */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertion_sort(int arr[], unsigned int n) {
    int i, j, x;

    for (i = 1; i < n; i++) {
        x = arr[i];
                        
        for (j = i - 1; ((j >= 0) && (x < arr[j])); j--) {
            arr[j + 1] = arr[j];
        }
                                                            
    arr[j + 1] = x;
    }
}


int main(void)
{
    int *a, i;
    unsigned int n = 100000;
    clock_t prgstart, prgend;
    a = (int*) malloc(sizeof(int)*n);
   
    for (i = 0; i < n; i++) {
        a[i] = rand();
    }

    prgstart = clock();
    insertion_sort(a, n);
    prgend = clock();

    printf("Runtime (unsorted): %.5f s\n", (float) (prgend-prgstart) / CLOCKS_PER_SEC);

    prgstart = clock();
    insertion_sort(a, n);
    prgend = clock();

    printf("Runtime (presorted): %.5f s\n", (float) (prgend-prgstart) / CLOCKS_PER_SEC);

    free(a);
    return 0;
}
