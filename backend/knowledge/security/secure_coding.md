# Secure Coding Guidelines

## SQL Injection

Never construct SQL queries by concatenating untrusted user input.

Use parameterized queries or prepared statements when interacting with databases.

## Secrets

Do not hardcode passwords, API keys, tokens, or credentials in source code.

Store secrets in environment variables or an appropriate secret-management system.

## Input Validation

Validate external input before processing it.

Do not assume client-provided data is safe.