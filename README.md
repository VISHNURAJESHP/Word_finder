<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>

<body>
    <div class="container">
        <h1>Word_finder</h1>

  <h2>Description</h2>
        <p>This project involves creating a REST API that accepts multiple paragraphs of text as input and stores each paragraph along with word-to-paragraph mappings in a PostgreSQL database. The API also provides functionality to search for specific words and retrieve the top 10 paragraphs where the word is present..</p>

  <h2>Table of Contents</h2>
        <ol>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#requirements">Requirements</a></li>
            <li><a href="#database-setup">Database Setup</a></li>
            <li><a href="#usage">Usage</a></li>
            <li><a href="#environment-variables">Environment Variables</a></li>
            <li><a href="#swagger-ui">Swagger UI</a></li>
            <li><a href="#additional-notes">Additional Notes</a></li>
        </ol>

  <h2 id="installation">Installation</h2>
        <p>To run this project locally, Docker and Docker Compose need to be installed on your machine.</p>

  <h3>Steps:</h3>
        <ol>
            <li><strong>Clone the repository:</strong></li>
            <pre><code>git clone &lt;https://github.com/VISHNURAJESHP/Word_finder.git&gt;
cd &lt;project-folder&gt;</code></pre>

  <li><strong>Set up environment variables:</strong></li>
            <p>Create a <code>.env</code> file in the root directory and add the following variables (example provided):</p>
            <pre><code># Example .env file
HASH_KEY=your_secret_hash_key_here

# Database configuration for PostgreSQL
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=db
DB_PORT=5432</code></pre>
            <p>Replace placeholders with your actual secret keys and PostgreSQL database details.</p>

  <li><strong>Build and run Docker containers:</strong></li>
            <pre><code>docker-compose up --build</code></pre>
            <p>This command will build the Docker images and start the containers.</p>

  <li><strong>Apply database migrations:</strong></li>
            <pre><code>docker-compose exec web python manage.py migrate</code></pre>

  <li><strong>Create a superuser (optional):</strong></li>
            <p>If you need access to Django admin:</p>
            <pre><code>docker-compose exec web python manage.py createsuperuser</code></pre>
            <p>Follow the prompts to create a superuser account.</p>
        </ol>

  <h2 id="requirements">Requirements</h2>
        <p>Below is the list of Python packages required for this project. To install all dependencies, run the following command:</p>
    <pre><code>pip install -r requirements.txt</code></pre>
        <pre><code>
asgiref==3.8.1
dj-database-url==2.2.0
Django==4.2.10
djangorestframework==3.15.2
drf-yasg==1.21.7
inflection==0.5.1
packaging==24.1
psycopg2-binary==2.9.9
PyJWT==2.8.0
python-dotenv==1.0.1
pytz==2024.1
PyYAML==6.0.1
sqlparse==0.5.1
typing_extensions==4.12.2
tzdata==2024.1
uritemplate==4.1.1
        </code></pre>

  <h2 id="database-setup">Database Setup</h2>
        <p>This project uses PostgreSQL as the database backend. Make sure you have PostgreSQL installed locally or accessible via a remote server.</p>
        <p>Set up your PostgreSQL database credentials in the <code>.env</code> file under <strong>Database configuration</strong>.</p>
        <p>Example:</p>
        <pre><code># Database configuration for PostgreSQL
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432</code></pre>
        <p>Ensure the <code>DB_HOST</code> matches the service name defined in your <code>docker-compose.yml</code> file for the database service.</p>

<h2 id="usage">Usage</h2>
<p>Once you have set up the project following the installation steps, you can interact with the application using the provided API endpoints. Here’s a brief overview of how to use the key features:</p>

<h3>User Registration and Login:</h3>
<ol>
    <li><strong>Register a new user:</strong> Send a POST request to `/userregister` with the following JSON payload:
        <pre><code>{
    "name" : "your_name"    
    "email": "example@example.com",
    "password": "your_password"
}</code></pre>
    </li>
    <li><strong>Login:</strong> Send a POST request to `/login` with the following JSON payload:
        <pre><code>{
    "email": "example@example.com",
    "password": "your_password"
}</code></pre>
        <p>Upon successful login, you will receive a JWT token in the response.</p>
    </li>
</ol>

<h3>Paragraph Operations:</h3>
<ul>
    <li><strong>Process Paragraphs:</strong> Send a POST request to `/process-paragraphs` with the paragraph data you want to process. This endpoint handles various operations on paragraphs.</li>
</ul>

<h3>Word Search:</h3>
<p>To search for specific words within the text, send a GET request to `/search-word` with the query parameters needed for searching.</p>
  <h2 id="environment-variables">Environment Variables</h2>
        <ul>
            <li><strong>HASH_KEY:</strong> Secret key for hashing.</li>
            <li><strong>Database Configuration:</strong> Configure your PostgreSQL database settings in the <code>.env</code> file as shown above.</li>
        </ul>
        <p>Ensure these environment variables are set correctly in your <code>.env</code> file.</p>

  <h2 id="swagger-ui">Swagger API Documentation</h2>
  <p>For detailed API documentation, you can access the Swagger UI at the following URL:</p>
  <p><a href="http://localhost:8000/swagger/">Swagger API Documentation</a></p>
<h2 id="additional-notes">Additional Notes</h2>
<p>This project creates a REST API that stores paragraphs in a PostgreSQL database with word-to-paragraph mappings. It also supports searching for words and retrieving the top 10 paragraphs containing those words.</p>

<h3>Technologies Used:</h3>
<ul>
    <li><strong>Django:</strong> Backend framework for building web applications in Python.</li>
    <li><strong>Django REST Framework (DRF):</strong> Powerful and flexible toolkit for building Web APIs in Django.</li>
    <li><strong>JWT (JSON Web Tokens):</strong> Used for API authentication.</li>
    <li><strong>PostgreSQL:</strong> Relational database used to store application data.</li>
    <li><strong>Docker:</strong> Containerization platform used for development and deployment.</li>
</ul>

<h3>Usage Notes:</h3>
<ul>
    <li>Ensure Docker and Docker Compose are installed on your machine before starting.</li>
    <li>Modify the <code>.env</code> file with your actual secret keys and PostgreSQL database credentials before running the application.</li>
    <li>Use the provided API endpoints to interact with the application (e.g., user registration, login, friend requests). You can use tools like <a href="https://www.postman.com/">Postman</a> to test the endpoints.</li>
    <li>Refer to the <code>requirements.txt</code> file for Python package dependencies.</li>
</ul>

  </div>
</body>
</html>
