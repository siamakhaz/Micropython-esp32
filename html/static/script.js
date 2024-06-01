document.addEventListener('DOMContentLoaded', function() {
    const connectButton = document.getElementById('connect');
    const outputRadioButtons = document.getElementsByName('output');
    const adaptiveCheckbox = document.getElementById('adaptive');
    const stimulationOptions = document.getElementById('stimulation-options');
    const behavioralOptions = document.getElementById('behavioral-options');
    const adaptiveOptions = document.getElementById('adaptive-options');
    
    // Handle Connect button click
    connectButton.addEventListener('click', function() {
        const rat_id = document.getElementById('rat_id').value;
        const save_location = document.getElementById('save_location').value;
        const calibration_file = document.getElementById('calibration_file').value;

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                rat_id: rat_id,
                save_location: save_location,
                calibration_file: calibration_file
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                alert('MotoTrak connected successfully!');
            }
        });
    });

    // Handle output mode change
    outputRadioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            if (radio.value === 'Stimulation') {
                stimulationOptions.style.display = 'block';
                behavioralOptions.style.display = 'none';
            } else {
                stimulationOptions.style.display = 'none';
                behavioralOptions.style.display = 'block';
            }
        });
    });

    // Handle adaptive mode change
    adaptiveCheckbox.addEventListener('change', function() {
        if (adaptiveCheckbox.checked) {
            adaptiveOptions.style.display = 'block';
        } else {
            adaptiveOptions.style.display = 'none';
        }
    });

    // Fetch and display plot
    fetch('/plot')
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('plot').src = data.plot_url;
        }
    });
});
