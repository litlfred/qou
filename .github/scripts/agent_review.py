"""
Agent Review System

A review coordinator that orchestrates multiple AI reviewers to provide
feedback on commits to main. Reviews are synthesized into a summary
GitHub issue identifying common criticisms and actionable feedback.

Reviewers:
  - Accuracy Reviewer (Claude): Scientific and mathematical rigor checks
    using methodology from K-Dense-AI/claude-scientific-skills.
  - Claude Reviewer: General code and content review via Anthropic API.
  - Gemini Reviewer: General code and content review via Google Gemini API.
  - GitHub Copilot Reviewer: General code and content review via GitHub Models API.

Configuration:
  Set the following repository secrets to enable each reviewer:
    ANTHROPIC_API_KEY  - enables Claude and Accuracy reviewers
    GEMINI_API_KEY     - enables Gemini reviewer
    GITHUB_TOKEN       - enables GitHub Copilot reviewer (provided by default)
"""

import os
import requests

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

COMMIT_DIFF = os.environ.get("COMMIT_DIFF", "")
COMMIT_MESSAGE = os.environ.get("COMMIT_MESSAGE", "")
COMMIT_SHA = os.environ.get("COMMIT_SHA", "")
COMMIT_AUTHOR = os.environ.get("COMMIT_AUTHOR", "")
REPO_NAME = os.environ.get("REPO_NAME", "")

CLAUDE_MODEL = "claude-sonnet-4-20250514"
GEMINI_MODEL = "gemini-2.5-pro"
COPILOT_MODEL = "gpt-4o"

# ---------------------------------------------------------------------------
# Scientific accuracy review prompt (sourced from K-Dense-AI/claude-scientific-skills)
# ---------------------------------------------------------------------------

ACCURACY_REVIEW_SYSTEM = """You are a scientific accuracy reviewer. Your role is to
evaluate commits for mathematical correctness, scientific rigor, and logical
consistency. Use the following structured methodology derived from established
scientific peer-review practices.

## Review Methodology

### 1. Mathematical Verification
- Check all equations, formulas, and numerical computations for correctness.
- Verify dimensional analysis and unit consistency.
- Confirm boundary conditions and edge-case handling.

### 2. Scientific Rigor
- Assess whether claims are supported by evidence or sound reasoning.
- Check that scientific terminology is used correctly.
- Verify that any referenced constants, data, or facts are accurate.

### 3. Statistical & Methodological Soundness
- Evaluate statistical methods for appropriateness.
- Check sample sizes, power calculations, and significance thresholds.
- Look for common pitfalls: p-hacking, multiple comparisons, survivorship bias.

### 4. Logical Consistency
- Identify logical fallacies or unsupported leaps in reasoning.
- Check that conclusions follow from the presented evidence.
- Verify internal consistency across the changeset.

### 5. Reproducibility
- Assess whether methods are described with sufficient detail to reproduce.
- Check for hard-coded magic numbers without explanation.
- Verify that algorithms are correctly implemented.

## Output Format
Provide your review as structured feedback with:
- **Summary**: One-paragraph overall assessment.
- **Issues Found**: Numbered list of specific problems (severity: critical/major/minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
"""

GENERAL_REVIEW_SYSTEM = """You are an expert code and content reviewer. Provide a
thorough review of the following commit diff. Focus on:

1. **Correctness**: Logic errors, bugs, or incorrect behavior.
2. **Security**: Potential vulnerabilities, secret exposure, injection risks.
3. **Performance**: Inefficiencies, unnecessary complexity, scalability concerns.
4. **Maintainability**: Code clarity, naming, documentation, modularity.
5. **Best Practices**: Adherence to language/framework conventions and standards.

## Output Format
Provide your review as structured feedback with:
- **Summary**: One-paragraph overall assessment.
- **Issues Found**: Numbered list of specific problems (severity: critical/major/minor).
- **Suggestions**: Numbered list of improvements.
- **Verdict**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.
"""

