let heartList = '';
const n = 99;
for (let i = 0; i <= n; i++) {
    heartList += `
      <svg t="1587910011145" class="icon" viewBox="0 0 1024 1024" version="1.1" 
           xmlns="http://www.w3.org/2000/svg" p-id="1253" width="32" height="32" fill="${getRandomColor()}">
        <path d="M677.51936 192.03072c113.1008 0 204.8 91.6992 204.8 204.77952 0 
                 186.91072-370.3296 435.15904-370.3296 435.15904S141.68064 592.67072 141.68064 
                 396.81024c0-140.78976 91.6992-204.77952 204.77952-204.77952 68.11648 0 
                 128.28672 33.40288 165.5296 84.55168C549.24288 225.4336 609.41312 192.03072 
                 677.51936 192.03072z" p-id="1254"
        ></path>
      </svg>
    `;
}
document.getElementById('heart').innerHTML = heartList;
function getRandomColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}