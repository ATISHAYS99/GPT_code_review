import click
from gpt_integration import GPTCodeReview
from error_handling import generate_feedback_report_with_retry

@click.command()
@click.argument('file_path')
@click.option('--language', default='python', help='Programming language of the code.')
def review_code(file_path, language):
    """
    Command-line interface for reviewing code.

    Arguments:
    file_path -- The path to the file containing the code to be reviewed.
    language -- The programming language of the code (default: python).
    """
    code_review = GPTCodeReview()
    with open(file_path, 'r') as file:
        code = file.read()
    report = generate_feedback_report_with_retry(code, language)
    print("Feedback Report:\n", report)

if __name__ == "__main__":
    review_code()
