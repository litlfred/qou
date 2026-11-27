import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# QOU.Eightfold.HyperbolicVolumeFormType — the hyperbolic volume form is a
**third** kind of degree-3 form, on a **fourth** three-manifold, and it is real

Bean `qou-xlw1`, epic `qou-8lxd`.  Third companion to
`QOU.Eightfold.ContactDistributionRank` and
`QOU.QuantumObservableUniverse.SelfDualityDegree`.

## The question this answers

Raised by the owner: *"when we get to the knot complement there's an `S³` there
and we need a hyperbolic volume … so we need a volume form that is that
hyperbolic metric on the knot complement, which is outside the exceptional
divisor.  On the exceptional divisor, with the Reeb flow, it should not
necessarily be [hyperbolic]."*

Both halves are right, and the second half is provable.

## Four three-manifolds, three geometries

The prior audit
([`2026-09-04-where-the-ambient-s3-comes-from`](../../../../../docs/audits/2026-09-04-where-the-ambient-s3-comes-from.md))
separated three objects the corpus writes as `S³`.  The hyperbolic volume lives
on a **fourth**, which that audit missed because it is not called `S³` — it is
`S³` with something *removed*:

| object | geometry | curvature | compact | `π₁` | its volume form |
|---|---|---|---|---|---|
| `S³_AM` — Alexander–Markov closure arena | topological only | — | yes | trivial | none stated |
| `S³_Reeb` — Hopf bundle over `𝒮_p ≅ S²` | **round / spherical** | `+1` | yes | **trivial** | `Θ ∧ dΘ` |
| `M_S` — circle bundle in `T*S` | contact, genus-4 base | — | yes | infinite (`b₁ ≥ 8`) | `Θ ∧ dΘ` |
| **`S³ ∖ K` — the knot complement** | **hyperbolic** | `−1` | **no, cusped** | infinite | **`Vol(K)`** |

## Why `S³_Reeb` cannot be the hyperbolic one — cited, and the reason is `π₁`

`virtual-particles-exceptional-divisor.md:7` puts the Reeb bundle over the
exceptional divisor as the Hopf fibration `U(1) ↪ S³ → 𝒮_p`.  That total space
is `S³`: compact and **simply connected**.

A complete finite-volume hyperbolic 3-manifold is `ℍ³/Γ` with `Γ ⊂ PSL(2,ℂ)`
discrete and torsion-free, so `π₁ = Γ`; and `Γ` must be **infinite**, since
`ℍ³` itself has infinite volume.  Hence **no simply connected 3-manifold carries
a complete finite-volume hyperbolic metric**, and `S³_Reeb` is not hyperbolic.

That is standard hyperbolic geometry, **cited and not formalised** — Mathlib has
no hyperbolic-manifold API.  It is recorded here because it is what makes the
owner's second half correct: on the exceptional divisor, with the Reeb flow, the
geometry is the round Hopf one, and it is *not* hyperbolic, provably rather than
incidentally.

## What is formalised: the third pair of "different threes"

The hyperbolic volume form is a top form on a **real** 3-manifold, so the object
it is a volume form *of* is the real rank-3 tangent bundle.  `Λ³` of that is a
line, so it is a genuine degree-3 volume form — and the object is
**self-conjugate**, i.e. real Frobenius–Schur type, which
`QOU.Eightfold.Sym2GateFSTrichotomy.real_triple_fails_gate` excludes.

What the eightfold way needs is a **complex** rank-3 object, whose underlying
real rank is `6`, not `3` (`realRank_of_complexRank`, `three_ne_six`).

So this is the **third** instance of one trap, and they should be read together:

| file | the two threes |
|---|---|
| `ContactDistributionRank.degree_three_but_rank_one` | at `dim M = 3` the contact volume form has **degree 3** while `ξ` has complex rank **1** |
| `ContactDistributionRank.dim_seven_two_distributions` | at `dim M = 7` the Sasakian distribution has complex rank **3** while the quaternionic-contact one has **2** |
| **here** | the hyperbolic volume form has **degree 3** while its object has **real** rank 3, not **complex** rank 3 |

