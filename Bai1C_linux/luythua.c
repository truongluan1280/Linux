#include<stdio.h>
#include<math.h>
void luythua(int x,int n)
{
	int p=1;
	for(int i =1;i<=n;i++)
	{
		p=p*x;
	}
	printf("luy thua cua %d ^ %d la :%d ",x,n,p);
}
