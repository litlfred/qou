# The curved `d_q` and the Floer cluster — what is method, what is analogy

**Date:** 2026-08-24 · **Bean:** `qou-fngs` (LES/spectral arc) · **Uploads:**
`aa17903e09f` (Smith 1006.1099v3, Pascaleff 1109.3255v2, Chanda 2301.08311v4,
McLean ICM-2022 ch. 5483)

Four symplectic-geometry papers arrived with the question *"not sure if
actually useful or just a good connection to make."* This note is the answer,
and it is not uniform across the four. One of them is method the arc can use
today, two contribute a single sharp idea each, and the specific geometry that
prompted the question — the binodal cubic, the twisting sheaf `O(1)` — is a
**false cognate** that would do damage if imported literally.

## The short answer

The cluster is **method, not content**. None of it is about `q`-deformed
Frobenius–Hopf objects, Gröbner filtrations, or the QOU substrate, and no
content block should claim otherwise. What it does is supply the standing
*name* for the obstruction the arc isolated this week, and the standard cure
for it.

That was worth having. Acting on it produced one theorem the same day —
`QOU.DqTwist.dq_sq_eq_curvature` — which is stated below and is the concrete
return on reading these papers.

## What the arc had isolated

`QOU/QuantumObservableUniverse/DqTwist.lean` factors the `q`-deformed
derivative as a twist of the classical one,

    d_q = T_q ≫ d,    T_q = q⁻¹ • 𝟙 + (1 − q⁻¹) • π_V

and shows the failure of `d_q ≫ d_q = 0` is exactly the failure of `T_q` to
commute with `d`. `QOU/Mathlib/PagedSpectralSequence.lean` requires
`d ∘ d = 0`, so `d_q` is **not** a valid differential for it: `ker ⧸ im` is not
defined when `im ⊄ ker`. An object with `d² ≠ 0` has no cohomology.

The corpus had no name for this situation. It has one everywhere else: such an
object is **curved**, and the established apparatus for taming one is a
Maurer–Cartan element (a *bounding cochain*, in Fukaya–Oh–Ohta–Ono's
terminology) — an element `b` whose deformation `d^b` is a genuine
differential. Curvature is the reason Floer theory needs that apparatus at all,
which is why it is these papers that carry it.

## The theorem this produced

Naming the situation suggested computing the curvature instead of merely giving
conditions for it to vanish. Writing `κ = d ≫ π_V − π_V ≫ d` for the projector
commutator, and assuming only `d² = 0`:

> **`dq_sq_eq_curvature`** — `d_q ≫ d_q = (1 − q⁻¹) • (T_q ≫ κ ≫ d)`.

Three consequences, and the third is the one that matters:

1. `q = 1` kills it through the **scalar**, recovering `dq_classical` from the
   formula rather than from a commutation hypothesis.
2. `κ = 0` kills it for **every** `q` (`dq_sq_eq_zero_of_projComm`). The
   deformation parameter was never the obstruction; the vertical projector was.
   `twist_comm_iff` confirms the earlier commutation hypothesis was exactly
   `(1 − q⁻¹) • κ = 0`.
3. **The curvature is first order in `(1 − q⁻¹)`.** `d_q` has a degree-zero
   leading term and its failure to square to zero lives entirely in degree
   ≥ 1 — precisely the condition under which filtering makes the associated
   graded a genuine complex and pushes the curvature into a higher
   differential.

Point 3 is the bridge the arc was missing. "Filter so the curvature sits in
higher filtration degree" was a general prescription; now there is a specific
filtration — powers of `(1 − q⁻¹)` — with the curvature verifiably in degree
≥ 1. This is what makes the twist thread and the `S-GB-spectral-collapse`
thread one problem rather than two.

All declarations axiom-clean: `[propext, Classical.choice, Quot.sound]`.

## Paper by paper

### Smith, *Floer cohomology and pencils of quadrics* (1006.1099v3) — most useful

§3.6 **Formality** is the item. Formality says an `A_∞` algebra is
quasi-isomorphic to its cohomology — all higher products vanish — and the
standard proof technique is a **grading/purity argument**: a product that must
shift a grading, landing where the grading is wrong, is zero for degree
reasons.

That is, line for line, the argument in
`QOU/Mathlib/BarGradedCollapse.lean`: `collapses_of_parity_mismatch` proves a
differential vanishes because it runs purely-even → purely-odd under the bar
involution `q ↦ q⁻¹`. The corpus reached this technique independently and at
small scale; Smith §3.6 is the professional version, and §3.5 *Grading and
deformations* is the same technique in the presence of a deformation
parameter, which is the QOU situation exactly.

§3.3 *Twisting and generation* is where twisted complexes appear — the
category-level home for objects whose differential squares to zero only after
correction.

**Verdict:** read for technique. It is the closest thing in the cluster to a
worked template for what `BarGradedCollapse` leaves open.

