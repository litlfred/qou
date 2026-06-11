---
name: compute-code-review
roles: [collaborator, owner]
user_invocable: false
description: >
  QA skill for thorough code-review of assets (Lean, Python, Rust, etc.)
  referenced by content blocks.
allowed-tools: Read Edit Write Bash Grep Glob AskUserQuestion
---

# /compute-code-review — Deep Canonical + Contextual Audit

This skill involves a thorough audit of technical assets, ensuring they are not only
technically sound but also correctly oriented within the paper's mathematical framework.

## Workflow

1.  **Read Narrative Context**: Start by reading the `.md` file of the block.
    Identify the mathematical claims, formulas, and required precision.
2.  **Analyze Assets**: Perform a deep review of the code (Python, Lean, etc.) using
    `local/qou-canonical-code-review` standards.
3.  **Cross-Check**: Verify that the code implementation exactly matches the
    mathematical definitions in the narrative. Flag any "notation drift" or
    "formula mismatch."
4.  **Log Findings**:
    *   Create a **GitHub Issue** using `gh issue create`.
    *   Title: `[Deep Audit] <Block Label> — <Summary>`.
    *   Body: Detailed evidence, standard violations, and paper alignment issues.
5.  **Update QA Sidecar**:
    *   `--criterion compute-code-review`.
    *   `--result fail|warn|pass`.
    *   `--evidence "Issue #<number>: <Title>"`.
    *   `--notes "Agent: Gemini 3.5 Pro; <Contextual Summary>"`.

## Referencing Back

*   **GitHub Issue -> Sidecar**: The sidecar `evidence` field MUST contain the
    GitHub issue number.
*   **Sidecar -> GitHub Issue**: The GitHub issue body SHOULD mention the
    block path and label.
*   **Resolution**: When an issue is resolved, a new QA entry (human or agent)
    should be added to the sidecar with `--result pass` and a note referencing
    the resolution commit or the closed issue.

## Examples

```bash
# Agent logs a finding
bun run content/pipeline/qa-agent-write.ts \
  --block content/.../my-block \
  --criterion compute-code-review \
  --result warn \
  --severity minor \
  --evidence "Issue #1234: Hardcoded precision in q_pinning_50_digit.py" \
  --notes "Model: gemini-1.5-pro; Precision is set to 50 but paper claims 100." \
  --model gemini-1.5-pro --skill local/compute-code-review

# Human reviews and resolves
bun run content/pipeline/qa-agent-write.ts \
  --block content/.../my-block \
  --criterion compute-code-review \
  --result pass \
  --evidence "Resolved: issue #1234 closed via commit abc123def" \
  --notes "Fixed the precision to match narrative." \
  --model litlfred --skill human
```
