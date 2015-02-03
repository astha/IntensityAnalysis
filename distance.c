#include <stdio.h>
#include <string.h>
#include <math.h>
#include <malloc.h>

const int max_size=2000;
const int N=40;
const int max_w=50;

int main(int argc, char **argv)
{
    FILE *f;
    char st1[max_size], bestw[N][max_size], file_name[max_size];
    float dist, len, bestd[N];
    int words, size, a, b, c, d;
    float *M;
    char *vocab;
    
    if (argc<2) {
	printf("Usage: ./dist <FILE>\nwhere FILE contains word projections\n");
	return 0;
    }
    
    strcpy(file_name, argv[1]);
    
    f=fopen(file_name, "rb");
    if (f==NULL) {printf("Input file not found\n"); return -1;}
    fscanf(f, "%d", &words);
    fscanf(f, "%d", &size);
	
    vocab=(char *)malloc(words*max_w*sizeof(char));
    M=(float *)malloc(words*size*sizeof(float));
    if (M==NULL) {
        printf("Cannot allocate memory: %ld MB\n", words*size*sizeof(float)/1048576); 
        return -1;
    }
    
    for (b=0; b<words; b++) {
        fscanf(f, "%s", &vocab[b*max_w]);
        for (a=0; a<size; a++) fscanf(f, "%f", &M[a+b*size]);
        len=0;
        for (a=0; a<size; a++) len+=M[a+b*size]*M[a+b*size];
        len=sqrt(len);
        for (a=0; a<size; a++) M[a+b*size]/=len;
    }

    for (a=0; a<words*max_w; a++) vocab[a]=toupper(vocab[a]);
    fclose(f);
    
    while (1) {
    	for (a=0; a<N; a++) bestd[a]=0;
    	for (a=0; a<N; a++) bestw[a][0]=0;
    
	printf("Enter word (EXIT to terminate): ");
	scanf("%s", st1);
	for (a=0; a<strlen(st1); a++) st1[a]=toupper(st1[a]);
	if (!strcmp(st1, "EXIT")) break;
    
	for (b=0; b<words; b++) if (!strcmp(&vocab[b*max_w], st1)) break;
	
	if (b==words) printf("Word was not found in dictionary\n");
	else {
	    for (c=0; c<words; c++) {
		dist=0;
		for (a=0; a<size; a++) dist+=M[a+b*size]*M[a+c*size];

		for (a=0; a<N; a++) {
		    if (dist>bestd[a]) {
			for (d=N-1; d>a; d--) {
			    bestd[d]=bestd[d-1];
			    strcpy(bestw[d], bestw[d-1]);
			}
			bestd[a]=dist;
			strcpy(bestw[a], &vocab[c*max_w]);
			break;
		    }
		}
	    }
	
	    printf("Closest words:\n");
	    for (a=0; a<N; a++) printf("%20s\t\t%f\n", bestw[a], bestd[a]);
	}
    }
    
    return 0;
}
