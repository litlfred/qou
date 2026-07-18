# α_EM shared-wall gate self-test: `D(q₀) ∉ {8, 8π}` — falsified on the observable side

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure · **Tier:** measurement
(scope-(a) **negative**; no `α_k` wired; no fit; `1/(8π)` stays a phase-4
identification). **Branch:** `claude/alpha-em-2I-quantum-dim-gate-test-2026-07-17`.
Self-test of the merged shared-wall acceptance gate (#3853).

## What was tested

The merged gate (#3853) reduced the α_EM ↔ W_λ shared-wall hypothesis to one
falsifiable number: the two walls are one (via a nonabelian `S₀₀ = 1/D`) **iff**
the keystone total quantum dimension `D(ζ→q₀) ∈ {b₁, π·b₁} = {8, 8π}`. This audit
runs that gate against the corpus's **own fixed** modular data — no wait on
Front-2's colored-LR amplitude, and crucially **no level scan**.

The data is fixed unambiguously by `KeystoneVerlindeSMatrixBridge`:
`D = √(Σ_{λ∈P} d_q(λ)²)` with `P = partitions of n=5` (McKay / A₅⊂S₅ / binary
icosahedral 2I, `|S₅|=|2I|=120`); `d_q(λ)` is the hook-content quantum dimension.
At the observable substrate `q₀` (real ≈ 1.11, not a root of unity) the full
untruncated `λ⊢5` set is the only well-defined choice — the non-unitary object
the merged keystone gate identified (`Σ_λ W_λ = Z(q₀) < 1`).

## Result — falsified

```
D(q₀) = √(Σ_{λ⊢5} d_q(λ)²) = 11.3569…      D(1) = √5! = √120 = 10.9545
targets:  b₁ = 8,   π·b₁ = 8π = 25.1327
D/8 = 1.4196   (≠ 1)         D/8π = 0.4519   (≠ 1)
```

`D(q₀) = 11.357` is **neither 8 nor 8π**. So the naive `S₀₀ = 1/D` identification
**fails**: the keystone total quantum dimension `D` (from the n=5 partition modular
datum) is not the photon count `b₁ = 8` (a genus-4 homology count) and not `8π`.
On the observable side the α_EM per-loop measure `1/(π b₁)` and the W_λ keystone
`1/D` are **distinct normalizations**. `b₁ = 8` and `D(q₀) = 11.357` are different
objects.

## Scope — a scope-(a) negative, NOT a structural exclusion

Per the anti-over-claim discipline: this refutes the **specific** identification
"photon `b₁` = keystone `D` at `q₀`", tested against the corpus's fixed data. It
does **not** exclude every shared-wall form. Still open:

- a **fibre-side** level-truncated *admissible* `D(ζ)` at a root of unity `ζ`
  (Front-2's colored-LR Σ(2,3,5) territory) — a different (smaller) number than
  the observable-side untruncated `D(q₀)`;
- `b₁` entering the photon measure via a route other than the total quantum
  dimension (a per-irrep `d_q(λ)`, an index, or a different combination).

## Why this is a positive contribution

The #3853 gate was built to be **falsifiable**; this audit fed it non-tunable
corpus data and it returned an honest **NO**. That closes a tempting but wrong
unification (the α_EM measure and the m_p/m_μ W_λ keystone are *not* the same
observable-side normalization), preventing future agents from chasing it, and it
sharpens where a real link — if any — must live (the fibre side, or a non-`D`
route). No number was tuned; `1/(8π)` remains a phase-4 identification.

## Correction to the earlier coordination

My earlier comments on #3822 raised the shared-wall as a *hopeful* two-for-one
(if `D = 8`). This self-test settles it on the observable side: `D(q₀) = 11.357 ≠
8`. The hopeful framing is retracted; the honest status is the scope-(a) negative
above, with the fibre-side check left to Front-2.

## Cross-references

- Gate: #3853, [`2026-07-17-alpha-em-wlambda-shared-wall...`] (the acceptance predicate)
- Prunes: #3834 (`ζ(0)=−b₁`), #3842 (μ-sector fitting trap), #3848 (abelian RT covolume)
- Keystone modular data: `KeystoneVerlindeSMatrixBridge.lean`, `2026-07-17-keystone-wlambda-unitarity-normalization-gate.md`
- Witness: `computations/alpha_em/alpha-em-2I-total-quantum-dimension-gate-test.witness.json`
