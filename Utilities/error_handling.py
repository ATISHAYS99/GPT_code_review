import time
import requests
from gpt_integration import GPTCodeReview

code_review = GPTCodeReview()

def generate_feedback_with_retry(code, language, retries=3, delay=5):
    """
    Generates feedback for the given code with retry logic in case of failures.

    Arguments:
    code -- The code to be reviewed.
    language -- The programming language of the code.
    retries -- Number of retry attempts (default: 3).
    delay -- Delay between retry attempts in seconds (default: 5).

    Returns:
    The feedback report generated by the GPT model or an error message after multiple attempts.
    """
    for i in range(retries):
        try:
            return code_review.generate_feedback(code, language)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    return "Failed to generate feedback after multiple attempts."

def generate_feedback_report_with_retry(code, language):
    """
    Generates a detailed feedback report with retry logic.

    Arguments:
    code -- The code to be reviewed.
    language -- The programming language of the code.

    Returns:
    A detailed feedback report.
    """
    feedback = generate_feedback_with_retry(code, language)
    report = f"Code Review Report for {language.capitalize()} Code:\n\n"
    report += feedback
    return report
