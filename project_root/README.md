# Django Document Similarity App

This is a Django web application that allows users to upload one or multiple Word or PDF documents, with a total size not exceeding 1GB per search. The application uses the transformers pretrained model `stsb-mpnet-base-v2` to ingest documents into a database. The purpose of this application is to process multiple documents that have similarities and present the content in an interactive list, categorized by similarity.

## Installation

1. Clone the repository:
```
git clone https://github.com/your-github-username/your-repo-name.git
```

2. Navigate to the project directory:
```
cd your-repo-name
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Run migrations:
```
python manage.py migrate
```

5. Start the server:
```
python manage.py runserver
```

## Usage

1. Open your web browser and navigate to `http://localhost:8000`.

2. Upload your documents. The application will ingest the documents into the database and process them.

3. The content of all documents will be represented in a categorized interactive list, in order of similarity.

4. Select any text on the list to view it in its original context within the merged document bundle of the uploads.

5. You can delete or change list entries. The uploaded document will be updated accordingly.

6. You can create new documents from the remaining text.

## Note

The application is designed for individuals with memory or cognitive issues, to help them easily eliminate unwanted content without losing the original content.

The code for the algorithms used in this application can be found at https://github.com/guenter-r/knn.git. The `reuters` code in this repository is replaced with the database of the ingested documents supplied by the user.

The application processes the uploaded documents as follows:

1. Cleaning data with Regex and NLTK
2. Creating bags of words
3. Ranking and sorting data from dictionaries
4. Creating word to vector instances
5. Merging data into a matrix
6. Identifying related text elements
7. Calculating similarity

All top words are gathered together in a single words vector. Vectors are created for every bag and then all vectors are stacked together to a single matrix. The application uses a simple iteration to find all related documents that are at least x% similar, where x is defined arbitrarily.