# solar_forcaster
This solar forcaster currently takes the data from Solcast for the solar panels facing east and west, combines the data, and will tell me how much I will generate along with a graph. 
However, it has found during the testing that Solcast is not so accurate compared to reality.
There for I am researching to implement: 
1. Kalman filter on the data I will collect on Solcast and from the solar panels - this will give me more accuate data 
2. use this information to email me or provide a notifcation when I need to change the battery charge percentage. It will also notify the home automation of Pi Pico. 
