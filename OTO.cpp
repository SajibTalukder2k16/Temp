#include<bits/stdc++.h>
using namespace std;
#define fileread freopen("input_oto.txt","r",stdin);
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
    double ipi[n+1]={0};
    double cdf_ipi[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        pk[i]=ara[i]/sum;
        ipi[i]=(double)(i-1)*pk[i];
        cdf_ipi[i]=ipi[i]+cdf_ipi[i-1];
        cdf[i]=pk[i]+cdf[i-1];
    }
    double  val = cdf_ipi[n];
    double m_p1_mul_mg_sq[n+1]={0};
    double sigma_square[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        double temp = cdf_ipi[i] - cdf[i]*val;
        temp=temp*temp;
        m_p1_mul_mg_sq[i]=temp;
        sigma_square[i]=(m_p1_mul_mg_sq[i])/(cdf[i]*(1-cdf[i]));
    }
    cout<<"i\tn_i\tp_i\tP1\ti*pi\tm\t(m-p1*m_g)^2\tsigma2_B"<<endl;
    for(int i=1;i<=n;i++)
    {
        printf("%d\t%d\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\t %.4f\n",i,ara[i],pk[i],cdf[i],ipi[i],cdf_ipi[i],m_p1_mul_mg_sq[i],sigma_square[i]);
    }

}
