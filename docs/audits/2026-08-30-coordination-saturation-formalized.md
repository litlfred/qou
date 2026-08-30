# Nuclear saturation forces bounded coordination — formalized (extensive-term structural half)

**Date:** 2026-08-30
**Tier:** formalize-first partial (hardens an existing qualitative corpus argument; no new physics claim)
**Arc:** bk-crossing mass-binding, items 1 + 3a · **Bean:** `qou-brng` (the amplitude assignment stays open)
**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/CoordinationSaturation.lean`

## Why this, and what it is NOT

Investigating the extensive-binding term (the arc's one real open problem), the
**scaling** half turned out to be already understood qualitatively in the corpus —
`bk-coordination-multiplicity.md` ("for n_α ≥ 5 the complete graph over-counts …
saturates to a geometric close-packing count") and `q-clt-jsj-mass-scaling.md`
("B/𝔪 plateaus under nuclear saturation"). Per the corpus-grep discipline this is
**not re-derived as novel**. What was missing was a **machine-checked** statement,
which this adds.

It is explicitly **not** a derivation of the extensive term's coefficient or
mechanism. Those remain open/suspect (see below).

## What is now proved (Lean, sorry-free)

Writing `B(A) = ε·M(A)` (`ε > 0` per-bond energy, `M` = total bond count):

- `complete_graph_no_saturation` — for the complete graph `M = C(A,2)` (the
  `z = A−1` law of `CoordinationBinding.lean`), `B(A)/A = ε·(A−1)/2` is
  **unbounded**: `∀ B, ∃ A, B/A > B`. No finite plateau exists — the complete
  graph predicts per-nucleon binding → ∞.
- `bounded_degree_saturates` — for bounded-degree-`k` coordination (`k·A/2`
  bonds), `B(A)/A = ε·k/2`, **constant in A**: a finite plateau. Genuine
  cancellation (`perNucleonBounded_eq`), not a definitional constant.

Ground ring `ℝ` (archimedean; the claim is unboundedness). No fit — `ε`, `k` are
free positive parameters.

## What it establishes for the arc

- **Item 1 (`z = A−1`) is refuted structurally, not just numerically.** The
  complete-graph coordination cannot saturate; saturation is observed; therefore
  the complete graph is excluded for heavy `A`. This upgrades the "⁴He gives M≈2
  not 3" numerical refutation to a structural one.
- **Item 3a (close-packing / fcc) is the forced regime.** Only a bounded
  coordination number gives the observed finite `B/A` plateau. Items 1 and 3a are
  two faces of one saturation principle.

## What stays open (do not read as closed)

- **The coefficient.** `ε` (equivalently the per-bond `b_αα`, `a_D`) is not
  derived here; the exact-ℏ_q² saturation value is **suspect numerology** and the
  volume-defect route to it is refuted (`qou-brng`).
- **The amplitude assignment (the real mechanism).** *Why* the binding multiplier
  is the mutual (coordination) linking count while the mass multiplier is the
  self-linking weight `lw` — the linking-vs-self-energy distinction — is **not**
  proved. It needs new substrate structure and is the surviving open route
  (`qou-brng`). This file deliberately stops before it rather than fitting it.

## Convergent frontier (sibling landings, 2026-08-29/30)

This lemma is one of several formalize-first prunes converging on the extensive
term. Read together:

- **`ChainBondOrderDependence.orderIndependent_iff`** — the linear-chain bond sum
  is arrangement-invariant **iff** `L_pp = L_pn = L_nn`; a nucleus has no
  arrangement, so bond-type-dependent scalars are a non-physical DOF (scope-(b)
  excluded at `q ≠ 1`, bean `qou-m07y`). **My uniform-ε assumption is exactly that
  order-independent regime** — so the saturation dichotomy here holds precisely in
  the physical case, and the linear chain is excluded there while the complete
  graph is excluded here.
- **`BodyOrderRecurrenceDepth.three_le_depth`** — body-order recurrence depth ≥ 3
  is forced (0- and 1-body vanish, deuteron binds), and 3 terms cannot test it.
- **`MayerThreeBodySign`** — the connected 3-body Ursell cumulant sign is
  threshold-forced and wrong against AME (`−2.744` vs `+1.426`), independent of
  the bond set (bean `qou-rraz`).

So **both** simple coordination ansätze (complete graph, linear chain) are now
excluded, depth ≥ 3 is forced, and the Mayer 3-body route is wrong-signed. The
admissible structure of the extensive term is being pruned from several directions
simultaneously; this file adds the saturation constraint.

## Verdict

The extensive term's **scaling** (bounded coordination ⇒ saturation; complete
graph ⇒ collapse) is now machine-checked. Its **coefficient** and **mechanism**
remain open — the honest boundary of what a formalize-first pass can close without
a fit.
