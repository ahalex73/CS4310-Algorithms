#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
 
int main() {
     struct timeval tt;
     long tsec,tusec;
     int f,i,j,num_it = 10000000;
     double u[10],x[10];
     float e;
     unsigned short xs[3];

     xs[0] = 1;
     xs[1] = 2;
     xs[2] = 3;

     f = gettimeofday(&tt,0);
     tsec = tt.tv_sec;
     tusec = tt.tv_usec;

     for(j=0;j<num_it;j++)
     /* section to be timed */
     for(i=0;i<10;i++) {
        u[i] = erand48(xs); // random number in the range (0,1)
        x[i] = 2*u[i] - 1; // random number in the range (-1,1)
     }

     f = gettimeofday(&tt,0);
     printf("Random numbers u, x:\n");
     for(i=0;i<10;i++) printf("%le %le\n",u[i],x[i]);

     printf("Elapsed:\n");         
     e = (float)(tt.tv_sec - tsec) + (float)(tt.tv_usec - tusec)/1000000;
     e = e/num_it;
     printf("= %g seconds\n",e);

}