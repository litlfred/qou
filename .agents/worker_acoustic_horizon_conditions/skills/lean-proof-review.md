# Lean Proof Review (Copied from local skill)

Refer to `.claude/skills/local/lean-proof-review.md` for full instructions.

Key highlights:
- Check for `sorry` usage (target: sorry-free).
- Verify statement integrity: do not weaken/change signature to pass the compiler without explicit author-approved restatements.
- Axioms audit: no `sorryAx` or unexpected axioms.
- Verify type signatures against LaTeX/Markdown intent.
