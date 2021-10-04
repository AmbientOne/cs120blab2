/*	Author: aabdi005
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #2  Exercise #1
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
	DDRA = 0x00; PORTA = 0xFF;
	DDRB = 0x00; PORTB = 0xFF;
	DDRC = 0x00; PORTC = 0xFF;
	DDRD = 0xFF; PORTD = 0x00;

	unsigned char tmpA = 0x00;
	unsigned char tmpB = 0x00;
	unsigned char tmpC = 0x00;
	unsigned char tmpD = 0x00;
	unsigned short totalWeight = 0x00;
	

    /* Insert your solution below */
    while (1) {
	tmpA = PINA;
	tmpB = PINB;
	tmpC = PINC;

	totalWeight = tmpA + tmpB + tmpC;
	if(totalWeight > 140){
	   tmpD = (tmpD | 0x01);
	}
	else {	
		tmpd = (tmpD | 0x02);
	}
	
	if ((tmpA - tmpC) > 80 || (tmpC - tmpA) > -80) {
		tmpD = (tmpd | 0x02);
	}else {
		tmpD = tmpD | 0x02;
	}
	
	PORTD = tmpD;	 
	
	}
    return 0;
}