Each time, a `3` that is a *degree* has been read as a `3` that is a *rank*.

## Consequences for the framework, stated plainly

**1. `Vol(K)` is currently an *input*, which is a fact about the corpus's present
state and NOT a claim that it must stay one.**  It is computed by SnapPy
(`knot-volumes-verification.md`) and enters `q₀` alongside CODATA `m_μ/m_e`
(`local-substrate-q-proof.md:14`).  By **Mostow rigidity** the complete
hyperbolic metric on a finite-volume 3-manifold is unique up to isometry, so
`Vol(K)` is a *topological invariant of the knot* — there is no metric to
*choose*.  The corpus leans on exactly this: *"Mostow rigidity (geometric
confinement) makes the resulting topology — and hence the mass — discrete"*
(`approach-to-exceptional-divisor.md`).

> **🛑 An earlier draft of this file said the hyperbolic volume form "is not a
> QOU structure — it is imported", and that is RETRACTED.**  Rigidity means the
> metric is not *chosen*; it does not mean the volume is not *derivable*.  The
> corpus in fact asserts the opposite of what I wrote:
> `brings-surface/thurston-relaxation.md` states that the `q`-Pochhammer poles
> are in bijection with the `n` ideal tetrahedra of a hyperbolic triangulation, that
> Newton iteration on Thurston's gluing equations seeded by those poles converges
> to the shape parameters realising the complete hyperbolic structure, and that
> *"the same algebraic-residue data feeds both the SDP and the gluing solver;
> they are different **evaluations of one categorical object**"*
> (`conj:algebraic-geometric-dilog-equivalence`).  The volume-conjecture leg
> points the same way: the Kashaev invariant / coloured Jones is a categorical
> object the framework already computes, and its root-of-unity asymptotics *are*
> `Vol(S³∖K)`.  Whether those links are proved, conjectured or merely asserted is
> a separate question and is being measured — but "not a QOU structure" was an
> impossibility claim I never established, against a route the corpus names.

**2. It is not a fourth calibration.**  `Vol(4₁) = 2·Cl₂(π/3)` is a closed form,
known exactly; SnapPy verifies it numerically rather than supplying it.  Its
status is that of `π`, not that of a measured input.  (For a general knot no
closed form is known and the SnapPy value is the only source — that dependency
is real, and is separate from the `4₁` case.)

**3. The two volume forms are on different manifolds and neither yields the
other.**  `Θ ∧ dΘ` is a contact volume form on a compact simply connected `S³`;
the hyperbolic volume form is the Riemannian volume of a cusped, non-compact,
infinite-`π₁` manifold.  No restriction, deformation or limit of one is the
other, because they are not forms on the same space.

**4. The hyperbolic volume form does not supply `W` either.**  Fifth
independent route to land on real type, after `𝔰𝔲(2) = Im ℍ`, the tetraplectic
`Sp(1)ⁿ`, the affine-`W` compactification, and `Ad(A)`.

## What is proved here, and what is not

**Proved (unconditional integer arithmetic):** that a complex rank-`n` object has
real rank `2n`; that complex rank 3 means real rank 6; that real rank 3 has a
one-dimensional top exterior power (so the hyperbolic volume form is a genuine
volume form) while its object is not complex rank 3; and the three-way table
above as arithmetic.

**Not proved, and asserted nowhere below:**

