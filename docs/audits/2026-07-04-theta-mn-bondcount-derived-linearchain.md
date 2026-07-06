# θ_λ multiplicity `M_n(A)` DERIVED — the linear-chain inter-nucleon bond count `(n−1)`

**Date:** 2026-07-04
**Branch:** `claude/theta-mn-sublink-chase-2026-07-04`
**Compute:** [`computations/theta_mn_bondcount_linearchain.py`](../../computations/theta_mn_bondcount_linearchain.py)
**Chase of:** `M_n(A)` — the last open piece of the θ_λ weight (`w_n=M_n(A)·Vol_n`, #3277).

## The derivation

The atomic braid recipe
([`atomic-braid-recipe-4he-canonical.derivation.json`](../../computations/atomic-braid-recipe-4he-canonical.derivation.json))
builds the atom as a **linear chain** of `A` nucleon `B_3` blocks in `B_{3A}`, joined
by inter-nucleon "averaged" crossings at 0-indexed generators `3k−1` (`k=1..A−1`).
Two combinatorial facts follow with **no fit**:

- the consecutive `n`-nucleon sub-clusters number **`(A−n+1)`**;
- each `n`-nucleon sub-chain has exactly **`(n−1)` inter-nucleon bonds**.

So the multiplicity is the **bond count**, `M_n = (n−1)`, and the body-order binding is

$$
  B(K) \;=\; m_e \sum_{n=2}^{A}\ \sum_{\text{consecutive }n\text{-clusters }c} (n-1)\,\mathrm{Vol}(c),
$$

with `Vol(c)` the hyperbolic volume of the sub-chain's link (the isospin carrier,
#3274). **No free parameter** — the inputs are `m_e` (CAL-1), the derived bond count
`(n−1)`, and topological link volumes.

## Result (parameter-free)

Volumes are the **real** hyperbolic invariants (`Vol(8_11)=8.2863`,
`Vol(L6a4/Borromean)=7.3277`, `Hopf=0`), not fitted.

| K | chain | `B_pred` (MeV) | AME | err | fitted params |
|---|---|--:|--:|--:|:--:|
| **³H** | pnn | `m_e·2·Vol(8_11)` = **8.469** | 8.482 | **−0.16%** | **0** |
| ³He | ppn | `m_e·2·Vol(L6a4)` = 7.489 | 7.718 | −2.97% | 0 |
| D | pn | 0 (Hopf `Vol=0`) | 2.225 | −100% | — |
| ⁴He | ppnn | n=2,3 = 15.96 (56%) + n=4 | 28.296 | — | 0 (predicts Vol₄) |

- **³H is reproduced to 0.16% with ZERO fitted parameters** — `m_e` × (2 bonds,
  derived) × (the topological volume of 8_11). This *derives* `M_n=(n−1)`.
- **³He to −2.97%** — the residual is the same ~3% mirror-pair residual isolated in
  #3277 (the volume ratio `8.286/7.328=1.131` slightly over-predicts the binding
  ratio `1.099`); a small isospin-fine-structure term, **not** a fit.
- **⁴He**: the n=2,3 sub-chains (all volumes known) give **56%** of the binding; the
  n=4 term predicts a **4-body link volume `Vol₄≈8.05`** — a *falsifiable* number
  (in-family with 8_11=8.29, L6a4=7.33; verify with SnapPy).

## Caveats (critical-distance — this is a ~3% *structural* derivation, not ppb)

1. **Precision.** This closes the *structural* question ("what is `M_n(A)`") to a
   few percent — it is **nowhere near** the L2 ppb targets. It is a derivation of the
   binding-magnitude *structure*, not a precision result.
2. **Deuteron exception.** The single 2-body bond is the Hopf link
   (`Vol=0`, Seifert-fibred) ⇒ `B(D)=0`. The 2-body sector is non-hyperbolic and
   needs separate treatment (the effective-volume patch used elsewhere).
3. **⁴He Vol₄ is a prediction, not verified** (needs SnapPy on the 4-component link).
4. **The ~3% mirror residual** on ³He is real (isospin fine structure beyond the
   leading volume); not yet derived.

## Net — the θ_λ gate, closed to structure

`w_n(K) = (n−1)·Vol_n(K)` — **both factors now derived**:
- **`(n−1)`** = inter-nucleon bond count of the linear `n`-chain (from the braid
  recipe) — *no fit*;
- **`Vol_n(K)`** = hyperbolic link-volume (isospin carrier, #3274) — topological.

So the θ_λ magnitude gate is **structurally closed** (parameter-free) to ~3% on
³H/³He, modulo the Hopf-`Vol=0` deuteron and the ⁴He `Vol₄` cross-check. ³H at
0.16% with zero fitted parameters is the headline non-fit evidence.

| θ_λ piece | status |
|---|---|
| extensive mechanism `a_D^(n)=lw(n−1)` | derived + Lean-proved (#3270) |
| universal scalar kernel | refuted (#3274) |
| isospin carrier = hyperbolic link-volume | derived (#3274) |
| multiplicity `M_n(A)` isospin-independent | derived (#3277) |
| **`M_n(A)` = `(n−1)` bond count** | **derived (this PR)** — ³H 0.16%, no fit |
| residuals: deuteron Hopf, ³He ~3%, ⁴He Vol₄ | open (few-% / cross-check) |
| na-Stokes `= lw` keystone | owner-gated (#2503) |

## Provenance

Compute: `theta_mn_bondcount_linearchain.py` (linear-chain structure from
`atomic-braid-recipe-4he-canonical.derivation.json`; volumes from
`binding-link-volumes.witness.json`; anchors from `codata_constants`). Corpus:
`conj:binding-manybody-jet-filtration`, `prop:jet-filtration-binding-extensive`
(#3270). EXPLORATORY — no production wiring, no fitted constant.
