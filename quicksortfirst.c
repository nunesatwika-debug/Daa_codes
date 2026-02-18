#include <stdio.h>

void quicksort(int a[],int low,int high);

int main()
{
    int n;
    printf("Enter the no of elements: ");
    scanf("%d",&n);
    int a[n],i;
    printf("Enter the elements: ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    quicksort(a,0,n-1);
    printf("Sorted array is: ");
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    return 0;
}

void quicksort(int a[],int low,int high){
    int i,j,pivot,temp;
    if(low<high){
        i=low;
        j=high;
        pivot=low;
        while(i<j){
            while(i<=high && a[pivot]>=a[i]){
                i++;
            }
            while(a[pivot]<a[j]){
                j--;
            }
            if(i<j){
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
        temp=a[j];
        a[j]=a[pivot];
        a[pivot]=temp;
        
    quicksort(a,low,j-1);
    quicksort(a,j+1,high);
    }
}