COORDINATOR_SYSTEM = """You are the Review Coordinator. You are given feedback from
multiple AI reviewers about a code commit. Your job is to:

1. **Synthesize** all reviews into a coherent summary.
2. **Identify common criticisms** raised by multiple reviewers.
3. **Highlight critical issues** that need immediate attention.
4. **Resolve contradictions** between reviewers when they disagree.
5. **Prioritize** the feedback from most to least important.
6. **Provide a final recommendation**: APPROVE, REQUEST_CHANGES, or NEEDS_DISCUSSION.

## Output Format
Use the following markdown structure:

### Overall Assessment
(one paragraph synthesis)

### Critical Issues
(numbered list, if any)

### Common Themes
(feedback points raised by more than one reviewer)

### Reviewer Summaries
(brief summary from each reviewer)

### Consolidated Suggestions
(prioritized list of all unique suggestions)

### Final Recommendation
(APPROVE / REQUEST_CHANGES / NEEDS_DISCUSSION with justification)
"""

# ---------------------------------------------------------------------------
# Reviewer helpers
# ---------------------------------------------------------------------------


def build_review_prompt(diff, commit_message, commit_sha, commit_author):
    """Build the user prompt containing commit context and diff."""
    return (
        f"## Commit Details\n"
        f"- **Author**: {commit_author}\n"
        f"- **SHA**: {commit_sha}\n"
        f"- **Message**: {commit_message}\n\n"
        f"## Diff\n```diff\n{diff}\n```"
    )


def call_anthropic(system_prompt, user_prompt, model=CLAUDE_MODEL):
    """Call the Anthropic Messages API and return the response text."""
    resp = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": ANTHROPIC_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json",
        },
        json={
            "model": model,
            "max_tokens": 4096,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_prompt}],
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["content"][0]["text"]


