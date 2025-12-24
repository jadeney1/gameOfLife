Conway's Game of Life with different survival and rebirth rates. 
<br>
<br>
Each pixel is randomly selected to begin either on or off. 
<br>
<br> 
Parameters are labelled $(l, u, r)$ where all are greater than zero and less than eight, weakly. Lower is weakly less than upper.
<br>
<br>
Each pixel has $8$ neighbors (using the Torodial topology). An "on" pixel turns off if the total number of on neighbors exceeds $u$ or is below $l$ (strictly). An "off" pixel turns on if its total number of on neighbors exactly matches $r$. Otherwise, the pixel remains in its same state as the previous stage.
<br>
<br>
Conway's initial parameters were $(l, u, r) = (2,3,3)$.
<br>
<br>
This code was generated pretty much entirely by ChatGPT
