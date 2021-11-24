process.stdin.resume();
process.stdin.setEncoding('utf-8');
let inputString = '';
let currentLine = 0;
process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(str => str.trim());
    main();
});
 
function readLine() {
    return inputString[currentLine++];
}
function allDigitSame(str)
{
    let len=str.length;
    let digit=str[0];
    let cnt=0;
    for(let i=0;i<len;i++)
    {
        if(str[i]===digit)
        {
            cnt++;
        }
    }
    if(cnt===len)
    {
        return true;
    }
    else
    {
        return false;
    }
}
function pallindromeCheck(str)
{
    let len=str.length;
    let half=parseInt(len/2);
    for(let i=0,j=len-1;i<half;i++,j--)
    {
        if(str[i]!=str[j])
        {
            return false;
        }
    }
    return true;
}
function consecutiveCheck(str)
{
    let len=str.length;
    for(let i=1;i<len;i++)
    {
        let previousVal=str[i-1];
        let currentVal=str[i];
        let dif = Math.abs(previousVal-currentVal)
        if(dif===9)
            dif=1;
        if(dif>1)
            return false;
    }
    return true;
}
function uniqueDigitTwice(str)
{
    let len=str.length;
    let digits=[0,0,0,0,0,0,0,0,0,0];
    for(let i=0;i<len;i++)
    {
        let val=str[i];
        digits[val]++;
    }
    for(let i=0;i<10;i++)
    {
        if(!(digits[i]===0||digits[i]===2))
            return false;
    }
    return true;
}
function firstDigitFollow(str)
{
    let len=str.length;
    for(let i=1;i<len;i++)
    {
        if(str[i]!='0')
            return false;
    }
    return true;
}
function main()
{
    let number=readLine();
    let len=number.length;
    if(len<3)
    {
        console.log("No");
    }
    else
    {
        if(allDigitSame(number)||pallindromeCheck(number)||consecutiveCheck(number)||uniqueDigitTwice(number)||firstDigitFollow(number))
        {
            console.log("Yes");
        }
        else
        {
            console.log("No");
        }
    }
    
}
