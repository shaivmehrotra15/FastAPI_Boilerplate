# FastAPI Blog Backend Boilerplate

This repository contains a FastAPI boilerplate for building a powerful blog backend that performs CRUD operations, user creation, user authentication, and authorization using sessions, hashing with bcrypt, and JSON web tokens.

## Features

- **FastAPI**: Utilize the speed and performance of FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **CRUD Operations**: Ready-to-use endpoints for creating, reading, updating, and deleting blog posts, users, and more.
- **User Creation**: Implement user registration functionality with email validation.
- **User Authentication**: Securely authenticate users with sessions and JSON web tokens (JWT).
- **Authorization**: Define different user roles and permissions to control access to certain API endpoints.
- **Password Hashing**: Safeguard user passwords by hashing them using bcrypt before storage.
- **Database**: Pre-configured support for SQLAlchemy to interact with the database.
- **Pydantic Schemas**: Use Pydantic models for data validation and serialization.
- **Testing**: Includes unit tests to ensure the functionality of the API.

## Getting Started

Follow these steps to get the blog backend up and running on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/FastAPI_Boilerplate.git
   cd fastapi-blog-boilerplate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database:

   - Create a PostgreSQL database and update the database URI in the `app/config.py` file.

4. Run the migrations:

   ```bash
   alembic upgrade head
   ```

5. Start the server:

   ```bash
   uvicorn app.main:app --reload
   ```

6. The FastAPI server should now be running on `http://localhost:8000`.

## API Documentation

To view the automatically generated API documentation, go to `http://localhost:8000/docs`.

## Endpoints

The following endpoints are available in the API:

- **POST /user/**: Register a new user with email and password.
- **POST /authentication/login**: Log in with email and password to obtain a JSON web token.
- **GET /user/{user_id}**: Get the current user's details.
- **POST /blog/**: Create a new blog post.
- **GET /blog/{post_id}**: Get a specific blog post by ID.
- **GET /blog/**: Get all blogs post.
- **PUT /blog/{post_id}**: Update a blog post by ID.
- **DELETE /blog/{post_id}**: Delete a blog post by ID.

## Testing

To run the tests, execute the following command:

```bash
pytest
```

## Contributing

Contributions to this project are welcome! Feel free to submit pull requests or open issues for bug fixes, features, or improvements.


Thanks for checking out our FastAPI Blog Backend Boilerplate! We hope it helps you kickstart your blog backend development with ease. If you have any questions or feedback, please don't hesitate to get in touch.

Happy coding! 😄
