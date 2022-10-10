#include <stdio.h>
#include <ctype.h>
#include <string.h>
char stack[20];
int top=-1;
int priority(char ch)
{
    if (ch == '^' || ch == '$')
    {
        return 3;
    }
    else if (ch == '*' || ch == '/')
    {
        return 2;
    }
    else if (ch == '+' || ch == '-')
    {
        return 1;
    }
    else if( ch =='(' || ch== ')'){

        return 0;
    }   
    else
    {
        return -1;
    }
    
}
char peep()
{
    return stack[top];
}
void push(char ch)
{
    stack[++top]=ch;
}
char pop()
{
    return ( stack[top--]);
}
int calci(int first, int second, char ch)
{
    int f= (int)(first);
    int s =(int)(second);
    if (ch=='+')
    {
        return (f+s);
    }
    else if (ch=='-')
    {
        return (f-s);
    }
    else if (ch=='*')
    {
        return (f*s);
    }
    else if (ch=='/')
    {
        return (f/s);
    }
    else if (ch=='^')
    {
        int mul=1;
        for ( int i = 1; i <= s; i++)
        {
           mul=mul*f;
        }
        return mul;
    }
    return 0;
}
int evaluate(char array[20], int len)
{
    top=-1;
    for (int i = len-1; i >=0; i--)
    {
        char ch=array[i];
        if (isalnum(ch))
        {
            stack[++top]=ch-'0';
        }
        else
        {
            int first= stack[top--];
            int second =stack[top--];
            push(calci(first,second,ch));
        }
    }
    return(pop());
}
void strre(char s[],int len)
{
    char temp;
    for (int i = 0; i < len/2; i++)
    {
        temp=s[i];
        s[i]=s[len-1-i];
        s[len-1-i]=temp;
    }   
}
void infix_prefix(char infix[20],  int len,char postfix[20])
{
    int  i=0,j=0, p,n;
    char ch;
    push('[');
    strre(infix,len);
    while (infix[i]!='\0')
    {
        ch= infix[i];
        if (isalnum(ch) || ch==')')
        {    
            if(ch==')')
              stack[++top]=ch;
            else
            postfix[j++]=ch;
        }
        else if (ch=='(')
        {
            while ( peep() != ')' )
               {
                    postfix[j++]=pop();
               }
               pop();
        }
        else
        {
            p= priority(ch); 
            if (p <  priority (peep()))
            {        
               while (peep() != '[' )
               {
                    if (p == priority (peep()))
                    {
                        break;
                    }            
                    postfix[j++]=pop();
               }
               stack[++top]=ch;
            }
            else
            {
                stack[++top]=ch;
            }     
        }
        i++;
    }
    while (peep() != '[') 
    {
        postfix[j++]=pop();
    }
    len= strlen(postfix);
    strre(postfix,len);
    printf("%s \n", postfix);
}
int main()
{
    char infix[20]={'\0'};
    char postfix[20]={'\0'};
    int len;
    scanf("%s", infix);
    len= strlen(infix);
    infix_prefix(infix,len,postfix);
    printf("%d\n", evaluate(postfix, len)) ;
    
}