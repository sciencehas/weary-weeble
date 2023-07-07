```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const uploadButton = document.querySelector('#uploadButton');
    const fileInput = document.querySelector('#fileInput');
    const resultsList = document.querySelector('#resultsList');

    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (event) => {
        const files = event.target.files;
        uploadFiles(files);
    });

    resultsList.addEventListener('click', (event) => {
        if (event.target && event.target.nodeName == "LI") {
            highlightText(event.target.textContent);
        }
    });
});

function uploadFiles(files) {
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
        formData.append('files[]', files[i]);
    }

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displayResults(data.results);
        } else {
            alert('Error: ' + data.error);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function displayResults(results) {
    resultsList.innerHTML = '';
    results.forEach(result => {
        const li = document.createElement('li');
        li.textContent = result;
        resultsList.appendChild(li);
    });
}

function highlightText(text) {
    const content = document.querySelector('#content');
    const index = content.textContent.indexOf(text);
    if (index >= 0) {
        const range = document.createRange();
        range.setStart(content.firstChild, index);
        range.setEnd(content.firstChild, index + text.length);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        content.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}
```