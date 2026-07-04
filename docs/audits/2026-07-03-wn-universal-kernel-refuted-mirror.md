# θ_λ closure option 2 — universal scalar kernel `R(q,x)` REFUTED by the mirror pair

**Date:** 2026-07-03
**Branch:** `claude/theta-wn-closure-2026-07-03`
**Compute:** [`computations/theta_wn_kernel_derive_or_refute.py`](../../computations/theta_wn_kernel_derive_or_refute.py)
**Follow-up to:** PR #3270 (θ_λ extensive mechanism, merged) — closure option 2.

## Setup

The jet-filtration binding `B(K)=Σ_{n=2}^{A} m_e·a_D^(n)·w_n(K)` has its extensive
mechanism established and Lean-proved (`QOU.Mass.jetBinding_mono`, PR #3270). The
open piece is the residue weight `w_n(K)`. Closure **option 2** tests the
conjecture's own claim that its growth is a **q-difference recursion output**
`G(qx;q)=R(q,x)G(x;q)` — i.e. a *universal* (K-independent) scalar kernel — versus
a per-isotope (fitted) weight.

## The decisive test — the mirror pair

Extract the universal per-body-order weights from the four AME anchors
(`a_D^(n)=lw(n−1)` from the merged probe; `a_D^(2,3,4) = 1.000, 1.337, 2.533`):

| weight | from | value |
|---|---|--:|
| `w_2` | D (A=2, only n=2) | 4.353 |
| `w_3` | ³H (A=3) | **9.159** |
| `w_3` | ³He (A=3) | **8.041** |
| `w_4` | ⁴He (A=4) — *conditional*† | 15.604 |

†`w_4` is only defined *after* choosing the `w_3` to subtract; since universality is
already refuted at A=3, there is no unambiguous universal `w_4`. The value shown uses
the isospin-symmetric mirror average `w_3=(w_3^{³H}+w_3^{³He})/2` (⁴He has T₃=0), for
completeness — it is **not** a well-defined universal weight.

The **mirror pair** ³H (Z=1,N=2) and ³He (Z=2,N=1) have the same `A=3` and the same
body orders `{2,3}`, so a *universal scalar* `w_n` forces `w_3(³H)=w_3(³He)`.
Measured split: **13.0 %** — decisively non-zero.

## Verdict — REFUTED (a fit shortcut ruled out; convergence on option 1)

- **A universal scalar q-difference kernel `R(q,x)` is refuted.** The mirror split
  means `w_n(K)` depends on `(Z,N)`, not just the body order `n` and mass `A`.
  Forcing a single scalar kernel to fit both mirror partners would require a
  per-isotope constant — i.e. a **fit**, which the three-calibration discipline
  forbids (STRICT). So option 2 *rules out the scalar-kernel shortcut* rather than
  supplying a closure.
- **`w_n(K)` carries isospin (`T₃`) structure** — exactly the **IMME degree-2**
  form already established on main
  (`docs/audits/2026-06-29-delta-lambda-imme-askey.md`:
  `log_q₀ Δ_λ = a(A) + b(A)·T₃ + c(A)·T₃²`). The residue weight is `w_n(A, T₃)`,
  not a single scalar recursion output. The 13 % `w_3` split *is* the `b(A)·T₃`
  term of the mirror pair (this is also the open **A=3 mirror magnitude**, gap #3).
- **Closure converges on option 1.** A `(Z,N)`-aware weight is exactly what the
  **per-sub-link hyperbolic volume** supplies: the `n`-body inter-nucleon sub-link
  of `𝓑_K` has a topology (linking, chirality) that distinguishes ³H from ³He, so
  its hyperbolic volume is intrinsically isospin-dependent. Option 2 therefore
  **eliminates the scalar-kernel alternative and points closure at option 1**
  (`w_n(K)` = hyperbolic link-volume), the recommended non-fit route.

## Net

Two closure options were on the table for `w_n(K)`; option 2 (universal kernel) is
**refuted** — cleanly, by a parameter-free mirror-pair test — leaving **option 1**
(per-sub-link hyperbolic volume) as the route, now motivated not just by the `n=4`
`Vol(L6a4)` anchor but by the *requirement* that the weight be isospin-aware. Next:
compute the `n`-body sub-link hyperbolic volumes (option 1); coordinate the
per-knot volume infra with #3205.

## Provenance

Compute: `theta_wn_kernel_derive_or_refute.py` (anchors from `codata_constants`;
`a_D^(n)=lw(n−1)`). Corpus: `conj:binding-manybody-eq-jet-filtration`,
`docs/audits/2026-06-29-delta-lambda-imme-askey.md` (IMME T₃ form),
`prop:jet-filtration-binding-extensive` (PR #3270). EXPLORATORY — no production
wiring, no fitted constant.
