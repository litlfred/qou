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
    *   Create a local **bean** file in `.beans/`.
    *   Name: `[local-id]-[clean_title].md`.
    *   Frontmatter: `type: issue`, `source: local`, `status: todo`.
    *   Body: Detailed evidence, standard violations, and paper alignment issues under an H1 title.
5.  **Update QA Sidecar**:
    *   `--criterion compute-code-review`.
    *   `--result fail|warn|pass`.
    *   `--evidence "Bean .beans/[name].md: <Title>"`.
    *   `--notes "Agent: Gemini 3.5 Pro; <Contextual Summary>"`.

## Referencing Back

*   **Bean -> Sidecar**: The sidecar `evidence` field MUST contain the bean filename.
*   **Sidecar -> Bean**: The bean body SHOULD mention the block path and label.
*   **Resolution**: When a bean is resolved, update its status to `done`, and a new QA entry (human or agent) should be added to the sidecar with `--result pass` and a note referencing the resolution commit.

## Examples

```bash
# Agent logs a finding
bun run content/pipeline/qa-agent-write.ts \
  --block content/.../my-block \
  --criterion compute-code-review \
  --result warn \
  --severity minor \
  --evidence "Bean .beans/local1-hardcoded_precision.md: Hardcoded precision in q_pinning_50_digit.py" \
  --notes "Model: gemini-1.5-pro; Precision is set to 50 but paper claims 100." \
  --model gemini-1.5-pro --skill local/compute-code-review

# Human reviews and resolves
bun run content/pipeline/qa-agent-write.ts \
  --block content/.../my-block \
  --criterion compute-code-review \
  --result pass \
  --evidence "Resolved: bean local1-hardcoded_precision marked done via commit abc123def" \
  --notes "Fixed the precision to match narrative." \
  --model litlfred --skill human
```
