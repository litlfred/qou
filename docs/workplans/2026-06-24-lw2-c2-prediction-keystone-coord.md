# lw(2) c=2 prediction test + keystone a_D=lw coordination (2026-06-24)

**Branch:** `claude/lw2-c2-prediction-keystone-coord-2026-06-24`
**Follows:** merged #2612 (lever-1 selection-rule unification; `a_D^(n)=lw(n−1)`).
**Discipline:** formalize-first, no-fit, corpus-grep (no fabricated c=2 observable).

Two-pronged tranche (user-directed "1 2"):

## Option 1 — test the lw(2) c=2 prediction

The selection rule `lw(c)=(1/(c+1))·Σ_{λ⊢c+1} dim_q` gives
`lw(2)=(q+1)²/(3q) ≈ 1.337` (c=2, 2-component link, e.g. Hopf) — confirmed
derivation-tight via the canonical q-hook `dim_q`
([`binding_selection_rule_tau_closure.py`](../../computations/binding_selection_rule_tau_closure.py),
merged #2612). c=1 (muon, `lw=1`) and c=3 (proton, Family-A) are the established
mass anchors; **lw(2) is the rule's first falsifiable prediction beyond them.**

- **TODO:** find/compute an *independent* 2-component-link linking-weight
  observable (Hopf / gluon EM-linking / di-nucleon / deuteron-as-link) to test
  `lw(2)` against. **If none exists in the corpus, document `lw(2)` as an
  untested prediction awaiting a c=2 observable — do NOT manufacture one.**

## Option 2 — coordinate the a_D=lw residual with the keystone

The residual from #2612 lever-1: the geometric↔algebraic identification
`a_D^(n)=lw(n−1)` (SW prolonged period = selection-rule value) **is** the
keystone's W_λ geometric-origin frontier.

- **TODO:** coordinate with the active keystone PRs (#2488 / #2503 / #2524 /
  #2608 / #2409) — post the `a_D=lw` framing on the natural one + update
  `docs/coordination/s5-so3-keystone.md`.

## Status

**Both options resolved (2026-06-24).**

- **Option 1 — DONE (honest negative).** `lw(2)=(q+1)²/(3q)≈1.337` is
  derivation-tight + Lean-proved but **untested**: corpus-grep found no
  independent c=2 (2-component-link) linking-weight observable. The deuteron is
  the 6₂ knot (not a c=2 link); the Hopf diquark exists topologically but has no
  mass prediction. Documented as the rule's first falsifiable prediction awaiting
  a c=2 observable (Hopf-diquark candidate) — **no fabricated test**. See
  [`docs/audits/2026-06-24-lw2-c2-prediction-untested-status.md`](../audits/2026-06-24-lw2-c2-prediction-untested-status.md).
- **Option 2 — DONE.** `a_D=lw` residual coordinated on the keystone scope hub
  **#2488** (the natural forum; it names `a_D=lw` as the residual). Framed as the
  **functional-level** identification of the Seifert–CS W_λ index (#2524) with the
  Hecke `lw(c)` selection rule — respecting #2608's caveat that it is *not* a naive
  ~8%-off number-match. Keystone ledger
  [`s5-so3-keystone.md`](../coordination/s5-so3-keystone.md) updated with the bridge.
