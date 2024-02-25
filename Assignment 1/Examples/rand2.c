/* Compile this file as:    cc rand2.c -lm        */
#include <stdio.h>

int main() {
        int namelen,num,seed;
        void nrand();
        printf("input string length, number of strings, seed\n");
        scanf("%d %d %d",&namelen,&num,&seed);
        nrand(namelen,num,seed);
}

void nrand(namelen,num,seed)
int namelen,num,seed;
{	
	int i,j,x,t;
        int val = 4;
        extern int rand(),srand();

	srand(seed);
        for(i=0;i<num;i++) {
          for(j=0;j<namelen;j++) {
            x = rand();
            t = x%val;
            if(t == 0) printf("%c",'A');
            if(t == 1) printf("%c",'T');
            if(t == 2) printf("%c",'G');
            if(t == 3) printf("%c",'C');
          }
          printf("\n");
        }
}      