#include <netdb.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h> 
#include <unistd.h>

#include <wiringPi.h>
#include <stdio.h>

/*filas -> ENTRADAS
 * columnas -> SALIDAS  */

		//wPi	//fisico
#define f1 6	//22
#define f2 10	//24
#define f3 11	//26
#define f4 31	//28
#define c1 26	//32
#define c2 27	//36
#define c3 28	//38
#define c4 29	//40

#define SERVER_ADDRESS  "127.0.1.1"     /* server IP */
#define PORT            8080 

/* Test sequences */
char buf_tx[2];      
char buf_rx[100];                     /* receive buffer */
 
 int teclado();	//revisa que tecla ha sido pulsada y retorna un valor asociado (fila)(columna)
				/*11 - 12 - 13 - 14
				 *21 - 22 - 23 - 24
				 *31 - 32 - 33 - 34
				 *41 - 42 - 43 - 44*/
                 
/* This clients connects, sends a text and disconnects */
int main() 
{ 
    int sockfd; 
    
    //VARIABLES
	int tecla = 0;
	char opc[2];
	//Setup 
	wiringPiSetup();		//inicializamos wiringPi
	pinMode(f1,INPUT);		//filas 
	pinMode(f2,INPUT);
	pinMode(f3,INPUT);
	pinMode(f4,INPUT);
	pinMode(c1,OUTPUT);		//columnas
	pinMode(c2,OUTPUT);
	pinMode(c3,OUTPUT);
	pinMode(c4,OUTPUT);
    
    struct sockaddr_in servaddr; 
    
    
    
    while(true){
        while(tecla == 0)
            tecla = teclado();
		if(tecla!=0)
			//printf("Presionaste: %d \n",tecla);
		switch(tecla){
			case 11:
				opc[0] = '1';
                opc[1] = '1';
				break;
			case 12:
				opc[0] = '1';
                opc[1] = '2';
				break;
			case 13:
				opc[0] = '1';
                opc[1] = '3';
				break;
			case 14:
				opc[0] = '1';
                opc[1] = '4';
				break;
			case 21:
				opc[0] = '2';
                opc[1] = '1';
				break;
			case 22:
				opc[0] = '2';
                opc[1] = '2';
				break;
			case 23:
				opc[0] = '2';
                opc[1] = '3';
				break;
			case 24:
				opc[0] = '2';
                opc[1] = '4';
				break;
			case 31:
				opc[0] = '3';
                opc[1] = '1';
				break;
			case 32:
				opc[0] = '3';
                opc[1] = '2';
				break;
			case 33:
				opc[0] = '3';
                opc[1] = '3';
				break;
			case 34:
				opc[0] = '3';
                opc[1] = '4';
				break;
			case 41:
				opc[0] = '4';
                opc[1] = '1';
				break;
			case 42:
				opc[0] = '4';
                opc[1] = '2';
				break;
			case 43:
				opc[0] = '4';
                opc[1] = '3';
				break;
			case 44:
				opc[0] = '4';
                opc[1] = '4';
				break;
		}
        
        /* Socket creation */
    sockfd = socket(AF_INET, SOCK_STREAM, 0); 
    if (sockfd == -1) 
    { 
        printf("CLIENT: socket creation failed...\n"); 
        return -1;  
    } 
    else
    {
        printf("CLIENT: Socket successfully created..\n"); 
    }
    
    
    memset(&servaddr, 0, sizeof(servaddr));
    
    /* assign IP, PORT */
        servaddr.sin_family = AF_INET; 
        servaddr.sin_addr.s_addr = inet_addr( SERVER_ADDRESS ); 
        servaddr.sin_port = htons(PORT); 
    
        /* try to connect the client socket to server socket */
        if (connect(sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) != 0) 
        { 
            printf("connection with the server failed...\n");  
            return -1;
        } 
        
        printf("connected to the server..\n"); 
        buf_tx[0] = opc[0];
        buf_tx[1] = opc[1];
        /* send test sequences*/
        write(sockfd, buf_tx, sizeof(buf_tx));     
        //read(sockfd, buf_rx, sizeof(buf_rx));
        //printf("CLIENT:Received: %s \n", buf_rx);
       
        
		tecla = 0; 
		//printf("Pass\n");
        
         /* close the socket */
        close(sockfd); 
	}
    
    
        return 0;
} 

int teclado(){
	int tecla = 0;
	for(int i=0;i<4;i++){	// BLUCLE DE COLUMNAS 
		digitalWrite(c1+i,1);		//MANDA 1'S A LAS COLUMNAS 
		if(digitalRead(f1))			//REVISA FILA 1
			tecla = (1 * 10) + i + 1;
		if(digitalRead(f2))			//REVISA FILA 2
			tecla = (1 * 20) + i + 1;
		if(digitalRead(f3))			//REVISA FILA 3
			tecla = (1 * 30) + i + 1;
		if(digitalRead(f4))			//REVISA FILA 4
			tecla = (1 * 40) + i + 1;
		delay(50);
		digitalWrite(c1+i,0);
	}
	
	return tecla;
}
