import github3
from gpt_integration import GPTcodereview
from dotenv import dotenv_values

config = dotenv_values(".env")
TOKEN  = config["Github_token"]

code_rev = GPTcodereview()
def get_github_repo(repo_name):
    github = github3.login(token=TOKEN)
    return github.repository(repo_name)

def add_review_comment(repo, pr_number, comment):
    pr = repo.pull_request(pr_number)
    pr.create_review(body=comment, event='COMMENT')

def review_pull_request(repo_name, pr_number, language):
    repo = get_github_repo( repo_name)
    pr = repo.pull_request(pr_number)
    code = ""
    for file in pr.files():
        code += file.contents() + "\n"
    report = code_rev.generate_feedback_report(code, language)
    add_review_comment(repo, pr_number, report)


review_pull_request( "single_model_translation2","1ba292c" , "python")