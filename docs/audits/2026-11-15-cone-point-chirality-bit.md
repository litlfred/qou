# Does the cone point u pick the weak vertex's L/R bit? (D-W1 = A)

Bean `qou-hlx7` (epic `qou-qs0e`). The owner chose D-W1 = A on 2026-11-15: test whether 6b's
polarization point u (#7825) selects which one-sided flavour flip is the weak vertex. The
candidates are W_L = q⁻¹J (L-only) and W_R = qJ (R-only) (`OneSidedWeakVertex.lean`, #7844).

Lean: `folio/quantum-observable-universe/lean/QOU/QuarkState/ConePointChiralityBit.lean`.
It is sorry-free, compiles lean-direct with exit 0, and uses standard axioms only.

## 0. Result

**Not equivariantly. Scope (b) under the stated requirement.** Any assignment from cone
points to vertex types that respects the cone's unit-quaternion gauge gives the **same**
vertex type at u and at −u. By 6b, u ↦ −u is the photon swap Γ ↦ −Γ. So the vertex type
cannot follow which polarization line Γ_u calls left-handed.

The only operation that swaps W_L ↔ W_R is the bar involution q ↦ q⁻¹, and it is not
K-linear. **The L/R bit is the orientation of q** (equivalently, which crossing carries the
weight q, `two_smul_oneSidedL_eq_skein`). **It is not the cone point.**

## 1. The requirement, stated so it can be checked

"u selects the bit" is modelled as:
* a letter field ℓ on cone points;
* a type τ(u) ∈ {L, R};
* the requirement that both are **equivariant**: unit quaternions g act on u by conjugation
  (6b `hopf_leftMul`) and on the algebra by **any** K-algebra maps ρ g, the trivial one
  included.

Without equivariance, u selects nothing. A non-equivariant τ is a gauge fixing, which is a
choice, and #7825 already established that u is a global gauge.

## 2. Proved

| theorem | statement |
|---|---|
| `map_oneSidedL`, `map_oneSidedR` | a K-algebra map sends the L-only (R-only) flip of s to the L-only (R-only) flip of φ(s): algebra maps fix q, and q labels the lines |
| `map_isLetter` | the image of a letter is a letter at the same q |
| `oneSidedL_ne_oneSidedR` | W_L ≠ W_R in any nontrivial algebra unless q² = 1 |
| `type_invariant` | an equivariant τ is constant along every gauge orbit (any action, any ρ) |
| `conjBy_unitJ_unitI` | conjugation by the unit j sends u = i to −i |
| **`cone_point_cannot_pick_bit`** | for every equivariant (ℓ, τ, ρ): τ(−i) = τ(i) |
| `const_assignment_equivariant` | non-vacuity: a constant τ (a fixed convention) satisfies all hypotheses |

Generic `[Field K]`, `[Ring A] [Algebra K A]`, with the cone over generic `[CommRing R]`. No ℝ.

## 3. What it means

* **The equivariant assignments are exactly the conventions.** A constant type satisfies the
  hypotheses (`const_assignment_equivariant`), and the theorem shows nothing else can follow
  u to its antipode. So "the weak vertex is L-only" is either a convention or comes from an
  extra datum on which the gauge acts trivially.
* **The bit lives on the q side.** The three established results line up:
  - bar swaps W_L ↔ W_R (`oneSidedL_flip`);
  - the skein weighting picks W_L or W_R (`two_smul_oneSidedL_eq_skein`);
  - K-linear symmetries cannot swap them (this file).

  So the L/R bit of the one-sided vertex is the same datum as **q vs q⁻¹**, i.e. the
  orientation in which the Hecke parameter is read.
* **Physical reading (the agent's, not an identification):** parity violation would then be
  tied to the direction of the q-deformation, not to a polarization frame. Not written
  into content.

## 4. Scope of the negative

* **(b)**, invariant: algebra homomorphisms preserve eigenvalues, hence the L/R type
  (`map_oneSidedL`), and the gauge orbit of u contains −u. This holds for every equivariant
  assignment, with any ρ.
* **(a)** for anything outside the requirement:
  - a gauge-fixed (non-equivariant) assignment can pick either side, by choice;
  - an assignment through a datum the gauge does not act on (e.g. a fixed orientation of q)
    is not excluded, and §3 says that is where the bit is.
* Modelling step, stated: the gauge acts on the algebra by **K-linear** maps. A gauge that
  also acted by q ↦ q⁻¹ would be a different structure. The corpus has none, and it would
  carry the bit by construction.

## 5. Verification

* Compiled lean-direct, each exit 0: `BringCone`, `BringConeIcosahedral`,
  `ChiralityPolarizationHopf`, and the #7844 chain (`OneSidedWeakVertex` and its deps).
* `lean -DautoImplicit=false -s 65536 ConePointChiralityBit.lean`: exit 0, no warnings,
  0 `sorry`.
* `#print axioms` on `cone_point_cannot_pick_bit`, `type_invariant`, `map_oneSidedL`,
  `oneSidedL_ne_oneSidedR`: `[propext, Classical.choice, Quot.sound]`. On
  `conjBy_unitJ_unitI`: `[propext, Quot.sound]`.

## 6. Owner decision D-W3: where does the L/R bit come from, then?

* **(A) Record it as a convention.**
  - *Means:* "the weak vertex is the L-only flip" is fixed by declaring that the weight q sits
    on L₊. This is the same convention that labels the BW +q root as L (D-H1 = A).
  - *Costs:* nothing beyond a note.
  - *Risks:* parity violation becomes conventional inside this model, rather than derived.
  - *Commits to:* V−A not being a derived feature of the letter algebra.
* **(B) Look for a datum that fixes the orientation of q.**
  - *Means:* a bean asking whether anything in the corpus breaks q ↔ q⁻¹ (e.g. the substrate
    pin q₀ > 1, which is archimedean).
  - *Costs:* research, outcome unknown.
  - *Risks:* q₀ > 1 is a comparison-boundary fact. Deriving chirality from it would put an
    archimedean input under a structural claim.
  - *Commits to:* searching outside the letter and cone algebra.
* **(C) Stop here.** `qou-hlx7` is recorded with the bit located (q orientation), not
  derived.

**Default if nothing is said: (C).** **Recommendation (judgement): (C) now, and (B) only if
a structural q-orientation turns up.** (A) would be honest but adds nothing the corpus does
not already say through D-H1.
