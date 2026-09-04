---
# qou-jvua
title: 'BUILD: differential k-forms on a manifold as ContMDiffSection of the alternating bundle — Mathlib has them on normed spaces only'
status: todo
type: task
priority: normal
created_at: 2026-09-04T09:07:55Z
updated_at: 2026-09-04T09:07:55Z
parent: qou-8lxd
---

**BUILD (also upstreamable).** The corpus cannot state `Θ ∧ dΘ`, or the hyperbolic
volume form, *as a form*. `QOU/Eightfold/ContactDistributionRank.lean` and
`QOU/Eightfold/HyperbolicVolumeFormType.lean` are honest about this and work entirely
in `ℕ` arithmetic as a result — every "degree 3" statement there is a `Nat.choose`
identity, not a statement about a form.

**Mathlib status, measured 2026-09-04 at mathlib `f897ebcf72c`:**
* `Analysis/Calculus/DifferentialForm/Basic.lean` — forms and `extDeriv` on a **normed
  space**, with `d ∘ d = 0`. Present.
* Manifolds — **absent**, and Mathlib says so: its own TODO at `Basic.lean:34-38` reads
  *"same for manifolds (**not defined yet**)"* and asks for a Zulip design discussion.
* `grep -rn 'MDifferentiableForm\|DifferentialForm' Geometry/` → nothing.
* No Hodge star (`Hodge` occurs once in all of Mathlib, at `ModelTheory/Fraisse.lean:60`,
  citing the model theorist W. Hodges).
* Stokes exists only as the divergence theorem
  (`MeasureTheory/Integral/DivergenceTheorem.lean`).

**Construction:** a `C^r` `k`-form on `M` is a `ContMDiffSection`
(`Geometry/Manifold/VectorBundle/SmoothSection.lean:325`) of the bundle whose fibre at
`x` is `ContinuousAlternatingMap ℝ (TangentSpace I x) F (Fin k)`. The fibre type, the
bundle constructions (`VectorBundle/Hom.lean`,
`Topology/VectorBundle/Constructions.lean`) and the pointwise exterior derivative all
exist; the work is assembling the bundle and transporting `extDeriv` chart-wise.

**Size: ~300-600 lines.** The largest BUILD item in the inventory, and the one that
unblocks the most: it is the prerequisite for any statement about the contact volume
form or the hyperbolic volume form as objects rather than as degree counts.

Classified BUILD rather than UPSTREAM because an in-repo version unblocks the arc now
and the upstream route is gated on Mathlib's requested design discussion. Upstreaming
later is not foreclosed.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §B3, §H2.
