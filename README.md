# Text-Retrieval-Search-Engine

# Assignment 2

Overview
This README provides an overview of the Information Retrieval System developed as part of Assignment 2 for the course CP423. The system is designed to preprocess text documents, construct a positional index, perform phrase query searches, and compute document relevancy using TF-IDF matrices with various weighting schemes.
Methodology Preprocessing
The preprocessing stage transforms the raw text data to make it suitable for indexing and analysis. The following steps are performed on each document:

1. Lowercasing: Convert all text to lowercase to ensure uniformity.
2. Tokenization: Break the text into words or tokens using NLTK's punkt tokenizer.
3. Stopword Removal: Remove common words that may not contribute significantly to
   text meaning using NLTK’s English stopwords list.
4. Punctuation Removal: Strip punctuation marks to focus solely on words.
5. Whitespace Removal: Eliminate tokens that only contain spaces.
   Positional Index
   A positional index is constructed to enable efficient phrase queries. This index maps each unique word to its positions across all documents. This facilitates quick retrieval of documents that contain exact phrases as specified in a query.
   Phrase Query Search
   The system supports phrase query searches up to a length of five words. It utilizes the positional index to find documents where the query phrase appears exactly as specified.
   TF-IDF Calculation
   TF-IDF (Term Frequency-Inverse Document Frequency) is used to evaluate how important a word is to a document in a corpus. The following steps outline the TF-IDF computation process:
6. Term Frequency (TF): Count how frequently each term appears in a document. Several TF weighting schemes are supported:
   ○ Binary: Indicates the presence or absence of terms.
   ○ Raw Count: Counts the actual occurrences of terms.
   ○ Term Frequency: Normalizes the term count by the total number of terms in
   the document.
   ○ Log Normalization: Applies logarithmic scaling to the term frequency.
   ○ Double Normalization: Normalizes term frequency relative to the highest
   frequency term in a document.
7. Inverse Document Frequency (IDF): Calculate the log of the ratio of the total number of documents to the number of documents containing each term, adjusted for smoothing.
   Cosine Similarity
   Cosine similarity is used to determine how similar two documents (or a document and a query) are in terms of their content. It is calculated by taking the dot product of the TF-IDF vectors of the documents and dividing by the product of their magnitudes.
   Outputs and Analysis
   The system was tested with several queries. For example, the query "data" retrieved 36 documents, indicating that the term is relatively common across the corpus. The different TF-IDF weighting schemes provided varying results:
   ● Binary scheme: Retrieved documents where the term appears, regardless of frequency.
   ● Raw count and term frequency schemes: Highlighted documents where the term is frequent.
   ● Log normalization and double normalization schemes: Offered a balance between presence and frequency, potentially identifying documents where the term is significant but not overly repeated.
   Each scheme has its advantages depending on the search context. Binary is straightforward but less nuanced, while normalization schemes provide a more sophisticated analysis of term significance.
   Conclusion
   This information retrieval system effectively processes, indexes, and searches through a collection of documents, providing a robust tool for exploring large datasets. The flexibility in TF-IDF weighting schemes allows for tailored searches that can adapt to different informational needs and preferences.
