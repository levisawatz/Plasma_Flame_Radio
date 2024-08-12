# Plasma_Flame_Radio


This personal project was my deepest step into RF circuits to date and pushed me to buy an oscilloscope and a vector network analyzer (VNA).


## Part 1: Plasma Flame  
<img src=".\Media\plasma flame.gif" height="200"  />  

My inspiriation from some youtube videos I've watched which show off flashy and dangerous plasma.  
It is a less deadly and budget friendly version of Styropyro's "fire death machine": https://youtu.be/UNisqZOAaAs?si=NMkZ1_NP11LKSfkR&t=481  
The main 10MHz oscillator uses a self resonant ZVS class E amplifier to drive the antenna.  

#### Plasma flame circuit  
<img src=".\Media\flame_ltspice.png" height="300"  />  

## Part 2: 100W+ AM radio transmitter  

I modified the "plasma flame" into an AM radio transmitter. This allowed me to transmit music as AM radio and listen to it using a handheld shortwave radio reciever.  

#### AM radio circuit  

<img src=".\Media\radio circuit.jpg" height="200"  />  

Using this circuit, I can transmit music as AM radio and listen to it using a handheld shortwave radio reciever.  

this circuit uses an audio amplifier to modulate the supply voltage to the RF amplifier. Below are measurements of the mosfet's drain as I feed a sine wave and a square wave into the "audio in" of the circuit. It shows the audio frequency signals modulated with the 10MHz carrier frequency.

<img src=".\Media\AM sine.png" height="200"  />   <img src=".\Media\AM square.png" height="200"  />  

The antenna is tuned and matched using a lumped network to allow for the ideal power to be transfered to the antenna.

### tuning the antenna 

<img src=".\Media\plasma candle antenna vna.jpg" height="200"  />   

A vector network analyzer made it possible analyze and simulate the antenna in order to calculate the bast values for the lumped network.
