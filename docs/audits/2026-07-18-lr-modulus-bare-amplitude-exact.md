# The bare flat-connection amplitude of Σ(2,3,5) is the vacuum modular S-matrix element, exactly: A_m(1) = (2/√5)·sin(mπ/5)

**Date:** 2026-07-18 · **Branch:** `claude/lr-modulus-habiro-continuation-2026-07-18` ·
**Tier:** exact-arithmetic (sympy + ℚ(√5)) · **Discipline:** scope-(a); no fit; nothing wired;
μ–p tension NOT resolved; no `c_k` wired; L2 unchanged (2/7). **Closes:** the ~1% machine-evidence
bare-amplitude precondition left open by `habiro_interpolation_wlambda.py` (the `loc_matches` /
`bwS0_eq_hecke` gate).

## What this closes

The W_λ keystone value-map (targeting m_p/m_μ) rests on the Lawrence–Rozansky modulus identity
`|S_{0λ}(ζ)| = 2·d_ζ(λ)/D(ζ)`. Merged #3822 established this at the fibre **roots** exactly in
ℚ(√5); `habiro_interpolation_wlambda.py` then extended the uniform candidate `F_λ = [mark]²/D²`
to all four exceptional-fibre roots — but left the **bare flat-connection amplitude** `A_m(1)`
(the color-independent factor in `|A_m(α)| = |A_m(1)|·|[α]_ζ|`) as **~1% machine-evidence** from
a finite-N Gauss-sum extraction. That is the amplitude the Lean `KeystoneLRModulusFold.lean`
carries as `A_m(α) = ±(2/√5)sin(αmπ/5)` without proof, and it is the precondition for the
`loc_matches` gate. This probe closes it **exactly**.

## The result (exact, no fit)

For the two flat connections `m ∈ {1,2}` of Σ(2,3,5) (roots `ζ^m = e^{imπ/5}`, the Galois pair):

    A_m(1) = 2/D(ζ^m) = (2/√5)·sin(mπ/5),      D(ζ¹)² = 10+2√5,  D(ζ²)² = 10−2√5.

i.e. the bare amplitude **is** the vacuum modular S-matrix element `S_{00}(ζ^m)`. Two ingredients,
both exact:

1. **The exact radical identity** `(2/√5·sin(mπ/5))² = 4/(10±2√5)` — verified symbolically
   (sympy, exact radicals), reducing to `0` for both `m`.
2. **The exact fold value** `D²(ζ^m) = Σ_McKay [mark]²_{ζ^m} = 10±2√5` — verified in exact ℚ(√5)
   arithmetic (the #3822 fold machinery).
3. **The link `A_m(1) = 2/D(ζ^m)`** is #3822's already-exact root identity `|S_{0λ}| = 2·d_ζ(λ)/D`
   read at the **vacuum** (`λ = triv`, mark 1, `d_ζ = [1] = 1 ⇒ |S_{00}| = 2/D`).

So `A_m(1)` is **derived from established exact quantities**, not extracted. Numerically
`A_1(1) = 2/√(10+2√5) = 0.5257311…`, `A_2(1) = 2/√(10−2√5) = 0.8506508…` (the Fibonacci/icosahedral
S-matrix entries).

### Corroboration (not load-bearing)

A parameter-free 2×2 flat-basis inversion of Hikami's colored Gauss sum `τ_N` agrees with
`2/D(ζ^m)` to ≈0.5% on well-conditioned N-pairs (|det| ≳ 100). Some N-pairs are **ill-conditioned**
— the two connections' Chern–Simons phases `e^{−πiN/60}, e^{−49πiN/60}` align, collapsing the 2×2
basis determinant to `~10⁻³⁷` — and are skipped. This is an illustration of the exact result, not
a proof; the result rests on the exact ingredients above.

## Consequence — the full colored amplitude closes exactly

With the LR factorization `|A_m(α)| = |A_m(1)|·|[α]_{ζ^m}|` (verified at orders 2,3,5 in
`habiro_interpolation_wlambda.py`) and the color character `|[α]_{ζ^m}| = |sin(αmπ/5)/sin(mπ/5)|`:

    A_m(α) = (2/√5)·|sin(α·m·π/5)|   (exact closed form).

This upgrades the `KeystoneLRModulusFold.lean` amplitude from ~1% machine-evidence to an **exact
identity** — the precondition for the `loc_matches` / `bwS0_eq_hecke` gate and for the archimedean
Habiro continuation of the folded root identity to generic q₀ (the standing m_p/m_μ continuation
problem, #3652/#3681).

**Lean-ready.** The core is a pure exact-radical identity `(2/√5·sin(mπ/5))² = 4/(10±2√5)` plus the
exact ℚ(√5) fold `D²(ζ^m) = 10±2√5` — both discharge with `nlinarith`/`nsimplify`-style radical
arithmetic once `sin²(mπ/5)` is written via the minimal polynomial of `2cos(mπ/5)`. It is the
next commit in `KeystoneLRModulusFold.lean` (promoting the amplitude comment to a theorem).

## What this does NOT do

It closes the *bare-amplitude precondition*, not the keystone. The open piece remains the
**archimedean 4-class separation** — whether the explicit `F_λ(q)` continues to real q₀>1 with the
`(1, [4]_q, [5]_q, [5]_q+1)` separation the mass ratio needs, and whether the multi-root values
*uniquely* pin the Habiro element (Habiro injectivity, class hypothesis #3681). μ–p tension is NOT
resolved; nothing is wired.

## Compute

- Probe: [`computations/lr_modulus_bare_amplitude_exact.py`](../../computations/lr_modulus_bare_amplitude_exact.py) (exit 0)
- Witness: `computations/lr-modulus-bare-amplitude-exact.witness.json`

## Cross-references

- The exact root identity this builds on: [`2026-07-17-lr-modulus-identification.md`](2026-07-17-lr-modulus-identification.md) (#3822), `computations/lr_modulus_identification_sigma235.py`
- The candidate + factorization: `computations/habiro_interpolation_wlambda.py`
- Lean carrier: [`content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneLRModulusFold.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneLRModulusFold.lean)
- Keystone ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
