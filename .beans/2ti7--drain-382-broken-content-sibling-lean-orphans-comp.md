---
# 2ti7
title: Drain 382 broken content-sibling .lean orphans (compile sweep 2026-06-28)
status: todo
type: task
created_at: 2026-06-28T16:49:39Z
updated_at: 2026-06-28T16:49:39Z
---


## Context

Surfaced by the 2026-06-28 content-sibling compile sweep (PR #2974).
382 of 926 content-block `.lean` siblings (outside the `lean/` library
tree) genuinely fail `lean`-direct on `main` — pre-existing breakage
that escaped CI because these files are outside the `lake build QOU`
target.

- **Findings doc:** `docs/audits/2026-06-28-content-sibling-compile-sweep.md`
- **Genuine list (382, `file ||| first-error`):**
  `docs/audits/2026-06-28-content-sibling-compile-sweep.genuine.txt`
- **CI now prevents new drift** via `lean-content-siblings.yml` +
  `scripts/lean-verify-siblings.sh` (diff-scoped; the 382 are not
  retroactively blocked).

## Attack order
1. Shared `unexpected token 'section'; expected 'lemma'` template family
   first (one fix → many files).
2. Densest chapters: `mass-theory` (72) + `quantum-observable-universes`
   (63) = 135/382.
3. Elaboration-error tail (`failed to synthesize`, `Function expected`,
   `unknown tactic`, …) per-file.

Verify a fix with: `scripts/lean-verify-siblings.sh <file.lean>` (exit 0).

## 2026-06-28 finding — the `noncomputable section` family is NOT a mechanical drain (refuted)

Tested the leading hypothesis ("one template fix → many files green"). The
77 files with `unexpected token 'section'; expected 'lemma'` share a uniform
*parse* bug — a doc-comment stranded directly above `noncomputable section`
(the docstring can't attach to a `section`). The mechanical fix (move
`noncomputable section` above the docstring) clears the parse error AND the
cascade IR errors — **but greens 0/77 files.** Every file has deeper genuine
errors underneath:

- 18 `failed to synthesize` (missing instances — real API gaps)
- 21 deeper `unexpected token` (more parse breakage further down)
- 10 `Unexpected name … after end` (unclosed `noncomputable section` vs
  `end QOU` — a second structural bug, also uniform-ish)
- 6 `Function expected`, 5 `unsolved goals`, 3 `sorryAx is not a structure`,
  division on `R_q = LaurentPolynomial ℤ` (not a field → `q⁻¹`, `/(q−q⁻¹)`
  don't typecheck), type mismatches, universe errors.

**Conclusion:** these are genuinely incomplete formalizations, not a
cosmetic template defect. Draining them requires per-file Lean work and, in
many cases, a math-design decision (e.g. represent `q⁻¹` over the fraction
field of `R_q`, or `sorry`+`-- Ref:` the unproved parts) — which likely
wants author intent (repair vs honest-stub vs delete). The mechanical
`fix_ncs.py` transform is preserved in the session scratchpad but was NOT
committed (greened nothing). Next attempt should treat these per-cluster
with formalizer-level effort, not a sweep.
