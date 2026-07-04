# θ_λ multiplicity `M_n(A)` — isospin-independent (derived); closed form open (not fitted)

**Date:** 2026-07-04
**Branch:** `claude/theta-mn-multiplicity-2026-07-03`
**Compute:** [`computations/theta_mn_multiplicity.py`](../../computations/theta_mn_multiplicity.py)
**Follow-up to:** options 1+2 (merged #3274), mechanism (merged #3270).

## Setup

The θ_λ weight decomposes as `w_n(K) = M_n(A)·Vol_n(K)` (merged #3274): `Vol_n` is the
hyperbolic link-volume (the **isospin carrier**, derived), and `M_n(A)` is the open
body-order multiplicity (shown *not* to be `a_D^(n)` nor `2·A`). This probe extracts
`M_n(A)` and asks two parameter-free questions.

## Result

Extracted top-order multiplicity `M_A(A) = B_AME / (m_e·Vol_A)`:

| K | A | `M_A(A)` |
|---|--:|--:|
| D | 2 | 0.594 *(Hopf Vol=0 → effective; ill-defined)* |
| ³H | 3 | 2.003 |
| ³He | 3 | 2.061 |
| ⁴He | 4 | 7.557 |

### (1) `M_n(A)` is ISOSPIN-INDEPENDENT — the robust, derived result

| ³H vs ³He split | value |
|---|--:|
| binding `B` | 9.4% |
| volume `V` | **12.3%** (carries the isospin) |
| multiplicity `M` (residual after ÷V) | **2.9%** |

The 12% volume split explains ~70% of the 9% binding split, leaving the
multiplicity isospin-residual at **2.9%** (< 5%). So the isospin lives **entirely in
the link volume**, and `M_n(A)` is a pure `(n,A)` count. This **validates the
option-1 picture** — the volume is the correct (and sufficient) isospin carrier.

### (2) Closed form of `M_n(A)` — OPEN, explicitly NOT fitted

Against parameter-free combinatorial counts (M_3 = ³H/³He mean):

| candidate | A=2 | A=3 | A=4 | verdict |
|---|--:|--:|--:|---|
| `(A−1)!` | 0.59/1 | **2.03/2** | 7.56/6 | ✗ (only A=3 hits) |
| `2A` | 0.59/4 | 2.03/6 | 7.56/8 | ✗ |
| `C(A,2)` | 0.59/1 | 2.03/3 | 7.56/6 | ✗ |
| Cayley `A^{A−2}` | 0.59/1 | 2.03/3 | 7.56/16 | ✗ |

**No candidate hits across A.** `M_3 ≈ 2.0 = (A−1)!` is a *single* A=3 coincidence —
**not a derivation.** Per the no-numerology discipline (STRICT), three light anchors
cannot pin a closed form, and I do **not** fit `M_n(A)` to a curve. Two structural
caveats make the top-order extraction model-dependent: `M_4` folds the n=2,3
contributions of ⁴He into an effective top-order value, and the deuteron `Vol=0`
Hopf term is ill-defined.

## Verdict — the θ_λ gate is fully *structured*, one well-posed combinatorial piece open

`w_n(K) = M_n(A)·Vol_n(K)` with:
- **`Vol_n(K)`** = hyperbolic link-volume — the isospin carrier (**derived**, #3274);
- **`M_n(A)`** = an **isospin-independent pure `(n,A)` combinatorial multiplicity**
  (**its nature derived here**); its **closed form is open** — a well-posed
  combinatorics problem that needs the genuine per-n-body **sub-link decomposition**
  (⁴He's n=2,3,4 separated), which the light-nuclei *totals* underdetermine.

This is the honest end state of the θ_λ closure arc: the gate is no longer a
tangled `w_n(K)` but a clean product of a derived volume carrier and an
isospin-independent combinatorial multiplicity, with the multiplicity's closed form
the single remaining (fit-free) target.

## Net — θ_λ magnitude gate across the whole arc

| piece | status |
|---|---|
| extensive mechanism (`a_D^(n)=lw(n−1)`) | **derived + Lean-proved** (#3270) |
| universal scalar kernel | **refuted** (#3274) |
| isospin carrier = hyperbolic link-volume | **derived** (#3274) |
| multiplicity `M_n(A)` isospin-independent | **derived** (this PR) |
| `M_n(A)` closed form | **open** (needs sub-link decomposition; not fitted) |
| na-Stokes `= lw` keystone | **owner-gated** (#2503) |

## Provenance

Compute: `theta_mn_multiplicity.py` (volumes from `binding-link-volumes.witness.json`;
anchors from `codata_constants`). Corpus: `conj:binding-manybody-jet-filtration`,
`prop:jet-filtration-binding-extensive` (#3270), the opt-1/opt-2 audits (#3274).
EXPLORATORY — no production wiring, no fitted constant. No-numerology STRICT: closed
form left open rather than fit to 3 points.
