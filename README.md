# Flask Basic Template
<h2>Uses:</h2>
<ul>
<li>ORM -> SQLAlchemy</li>
<li>Authentication & Authorization -> Flask JWT</li>
<li>Virtual Environment -> Pipenv</li>
<li>API Service -> Flask Restful</li>
<li>Language -> Python</li>
</ul>

<h2>Steps:</h2>

<ol>
<li>Create a Database (Suggest PostgreSQL)</li>
<li>Create the migrations. From the terminal enter the following commands: 
<ol>
    <li>python manage.py db init</li>
    <li>python manage.py db migrate</li>
    <li>python manage.py db upgrade</li>
</ol>
</li>
<li>Add your own code. Happy Coding with Flask!</li>
</ol>

<h2>API Authorization</h2>
<ol>
    <li>Create (Post) a user @ http://127.0.0.1:5000/register. Body: username and password. Content-Type: Application/JSON</li>
    <li>Get a JWT Token @ http://127.0.0.1:5000/auth. Body: username and password. Content-Type: Application/JSON</li>
    <li>Add @jwt_required() to your APIs</li>
    <li>Call the URLs, and add header: Authorization -> JWT <Your JWT Token></li>
</ol>

    