### Pascaleff, *…mirror of the projective plane and a binodal cubic curve* (1109.3255v2)

This is the paper the question singled out, so the false cognate needs saying
first.

**"Twisting sheaf `O(1)`" is not the QOU twist.** Serre's twisting sheaf is a
line bundle; twisting by it, `F ↦ F ⊗ O(n)`, shifts a grading. `T_q` is a
deformation of the identity endomorphism by an idempotent. Same English word,
unrelated notions, and a content block that ran them together would be wrong
in a way that is hard to unpick later.

**What does connect, and it is not nothing.** Pascaleff's theorem is that a
ℤ-indexed family of Lagrangians — mirror to the powers `O(n)` — has Floer
cohomology assembling into an algebra isomorphic to the **homogeneous
coordinate ring** `⊕_n H⁰(O(n))`. That is a ℤ-graded ring whose grading *is*
the twist power. The QOU ground ring is `R_q = ℤ[q, q⁻¹] = ℤ[ℤ]`, the group
ring on the same ℤ, and the bar involution `q ↦ q⁻¹` is its grading flip,
matching `O(n) ↔ O(−n)`.

So the paper is a **template for where a grading on the pages could come
from** — which is the input `BarGradedCollapse` explicitly does not supply for
the Gröbner filtration. That is a real hook, and it is a different hook from
the one the words suggested.

Two further rhymes, honestly labelled as rhymes:

- the Lagrangians are **sections** of a singular torus fibration and the
  product counts **horizontal sections** of a Lefschetz fibration — a
  base/fibre split with a horizontal part, like QOU's `π_H = 𝟙 − π_V`. Generic
  enough that it is a good connection rather than a usable one, absent an
  actual fibration on the QOU side;
- the **distinguished basis indexed by fractional integral points** of a
  singular affine structure is a combinatorial basis for a graded algebra with
  corrections at the singular points — suggestive next to a standard-monomial
  / Gröbner basis, but only suggestive.

**Verdict:** a good connection to make, and one genuine hook (the ℤ-grading
template). Not method the arc can pick up today. The specific geometry —
binodal cubic anticanonical divisor, focus-focus singularities, tropical
counts — has no QOU counterpart and should not be imported.

### Chanda, *Floer cohomology and higher mutations* (2301.08311v4)

One sharp idea: Floer cohomology is invariant under local mutation **up to a
change of local systems**. The object is not invariant; it is invariant *after
twisting*. That is structurally what `dq_eq_twist_comp` says — the classical
differential is recovered only after `T_q` is accounted for — and it suggests
reading `T_q` as a wall-crossing transformation.

Suggestive only: there is no wall in the QOU setup as formalised, and the
paper's technical core (SFT compactness, moduli of broken maps) is not
importable.

**Verdict:** one idea, worth the citation, not the machinery.

### McLean, *Floer cohomology, singularities, and birational geometry* (ICM 2022)

One sharp idea, and it validates work already done. McLean proves part of the
cohomological McKay correspondence by **computing one Floer cohomology group in
two different ways** — an invariant evaluated wherever it is accessible.

That is exactly the use of `QOU/Mathlib/EulerCharacteristic.lean`'s
`eulerChar_bump_eq`: the alternating sum is page-independent, so it may be
computed on whichever page is reachable, while an individual rank may not
(`finrank_bump_eq_iff`). The minimal-discrepancy result — a numerical invariant
of a singularity extracted by dynamical means — is the same shape as extracting
`Δ_λ` from an index.

**Verdict:** confirms the method already in the corpus. Supplies no new
machinery, and is the right citation when the index argument needs one.

## What not to do

The corpus has a standing failure mode — axioms and classes that assert a
result rather than prove it, discharged by trivial witnesses (see
`SpectralSequence.collapse_is_definitional`). Importing Fukaya-categorical
language without a symplectic model would be the same failure in new
vocabulary: mirror symmetry asserted, nothing proved.

So: **no content block claiming a mirror-symmetry statement about the QOU
substrate.** These are cited where a technique is actually used — which today
means Smith §3.5–3.6 next to `BarGradedCollapse`, and the curved-complex
framing next to `DqTwist`.

## Next, in the order the arc needs it

1. **Maurer–Cartan for `d_q`.** `dq_sq_eq_curvature` computes the curvature;
   the next step is a bounding-cochain statement — an explicit `b` for which
   the corrected differential squares to zero — rather than conditions under
   which the curvature happens to vanish.
2. **The `(1 − q⁻¹)`-adic filtration as a `PagedSS`.** Point 3 above says the
   curvature has filtration degree ≥ 1. Turning that into an actual
   `PagedSS` instance is what `S-GB-spectral-collapse` has always needed, and
   it is now a bounded amount of work rather than an open-ended one.
3. **A grading for the Gröbner filtration**, so
   `collapses_of_parity_mismatch` becomes applicable rather than merely true.
   Pascaleff's coordinate-ring grading is the template to try.
