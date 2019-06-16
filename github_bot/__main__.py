from octomachinery.app.server.runner import run as run_app
from octomachinery.app.routing import process_event_actions
from octomachinery.app.routing.decorators import process_webhook_payload
from octomachinery.app.runtime.context import RUNTIME_CONTEXT
from octomachinery.github.api.raw_client import RawGitHubAPI


@process_event_actions('issues', {'opened'})
@process_webhook_payload
async def on_issue_opened(
        *,
        action, issue, repository, sender, installation,
        assignee=None, changes=None,
):
    """Whenever an issue is opened, greet the author and say thanks."""
    github_api: RawGitHubAPI = RUNTIME_CONTEXT.app_installation_client
    comments_url = issue["comments_url"]
    author = issue["user"]["login"]
    await github_api.post(
        comments_url,
        data=dict(
            body=f"ha ha ha! @{author} are you sure?? 🤖"
        )
    )


if __name__ == "__main__":
    run_app(
        name='simple-vios-bot',
        version='1.0.0',
        url='https://github.com/apps/pyyyyyycoooon-booooot111',
    )
