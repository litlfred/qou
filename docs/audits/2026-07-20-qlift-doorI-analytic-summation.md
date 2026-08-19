# Door-i: analytic q-Borel–Laplace summation — C1 (slope ½) vs GGM eq 49 (slopes ±1) (2026-07-20)

**Question.** Routes A and D proved the two order-2 q-difference modules
C1 `[m+2]_q b_{m+2} = b_{m+1} + b_m` (slope ½ at ∞) and GGM eq 49
`y_{m+1} − (2−q^m) y_m + y_{m−1} = 0` (slopes {−1,+1} at ∞) inequivalent
under **formal / diagonal** operations: as RSZ q-difference modules over
`C((x))` / `C({x})` (Route A: Newton-polygon + fuchsian + determinant
invariants), and under the **formal** (coefficient-level) q-Borel/q-Laplace
transform, which is itself a diagonal gauge (Route D). Both left one door
open: the **analytic (transcendental)** q-Borel–Laplace summation of
Ramis–Sauloy–Zhang, *Local analytic classification of q-difference
equations* (Astérisque 355, `library/arxiv-0903.0853v3/0903.0853v3.pdf`), **ch. 5** — the
Borel-plane analytic continuation + discrete q-Laplace along a q-spiral,
whose continuation step mixes all coefficients and is *not* diagonal.
Door-i asks: can that summation functor map C1 to GGM, and is a **ramified
pullback** `x → x^{1/2}` (natural for the half-integer slope ½) the bridge?

## 1. Formalize-first: what the RSZ summation functor can and cannot do

Read directly from RSZ §2.2–2.3 and ch. 5:

1. **Slope filtration is strictly functorial (Thm 2.2.4 / §2.2.3, p. 20).**
   Every module has a unique filtration with pure-isoclinic quotients; the
   graded `gr M = ⊕_{µ∈S(M)} M(µ)` functor is exact, faithful, ⊗-compatible,
   and *all* morphisms respect the filtration.
2. **Formal class = gr M (§2.3, p. 21).** "The formal class of M is equal to
   the formal class of gr M" — the slope multiset together with the isoclinic
   pieces is the **complete formal invariant**.
3. **Summation stays inside one formal class (§5.5.2, Thm 5.5.7, p. 96–97).**
   The summation `F^A_{(Λ₁,…,Λ_{k−1})}` produces the *analytic realizations*
   of a formal module M with `gr M = A₀`, indexed by a choice of generic
   divisor partition. The ambiguity between partitions is the q-Stokes
   phenomenon: the Stokes matrices `St_{λ₀}(λ;A)` are **upper-triangular
   unipotent**, flat at 0, satisfying `(σ_q Y)A₀ = A₀Y` — i.e. automorphisms
   inducing the **identity on gr M₀** (the Stokes sheaf, §4.4). `{St, A₀}` is
   a complete analytic invariant *of a module already in the formal class*
   `C_{A₀}`.

**Consequence (the key structural fact).** The analytic q-Borel–Laplace
summation never changes `gr M`. It moves *within* a formal class, not
between classes. Hence a module N can be a summation-image of M **only if**
`gr M ≃ gr N` — same slope multiset, same isoclinic type.

- C1 at ∞: `S = {½}`, mult 2 → **pure isoclinic** (Def §2.2.2, p. 18); with
  slope `d/r = 1/2` coprime, `r = 2`, it is the *irreducible* rank-2 module
  `E(2,1,·)`, the restriction of scalars of a rank-1 slope-1 line on the
  2-cover (§2.2.2.2, p. 19). `gr(C1) =` one isoclinic block.
- GGM at ∞: `S = {−1,+1}` → pure but **anisoclinic**: `gr(GGM) =`
  slope(+1) ⊕ slope(−1), two distinct integral isoclinic lines (reducible).

`gr(C1) ≠ gr(GGM)`. By facts 1–3, **no RSZ summation functor maps C1 → GGM.**

## 2. Does the ramified pullback `x → x^{1/2}` bridge the gap? No.

RSZ **Thm 2.2.1(iv)** (Newton polygon under ramification, p. 16): with
`z′ = z^{1/ℓ}` and `q′` an ℓ-th root of q, slopes rescale **uniformly**,
`r_M(µ) = r_{M′}(ℓµ)` — the ℓ-fold pullback multiplies every slope by ℓ.

