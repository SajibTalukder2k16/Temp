#include<bits/stdc++.h>
using namespace std;
#define fileread freopen("input_mat.txt","r",stdin);
vector<int> foo(int ara[],double sum,int n)
{

    double pk[n+1]={0};
    double cdf[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        pk[i]=ara[i]/sum;
        cdf[i]=pk[i]+cdf[i-1];
    }
    cout<<"rk\tnk\tpdf\tcdf\tcdf*(l-1)\tsk"<<endl<<endl<<" ";;
    vector<int>ret(n+1);
    for(int i=1;i<=n;i++)
    {
        //cout<<i<<"\t"<<ara[i]<<"\t"<<"\t"<<pk[i]<<"\t"<<cdf[i]<<endl;
        double val = cdf[i]*(double)(n-1);
        ret[i]=llround(val);

        printf("%d \t %d \t %.2f \t %.2f \t %.2f  \t %d\n ",i-1,ara[i],pk[i],cdf[i],val,llround(val));
    }
    return ret;
}
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
    vector<int>in,target;
    in=foo(ara,sum,n);
    vector<int>unique_val;
    map<int,bool>mp;
    map<int,int>target_mp;;
    for(int i=1;i<=n;i++){
        if(mp[in[i]]==false)
        {
            unique_val.push_back(in[i]);
            mp[in[i]]=true;
        }
    }
    cout<<endl<<endl<<endl;
    sum=0;
    for(int i=1;i<=n;i++)
    {
        cin>>ara[i];
        sum+=ara[i];
    }
    target=foo(ara,sum,n);
    for(int i=1;i<=n;i++)
    {
        target_mp[target[i]]=i-1;
    }
    cout<<endl;
    for(int i=0;i<unique_val.size();i++)
    {
        int temp_val=unique_val[i];
        cout<<temp_val<<"\t";
        if(target_mp[temp_val]!=0)
        {
            cout<<target_mp[temp_val]<<endl;;
        }
        else
        {
            for(int j=1;j<=n;j++)
            {
                if(target[j]>temp_val)
                {
                    if(abs(target[j]-temp_val)<abs(target[j-1]-temp_val))
                    {
                        cout<<target[j]<<endl;
                    }
                    else
                        cout<<target[j-1]<<endl;
                    break;
                }
            }
        }
    }
        //cout<<unique_val[i]<<endl;

}
