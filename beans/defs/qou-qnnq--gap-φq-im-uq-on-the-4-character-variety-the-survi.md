---
# qou-qnnq
title: "GAP: ϑ_K(q₀) — angular/spin deformation on the character variety of knot K. The surviving open DOF in the Δ_λ magnitude chain (\U0001D532_K = ln q₀ + i·ϑ_K). Knot-dependent: different particles = different ϑ. Determined by A(e^\U0001D532,ℓ)=0 boundary condition = G3 monodromy datum. Closes if Faddeev rigidity (hibinv+hratio) forces A_ω=3 AND pins the sheet. Probed values: ϑ_{4₁}(proton)=0.203, ϑ_{4₁}(muon)=0.059, ϑ_{4₁}(q*)=ln q*=0.104."
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-27T15:06:31Z
updated_at: 2026-10-04T15:13:02Z
parent: qou-n4nr
---

## Re-scope (2026-08-01, qou-fs0m) — corrected framing after Fantini–Wheeler

Reading Fantini–Wheeler 2024 (arXiv:2410.20973) onto this gap corrects two
framings that made the problem look harder than it is. See
`docs/audits/2026-08-01-fantini-wheeler-summability-c3-borel-reframe.md`.

1. **The "off-lattice ϑ" is NOT the obstruction it seemed — category error.**
   FW's ϑ is a *Borel ray angle* (peacock rays, accumulate at arg τ = ±π/2);
   this bean's ϑ_K is the *cusp shape* Im(𝔲_K) that feeds the volume V. Two
   different ϑ's. The cusp shape is **transcendental by construction** (it's
   the geometric datum), so ϑ_K being off the integer lattice is **expected**,
   not a defect. The "T4-inverted ϑ off the lattice = sharpest obstruction"
   framing is retired.

2. **"A_ω = 3 for all winding classes" is too coarse.** The literature Stokes
   object for these knots is an **integer matrix** S(q) ∈ GL_{max{A,B}}(Z[q^±])
   with a KS cocycle (FW eqs. 26–27), not a scalar. For 5₂: (A,B)=(2,3),
   max=3 (the σ₁σ₂σ₃ geometric connections); the "4-character variety" here =
   the *extended* matrix (+ trivial σ₀). The AK state integral is the
   (m,ℓ)=(0,0) member of a rank-max{A,B} `Z[q^±]`-module `I_{m,ℓ}`.

**Restated open problem:** not "which single integer (m,ℓ)/A_ω does a braid
word pick" but **which entry/row of the GL_{max{A,B}}(Z[q^±]) Stokes matrix a
given braid closure selects, and how c₃ reads off it.** This is route 2 of the
original analysis, now literature-supported. Follow-ups: qou-3xug (5₂ AK
integral), qou-6yf7 (4₁ Stokes series), qou-cm6a (Lean conditional bridge).
Still OPEN — no fit, nothing wired.

## Cusp-shape fork (2026-08-01, qou-iyf6 finding B) — the premise needs a choice

This bean's framing ("different particles = different ϑ_K") silently assumes a
**free, per-particle** cusp datum *on a fixed knot*. That is **forbidden by the
geometric invariant**: the complete-hyperbolic-structure cusp shape is a *fixed
topological invariant of the knot*. The corpus's own
[`cusp-shape-bar-parity`](../folio/quantum-observable-universe/braids-and-knots/cusp-shape-bar-parity.md)
pins `4₁ → ω = e^{iπ/3}` (Φ₆ root, trace field ℚ(√−3)), computable by
Neumann–Zagier / SnapPy. So if the proton and the muon are **both** 4₁-based
they have the **same** geometric ϑ_K — the per-particle-varying ϑ is impossible
at the complete structure. The probed off-lattice values
(`ϑ_{4₁}(proton)=0.203`, `ϑ_{4₁}(muon)=0.059`) are therefore **not** the
geometric cusp shape.

**The fork — pick one; do not leave it unqualified:**

1. **Deformed / incomplete structure (same knot).** ϑ_K is the cusp datum of an
   *incomplete* hyperbolic structure (a Dehn-filling / boundary-holonomy
   deformation off the complete point), so a single knot supports a
   one-parameter family of ϑ and different particles sit at different points of
   it. Consistent with
   [`meridian-holonomy-boost`](../folio/quantum-observable-universe/braids-and-knots/meridian-holonomy-boost.md):
   at real `q₀>1` the meridian turn is a **boost of rapidity ln q₀**, i.e. the
   incomplete/deformed regime, not the compact-spin complete point. If this is
   the intended reading, restate ϑ_K as an *incomplete-structure boundary
   holonomy*, not "the cusp shape," and the selection question becomes *which
   deformation parameter* the observable fixes.

2. **Different knots (fixed complete structures).** Each particle is a
   *different* knot/link, each with its own fixed geometric ϑ_K; then "different
   particles = different ϑ" is just "different knots have different cusp
   shapes," and the open problem is the *particle → knot* assignment, not a
   continuous ϑ.

