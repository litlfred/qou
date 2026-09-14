---
# qou-pzsi
title: 'GAP: no map from a braid word to a curve on the Bring surface — the embedding-energy selection rule cannot be built without it'
status: todo
type: task
created_at: 2026-09-14T16:50:05Z
updated_at: 2026-09-14T16:50:05Z
---



## The gap, precisely

Opened 2026-09-14 from the owner's objection on `qou-99qc`: *"The selection rule
shouldn't be minimum crossing... It may be higher energy than a non-minimal
crossing. A sibling has worked on connecting hecke energy to O'Hara energy via
brings embedding... You're minimizing not just the hecke energy but how the knot
is embedded into brings surface."*

**Why it is needed.** The gluon-dressing selection on `qou-99qc` is blocked on
its cost function. Two proxies have been measured and both fail, for one
structural reason:

- **crossing count** — `FrobeniusSelected`'s own instantiation. Ties σ₁ with
  σ₁⁻¹.
- **crossing energy** (`def:crossing-energy`) — breaks that tie (σ₁⁻¹ = −0.90092
  beats σ₁ = +1.10998) but ties all three 2-crossing candidates at `2q`.

Both are **sums over letters**, hence constant on the permutation orbit of a
letter multiset — while the closure is not. That is now a **scope-(b) structural
exclusion of the whole letter-sum class** (probe
`qbeta_embedding_energy_can_discriminate_probe.py`, 5/5, PR #7370): σ₁σ₀ and
σ₀σ₁ have the same multiset and the same writhe `+2` and close to **different
links** (traces apart by 6.78e-2 / 1.42e-2). So no functional of the multiset
alone can select here, for any `q` and any coefficients.

**And an isotopy-class energy is NOT barred** — all four 2-crossing candidates
are distinct links, so the O'Hara/Möbius **infimum** can take different values on
them. Green light for the route on discriminability grounds.

## What exists

- [`mobius_cross_energy_hopf_calibration.py`](computations/mobius_cross_energy_hopf_calibration.py)
  — a cross-energy integrator **calibrated against the proved** `E(Hopf) = 2π²`
  (Agol–Marques–Neves, arXiv:1205.0825), mpmath end to end.
- `mobius_cross_energy_borromean.py`, `mobius_borromean_topology_guard.py`.
- `QOU.MobiusEnergy` — categorical `E_cat` from the Frobenius–Hopf
  comultiplication and the q-Hodge star, with the encoded relation
  `E_cat = ¼·E_classical + const`.
- Bring machinery: period matrix, mapping-torus residue weights, zero modes.
- Beans `qou-zfs6` (Möbius invariance / FHW bound / minimiser as Lean gates) and
  `qou-dux3` (the Möbius-invariant exponent) are `completed`; `qou-6xt9`
  (ingest the knot-energy literature) is `in-progress`.

## What is missing — the gap itself

**Any map from a braid word to a curve in or on the Bring surface.** The
integrators consume hand-parametrised *named* embeddings (Hopf, Borromean);
nothing feeds them an arbitrary 9/10/11-letter Hecke word. Searched
`computations/` and `tools/` for embedding/curve/parametrisation code near
"bring", and for every consumer of
`mobius_energy|ohara_energy|E_mobius|mutualIntegrand|cross_energy`.
`embeddable_knot_operator.py` is **not** it — it is σ/π orbital-overlap
weighting with a per-system `w_perp`. **An absence on the surfaces searched, not
a proof of absence.**

## Why it is hard, not merely unbuilt

Möbius energy is a property of an **embedding** and is **not a knot invariant** —
it varies over the isotopy class, and the invariant is the **infimum** (FHW). So
"the energy of a word" needs either

1. the **minimiser** over the isotopy class (existence is the FHW theorem's
   content, and computing it is a variational problem), or
2. a **canonical embedding** — which is exactly what the Bring surface would be
   for, and is the substantive proposal.

That is the research content. It is not a wiring job.

## Caveat that must not be skipped

`QOU/MobiusEnergy.lean` carries **2 sorries**, and its own header records a
prior vacuity incident in which `classicalLimit` made `E_cat` **blind**
(`E_cat = 1 + const` for every knot) **with no `sorry` to flag it**. The
categorical↔classical leg therefore cannot bear weight unexamined — check it
before building on it.

## Next honest step

Not "build the bridge". First establish which of (1) or (2) above the Bring
surface is supposed to supply, and whether `E_cat`'s classical limit is sound
after the recorded vacuity incident. Until then the gluon dressing stays
unselected and the `qou-99qc` dashboard rows stay un-re-scored.

---

## CORRECTION (2026-09-14) — the headline claim of this bean is WRONG

This bean, and PR #7370 which opened it, assert that the corpus has **no map
from a braid word to a curve in or on the Bring surface**. The owner said
otherwise and was right. `computations/qbeta/qbeta_cusp_lattice_geodesic_probe.py`
carries exactly that map, on the author's own steering of 2026-07-27: *"we can
associate to a braid word a geodesic (flow) on the torus for the particle/vortex
path"*. It is filed under **geodesic**; I searched for *embed / curve /
parametrise* near *bring*, and for consumers of the Möbius integrators, and the
map was one word away from every query I ran. A detector-blindness instance in
my own corpus-grep, not in a tool.

What was genuinely missing was the **geodesic → O'Hara energy** step, and that is
now built (`qbeta_bring_ohara_bridge_probe.py`, 7/7, merged #7374).

## What the built bridge gives — a NEGATIVE, and it is structural

`(m, ℓ) = (exponent sum, strand count)`. Both are letter-sum-type: the exponent
sum is a sum over letters, the strand count does not depend on the word at all.
So all four two-crossing gluon dressings share one lattice class, one geodesic
and one energy. **The O'Hara energy is innocent; the cusp-torus embedding is the
lossy step**, and it provably forgets the knot — the class is computed before the
modulus is ever consulted, so no modulus can repair it.

## Modulus sensitivity — DERIVED from Neumann–Zagier, correcting my own number

The bridge computes at `ω = e^{iπ/3}`, the shape at the **complete** structure
`u = 0`; the framework evaluates at meridian log-holonomy `∼ ln q₀ ≠ 0`, which
is the concern `qbeta_cusp_shape_drift_robustness_probe` raises. I first answered
it by drifting `ω` by hand at the `O(u) = 10.4 %` scale and reported 3.9–16.3 %
energy shifts. **That was an assumption about the drift dressed as a measurement
of it.**

`qbeta_neumann_zagier_cusp_modulus_probe.py` (8/8) derives the deformation from
NZ's own gluing equations (65)–(66) for `4₁` by series-inverting `u(v)`:

    τ(u) = 2√−3 · (1 + u²/3 + O(u⁴))

with `τ₀ = c₁ = 2√−3` and `c₃/c₁ = 1/3` **exactly**, matching NZ eq. (68) at
that slot; NZ eq. (52)'s odd-only structure is **verified on the computed
series**, not imposed, which is what forces the leading correction to be `u²`.
Cross-check worth having: `2√−3 = −2 + 4ω` **exactly**, so the NZ
meridian–longitude lattice is the index-4 sublattice of the corpus's hexagonal
`ℤ⟨1, ω⟩` (`cusp-shape-bar-parity.md`) — two independent sources, one lattice,
an exact integer relation.

Consequence: the real drift is **second order**, so the `(2,3)` energy moves
**0.163 %** (`u = ln q₀`) or **0.637 %** (`u = 2 ln q₀`), against the 4.29 % my
hand-picked `O(u)` drift gave. The bridge's figures are **robust at the
sub-percent level**, and the concern is answered without needing the
normalisation binary resolved — both branches clear it.

## What stays OPEN

The `u = ln q₀` vs `u = 2 ln q₀` meridian normalisation is the same factor of two
as bean `qou-yh67`'s NZ-½ binary (`κ_shape = √3/2` vs `κ_pot = √3/4`, the
`Φ = 2𝔙` factor), which `qou-yh67` records **cannot be settled numerically**.
Both branches are computed and **neither is adopted** — choosing the one that
lands a target is selection against the target. The factor enters `τ` squared, so
the two drifts differ by exactly 4×.

The `qou-99qc` dashboard rows stay un-re-scored and the gluon dressing stays
unselected: this bridge does not select, and nothing here proposes that it
should.
