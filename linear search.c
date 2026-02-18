#include <stdio.h>
 
int main()
{
    int n;
    printf("Enter the no of elemets in the array:");
    scanf("%d",&n);
    printf("Enter the array\n");
    int a[n],i,key,flag=0;
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    printf("Enter the element to be searched");
    scanf("%d",&key);
    for(i=0;i<n;i++){
        if(a[i]==key){
            printf("Element %d found at pos %d",key,i+1);
            flag=1; 
            break;
        }
    }
    if(flag==0){
        printf("Element not found in the array");
    }
    return 0;
}