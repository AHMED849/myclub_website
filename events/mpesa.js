// static/js/mpesa.js

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('initiate-stk-push').addEventListener('click', function() {
        fetch('/events/initiate_stk_push/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                phone_number: '0114521175',
                amount: 5,
                payment_type: 'till_number'
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
