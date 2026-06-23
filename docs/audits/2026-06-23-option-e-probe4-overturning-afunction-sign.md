# PROBE-4 re-scoped: the Δ_λ chirality sign is the a-function (b-invariant) parity — not exogenous

**Date:** 2026-06-23
**Branch:** `claude/nice-dirac-ywun65`
**Status:** formalize-first RE-SCOPING of the KL-positivity prune; no fit; nothing wired; Δ_λ magnitude stays open.
**Script:** [`docs/audits/scripts/option_e_probe4_overturning_afunction_sign.py`](scripts/option_e_probe4_overturning_afunction_sign.py) (exit 0, combinatorics only)
**Witness:** [`computations/probes/option-e-probe4-overturning-afunction-sign.witness.json`](../../computations/probes/option-e-probe4-overturning-afunction-sign.witness.json)
**Supersedes-in-scope (does not retract):** [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md)

## Question (owner: "check not over-zealous refutation")

The PROBE-4 prune concludes the Δ_λ chirality sign `sgn(w_0^{S_{λ'}})` "must be
supplied **exogenously**" because KL/crystal multiplicities `n^w_λ ≥ 0` cannot
produce a mixed-sign target from an **unsigned** sum `Σ_w n^w_λ X_w`. Is that
obstruction **airtight**, or only **scoped** to unsigned sums — leaving a
*forced* signed sum `Σ_w ε_w n^w_λ X_w` (ε_w = ±1 from the Hecke/cell structure)
untouched?

## Finding: the prune is SCOPED, not airtight — the sign is the a-function parity

A two-sided Kazhdan–Lusztig cell of `S_n` is indexed by a partition `λ`, and
Lusztig's **a-function is constant on the cell**: `a(w) = a_λ` for all `w` in the
cell of `V_λ`. So any `ε_w = (-1)^{a(w)}` factors straight through the
non-negative sum:

$$\sum_w (-1)^{a(w)}\, n^w_\lambda\, X_w \;=\; (-1)^{a_\lambda}\sum_w n^w_\lambda X_w \;=\;(-1)^{a_\lambda}\,|\Delta_\lambda|.$$

For `S_n` every irreducible is *special*, so `a_λ = b_λ` (the b-invariant = lowest
fake-degree exponent = `min_{T∈SYT(λ)} maj(T)`), and the classical value is
`a_λ = b_λ = n(λ) = Σ_i (i-1)λ_i = Σ_i C(λ'_i,2)`. But the target sign is
`sgn(w_0^{S_{λ'}}) = Π_i (-1)^{C(λ'_i,2)} = (-1)^{n(λ)}`. Therefore

$$(-1)^{a_\lambda} \;=\; (-1)^{n(\lambda)} \;=\; \mathrm{sgn}(w_0^{S_{\lambda'}}) \;=\; \text{the target chirality sign, identically.}$$

**Verified (script, exit 0, no KL engine needed):**

1. `sgn(w_0^{S_{λ'}}) == (-1)^{n(λ)}` for all `λ ⊢ n`, `n ≤ 8`.
2. `b_λ = min_{T∈SYT(λ)} maj(T) == n(λ)` computed INDEPENDENTLY by enumerating
   SYT (confirms `a_λ=b_λ=n(λ)` is really the fake-degree valuation, not asserted),
   `n ≤ 7`.
3. The forced cell-constant sign reproduces the target for every `λ`; sign-counts
   match the audit anchors: **n=3 → 1+/2−, n=6 → 6+/5−** (full ladder
   n=2..8: 1/1, 1/2, 3/2, 5/2, 6/5, 6/9, 11/11).
4. A cell-constant `ε_w` factors through any non-negative multiplicity sum.

## Honest verdict — re-scope, NOT a closure (no over-claim)

- **The prune is SOUND but SCOPED.** It correctly kills *positive* (unsigned)
  multiplicity sums. It does **not** kill a *forced, a-graded* signed sum: the
  chirality sign is the **a-function / b-invariant parity**, an intrinsic
  Hecke-cell invariant — **not exogenous**, contrary to the prune's wording.
- **This does NOT close Δ_λ.** The MAGNITUDE `|Δ_λ| = dim` still requires
  `Σ_w n^w_λ X_w = dim` — the prune's own observation that the unsigned sum "at
  best re-derives `|Δ_λ|=dim` by a longer route" stands. The open problem is the
  **magnitude**, not the sign.
- **Fair skeptic's objection (stated, not hidden):** `(-1)^{a_λ}` and
  `sgn(w_0^{S_{λ'}})` are the *same* partition-level sign, so this **relocates**
  the chirality into the **a-grading** rather than conjuring new content. The
  value is that the a-grading is the natural home of the **writhe/framing
  channel** (the "growth sector" of
  [`2026-06-20-qbessel-reeb-flow-radial-argument.md`](2026-06-20-qbessel-reeb-flow-radial-argument.md)),
  so this gives a **derivation target** (`Δ_λ` sign = framing-grading parity)
  instead of an ad-hoc `sgn(w_0)` decoration.

## Recommendation

Re-scope the PROBE-4 line in [`option-e.md`](../coordination/option-e.md) from
"the sign must be supplied exogenously" to: **"the chirality sign is the
a-function (b-invariant) parity `(-1)^{n(λ)}`, a forced Hecke-cell invariant; the
open Δ_λ problem is the MAGNITUDE `Σ_w n^w_λ X_w = dim`, not the sign."** The
honest Option-E frontier remains **PROBE 2** (the A=4 interface operator, where
the magnitude lives) and the **s5-so3 keystone** `W_λ` geometric realization. The
`deltaSign_mixed` / `binding_magnitude_eq_dim` Lean facts
(`S5SO3FiberAction.lean`) are untouched and now have a combinatorial companion
(`b_λ = n(λ)` via SYT). No production change.

## Cross-references

- [`2026-06-16-option-e-probe4-kl-positivity-prune.md`](2026-06-16-option-e-probe4-kl-positivity-prune.md) — the prune being re-scoped
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure ledger
- `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean` — `deltaSign_mixed`, `binding_magnitude_eq_dim`
