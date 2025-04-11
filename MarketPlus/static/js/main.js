// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        
        const symbol = document.querySelector('input[name="symbol"]').value;
        const outputsize = document.querySelector('select[name="outputsize"]').value;

        // Provide user feedback about the symbol being processed
        alert('Fetching data for ' + symbol + ' with ' + outputsize + ' data size.');

        // This part is optional: you could also dynamically display a loading message
        // or handle UI updates here if you are going to modify the page using AJAX
    });

    // Optionally, add functionality for handling AJAX requests (if you want to make it dynamic)
    // For example, if you plan to fetch data via AJAX and update the page without a reload:
    // function fetchData(symbol, outputsize) {
    //     fetch('/your-api-endpoint', {
    //         method: 'POST',
    //         headers: { 'Content-Type': 'application/json' },
    //         body: JSON.stringify({ symbol: symbol, outputsize: outputsize })
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         // Update the page with the returned data (e.g., stock chart, table, etc.)
    //     })
    //     .catch(error => {
    //         console.error('Error:', error);
    //         alert('An error occurred while fetching stock data.');
    //     });
    // }
});
