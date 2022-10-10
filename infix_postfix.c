#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


char stack[50];
int top=-1;

int priority(char);
char peep();
int check(char);
void push(char ch);

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
    
    else{
        return 0;
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

void infix_postfix(char infix[50],  int len,char postfix[50])
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
   
    while (peep() != '['  )
    {
        postfix[j++]=pop();
    }

    
    len= strlen(postfix);
    
    printf("%s ", postfix);
}

int main()
{
    char infix[50]={'\0'};
    char postfix[50]={'\0'};
    
    int len;
    
    scanf("%s", infix);
    len= strlen(infix);
    
    infix_postfix(infix,len,postfix);
    
    
    
}