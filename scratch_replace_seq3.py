import re

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-mass-binding-algorithms_seq3.md", "r") as f:
    text = f.read()

repl1 = r"*Per AGENTS.md \"$\\Delta_\\lambda$ gate (Track A blocker)\" rule: **do not propose a seventh fit-based ansatz**. The three-calibration discipline review will reject it. Productive directions include GAP-A-3, GAP-A-4 (categorical brane-tower level selection / $\\rho$ general rule) and Option E (Kashiwara crystal). Full context: [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](../../../docs/audits/2026-05-18-delta-lambda-gating-context.md).*"
text, n1 = re.subn(r"\*Per AGENTS\.md \"Δ_λ gate \(Track A blocker\)\".*?context\.md\)\.\*", lambda m: repl1, text, flags=re.MULTILINE|re.DOTALL)

print(f"n1: {n1}")

with open("/Users/litlfred/space_cats/qou/amalgamated_done/appendix-mass-binding-algorithms_seq3.md", "w") as f:
    f.write(text)

