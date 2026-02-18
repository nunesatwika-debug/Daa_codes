#include <stdio.h>
int main()
{
    int n,key,i;
    printf("Enter the no of elements in the array");
    scanf("%d",&n);
    int a[n];
    printf("Enter the Array");
    for(i=0;i<n;i++){
        scanf("\n%d",&a[i]);
    }
    printf("Enter the element to be searched");
    scanf("%d",&key);
    int low=0,high=n-1,mid,found=0;
    while(low<=high){
         mid=(low+high)/2;
         if(a[mid]==key){
             printf("Element found at position %d",mid+1);
             found=1;
             break;
         }
         else if(a[mid]>key){
             high=mid-1;
         }
         else{
             low=mid+1;
         }
    }
    if(found==0){
        printf("Element not found in the array");
    }
    return 0;
}

