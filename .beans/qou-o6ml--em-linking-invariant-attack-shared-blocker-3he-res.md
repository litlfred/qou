---
# qou-o6ml
title: 'EM-linking invariant ATTACK (shared blocker: 3He residual 69% + m_d-m_u extraction): trichotomy of routes — (1) higher-order Milnor/third-order-helicity integrals (pairwise lk=0 in Brunnian B3 kills first-order Gauss), (2) Mobius/knot-energy class (nonzero for unlinked pairs; corpus MobiusEnergy.lean exists), (3) h-graded per-pair Hecke trace channel at H_2A with Hochschild-homology classification of trace functionals (Solleveld 1108.5286, uploaded). GATE: must reproduce kappa(A) profile 3.2->2.1-2.3 from em-linking-invariant-scoping witness; no tuned constant (CAL-4)'
status: todo
type: task
priority: normal
created_at: 2026-08-01T15:18:09Z
updated_at: 2026-08-30T12:41:35Z
---

**`qou-bn8e` merged in, 2026-08-30 — with two constraints on this bean's target.**

`qou-bn8e` ("intra-nucleon EM self-energy `E_EM` is not derived") is the same
object as this bean's two-like-charge EM-linking invariant. `qou-m3vl` said so
on 2026-08-01 — *"the intra-nucleon EM self-energy is the SAME open
two-like-charge EM-linking invariant that owns the ³He mirror residual; one
invariant blocks both"* — but that conclusion lives only in
`quark-mass-extraction-stage1.witness.json`, because `qou-m3vl`'s bean body is
empty, so a `.beans/` grep cannot find it.

**Constraint 1 — the coefficient is not free; the RATIO is a theorem.**
From the cheat sheet (§3 item 2, *"a theorem, not a fit"*) plus Lean:
`[n]_q = sinh(nλ)/sinh(λ)` with **cosh = strong, sinh = Coulomb**;
`h = 2 sinh(ln q)` (`QOU.Mass.MassVolDensity.h_crossing_eq_two_sinh_log`);
`[2]_q = 2 cosh(ln q)`. Hence the Coulomb-to-strong ratio is

    h / [2]_q = tanh(ln q)   →   tanh(ln q₀) = 0.10396371005241013891

derived, parameter-free. `quark-mass-extraction-stage1` independently names the
framework's only derived EM mechanism as **`tanh(ln q₀) × strong bond`**, and
`QOU.MassTheory.EmGermMomentVanishing.emMoment` (`−h/[2]_q`, reached from germ
curvature) is **algebraically identical** to `−tanh(ln q₀)` (checked to 3.3e-52
at 50 dps). So what this bean owes is **the bond `tanh(ln q₀)` multiplies**, not
a free coupling.

**Constraint 2 — `wᵢⱼ` must be EVEN in `μ̄₁₂₃`, which prunes route (1).**
Two proved facts compose:

* `mirror_split_s3_em_functional_probe.py` **(A3)**: for L6a4 (the Borromean
  link) every pairwise `lk_ij = 0`, so any nonzero `wᵢⱼ` is mediated by
  `μ̄(123)`, the triple channel.
* `QOU.BraidsAndKnots.MilnorTripleLinkingMagnus.odd_symmetric_functional_vanishes`
  (sorry-free): an **odd** `F` agreeing on the Borromean and swapped longitudes
  vanishes — hypothesis: exchange-symmetry of a two-like-charge Coulomb
  self-energy. Companion `linear_coefficient_must_vanish`: `E_EM = c·μ̄₁₂₃`
  forces `c = 0`.

⟹ **`wᵢⱼ` depends on `μ̄₁₂₃` evenly** (`μ̄²`, `|μ̄|`), never linearly. This bean's
route **(1)** (higher-order Milnor / third-order helicity) should not spend a
pass on a linear-in-`μ̄` ansatz; it is already excluded.

**What did NOT merge.** `bn8e`'s **self**-term question (`A·Σqᵢ²`). Probe axiom
(A1) derives `a = 0` for **binding energy** (`B = Z·m_p + N·m_n − M`) because
single-component self-energy lives in `m_p`, `m_n` — but `m_n − m_p` is a
difference of **free** masses, not a binding energy, so A1 does not touch it.
That stays in `bn8e`; this bean owns only the pairwise/linking channel.

Note `qou-17mq` (O2 neutrality obstruction) still reshapes this bean's
*statement*, independently of the above.
