#include <stdio.h>

void quicksort(int a[], int low, int high);

int main()
{
    int n, i;
    printf("Enter the no of elements: ");
    scanf("%d", &n);

    int a[n];
    printf("Enter the elements: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &a[i]);
    }

    quicksort(a, 0, n - 1);

    printf("Sorted array is: ");
    for (i = 0; i < n; i++) {
        printf("%d ", a[i]);
    }
    return 0;
}

void quicksort(int a[], int low, int high)
{
    int i, j, pivot, temp;

    if (low < high) {
        pivot = (low + high) / 2;   // 🔹 MID as pivot
        i = low;
        j = high;

        while (i <= j) {
            while (a[i] < a[pivot])
                i++;
            while (a[j] > a[pivot])
                j--;

            if (i <= j) {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
                i++;
                j--;
            }
        }

        quicksort(a, low, j);
        quicksort(a, i, high);
    }
}
