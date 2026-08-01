# Work-plan — pin the binding weighting convention (Markov y_λ vs Plancherel W_λ)

**Branch:** `claude/binding-weight-markov-pinning-2026-08-01` · **Axis:** Δ_λ / binding weight ·
**Prerequisite surfaced by:** PR #4491 (C_knot is weighting-convention-dependent → which weight is
*derived*?). **Discipline:** formalize-first, honest scope, no fit.

## Question

The binding trace `J_L = tr_M(ρ(β_L))` (Markov trace, §7a) can be weighted by `y_λ` (Wenzl),
`W_λ = d_q²/[n]!` (Schur-Weyl / q-Plancherel), or signed dim_q. **Which is the *derived* weight?** —
the well-posed prerequisite to any Δ_λ magnitude derivation.

## Finding (verified)

**The weight is PINNED to `y_λ` by the Markov axiom, and `W_λ` is doubly excluded.**

1. **`y_λ` is the Markov weight (canonical).** `wedderburn_jones_markov.py` (the module the binding
   formula imports) solves `y_λ` from the Markov axiom (`markov_weights_symbolic.solve_y_lambda`,
   `markov_trace_recursive`) and states the `schur_weyl_weight = d_q²/[n]!` form is **"NOT the
   Markov-trace weight."**
2. **`y_λ ≠ W_λ`** numerically (n=3: ratios 0.16–2.9) — genuinely different systems.
3. **`W_λ` is conjugation-SYMMETRIC** (`W_λ = W_{λ'}`) because hook lengths are transpose-invariant
   ⇒ `d_q(λ) = d_q(λ')`. Verified for all λ up to (5,2,1). But **`y_λ` is asymmetric**
   (y_(3)=0.415 ≠ y_(1,1,1)=0.023) — it carries the chirality/bar-parity split. Binding *requires*
   that asymmetry (GAP-1: a conjugation-symmetric Δ_λ gives g₂=0 for even A). So `W_λ` is excluded on a
   **second, independent structural ground** (scope-b: proved invariant) — it washes out the chirality.

**Consequences:** (a) three-walls Route 1's 33× W_λ overshoot is explained — wrong trace; (b) the
corpus mislabel in `alpha_em_b2_scalar_c_probe.py:116` ("Markov/Wedderburn weight w_λ = d_q²/[n]!")
contradicts the canonical module — flag; (c) **honest refinement of PR #4491's C_knot-not-universal**:
the 41× "convention spread" (5.85 vs 240) was right-weight (y_λ) vs wrong-weight (signed dim_q), NOT a
genuine ambiguity — with the weight pinned to y_λ, C_knot = 5.85 is well-posed; (d) the C_knot deficit
is therefore **not a weight issue** — it lives in `f^λ` / `sgn` / `E₀` scale / word-level, relocating
the open Δ_λ target.

## Steps (microcommits)

1. **[this]** work-plan → PR.
2. **Probe** — verify y_λ≠W_λ, W_λ=W_{λ'} (hook-transpose), y_λ asymmetric, the pinning + C_knot
   refinement.
3. **Lean** (formalize-first) — `W_λ` conjugation-symmetry from hook-transpose invariance; the
   asymmetry-required exclusion (scope-b). Sorry-free.
4. **Audit** — the pinning, the corpus mislabel flag, the C_knot refinement.

## Scope

DERIVED: the binding weight is pinned to y_λ (Markov axiom); W_λ excluded (scope-b, conjugation
symmetry). NOT a Δ_λ magnitude derivation (still open) — it makes the target well-posed. No fit;
nothing wired.
