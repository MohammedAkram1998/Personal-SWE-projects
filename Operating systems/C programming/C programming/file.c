#include <stdio.h>

int main()
{
    int count;
    int c;

    count=0;
    do
    {
        c = getchar();
	if (c == '\n' ) 
        {
            count = count + 1;
	}
    } while (c != EOF);
    
    printf ("The total number of characters is %d\n",count);
}
