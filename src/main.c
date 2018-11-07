/* Simple PWM demonstrator program
 * The program simply ramps the duty of pin 10
 * from 0% to 100%  and then resets back to 0%
 *
 */

#include "lpc111x.h"

void ConfigPins()
{
	SYSAHBCLKCTRL |= BIT6 + BIT16; // Turn on clock for GPIO and IOCON

	// Begin Port 0 setup.
	// Make Port 0 bit 5 behave as a generic output port (open drain)
	IOCON_PIO0_5 |= BIT8;
	// Make Port 0 bit 10 behave as a generic I/O port
	IOCON_SWCLK_PIO0_10  = 1;
	// Make Port 0 bit 11 behave as a generic I/O port
	IOCON_R_PIO0_11  = 1;
	// End Port 0 setup.


	// Make pin 10 behave as a PWM output CT32B1_MAT0
	IOCON_R_PIO1_1 |= BIT1 + BIT0;
}
void initPWM()
{
	// will use counter/timer CT32B1
	// Turn on CT32B1
	SYSAHBCLKCTRL |= BIT10;
	// Use match register 3 as period register because its output
	// is not pinned out.  A value of 48000000 produces a frequency of 1Hz
	// so, to generate a 30kHz pwm signal, set MR3 = 48000000/30000 = 1600
	TMR32B1MR3 = 1600;
	TMR32B1MR0 = 1600; // Zero output to begin with
	TMR32B1MCR = BIT10; // Reset TC on match with MR3
	TMR32B1TC = 0 ; // Zero the counter to begin with
	TMR32B1PWMC = BIT0; // Enable PWM on channel 0
	TMR32B1TCR = 1; // Enable the timer

}
void setDuty(int Duty)
{
	// sets the duty to the percent specified.
	// Need to 'invert' the requested duty as the PWM mechanism
	// resets the output at the start of each PWM cycle and then
	// sets it on match.
	TMR32B1MR0 = (100-Duty) << 4;
}
void delay(int dly)
{
	while(dly--);
}
int main()
{
	int Duty=50;
	ConfigPins();
	initPWM();
	while(1)
	{
		setDuty(Duty++);
		if (Duty > 100){
			for (Duty > 1; Duty--;){
				setDuty(Duty);
				delay(100000);
			}
		}
		delay(100000);
	}
}
