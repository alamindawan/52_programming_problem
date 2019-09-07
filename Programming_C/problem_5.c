#include <stdio.h>
#include <stdlib.h>

int main()
{
    int c, a;
    scanf("%d",&c);
    for(int i = 1; i <= c; i++){
        scanf("%d",&a);
        for(int j = 1; j <= a; j++){
            for(int j = 1; j <= a; j++){
                printf("*");
            }
            printf("\n");
        }
        if(i!=c){
            printf("\n");
        }
    }
}
