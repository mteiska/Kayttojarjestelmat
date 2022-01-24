#include <stdlib.h>
#include <stdio.h> // define the header file
#include <string.h>

typedef struct lista
{
    char line[120];
    struct lista *pNext;
} LISTA;

int main(int argc, char *argv[]) // komentoriviargumentit jotka otetaan kiinni
{
    size_t linesize = 0;
    char *linebuffer;
    size_t buffersize = 0; // alustetaan getlinea varten muuttujia
    int linecount = 0;
    char *tmp;

    LISTA *pAlku = NULL, *pLoppu = NULL;
    LISTA *pUusi, *ptr;

    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL)
    {
        return 1;
    }

    while (linesize != -1)
    {
        linesize = getline(&linebuffer, &buffersize, fp);
       
        if (linesize == -1) {
            break;
        }
         fprintf(stdout, linebuffer);
        if ((pUusi = (LISTA *)malloc(sizeof(LISTA))) == NULL)
        {
            perror("malloc failed.");
            exit(1);
        }
        
        strcpy(pUusi->line, linebuffer);
        pUusi->pNext = NULL;

        if (pAlku == NULL)
        {
            pAlku = pUusi;
            pLoppu = pUusi;
            
        }
        else
        {
            pLoppu->pNext = pUusi;
            pLoppu = pUusi;
            
        }
       
        
    }
    fclose(fp);
    

    

}