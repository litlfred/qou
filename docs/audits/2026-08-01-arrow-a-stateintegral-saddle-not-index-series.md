# W1 arrow (A): the volume-route resummation is the state-integral saddle, not the index q-series

**Date:** 2026-08-01
**Tier:** audit-only; scope-(a); no fit; nothing wired; L2 unchanged.
**Epic:** W1 binding-mass `I_𝓑₃ → tr_M(β_Bor)` bridge (arrow A). Follow-on to the
Jones-side chain (#4208 Vol=8G · #4238 c₀ · #4253 NZ-torsion=64 · #4261 factor
`2^(c−1)`) and the invariant list
[`2026-07-24-borromean-index-bridge-invariant.md`](2026-07-24-borromean-index-bridge-invariant.md).

## The question

The invariant list §1(d–e) names the DGG **volume-asymptotics route** (q→1
't Hooft limit; the index's leading asymptotics carry `Vol(M)`) as "the honest
candidate" for arrow (A) — but never says **how** to extract `Vol` from the
index. This audit settles that, on the cheap figure-eight testbed and the
Borromean target, and records the two natural routes that **fail**.

## Two index-series routes FAIL (empirical)

Producer [`arrow_a_stateintegral_saddle.py`](../../computations/probes/arrow_a_stateintegral_saddle.py),
using the corpus's validated `I_D` tetrahedron-index machinery
(`figure_eight_3d_index.py`, checked against GHHR Ex 4.1). Total index
`I^tot_{4₁}(q) = Σ_{e∈ℤ} I(eμ)(q)`, coefficients verified **stable to q⁶⁰**
(cutoff-independent):

`a = [1, −8, −9, 18, 46, 90, 62, 10, −170, −424, −707, −962, −980, −569, 192, 583, 350, 16, −32, …]`

1. **Naive `q→1` evaluation** — `I^tot(q)` is **sign-indefinite** near `q=1`
   (−48 at q=0.7 → −1500 at q=0.95): the truncated growing tail + the sign
   structure dominate, so `(1−q)·log I^tot` is meaningless.
2. **Circle-method coefficient asymptotics** — the coefficients **peak at n≈12**
   (`|a|≈980`) and **decay to ≈0 by n≈19**. There is **no `exp(V/(1−q))`
   essential singularity at `q=1`**, so the standard `log|aₙ| ~ 2√(Vn/2π)` law
   gives garbage (fit → `V≈1239`, not `2.03`). The total index is simply not the
   object that carries `Vol` as coefficient growth.

## The proper resummation — the state-integral saddle (uses symmetries)

The state integral (Andersen–Kashaev; "closely related to the total index",
GHRS arXiv:1303.5278 Rmk 1.13 \[garoufalidis-hodgson-rubinstein-segerman2015\]; corrected 2026-11-22, this read arXiv:1604.02688, which is GHHR, a different paper) is the **Borel sum** of the divergent
perturbative series; its `ℏ→0` **saddle value** is the complex volume.
Amphichirality of `4₁` (`CS = 0`) makes that saddle **purely real**, and the
octahedral `S₃` symmetry fixes the Borromean shapes. The saddle value is the
Bloch–Wigner dilogarithm at the shapes, `D(z) = Im Li₂(z) + arg(1−z)·log|z|`:

| link | saddle | value | exact |
|---|---|---|---|
| `4₁` | `2·D(e^{iπ/3})` | 2.02988321 | `Vol(4₁)` (CS=0) |
| **`𝓑₃`** | `8·D(i)` | **7.32772475** | **`8G = Vol(𝓑₃)`** |

Both reproduce the hyperbolic volume **exactly**, and `8G` matches the Jones-side
anchor (#4208) and the NZ-torsion probe (#4253). So the volume-route resummation
is the **state-integral saddle = classical dilog at the symmetry-fixed shapes** —
the **shared geometric datum** that both the colored-Jones asymptotics and the
index/state-integral carry.

## What this closes / does NOT close

- **Closes:** the *method* question for arrow (A)'s volume piece — it goes through
  the saddle, **not** the index series (two natural series routes empirically
  ruled out, per the record-eliminated-routes discipline). Future agents should
  not re-attempt naive `q→1` or circle-method coefficient asymptotics on the
  total index.
- **Does NOT close arrow (A):** the actual map `I_𝓑₃ → tr_M(β_Bor)` is the full
  DGG 3d-3d / quantum-modularity dictionary. The shared saddle data — leading
  `Vol` (this audit) and subleading 1-loop **torsion = 64** (#4253) — is the
  geometric anchor **both sides must share**, but the non-perturbative map to
  `tr_M`'s actual values remains the research-scale open sub-problem. The next
  rung is the state-integral **subleading** (the torsion/`ρ` amplitude) computed
  from the saddle Hessian, to be matched against #4253 on the index side.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
