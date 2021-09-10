#include<bits/stdc++.h>
using namespace std;
#define fileread freopen("input.txt", "r", stdin);
#define filewrite freopen("output.txt", "w", stdout);
int r,c;
char grid[101][101];
bool first=false;
int check(int i,int j)
{
    int cnt=0;
    ///upper row
    if(i-1>=1)
    {
        //upper left
        if(j-1>=1)
        {
            if(grid[i-1][j-1]=='*')
                cnt++;
        }
        if(grid[i-1][j]=='*')
            cnt++;
        if(j+1<=c)
        {
            if(grid[i-1][j+1]=='*')
                cnt++;
        }
    }
    ///current row
    if(j-1>=1)
    {
        if(grid[i][j-1]=='*')
            cnt++;
    }
    if(j+1<=c)
    {
        if(grid[i][j+1]=='*')
            cnt++;
    }
    ///lower row
    if(i+1<=r)
    {
        if(j+1>=1)
        {
            if(grid[i+1][j-1]=='*')
                cnt++;
        }
        if(grid[i+1][j]=='*')
            cnt++;
        if(j+1<=c)
        {
            if(grid[i+1][j+1]=='*')
                cnt++;
        }
    }
    return cnt;
}
int main()
{
    //fileread
    //filewrite
    int field=1;
    while(true)
    {
        cin>>r>>c;
        if(r==0 && c==0)
        {
            return 0;
        }
        if(first==true)
            cout<<endl;
        first=true;
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                cin>>grid[i][j];
            }
        }
        cout<<"Field #"<<field++<<":"<<endl;
        for(int i=1;i<=r;i++)
        {
            for(int j=1;j<=c;j++)
            {
                if(grid[i][j]=='*')
                    cout<<'*';
                else
                    cout<<check(i,j);
            }
            cout<<endl;
        }
        //cout<<endl;
    }

}
