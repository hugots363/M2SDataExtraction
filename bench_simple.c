//#include <stdio.h>

int main(){	
	float array[64];
	int i = 0;
	printf("Adreça del vector: vector[0] -> %x \n", & array[0]);
    	printf("Adreça del vector: vector[63] -> %x \n", & array[63]);
	for(i = 0; i < 64;i++ )
	{
		array[i] = 3.14;
	}
       	return 0;
    	}
