# Document Similarity Detector

This is a Django-based web application that allows users to upload one or multiple doc/pdf files or folders (doc and docx), with a total upload limit of 1GB per project/search. The application uses the transformers pretrained model `stsb-mpnet-base-v2` to ingest documents into a database after the upload is complete.

The purpose of this application is to quickly and effectively process multiple documents that have similarities. All information on each document is searched for duplicate content and then compared to the other documents uploaded. All content of all documents is represented on a categorized interactive list in order of similarity from exact to similar to unique, including any errors or unqualifiable content.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the project root directory.
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Django server:

```bash
python manage.py runserver
```

2. Open your web browser and navigate to `localhost:8000`.
3. Use the upload button to upload your documents.
4. The application will process the documents and display a list of content, categorized by similarity.
5. Select any paragraph/sentence on the list to view it in its original context within the merged document bundle of the uploads.
6. You can delete or change list entries, and the uploaded document will be updated accordingly.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)