# Python Best Practices

## Exception Handling

Catch specific exceptions rather than using a broad except clause.

Avoid silently ignoring exceptions.

Provide meaningful error messages when an operation fails.

## Functions

Functions should have a clear single responsibility.

Avoid excessively long functions.

Use descriptive function and variable names.

## Resource Management

Use context managers such as `with open(...)` when working with files.

Resources such as files and database connections should be properly closed.