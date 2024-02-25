#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
 
int main()
{
     struct timeval tt;
     long tsec,tusec;
     int f,i,x;
     float e;

     x = 0;
     f =  gettimeofday(&tt,0);
     tsec = tt.tv_sec;
     tusec = tt.tv_usec;

     for(i=0;i<100000000;i++) x = x+1;

     f =  gettimeofday(&tt,0);
     printf("Elapsed: %ld seconds and %ld microseconds\n",          
                      tt.tv_sec-tsec,tt.tv_usec-tusec);
     e = (float)(tt.tv_sec - tsec) + (float)(tt.tv_usec - tusec)/1000000;
     printf("= %g seconds\n",e);
     exit(0);
}



