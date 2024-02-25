/* Compile this file as:    gcc rand1.c -lm        */
#include <stdio.h>

int main() {
        extern int rand(),srand();
        int numweights,scale,seed,i,t,x;
        printf("input number of weights, scale, seed\n");
        scanf("%d %d %d",&numweights,&scale,&seed);

        srand(seed);
        for(i=0;i<numweights;i++) {
           x = rand();
           t = x%scale;
           printf("%d %d\n",x,t);
        }
}