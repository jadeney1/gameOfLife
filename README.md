Conway's Game of Life with different survival and rebirth rates. 
<br>
Each pixel is randomly selected to begin either on or off. 
<br> 
Parameters are labelled (lower, upper, rebirth) where all are greater than zero and less than eight, weakly. Lower is weakly less than upper.
<br>
Each pixel has either neighbors. An on pixel turns off if the total number of on neighbors exceeds the upper limit or is below the lower limit. An off pixel turns on if its total number of on neighbors exactly matches the rebirth number. Otherwise, the pixel remains in its same state as the previous stage.
<br>
Conway's initial parameters were (lower, upper, rebirth) = (2,3,3).
