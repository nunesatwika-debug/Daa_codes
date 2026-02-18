#include <stdio.h>
int main(){
    int n,i,j,minind,temp,count=0,k;
    printf("Enter the size of the array");
    scanf("%d",&n);
    int a[n];
    printf("Enter the array:");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("Array Before pass 1 is: ");
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    for(i=0;i<n-1;i++){
        minind=i;
        for(j=i+1;j<n;j++){
            count++;
            if(a[minind]>a[j]){
                minind=j;
            }
        }
        temp=a[i];
        a[i]=a[minind];
        a[minind]=temp;
        printf("\nArray after pass %d is: ",i+1);
        for(k=0;k<n;k++){
        printf("%d ",a[k]);
    }
    }
    printf("\nNo of time loop runs is : %d",count);
    printf("\nSorted array is: ");
    for(i=0;i<n;i++){
        printf("%d ",a[i]);
    }
    return 0;
}