def call_gemini(system_prompt, user_prompt, model=GEMINI_MODEL):
    """Call the Google Gemini API and return the response text."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model}:generateContent?key={GEMINI_API_KEY}"
    )
    resp = requests.post(
        url,
        headers={"content-type": "application/json"},
        json={
            "system_instruction": {"parts": [{"text": system_prompt}]},
            "contents": [{"parts": [{"text": user_prompt}]}],
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def call_copilot(system_prompt, user_prompt, model=COPILOT_MODEL):
    """Call the GitHub Models API (Copilot) and return the response text."""
    resp = requests.post(
        "https://models.inference.ai.azure.com/chat/completions",
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "content-type": "application/json",
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "max_tokens": 4096,
        },
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    return data["choices"][0]["message"]["content"]


# ---------------------------------------------------------------------------
# Review runners
# ---------------------------------------------------------------------------


def run_accuracy_review(user_prompt):
    """Run the scientific accuracy review via Claude."""
    print("🔬 Running accuracy review (Claude) ...")
    return call_anthropic(ACCURACY_REVIEW_SYSTEM, user_prompt)


def run_claude_review(user_prompt):
    """Run the general Claude review."""
    print("🟣 Running Claude review ...")
    return call_anthropic(GENERAL_REVIEW_SYSTEM, user_prompt)


def run_gemini_review(user_prompt):
    """Run the general Gemini review."""
    print("🔵 Running Gemini review ...")
    return call_gemini(GENERAL_REVIEW_SYSTEM, user_prompt)


def run_copilot_review(user_prompt):
    """Run the GitHub Copilot review."""
    print("🟢 Running GitHub Copilot review ...")
    return call_copilot(GENERAL_REVIEW_SYSTEM, user_prompt)


# ---------------------------------------------------------------------------
# Coordinator
# ---------------------------------------------------------------------------


def run_coordinator(reviews, user_prompt):
    """Synthesize all reviews and return the final summary.

    Uses the first available LLM in order of preference:
    Claude > Gemini > Copilot.
    """
    reviews_text = ""
    for name, content in reviews.items():
        reviews_text += f"## {name}\n{content}\n\n"

    coordinator_prompt = (
        f"Below are the reviews for a commit.\n\n"
        f"{reviews_text}\n\n"
        f"---\n\n"
        f"Original commit context:\n{user_prompt}"
    )

    if ANTHROPIC_API_KEY:
        return call_anthropic(COORDINATOR_SYSTEM, coordinator_prompt)
    if GEMINI_API_KEY:
        return call_gemini(COORDINATOR_SYSTEM, coordinator_prompt)
    if GITHUB_TOKEN:
        return call_copilot(COORDINATOR_SYSTEM, coordinator_prompt)

    return reviews_text  # fallback: raw concatenation


# ---------------------------------------------------------------------------
# GitHub Issue creation
# ---------------------------------------------------------------------------


def create_issue(title, body):
    """Create a GitHub issue with the review summary."""
    url = f"https://api.github.com/repos/{REPO_NAME}/issues"
    resp = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
        json={
            "title": title,
            "body": body,
            "labels": ["agent-review"],
        },
        timeout=30,
    )
    if resp.status_code == 422:
        # Label might not exist yet — retry without labels
        resp = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {GITHUB_TOKEN}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            json={
                "title": title,
                "body": body,
            },
            timeout=30,
        )
    resp.raise_for_status()
    issue_url = resp.json().get("html_url", "")
    print(f"✅ Created issue: {issue_url}")
    return issue_url


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    if not COMMIT_DIFF.strip():
        print("No diff found — skipping review.")
        return

    user_prompt = build_review_prompt(
        COMMIT_DIFF, COMMIT_MESSAGE, COMMIT_SHA, COMMIT_AUTHOR
    )

    reviews = {}

    # Accuracy reviewer (requires Anthropic key)
    if ANTHROPIC_API_KEY:
        try:
            reviews["Accuracy Reviewer (Scientific Rigor)"] = run_accuracy_review(
                user_prompt
            )
        except Exception as exc:
            print(f"⚠️  Accuracy review failed: {exc}")

    # Claude general reviewer
    if ANTHROPIC_API_KEY:
        try:
            reviews["Claude Reviewer"] = run_claude_review(user_prompt)
        except Exception as exc:
            print(f"⚠️  Claude review failed: {exc}")

    # Gemini reviewer
    if GEMINI_API_KEY:
        try:
            reviews["Gemini Reviewer"] = run_gemini_review(user_prompt)
        except Exception as exc:
            print(f"⚠️  Gemini review failed: {exc}")

    # GitHub Copilot reviewer
    if GITHUB_TOKEN:
        try:
            reviews["GitHub Copilot Reviewer"] = run_copilot_review(user_prompt)
        except Exception as exc:
            print(f"⚠️  GitHub Copilot review failed: {exc}")

    if not reviews:
        print("No API keys configured — no reviews to run.")
        return

    print(f"\n📋 Collected {len(reviews)} review(s). Running coordinator ...\n")

    # Coordinator synthesis
    summary = run_coordinator(reviews, user_prompt)

    # Build issue
    title = f"Agent Review: {COMMIT_MESSAGE} ({COMMIT_SHA})"
    body = (
        f"## Agent Review for commit `{COMMIT_SHA}`\n\n"
        f"**Author**: {COMMIT_AUTHOR}  \n"
        f"**Message**: {COMMIT_MESSAGE}\n\n"
        f"---\n\n"
        f"{summary}\n\n"
        f"---\n\n"
        f"<details><summary>Individual Reviews</summary>\n\n"
    )
    for name, content in reviews.items():
        body += f"### {name}\n\n{content}\n\n"
    body += "</details>\n"

    if GITHUB_TOKEN and REPO_NAME:
        create_issue(title, body)
    else:
        print("⚠️  Cannot create issue: GITHUB_TOKEN or REPO_NAME not set.")
        print(body)


if __name__ == "__main__":
    main()
