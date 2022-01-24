    #include <stdlib.h> 
    #include<stdio.h> // define the header file 
    #include<string.h>
    



    int main(int argc, char *argv[])   // komentoriviargumentit jotka otetaan kiinni  
    {  
        size_t linesize = 0;
        char* linebuffer;
        size_t buffersize=0; // alustetaan getlinea varten muuttujia
        char* ptr;
        char filecontent[300]; //Alustan vielä nyt stringin koon.

        FILE* fp =fopen(argv[1], "r");
        if(fp == NULL){
            return 1;
        }
        linesize = getline(&linebuffer,&buffersize, fp); //eka rivi, jotta while true ehto toteutuu

        //ptr = (char*) malloc(linesize *sizeof(char));
        while(linesize >= 0){
        
        fscanf(fp, "%s\n", linebuffer);
    
        fprintf(stdout,linebuffer); 
    
        fflush(stdout);

       

        //linesize = getline(&linebuffer,&buffersize, fp); // uusi rivi
        return 1;
        }

        fclose(fp);
    
       
    }  