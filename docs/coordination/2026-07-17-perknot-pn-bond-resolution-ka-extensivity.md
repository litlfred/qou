# Per-knot p≠n bond-resolution vs the k(A) extensivity gap (beans qou-cqqs / qou-r1sr)

**Date:** 2026-07-17 · **PR:** #3841 · **Base:** current `main` (`074dfccb4a`).

Coordination record for the λ_A per-knot salvage's two attacks on the single
open GAP-A-3/A-4 item — the **derived** k(A) extensivity multiplier
μ_ext(K) = B_AME/B_base (targets D 5.85, T 4.44, ³He 3.29, ⁴He 9.31;
non-monotone, "not fit-closable" for symmetric models;
`computations/deltalambda/deltalambda-extensivity-gap-synthesis.witness.json`).
Both attacks come from a **different context** than the active fronts
(deliberately, per owner steer — a fresh angle may find what a crowded front
misses); the outcomes are reported honestly against that mature state.

## What is already closed / mature on main (do not re-derive)

- **Magnitude base + sign CLOSED:** `|Δ_λ| = classical dim(λ)` (#3537), sign
  `(−1)^{n(λ)}` (g_ρ grading). B_base = m_e·|Σ y_λ χ^λ sgn·dim| is parameter-free.
- **Carrier is PROVED intensive:** `carrier-saturation-mechanism.witness.json`
  — via `prop:wedderburn-trace-identity` (Σ y_λ dim_λ = tr_M(1) = 1),
  S = E_p[|Δθ|] is a bounded mean (0.72–0.88 rad at all A). "The carrier was
  never extensive."
- **Level-selection NOT linear:** paper proposition
  `content/.../mass-theory/level-selection-not-linear.md` (§3b-cond).
- Active fronts: #3808 (mixed-interface 3-factor closure: envelope × A_light-amp
  × bar-parity fall), #3802 (A=4 binding-K PSD), deuteron-wall alien-resummation
  + Ursell-operator scoping (`docs/scope/2026-07-05-gap-a4-ursell-*`).

## Attack 1 — per-knot additive S(K) → μ_ext: **PRUNE** (bean qou-cqqs)

`computations/probes/perknot-additive-sk-vs-kA-extensivity.witness.json`.
The per-knot additive S(K) (PR #3205 verdict #5, the sole λ_A-artifact) is
uniform/compressed in A (spread ×1.14 vs μ_ext's ×2.83) and puts the deuteron
**smallest** (rank 4) where μ_ext has it 2nd; best real candidate Spearman
+0.40 does not beat the junk control (A itself, +0.32) at n=4. This is the
expected shadow of the **proved** carrier-saturation intensivity — a quantity
uniform in A cannot supply a non-monotone μ_ext. Scope-(a); not a structural
exclusion of tr_M in a richer operator-valued combiner.

## Attack 2 — per-knot p≠n bond-resolution → the T/³He split: **LEAD** (bean qou-r1sr)

`computations/deltalambda/perknot-pn-bond-resolved-extensivity.witness.json`.
The genuinely non-duplicative angle: **T=(p,n,n) and ³He=(p,p,n) have identical
A=3 and 3 bonds, yet μ_ext = 4.44 vs 3.29 (ratio 1.3501)** — a split every
symmetric/equal-weight bond model (main's `bond_extensivity_equal_weight.py`)
gives as exactly **1.000**. The p≠n-distinct traces resolve the pairs into
pp/pn/nn with distinct weights.

Result: the parameter-free **inverse-product** per-bond weight
`w(a,b) = 1/(tr_M(a)·tr_M(b))` under the product aggregate reproduces the split
to **−1.38%** (pred 1.3315). Under that aggregate the ratio reduces to
`w(nn)/w(pp)`, so the p≠n resolution supplies the sign+magnitude of the T≠³He
degeneracy-break — plausibly the same physics as #3808's bar-parity-fall factor.

**LEAD, not closure (honest bounds):**
- Does **not** reproduce the full non-monotone μ_ext: ⁴He is not the maximum;
  per-isotope magnitudes off by tens of %.
- 1 hit among ~8 screened weights with a binary direction choice — entropy
  caveat (PSLQ-bound discipline): a single <5% match is a lead to verify.
- **No categorical derivation of "why inverse"** — the open verification step.

## Next (verification of the LEAD, if pursued)

1. **Categorical grounding of the inverse-product weight** — is `1/tr_M` a
   natural per-bond object (dual density / inverse Markov weight)? Without this
   the −1.38% is numerology-adjacent. Formalize-first: state the bond-weight
   shape as a lemma before any wider scan.
2. **Cross-check with #3808's bar-parity-fall** — coordinated on
   #3808 (comment posted); if their factor already carries the p≠n split,
   this lead is subsumed and should be recorded as such.
3. Do **not** widen to a free-coefficient bond fit (adhb gate: no BW / no
   per-bond tuning to hit targets).