* that `S³` admits no complete finite-volume hyperbolic metric.  Cited standard
  hyperbolic geometry (`π₁` of such a manifold is infinite).

  > **🛑 The provenance note attached to this used to read "Mathlib has no
  > hyperbolic-manifold API and `library/` holds no source on it".  BOTH HALVES
  > ARE FALSE, measured.**  Mathlib carries
  > `Analysis/Complex/UpperHalfPlane/{Metric,Basic,Manifold,MoebiusAction,Topology}`
  > — the hyperbolic metric on `ℍ²` and the Möbius action — plus the whole
  > `NumberTheory/ModularForms/` tree; what it lacks is a *dilogarithm* and a
  > 3-dimensional hyperbolic-manifold API.  And `library/` is saturated with this
  > material: section-file hits are dilogarithm **849**, Kashaev **548**, volume
  > conjecture **381**, Thurston **321**, gluing equation **215**, ideal
  > tetrahedra **178**, Bloch–Wigner **135**, Neumann–Zagier **96**, Lobachevsky
  > **46**.
  >
  > The error was a change-of-vocabulary blind spot of exactly the kind this
  > corpus keeps recording: the search that produced "holds nothing" used the
  > **contact/CR** vocabulary (`Sasakian`, `CR manifold`, `7-manifold`), while
  > this layer is covered under the **knot-theory / dilogarithm** vocabulary.
  > Note also `Bloch-Wigner` (hyphen) returns 135 and `Bloch–Wigner` (en-dash)
  > returns 19 — one spelling of one name changes the count sevenfold.
* Mostow rigidity, or that `Vol(4₁) = 2·Cl₂(π/3)`.  Both cited.
* that the corpus's `S³_Reeb` and `S³ ∖ K` are the manifolds the corpus intends
  — the three-way `S³` ambiguity is unresolved and is the author's.
* anything about which knot is meant anywhere.  The corpus's own
  torus-vs-hyperbolic treatment (`pion-mass-hyperbolic-threshold.md`) is
  careful and is **not** disturbed by anything here.

Base ring: none — integer arithmetic (§7c: no `ℝ`, no ring at all).
-/

namespace QOU.Eightfold.HyperbolicVolumeFormType

/-- The real rank underlying a complex rank-`n` bundle. -/
def realRank_of_complexRank (n : ℕ) : ℕ := 2 * n

/-- The dimension of `Λ^k` of a real rank-`m` bundle. -/
def extPowerDim (m k : ℕ) : ℕ := Nat.choose m k

/-- **A real 3-manifold's tangent bundle has a genuine degree-3 volume form.**
`Λ³` of a real rank-3 bundle is a line — so the hyperbolic volume form really is
a volume form, and the route was not a category error on that count. -/
theorem real_three_has_volume_form : extPowerDim 3 3 = 1 := by decide

/-- **But its object is real rank 3, and complex rank 3 is real rank 6.** -/
theorem complexRank_three_is_realRank_six : realRank_of_complexRank 3 = 6 := by decide

/-- The two are different, which is the whole content of the trap. -/
theorem three_ne_six : (3 : ℕ) ≠ realRank_of_complexRank 3 := by decide

/-- Restated as the exclusion: a real rank-3 object is not the underlying real
bundle of any complex rank-3 object. -/
theorem real_three_not_complex_three {n : ℕ} (h : realRank_of_complexRank n = 3) :
    False := by
  simp only [realRank_of_complexRank] at h
  omega

/-- The complex rank a real rank-3 object would have to have is not an integer —
`3` is odd, and every complex bundle has even real rank. -/
theorem realRank_even (n : ℕ) : realRank_of_complexRank n % 2 = 0 := by
  simp only [realRank_of_complexRank]; omega

/-- **The third pair of different threes, stated side by side.**  The hyperbolic
volume form has degree 3 — genuinely — while the object it is a top form of has
*real* rank 3, and the eightfold way needs *complex* rank 3, i.e. real rank 6. -/
theorem degree_three_but_real_rank_three :
    extPowerDim 3 3 = 1 ∧ realRank_of_complexRank 3 ≠ 3 := by
  refine ⟨by decide, by decide⟩

/-- For contrast: a complex rank-3 object has real rank 6, whose `Λ³` is
**twenty**-dimensional, not a line.  The complex `Λ³_ℂ` that the eightfold needs
is not the real `Λ³_ℝ` of the same bundle — a further reason the two threes
cannot be identified. -/
theorem complex_three_real_extCube : extPowerDim 6 3 = 20 := by decide

end QOU.Eightfold.HyperbolicVolumeFormType
