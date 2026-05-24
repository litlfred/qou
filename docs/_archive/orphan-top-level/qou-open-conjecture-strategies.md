# QOU open-conjecture proof-strategy sketches

This document records *proof strategies* — not actual proofs — for
the genuinely-open mathematical conjectures embedded in the QOU
formalisation as Lean typeclasses. Each entry summarises the
known mathematical approaches, their dependencies, and what
Lean infrastructure would be needed.

These are research-level open problems. None can be discharged in
a single session; each represents months to years of formalisation
work, contingent on substantial prior advances in Mathlib.

## Index

1. [`HasYangMillsMassGap`](#1-hasyangmillsmassgap) — Clay Millennium
2. [`PvsNPQou`](#2-pvsnpqou) — Clay Millennium
3. [`QGeometricLanglandsConjecture`](#3-qgeometriclanglandsconjecture)
4. [`SingleVolumeIrrational`](#4-singlevolumeirrational) — Kontsevich-Zagier
5. [`BorelZagierQOU`](#5-borelzagierqou)
6. [`HyperbolicVolumeIndependence`](#6-hyperbolicvolumeindependence) — Nesterenko
7. [`TowerNoncollapseImpliesIndependence`](#7-towernoncollapseimpliesindependence)
8. [`LeviDegeneracyConjecture`](#8-levidegeneracyconjecture)
9. [`FibreFunctorRigidity`](#9-fibrefunctorrigidity)
10. q-BSD predicates (Clay Millennium, classical case open)

---

## 1. `HasYangMillsMassGap`

**Claim.** For every `q > 1` and categorical transfer matrix `tm`,
there exists a `YangMillsMassGap` instance — i.e., a positive
spectral gap `Δ > 0` separating the vacuum from the first excited
state of the q-deformed Yang-Mills Hamiltonian.

**Status.** Clay Millennium Problem (2000). Open since the 1960s.

**Proof strategies (literature).**

(a) **Constructive QFT (Glimm-Jaffe approach):** build the Yang-
    Mills measure on ℝ⁴ via lattice approximation + continuum
    limit + reflection positivity. The hard step is showing the
    cluster expansion converges and the IR limit preserves the
    mass gap. Hardest known sub-problem: Wilson area-law for
    non-abelian Wilson loops in the continuum. **Mathlib gap:**
    no constructive QFT framework; would need
    `Probability.GaussianMeasure` extended to gauge fields.

(b) **Lattice mass-gap:** Reisz-Wolff theorem gives a mass gap
    in finite-volume lattice with periodic BCs. Take inverse-
    coupling continuum limit. Bridge to continuum via Osterwalder-
    Schrader axioms. **Mathlib gap:** OS axioms not formalised.

(c) **Categorical / TQFT approach:** specific to QOU framework.
    The categorical transfer matrix `tm : CategoricalTransferMatrix`
    encodes a Frobenius-Hopf object's spectral data. The mass gap
    becomes a categorical irreducibility condition + Perron-
    Frobenius for the transfer-matrix functor. **Mathlib gap:**
    Perron-Frobenius for monoidal endofunctors not in Mathlib;
    requires `CategoryTheory.Monoidal.EndofunctorAlgebra` +
    spectral theory.

**QOU-specific routing.** The class field
`witness : YangMillsMassGap` already abstracts the existence
claim. To prove from a *specific* construction one would need to
build a `YangMillsMassGap` term — i.e., supply `q`, `transferMatrix`,
`gap`, and the four invariants required by the structure.

**Estimated formalisation effort.** 2–5 person-years even after
the surrounding infrastructure exists.

---

## 2. `PvsNPQou`

**Claim.** P ≠ NP (in the QOU framework: surreal-rate-calculus
witnesses a separation between the surreal infinitesimal class
of polynomial-time Reeb dynamics and exponential-time Hausdorff
walks).

**Status.** Clay Millennium Problem (2000). Open since 1971
(Cook-Levin).

**Proof strategies.** All known approaches (relativisation, natural
proofs, algebrisation, geometric complexity theory) face known
*barriers*. The QOU framework recasts P ≠ NP as a surreal-Ow
valuation gap (Ow(reachableSet) vs Ow(NPwitness)). A formal proof
would require:

(a) Formalised circuit-complexity model with surreal-valuation
    metrics on circuit families.
(b) Aaronson-Wigderson-style algebrization barrier formalised
    enough to *avoid* it (no theorem violating it has yet been
    found; expected NOT possible).
(c) Geometric complexity theory (Mulmuley-Sohoni): obstructions
    via representation-theoretic invariants. **Mathlib gap:**
    full GCT machinery (orbit closures, plethysms) not in
    Mathlib.

**QOU-specific routing.** The class is `class PvsNPQou : Prop`
(no fields). An instance is the conjecture itself. There is no
"trivial" sub-case to discharge: P ≠ NP genuinely is the entire
content.

**Estimated formalisation effort.** Open-ended; not foreseeable
in current state of mathematics.

---

## 3. `QGeometricLanglandsConjecture`

**Claim.** Every Hecke eigensheaf on `Bun_G(q)` is recovered as
a tensor functor's image of an associated `^L G(q)`-local system,
with the eigenvalue identification `langlandsFunctor es =
es.eigenvalue`.

**Status.** Open in characteristic 0 in full generality. Geometric
case (over `ℂ`) for `GL_n` was claimed by Gaitsgory-Raskin (2024).
The q-deformation is open even after that.

**Proof strategies.**

(a) **Beilinson-Drinfeld geometric Langlands:** Hecke functors +
    derived equivalence between `D-mod(Bun_G)` and
    `IndCoh(LocSys_{^L G})`. **Mathlib gap:** no `D-mod` or
    `IndCoh` formalisations.

(b) **Quantum Geometric Langlands (Gaitsgory's formulation):**
    `q ≠ 1` deformation involves the Lurie quantum framework.
    **Mathlib gap:** quantum-group formalisation partial; quantum
    Frobenius not yet formalised.

(c) **Frenkel-Hartl-Mirković-Vilonen geometric Satake:** local
    case via affine Grassmannians. The q-deformed version is the
    main missing piece. **Mathlib gap:** affine Grassmannian
    `Gr_G` not in Mathlib.

**QOU-specific routing.** The class has fields
`langlandsFunctor`, `recovers_eigenvalue`, `oper_injective`. A
specific instance for `GL_2(q)` could be supplied if Mathlib had
the affine Grassmannian.

---

## 4. `SingleVolumeIrrational`

**Claim.** `Vol(4₁), Vol(5₂), Vol(6₃) ∉ ℚ` (hyperbolic volumes
of specific knots are irrational).

**Status.** Open. Special case of Kontsevich-Zagier irrationality
conjecture for periods.

**Proof strategies.**

(a) **Nesterenko-style transcendence theorems:** linear
    independence of `1, π, ζ(3), …` extended to dilogarithms at
    algebraic arguments. The Bloch-Wigner dilogarithm `D(z) =
    Im(Li₂(z)) + arg(1-z) log|z|` evaluated at the cusp shape of
    a hyperbolic 3-manifold gives the volume. **Mathlib gap:**
    Nesterenko's algebraic-independence machinery not in Mathlib;
    only basic `Irrational` and a few specific irrationalities
    are formalised.

(b) **Modular-form approach:** `Vol(4₁) = 3 · Cl₂(π/3)` where
    `Cl₂` is Clausen's function. Irrationality reduces to that
    of `Cl₂(π/3)`. Open.

**QOU-specific routing.** Each field of the class is an
`Irrational` claim. Supplying any one instance would discharge
that field. None are known irrational.

---

## 5. `BorelZagierQOU`

**Claim.** `1, Vol(4₁), Vol(5₂), Vol(6₃)` are linearly independent
over ℚ.

**Status.** Open. Stronger than `SingleVolumeIrrational`. The
Borel-Zagier framework relates volumes to motivic K-theory of
number fields; linear independence corresponds to algebraic
independence of motivic generators.

**Proof strategies.** Same family as #4 plus motivic refinements.
Beilinson conjectures + Bloch-Kato relate to special values of
L-functions; ζ-values irrationality (Apéry, Rivoal, Zudilin) is
the sub-area where most progress has been made, but extending to
hyperbolic-volume L-values is open.

**QOU-specific routing.** The field `linear_independent` quantifies
over rational coefficient functions; a counter-instance would
witness a non-trivial relation. None known.

---

## 6. `HyperbolicVolumeIndependence`

**Claim.** No non-trivial monomial relation holds among
`Vol(K₁), Vol(K₂), …, Vol(K_m)` over `ℚ` (Nesterenko-style
algebraic independence).

**Status.** Open. Implies all hyperbolic volumes are
algebraically independent — much stronger than mere linear
independence.

**Proof strategies.** Nesterenko's transcendence theorem (1996)
gives algebraic independence of `π, e^π, Γ(1/4)`. Extension to
hyperbolic volumes is open. The conjectural framework is
Grothendieck's period conjecture (algebraic independence of
periods controlled by motivic Galois group).

**QOU-specific routing.** The `no_relation` field is a universal
claim. Even discharging single specific cases would be a major
result.

---

## 7. `TowerNoncollapseImpliesIndependence`

**Claim.** Yekutieli's lifting condition for non-abelian
multiplicative integration implies algebraic independence of
hyperbolic volumes (a bridge from #6 to a structural condition).

**Status.** Open. Internal to QOU manuscript.

**Proof strategies.** The Yekutieli-2010 framework provides a
"tower" structure on non-abelian gerbes; non-collapse of the
tower is a topological / categorical condition. The bridge to
algebraic independence requires a Nesterenko-Yekutieli analogue
of the dilog-period theorem.

**QOU-specific routing.** The class takes a
`YekutieliLiftingCondition` as instance hypothesis; supplying
that witness is the conjectural input. The bridge theorem
(non-collapse → independence) is the QOU-internal claim.

---

## 8. `LeviDegeneracyConjecture`

**Claim.** Bring's surface CR-degeneracy is exactly Levi-flat
in the appropriate sense.

**Status.** Open. CR-geometry conjecture, paper-internal.

**Proof strategies.** Levi-flatness of a CR manifold is a partial
differential equation on the Levi form. Bring's surface has
explicit equations; the Levi form should be computable. The
"degeneracy" claim is that this Levi form vanishes on a positive-
codimension subset.

**Mathlib gap:** CR-manifold infrastructure partial in Mathlib;
Levi form formalisation incomplete.

---

## 9. `FibreFunctorRigidity`

**Claim.** Tannakian rigidity in the QOU framework: the fibre
functor `τ` is determined uniquely (up to natural isomorphism)
by the underlying tensor structure of `(C, A)`.

**Status.** Open in the q-deformed setting; classical case is
Saavedra's theorem (1972). Paper-internal.

**Proof strategies.** Saavedra-Rivano: classical Tannakian
duality gives uniqueness up to canonical iso. The q-deformation
involves quantum-group automorphisms and is more subtle.

**Mathlib gap:** Tannakian formalism (`CategoryTheory.Tannaka`)
exists in Mathlib in basic form; quantum extension absent.

---

## 10. q-BSD predicates

**Claim** (weak form). For the q-Birch-Swinnerton-Dyer L-function
of the Descartes elliptic curve `E_q`, `L(E_q, 1) ≠ 0` implies
the rank `r_q = 0`.

**Status.** Open. Even classical BSD is open (Clay Millennium).
Proven for `r ≤ 1` (Coates-Wiles, Gross-Zagier-Kolyvagin); the
general case is open.

**Proof strategies.**

(a) **Iwasawa main conjecture (Skinner-Urban):** the Iwasawa
    main conjecture for `GL_2` over ℚ implies BSD for analytic-
    rank-zero curves. **Mathlib gap:** Iwasawa theory not
    formalised.

(b) **Heegner points (Gross-Zagier):** for analytic rank 1.
    **Mathlib gap:** modular-form L-functions formalisation
    partial.

**QOU-specific routing.** The q-BSD is parametric over `q`; the
classical case `q = 1` is open. The QOU framework conjectures the
q-deformation is "easier" because the elliptic curve `E_q` has
extra structure (q-shifted points), but no direct proof is known.

---

## Summary table

| Conjecture | Status | Field of math | Estimated formalisation effort |
|---|---|---|---|
| YangMills mass gap | Clay Millennium | constructive QFT / TQFT | 2-5 person-years |
| P vs NP | Clay Millennium | complexity theory | open-ended |
| q-BSD | Clay Millennium (extends) | arithmetic geometry | 1-3 person-years |
| q-Geometric Langlands | Open (geom. case 2024) | algebraic geometry | 2-5 person-years |
| Single Vol Irrational | Open (KZ) | transcendence theory | 1-2 person-years |
| Borel-Zagier QOU | Open | motivic K-theory | 1-2 person-years |
| Hyp Vol Independence | Open (Nesterenko) | transcendence theory | 1-2 person-years |
| Tower Noncollapse | Open (paper) | non-abelian integration | unknown |
| Levi Degeneracy | Open (paper) | CR geometry | 6 months - 1 year |
| Fibre Functor Rigidity | Open (q-case) | Tannakian | 6 months - 1 year |

## What can be done now

For each conjecture above, the QOU formalisation provides:

1. **Typeclass surface** — the conjecture is a `class C` field-set
   making the dependency explicit.
2. **`Fact`-based discharge path** — when an external proof
   (e.g. via numerical witness, accepted reference, or restricted
   sub-case) is available, an `instance` lights up the typeclass.
3. **Conditional consequences** — downstream theorems take the
   class as a hypothesis and prove conditional results
   (`P → Q`-style, with `P` the open conjecture).

This makes the conjectural surface visible at every use site
without risking spurious "discharges" via ill-founded instances.
