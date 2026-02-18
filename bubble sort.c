#include <stdio.h>
int main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d",&n);
    printf("Enter the array\n");
    int a[n],i,j,k,temp,count=0;
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("Array before pass 1:");
    for(i=0;i<n;i++){
        printf(" %d",a[i]);
    }
    for(i=0;i<n-1;i++){
        for(j=0;j<n-i-1;j++){
            count++;
            if(a[j]>a[j+1]){
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
        }
        printf("\nArray after pass %d:",i+1);
        for(k=0;k<n;k++){
        printf(" %d",a[k]);
        }
    }
    printf("\nNo of times loop ran:%d\n",count);
    printf("Sorted array is: ");
    for(i=0;i<n;i++){
        printf(" %d",a[i]);
    }
    return 0;
}

