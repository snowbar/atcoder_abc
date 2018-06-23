#include <stdio.h>
int main(void){

    int sum=0;
    int c = getchar();

    for(int i;i<4;i++){
        switch(c){
        case '+': sum++;
                  break;
        case '-': sum--;
                  break;
        }
        c = getchar();
    }
    printf("%d\n",sum);
    return 0;
}
