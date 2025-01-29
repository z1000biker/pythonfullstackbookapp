# pythonfullstackbookapp
# Book List Application

This project consists of two parts: a frontend built with HTML/JavaScript and a backend using Flask. Below is a description of what each part does and how they work together.

## Frontend (HTML/JavaScript)

1. **HTML Structure**: The HTML code creates a simple page that contains a list of books and a form for adding new books. There is also a button for adding or updating books.

2. **JavaScript Functions**:
   - **`fetchBooks()`**: This function calls the API to retrieve the list of books and displays them on the page.
   - **`createEditButton(bookId)`**: Creates an "Edit" button for each book, which calls the `editBook()` function when clicked.
   - **`createDeleteButton(bookId)`**: Creates a "Delete" button for each book, which calls the `deleteBook()` function when clicked.
   - **`addBook()`**: This function sends a POST request to the API to add a new book.
   - **`editBook(bookId)`**: Fetches the details of the book to be edited and populates the form with those details.
   - **`updateBook()`**: Sends a PUT request to the API to update the details of a book.
   - **`deleteBook(bookId)`**: Sends a DELETE request to the API to remove a book.
   - **`clearForm()`**: Clears the form and resets the current book ID.

3. **Automatic Book Loading**: When the page loads, `fetchBooks()` is called to display the books.

## Backend (Flask)

1. **Creating the Flask App**: The code creates a Flask application and enables CORS to allow requests from other origins.

2. **Book Data**: It has a list of books containing objects with `id`, `title`, and `author`.

3. **API Routes**:
   - **`GET /api/books`**: Returns the list of all books.
   - **`GET /api/books/<int:book_id>`**: Returns the details of a specific book based on its ID.
   - **`POST /api/books`**: Adds a new book to the list.
   - **`PUT /api/books/<int:book_id>`**: Updates the details of a book based on its ID.
   - **`DELETE /api/books/<int:book_id>`**: Deletes a book based on its ID.

There is also a version of frontend in index1.html. This version is using Async Javascript
## Using Async Functions

Using `async` functions in JavaScript can improve the readability and maintainability of your code, especially when dealing with asynchronous operations like fetching data from an API. Here are the key changes made to the code:

1. **Async/Await**: The functions that perform API calls are now declared as `async`, allowing the use of `await` to pause execution until the promise is resolved.

2. **Error Handling**: Each asynchronous function includes a `try/catch` block to handle potential errors during fetch operations.

3. **Awaiting Fetch Calls**: The code uses `await` when calling `fetchBooks()` after adding, updating, or deleting a book to ensure the book list is updated correctly.

The code allows users to view a list of books, add new books, edit existing ones, and delete books. Communication between the frontend and backend occurs via HTTP requests, and changes to the books are stored in the memory of the Flask application.
Greek Version
# Εφαρμογή Λίστας Βιβλίων

Αυτό το έργο αποτελείται από δύο μέρη: ένα frontend που έχει κατασκευαστεί με HTML/JavaScript και ένα backend που χρησιμοποιεί Flask. Ακολουθεί μια περιγραφή του τι κάνει το κάθε μέρος και πώς συνεργάζονται.

## Frontend (HTML/JavaScript)

1. **Δομή HTML**: Ο κώδικας HTML δημιουργεί μια απλή σελίδα που περιέχει μια λίστα βιβλίων και μια φόρμα για την προσθήκη νέων βιβλίων. Υπάρχει επίσης ένα κουμπί για την προσθήκη ή την ενημέρωση βιβλίων.

