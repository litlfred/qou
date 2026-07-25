# α_EM B2 τ-identification — attack options (the last open input to `1/(8π)`)

**Date:** 2026-07-24 · **Axis:** α_EM per-loop measure (the single load-bearing wall) ·
**Tier:** research attack-plan (no new result; develops routes) · **Discipline:**
`1/(8π)` stays a phase-4 identification; the τ-functor is NOT constructed here; no
`TauRhoHodgeLift` instance is fabricated.

## The target (what is left)

Over #4151 + #4154 the B2 per-loop wall was stripped of every linear-algebra residue:

| premise ingredient | status |
|---|---|
| positivity / PSD | **unnecessary** (#4151) |
| reality + symmetry | **discharged Markov-side** — `bilinM_isSymm` + real `q₀` (#4154) |
| **τ-identification** `W = complexify(Markov Gram at q₀)` | **the SOLE remaining open input** |

The τ-identification asserts: the α_EM loop weight `W` on `H^{1,0}(Bring)` equals the
`complexify` of the canonical Markov channel weight (the seminormal Gram) at the
substrate `q₀`, transported by the archimedean fibre functor `τ`. Discharging it
legitimately instantiates `TauRhoHodgeLift` and lands `1/(8π)`.

## The keystone fact that shrinks the problem

`H^{1,0}(Bring) = std`, the **irreducible** 4-dim standard S₅-representation
(#2701, corpus). `std` is defined over `ℚ` (real / rational type ⇒ **absolutely
irreducible over ℝ**). By **Schur's lemma**, the space of S₅-**invariant symmetric
bilinear forms** on an absolutely-irreducible real representation is
**1-dimensional**. Both candidate forms on `std` are S₅-invariant and symmetric:

- the **Hodge metric** on `H^{1,0}(Bring)` — S₅ = Aut(Bring) acts by isometries on
  the period lattice;
- the **τ-image of the Markov Gram** — *if* it is S₅-equivariant on `std`.

So (modulo the equivariance premise) they are **proportional**:
`τ(Markov Gram) = c · Hodge Gram`, `c` a scalar. This converts "construct the whole
τ-functor and prove it carries ρ to Hodge conjugation" into **"prove τ-equivariance
on one irrep + fix one scalar `c`."** That is the leverage the attack plan is built
around.

## Attack options (priority order)

### B — Schur-uniqueness reduction  **[PRIMARY — highest leverage]**
Formalize: *invariant symmetric bilinear forms on an absolutely-irreducible
representation are unique up to a scalar* (Schur). Instantiate at `std`; conclude
`τ(Markov Gram) ∝ Hodge Gram`. **Open sub-pieces after B:** (i) the τ-image is
S₅-equivariant on `std` (should follow from the Bring-automorphism action commuting
with `τ` — the seminormal form's `bilinM_rep_invariant` is the Hecke-side
equivariance); (ii) the scalar `c` (fixed by the trace/`a₀` normalization, or by one
matrix entry — Option C). **Lean core:** Schur uniqueness of invariant forms;
Mathlib has `Module.End` Schur (`LinearMap.isUnit_or_eq_zero` on irreducibles) —
adapt to the symmetric-bilinear-form space. **Honest caveat:** a *reduction*, not an
automatic closure; but a large shrink. This is NOT fabrication — it derives
proportionality from irreducibility, it does not assume the identification.

### C — Explicit numerical pin / falsification  **[SUPPORT for B]**
Compute the **Hodge Gram** of `H^{1,0}(Bring)` from the Braden–Northover period
matrix `τ₀·C` (uploaded, registered), and the **Markov Gram** on the `std` block at
`q₀` (Hoefsmit seminormal / `WenzlSchurElement`). Verify proportionality numerically
and **extract `c`**. Double duty: confirms B's proportionality *and* falsifies the
equivariance premise if they are not proportional. Concrete probe (Hecke wheel +
period matrix); anti-laundering: report the ratio, do not tune it.

### A — Wedderburn-block identification  **[SUPPORT / feeds C]**
Pin the exact Wedderburn block of `H_n(q)` carrying `std` (partition `(4,1)`, the
relevant `n`), and compute its Markov weight matrix explicitly (Hoefsmit branching).
Supplies the concrete `Markov Gram` object that B references abstractly and C
evaluates.

### E — `MarkovTrace` general-`n` instance  **[MECHANICAL — unblocks the reduction]**
`TauFunctorReduction` threads `[MarkovTrace]` with a general-`n` instance gap; land
the Ocneanu-cyclicity bricks (#4126 / #4110) to close it. Does not close the
identification, but removes a threaded hypothesis blocking the reduction's F-laws.

### D — Full τ-functor construction  **[FALLBACK — multi-session]**
Construct the archimedean fibre functor on the relevant subcategory and prove it
carries the Markov weight to the Hodge metric. The complete categorical route; needed
only if B's equivariance premise cannot be established more cheaply. Large; last
resort.

## Recommended sequencing

**B → C → A → E → D.** B is the structural near-closure (potential proportionality
theorem); C pins/falsifies the scale immediately with data already in the corpus
(Braden–Northover period + Hoefsmit); A supplies the concrete block; E is a
mechanical unblock runnable in parallel; D is the fallback if equivariance resists.

## Scope discipline (STRICT)

No τ-functor is constructed here and no `TauRhoHodgeLift` instance is registered.
Option B derives proportionality from *irreducibility* (Schur) — it does not assume
the identification (that would be laundering). The scalar `c` and the equivariance
premise are stated as the open sub-pieces, not papered over. `1/(8π)` stays phase-4.

## Cross-references

- Wall-weakening (real+symmetric, PSD unnecessary): PR #4151 (`LoopWeightRealSymmReduction.lean`)
- Markov-side discharge (symmetric form ⇒ premise): PR #4154 (`MarkovGramRealSymm.lean`), `SpechtIrreducible.bilinM_isSymm`
- `H^{1,0}(Bring) = std` irreducible: [`2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md`](2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md) (#2701)
- Braden–Northover period matrix `τ₀·C`: [`[braden-northover-2012]`], `BringEllipticFactor.lean`
- Schur-element / Wenzl infra: `QOU/MathlibExt/WenzlSchurElement.lean`
- B2 interface + reductions: `QOU/Archimedean/{TauRhoHodgeLiftInterface,HodgeGramLift,LiftFromReality,TauFunctorReduction}.lean`
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)

## Update 2026-07-25 — sub-piece (ii) formalized as a conditional reduction

`TauS5EquivarianceReduction.lean` (sorry-free, lean-direct exit 0) closes the
*logical* role of sub-piece (ii). Two results:

- `invariantForm_pullback` — transport of an invariant form along an
  intertwiner: if `P` intertwines the Hecke action `ρH` and the S₅ action `ρS`
  (`ρH s · P = P · ρS s`) and `M` is `ρH`-invariant, then `Pᵀ M P` is
  `ρS`-invariant. This is the precise linear-algebra content of "an
  S₅-equivariant τ carries the Markov Gram to an S₅-invariant form."
- `tauImage_proportional_hodge` — assembling (i)+(ii)+Schur: given the τ-map on
  `std` as a `TauStdIntertwiner`, plus S₅-irreducibility (⇒ scalar commutant via
  `MatrixSchurCommutant`, PR #4182) and a unit Hodge form, the τ-image of the
  Markov Gram is `= c • G_Hodge`.

**The wall is now assembled modulo two named, un-fabricated inputs:**

| ingredient | status |
|---|---|
| Schur proportionality from commutant-scalar | PROVED (#4160) |
| (i) commutant scalar from irreducibility | PROVED (#4182, `MatrixSchurCommutant`) |
| symmetric / real type of the Markov Gram | PROVED (#4154, `MarkovGramRealSymm`) |
| (ii) equivariance ⇒ invariant-form transport ⇒ proportionality | PROVED conditional (this file) |
| sign of `c` (positive) | PROVED (Hodge+Markov both pos-def, #4182 item 2) |
| **τ is the `(4,1)` intertwiner** (the categorical claim) | **OPEN** — existence of *some* intertwiner is standard (Tits deformation); that the archimedean τ *is* it is the open input. No instance registered. |
| explicit `|c|` (magnitude) | **OPEN** — needs the Riera–Rodríguez symplectic period matrix `Z` (absent from corpus) |

No `TauStdIntertwiner` / `TauRhoHodgeLift` instance for the actual τ is
registered; `1/(8π)` stays a phase-4 identification; nothing is wired.
