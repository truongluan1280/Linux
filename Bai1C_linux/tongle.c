#include<stdio.h>
#include<math.h>
void tongle(int n)
{
	int s=0;
	for (int i=1;i<=n;i++)
	{
		if(i%2!=0)
		{
			s=s+i;
		}
	}
printf("tong cac so le tu 1 >>> 100 : %d ",s);
}
