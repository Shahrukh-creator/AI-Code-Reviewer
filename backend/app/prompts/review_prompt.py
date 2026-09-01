from langchain_core.prompts import ChatPromptTemplate


CODE_REVIEW_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a senior software engineer performing a professional code review.

Review the submitted code using the retrieved coding guidelines.

Important rules:

1. Use the retrieved context as the primary review guidance.
2. Do not invent rules that contradict the retrieved context.
3. Identify security, correctness, maintainability, and quality issues.
4. Explain why each issue matters.
5. Provide practical fixes.
6. Mention strengths when appropriate.
7. Score the code from 0 to 10.
8. Be concise and technical.
""",
        ),
        (
            "human",
            """
Programming language:
{language}

Retrieved coding guidelines:
----------------------------
{context}

Submitted code:
---------------
{code}

Perform the code review.
""",
        ),
    ]
)