2. **Λειτουργίες JavaScript**:
   - **`fetchBooks()`**: Αυτή η συνάρτηση καλεί το API για να πάρει τη λίστα των βιβλίων και να την εμφανίσει στη σελίδα.
   - **`createEditButton(bookId)`**: Δημιουργεί ένα κουμπί "Επεξεργασία" για κάθε βιβλίο, το οποίο καλεί τη συνάρτηση `editBook()` όταν πατηθεί.
   - **`createDeleteButton(bookId)`**: Δημιουργεί ένα κουμπί "Διαγραφή" για κάθε βιβλίο, το οποίο καλεί τη συνάρτηση `deleteBook()` όταν πατηθεί.
   - **`addBook()`**: Αυτή η συνάρτηση στέλνει ένα αίτημα POST στο API για να προσθέσει ένα νέο βιβλίο.
   - **`editBook(bookId)`**: Φέρνει τα στοιχεία του βιβλίου που θέλουμε να επεξεργαστούμε και τα τοποθετεί στη φόρμα.
   - **`updateBook()`**: Στέλνει ένα αίτημα PUT στο API για να ενημερώσει τα στοιχεία ενός βιβλίου.
   - **`deleteBook(bookId)`**: Στέλνει ένα αίτημα DELETE στο API για να διαγράψει ένα βιβλίο.
   - **`clearForm()`**: Καθαρίζει τη φόρμα και επαναφέρει το ID του τρέχοντος βιβλίου.

3. **Αυτόματη φόρτωση βιβλίων**: Όταν φορτώνει η σελίδα, καλείται η `fetchBooks()` για να εμφανιστούν τα βιβλία.

## Backend (Flask)

1. **Δημιουργία Flask App**: Ο κώδικας δημιουργεί μια εφαρμογή Flask και ενεργοποιεί το CORS για να επιτρέπει αιτήματα από άλλες προελεύσεις.

2. **Δεδομένα Βιβλίων**: Έχει μια λίστα με βιβλία που περιέχει αντικείμενα με `id`, `title` και `author`.

3. **Διαδρομές API**:
   - **`GET /api/books`**: Επιστρέφει τη λίστα όλων των βιβλίων.
   - **`GET /api/books/<int:book_id>`**: Επιστρέφει τα στοιχεία ενός συγκεκριμένου βιβλίου με βάση το ID του.
   - **`POST /api/books`**: Προσθέτει ένα νέο βιβλίο στη λίστα.
   - **`PUT /api/books/<int:book_id>`**: Ενημερώνει τα στοιχεία ενός βιβλίου με βάση το ID του.
   - **`DELETE /api/books/<int:book_id>`**: Διαγράφει ένα βιβλίο με βάση το ID του.
   - 
Υπάρχει μια έκδοση με Javascript Async functions στο αρχείο index1.html
## Χρήση Async Functions

Η χρήση των `async` συναρτήσεων στην JavaScript μπορεί να βελτιώσει την αναγνωσιμότητα και τη συντηρησιμότητα του κώδικα σας, ειδικά όταν ασχολείστε με ασύγχρονες λειτουργίες όπως η λήψη δεδομένων από ένα API. Ακολουθούν οι βασικές αλλαγές που έγιναν στον κώδικα:

1. **Async/Await**: Οι συναρτήσεις που εκτελούν κλήσεις API έχουν δηλωθεί ως `async`, επιτρέποντας τη χρήση του `await` για να σταματήσει η εκτέλεση μέχρι να επιλυθεί η υπόσχεση.

2. **Διαχείριση Σφαλμάτων**: Κάθε ασύγχρονη συνάρτηση περιλαμβάνει ένα μπλοκ `try/catch` για να διαχειριστεί πιθανά σφάλματα κατά τη διάρκεια των λειτουργιών fetch.

3. **Αναμονή Κλήσεων Fetch**: Ο κώδικας χρησιμοποιεί `await` όταν καλεί τη `fetchBooks()` μετά την προσθήκη, ενημέρωση ή διαγραφή ενός βιβλίου για να διασφαλίσει ότι η λίστα βιβλίων ενημερώνεται σωστά.

## Λειτουργία

Ο κώδικας επιτρέπει στους χρήστες να δουν μια λίστα βιβλίων, να προσθέσουν νέα βιβλία, να επεξεργαστούν υπάρχοντα και να διαγράψουν βιβλία. Η επικοινωνία μεταξύ του frontend και του backend γίνεται μέσω αιτημάτων HTTP, και οι αλλαγές στα βιβλία αποθηκεύονται στη μνήμη της εφαρμογής Flask.

