#include<stdio.h>
#include<math.h>
void giaithua(int n )
{
	int i,giaithua;
	giaithua =1;
   for(i=1;i<=n;i++)
	{
		giaithua = giaithua*i;
	}
	printf("giai thua cua %d la %d :",n,giaithua);
}
