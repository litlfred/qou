# Lever-1 fibre kernel, Stage 8: the binding correction core is a tower of pairwise-coprime, irreducible, bar-symmetric polynomials

**Date:** 2026-06-28
**Bean:** `z2bn` (Lever 1 [FOCUS] — fibre q-difference kernel `R(q,x)` for the binding genfun)
**Compute:** [`computations/substrate/lever1_binding_core_characterization.py`](../../computations/substrate/lever1_binding_core_characterization.py)
**Witness:** [`computations/substrate/lever1-binding-core-characterization.witness.json`](../../computations/substrate/lever1-binding-core-characterization.witness.json)
**Predecessors:** Stage 7 [`2026-06-28-lever1-binding-correction-cyclotomic-core-growth.md`](2026-06-28-lever1-binding-correction-cyclotomic-core-growth.md)
(the `(q−1)²·Φ_d` tower + growing core), Stage 6
[`2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md`](2026-06-28-lever1-binding-correction-not-single-qhypergeometric.md).
**Serves:** `kehn` (Q_β / m_n c_k Habiro closure), `s5bb` (Habiro-element keystone blocker).

## What this stage does

Stage 7 factored the binding correction `D(m) = S(m) − (S(m−1) + [m−1]_q·S(m−2))` exactly as
`D(m)·q^{a_m} = c_m·(q−1)²·∏_d Φ_d^{e}·R_m(q)` and found the non-cyclotomic core `R_m` has growing
degree (8, 10, 14, 28, 34, 46 for `m = 6..11`). This stage characterizes the cores `R_m` themselves —
read directly from the Stage-7 witness (no `S(m)` recompute), exact in `q`.

## Result

| m | deg `R_m` | palindromic? | `R_m(1)` | `R_m(q₀)` | irreducible /ℚ |
|---|---:|---|---:|---:|---|
| 6 | 8 | ✓ | 28 | 43.80 | ✓ |
| 7 | 10 | ✓ | 16 | 28.68 | ✓ |
| 8 | 14 | ✓ | 34 | 78.12 | ✓ |
| 9 | 28 | ✓ | 1232 | 6419.8 | ✓ |
| 10 | 34 | ✓ | 1328 | 10190.6 | ✓ |
| 11 | 46 | ✓ | 9024 | 147867 | ✓ |

Four exact, derived facts on `m = 6..11`:

1. **Uniform bar-symmetry.** Every core is **palindromic** — `q^{deg}·R_m(1/q) = R_m(q)`, i.e.
   invariant under the bar-involution `q ↔ 1/q`. The 2026-06-27 audit noted this for the `D(7)` core
   alone; it holds for *all* cores. The binding-correction residue is therefore **bar-even**, matching
   the framework's bar-symmetry requirement (the same `q ↔ q⁻¹` structure that governs the meson scale
   and the Q_β cyclotomic constraints).

2. **Each core is irreducible over ℚ.** No `R_m` factors further — each is a *single* irreducible
   bar-symmetric polynomial, so the Stage-7 cyclotomic strip removed everything cyclotomic and what
   remains is genuinely one irreducible piece per order.

3. **The cores are pairwise coprime.** Every `gcd(R_m, R_{m'}) = 1` — the cores do **not** nest and do
   **not** accrete a fixed growing factor. Each order `m` contributes a *genuinely new* irreducible
   bar-symmetric core, not a power/extension of a single element.

4. **Positivity at the substrate.** `R_m(1) > 0` and `R_m(q₀) > 0` for all `m` (the `(q−1)²` prefactor
   carries all of the `q=1` vanishing, so the core itself is `q=1`-nonvanishing and positive at the
   substrate).

The degree sequence (8, 10, 14, 28, 34, 46; diffs 2, 4, 14, 6, 12) and the `R_m(1)` sequence
(28, 16, 34, 1232, 1328, 9024) show no simple closed form — consistent with genuine
cyclotomic-completion content rather than a finitely-generated pattern.

## Interpretation and scope (AGENTS.md refuted-claim discipline)

- **Positive, derived (structural):** uniform palindromy (bar-evenness), per-order irreducibility,
  pairwise coprimality, and substrate positivity of the cores. These are exact facts on `m = 6..11`.
- **Bounded-`MMAX` observation, NOT a proved (b)-exclusion:** "the cores grow without bound and the
  binding correction is not reducible to a single finite element" is strongly supported (pairwise-coprime
  irreducibles of growing degree through `m = 11`) but is not a theorem. The Habiro-ring class remains
  the indicated home; nothing is refuted.

**Net structural picture (Stages 1–8).** The binding period `S(m) = Σ_{λ⊢m} dim_q(λ)` is the
q-involution skeleton (seed-exact) plus a correction `D(m)` that is *not* any finite low-order
q-difference operator (Stages 3–5) and *not* a single low-order q-hypergeometric element (Stage 6); its
exact structure is `(q−1)² ×` a `Φ_d` cyclotomic tower (with the odd-`d` rule `Φ_d | D(d+1)`, Stage 7)
`×` a tower of **pairwise-coprime, irreducible, bar-symmetric, substrate-positive** cores `R_m` of
growing degree (Stage 8). That is the genuine cyclotomic-completion (Habiro) residue the `kehn` /
`s5bb` shared object lives in.

## Next decidable step (not run here)

Two tractable directions: (i) test whether the bar-symmetric cores `R_m` are q-analogues of a known
combinatorial sequence (their `q=1` values 28, 16, 34, 1232, … and their substrate values are the data);
(ii) since each `R_m` is irreducible and bar-symmetric, examine its **root distribution on the unit
circle** vs off it — a bar-symmetric polynomial's off-circle roots come in `z ↔ 1/z` pairs, and the
on/off-circle split is the spectral fingerprint distinguishing a "q-special-function" core from a
generic bar-even residue.