Apply to C1's ∞-slope multiset `{½, ½}`:

```
{½, ½}  --(ℓ-cover)-->  {ℓ/2, ℓ/2}    for every ℓ ∈ ℕ*.
```

This is an **equal pair** for every ℓ. GGM's `{−1, +1}` is a **distinct
pair summing to 0**. There is no ℓ with `ℓ/2 = −1` *and* `ℓ/2 = +1`
simultaneously — impossible. The natural `ℓ = 2` (matching the denominator
of ½) lands C1 on **pure isoclinic slope 1, rank 2** — an *integral*-slope
pure module (now inside the domain where the RSZ level-1 q-Borel of §3.3
applies), but still a **single slope**. A level-1 summation then sends that
single slope 1 to slope 0 (fuchsian) — never to `{−1, +1}`.

**The surviving invariant is isoclinicity.** A single-slope (isoclinic)
module stays isoclinic under all three RSZ operations:

| Operation | Effect on the ∞-slope set | Isoclinicity |
|---|---|---|
| analytic summation (ch. 5) | preserves `gr M` (§1) | preserved |
| q-Borel/q-Laplace shear (§3.3, integral slopes) | uniform shift of the single slope | preserved |
| ramified pullback `z^{1/ℓ}` (Thm 2.2.1(iv)) | uniform scale `µ ↦ ℓµ` | preserved |

C1 is isoclinic at ∞ (`{½}`); GGM is anisoclinic (`{−1,+1}`). No composite
of summation, Borel shear, and ramified pullback can turn a pure-isoclinic
module into an anisoclinic one. **The ramified pullback is not the bridge.**

## 3. Verdict (per AGENTS.md refuted-discipline)

**Scope-(b) structural exclusion — (c) OBSTRUCTED.** The analytic
(transcendental) q-Borel–Laplace summation functor of RSZ ch. 5, *including*
a ramified pullback `x → x^{1/ℓ}` of any order, **cannot** map the C1 module
to the GGM eq-49 module. Invariant cited (a proved classification theorem,
not a failed fit): **isoclinicity of the ∞-slope filtration**, protected by
RSZ Thm 2.2.4 (functorial `gr`) + §2.3 (formal class = `gr M`) + Thm 5.5.7
(summation is unipotent-on-`gr`, stays in one formal class) + Thm 2.2.1(iv)
(ramification scales slopes uniformly, `{½,½} ↦ {ℓ/2,ℓ/2}`, an equal pair
that can never equal the distinct pair `{−1,+1}`). C1 is pure isoclinic at
∞; GGM is anisoclinic; every RSZ summation/Borel/ramification functor
preserves isoclinicity. This subsumes Route A (formal-module inequivalence)
and Route D (formal q-Borel = diagonal gauge) and **closes the last RSZ door**
— the "analytic summation content" that A and D had left explicitly live.

**Explicitly NOT excluded** (outside the RSZ q-difference-module category —
the same carve-outs Routes A/D noted; RSZ summation does not act here):
- **arbitrary sequence-level maps** `b_m ↦ y_m` not induced by a q-difference
  morphism `g(q^m)` (a raw bijection of sequences carries no slope invariant);
- **inhomogeneous identifications** (the 4₁ colored Jones is minimally order-2
  *inhomogeneous*; a forced term is not a module morphism);
these are the weakest, least-canonical identifications and lie entirely
outside the RSZ analytic-classification framework, so RSZ neither realizes
nor forbids them. They are the only formal residue after Doors A/D/i.

**No numeric probe added.** No concrete candidate kernel emerged — the
verdict is obstruction, and the decisive step is exact slope arithmetic
(`{ℓ/2,ℓ/2} ≠ {−1,+1}` for all ℓ; equal-pair vs distinct-pair). The
underlying ∞-Newton-polygon hulls `{½,½}` (C1) and `{−1,+1}` (GGM) were
already machine-verified (mpmath lower-hull) in Route A §2; nothing here
needs re-running.

**Discipline.** Formalize-first: the exclusion is a cited RSZ classification
theorem applied to hand slope algebra, run *before* (and instead of) any
scan. No AME data; no fit. The q-lift identification and
`conj:qdifference-kernel-prolongation-symbol` remain conjectures — nothing
here derives them; Door-i *narrows* the search by closing the analytic-
summation route, a strong negative for the C1↔GGM equivalence programme.
