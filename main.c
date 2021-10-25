
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

const int N=100;
const float J=1;
const float T=2;


unsigned long genrand_int32();    // declaring the mersene-twister functions

double genrand_real1(void);
void init_genrand(unsigned long );

/******magnetization********/

long double mag(int present[N][N])
{
long double mag=0;

for(int i=0;i<N;i++)
    {   for(int j=0;j<N;j++)
            {
               mag=mag+present[i][j];
             }

    }

return(mag/(N*N));
}

//energy difference for each prespective spin flip
 double  deltaE(int lattice[N][N],int i,int j)
{ 



return( 2*J*lattice[i%N][j%N]*( lattice[i%N][(j+1)%N]+lattice[i%N][(j-1)%N]+lattice[(i+1)%N][j%N]+lattice[(i-1)%N][j%N] ) );


      }




/**********evolve**********/

void evolve(int present[N][N])


{
long unsigned int i,j;

 double ediff;
int counter;
long unsigned int k=1;

//long double kb=1.38*pow(10,-23);
int n=N-1;

long unsigned int max,rand,m;
max=4294967295;
long double kb=1;
long double prob;
//unsigned long s;
time_t seconds; 






//FILE *file;
//file = fopen ("data450_T=1.txt","w");






    while(k>0)
{  
    seconds = time(NULL); //seeding mtwister
//seconds=seconds+k;
init_genrand(seconds+k);

  
m=max%(n+1);


do{rand=genrand_int32(); }  //casting the random no genearator to a range ,naive and wrong implementation ,needs refinement
  while(rand>=max-m);
  i=rand%(n+1);



do{rand=genrand_int32();}
  while(rand>=max-m);
   j=rand%(n+1);


ediff=deltaE( present,i,j);



//double r= genrand_real1(); //random real number in [0,1]

//prob=expl(-(Ediff)/(kb*T));



if( ediff < 0 ||  genrand_real1() < expl(-ediff/T))

          {  present[i][j]=-present[i][j];}







//fprintf (file, "spins flipped= %lu\tmagnetization=%Lf\n",k,magnetization);
 

//printf("\n");



printf("\033[H\033[J"); //clearing the screen



for(i=0;i<N;i++)     //printing the matrix
          {   counter=0;
		  for(j=0;j<N;j++)

                  {if(present[i][j]==1)  printf("\033[07m  \033[m");
			  else printf("  ");	  //printf("\t%d",next[i][j]);
			  counter++;
			  if (counter==N){ printf("\n");}  // printf("\n");printf("\n");}
		  }

           } 

//printf("i=%lu\tj=%lu\tgeneration=%lu\tEdiff=%Lf\tmagnetization=%Lf",i,j,k,Ediff,magnetization);
//count++;
k++;


usleep(9100);
}
//fclose(file);

}





int main()

{
time_t seconds;

    seconds = time(NULL); //seeding mtwister
init_genrand(seconds);



int RANDOM[N][N];
int i,j;

for(i=0;i<N;i++)

  {for(j=0;j<N;j++)
	{  unsigned long ran=genrand_int32();

           if(ran%2==0) RANDOM[i][j]=1;
           else RANDOM[i][j]=-1;
             
        }
}
//printf("%Lf",energy(RANDOM));
 evolve(RANDOM);
}
