These are genuinely different physical pictures with different open problems.
The bean must commit to one (or explicitly keep both live) rather than assume a
free same-knot per-particle ϑ, which the geometric invariant rules out. Still
OPEN — no fit, nothing wired.


## Target sharpening (PR #4554, 2026-08-02, A_omega=3 leg)

The A_omega = 3 closing condition is the **q-EXACT symmetry constant** (GGM eq 65,
S12+S21 = 3*S11), q-independent (StokesSymmetryConstant.symmetryConstant_const,
sorry-free). A q-independent quantity equals its own q-to-0 value, so there is no
resurgent tail in the integer target. Deriving A_omega=3 internally collapses to
deriving the decidable q-to-0 3d-index/DT count S+(0)_12 = 3 from Hecke/Bring data
(drivers 11/13, NOT driver-12 resurgence).

New sorry-free brick StokesSymmetryConstantQZero.lean (lean-direct exit 0) connects
StokesQZeroDTCount and StokesSymmetryConstant at q-to-0: the symmetry-constant reading
of the certified S+(0)=[[1,3],[0,1]] is exactly 3.

STILL OPEN (scope-(a)): the only route to that q-to-0 count is numerically identical to
importing GGM state integral; missing ingredient = a categorical formula for the DT
count from QOU Hecke/Bring data reproducing the pair {3,4} across knots — open in the
DT-categorification literature, not just QOU. disc(Q(sqrt-3))=-3 stays refuted (a 4
co-occurs); single-knot count-matching stays a trap (5_2 block is 3x3).

Tentative, UNCLAIMED re-scoping worth a probe: the symmetry constant 3 is narrower than
the spectrum {3,4}, so a scalar internal invariant for the constant alone may re-open,
subject to a cross-knot test on 5_2, unchecked.

Audit: docs/audits/2026-08-02-aomega-internal-derivation-symmetry-constant-target.md

## Bridge-derivation test + unification (PR #4599, 2026-08-02)

Owner directive: derive Stokes=DT (the bridge's first equality) from a QOU
structure, getting the DT count 3 as a QOU-computable graded Euler characteristic
("Euler = -6"). RESULT (honest negative, machine-checked sorry-free):

- The QOU Wedderburn/Springer Euler-char machinery (dtEulerG, proved on main) is a
  PARTITION-level object. For 4_1 = closure of 3-braid (s1 s2^-1)^2 -> H_3, blocks
  lambda|-3: Sigma Delta_lambda = 1-2-1 = -2.
- The GGM sandwich = -2*S+(0); off-diag -6 = (-2)*3. QOU supplies the NORMALIZATION
  -2 (= Sigma_{lambda|-3} Delta_lambda), NOT the COUNT 3. -2 != 3, decidable.
- So Stokes=DT does NOT derive from the QOU Euler-char machinery. The count 3 is the
  Behrend/BPS invariant of the character-variety spectral curve A_{4_1}=0 (rotated
  3d-index) - geometric, external. A non-degenerate Stokes=DT-conditional-on-QOU
  theorem CANNOT be honestly written (grading gives -2 not 3); forcing one = -6->3
  convention-fit (forbidden). None landed.
- UNIFICATION: same missing input as the Delta_lambda Springer-fibre DT-realization
  (Rossmann-CC, 2026-08-02, proved external) - a driver-built Behrend-weighted DT
  MODULI, at two levels (partition Springer fibre vs knot character variety).
- Maximal derivable fragment: Delta_lambda=DT (partition, proved) + Stokes-matrix
  SHAPE (AJ recursion order = A-poly L-degree = block dim, proved for 4_1). Both
  give the block SIZE, not the DT count (recursionOrder < dtOffDiag: 2<3, 3<4).
- L2: A_omega=3 is L2-ORTHOGONAL (zero movement). canonical_mass.py + Q_beta
  production formula carry no A_omega/Stokes; the 7 L2 observables derive from q0 +
  c_k. Banked as (a) real structural theorem, L2-orthogonal.

Lean: StokesDTCountExceedsRecursionOrder.lean (sorry-free, core-Lean).
Audit: docs/audits/2026-08-02-stokes-dt-bridge-moduli-gap-unification.md.
STILL OPEN: the named missing driver-14 (categorical Behrend-weighted DT moduli of
the character variety / T[K] BPS Hilbert space) - external per DT-categorification
literature; not a QOU wiring gap.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (PR litlfred/qou#8222)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8222 (`95ddc04a72f67a43b1ccf1d77e08572625847a9b`, scriptCommitSha `4ed1888aba96f0c3e837a57c93b666bdd892604e`)
- **Summary**: Added `stokes_unipotent_trace_inv`, `stokes_unipotent_det_one`, and `stokes_multiplier_add` in `QOU/TraceFormula/BorelSummability.lean`, verified by 80-dps mpmath probe `keystone_writhe_ramified_stokes_ladder_probe.py` (`scriptHash: 75539ba8f436`).
