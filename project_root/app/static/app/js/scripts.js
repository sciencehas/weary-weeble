```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const uploadForm = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const listView = document.getElementById('list-view');
    const editButton = document.getElementById('edit-button');
    const deleteButton = document.getElementById('delete-button');
    const saveButton = document.getElementById('save-button');

    uploadForm.addEventListener('submit', (e) => {
        e.preventDefault();
        let files = fileInput.files;
        if (files.length > 0) {
            let formData = new FormData();
            for (let i = 0; i < files.length; i++) {
                formData.append('files[]', files[i]);
            }
            fetch('/upload', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                listView.innerHTML = '';
                data.forEach(item => {
                    let listItem = document.createElement('li');
                    listItem.textContent = item.content;
                    listView.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error:', error));
        }
    });

    listView.addEventListener('click', (e) => {
        if (e.target.tagName === 'LI') {
            let content = e.target.textContent;
            fetch('/view', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({content: content}),
            })
            .then(response => response.json())
            .then(data => {
                window.location.href = '/view';
            })
            .catch((error) => {
                console.error('Error:', error);
            });
        }
    });

    editButton.addEventListener('click', (e) => {
        let selectedItems = listView.querySelectorAll('li.selected');
        selectedItems.forEach(item => {
            item.contentEditable = true;
            item.focus();
        });
    });

    deleteButton.addEventListener('click', (e) => {
        let selectedItems = listView.querySelectorAll('li.selected');
        selectedItems.forEach(item => {
            listView.removeChild(item);
        });
    });

    saveButton.addEventListener('click', (e) => {
        let items = listView.querySelectorAll('li');
        let contents = [];
        items.forEach(item => {
            contents.push(item.textContent);
        });
        fetch('/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({contents: contents}),
        })
        .then(response => response.json())
        .then(data => {
            window.location.href = '/view';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
```