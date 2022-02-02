#include<bits/stdc++.h>
using namespace std;
#define fileread freopen("input_histo.txt","r",stdin);
int main()
{
    fileread;
    int n;
    cout<<"Enter Size: ";
    cin>>n;
    int ara[n+1];
    cout<<"Enter the no of pixels for each: "<<endl;
    double sum = 0;
    for(int i=1;i<=n;i++)
    {
        cin>>ara[i];
        sum+=ara[i];
    }
    double pk[n+1]={0};
    double cdf[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        pk[i]=ara[i]/sum;
        cdf[i]=pk[i]+cdf[i-1];
    }
    cout<<"rk\tnk\tpdf\tcdf\tcdf*(l-1)\tsk"<<endl<<endl<<" ";;
    for(int i=1;i<=n;i++)
    {
        //cout<<i<<"\t"<<ara[i]<<"\t"<<"\t"<<pk[i]<<"\t"<<cdf[i]<<endl;
        double val = cdf[i]*(double)(n-1);

        printf("%d \t %d \t %.2f \t %.2f \t %.2f  \t %d\n ",i-1,ara[i],pk[i],cdf[i],val,llround(val));
    }
}
