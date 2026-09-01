# Organization Database Engineering Standards

These rules are mandatory for all backend applications in the organization.

## Database Access

Application services and API controllers must not access the database directly.

All database operations must be implemented through Repository classes.

For example:

UserService -> UserRepository -> Database

Direct calls such as `database.execute()` from services, controllers, or route handlers are prohibited.

## Query Security

All SQL queries must use parameterized queries or prepared statements.

String concatenation must never be used to insert user-controlled values into SQL statements.

## Error Handling

Database-specific exceptions must not be exposed directly to API consumers.

Repository classes should convert database exceptions into application-level exceptions.

## Data Retrieval

Avoid `SELECT *`.

Queries should retrieve only the columns required by the application.