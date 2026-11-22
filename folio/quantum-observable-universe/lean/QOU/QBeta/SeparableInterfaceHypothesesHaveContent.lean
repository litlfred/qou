import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.NormNum

/-!
# The Pauli-lock closure is carried entirely by its two hypotheses

**What this file establishes.** `QOU.QBeta.InterfaceScalar.separable_interface_degenerate`
is the theorem the two-nucleon channel-asymmetry closure rests on. Its statement is

```lean
theorem separable_interface_degenerate
    {Sp Is Sp3 : Type*} (fSpin : Sp → R) (fIso : Is → R) (fSpace : Sp3 → R)
    (s1 s0 : Sp) (t1 t0 : Is) (ell : Sp3)
    (hplus : fSpin s1 = fIso t1) (hminus : fSpin s0 = fIso t0) :
    fSpin s1 * fIso t0 * fSpace ell = fSpin s0 * fIso t1 * fSpace ell
```

and its proof is `rw [hplus, hminus, mul_comm (fIso t1) (fIso t0)]`. Three facts about
that shape, each machine-checked below:

1. **The hypotheses do work** (`separability_hypotheses_have_content`). Drop them and
   the conclusion is false — exhibited on a two-element index type over `ℝ`. So the
   closure is not a tautology about products.
2. **The residual mathematics is commutativity** (`degeneracy_is_commutativity`). Once
   `hplus`/`hminus` are in force the conclusion is `mul_comm`. Everything the theorem
   asserts about physics is asserted by its antecedent.
3. **Releasing the hypotheses releases the conclusion completely**
   (`asymmetry_attainable_with_distinct_scalars`, `distinct_positive_scalars_reach_any_ratio`).
   If the isospin `SU(2)` carries scalars `ν±` different from the spin `SU(2)`'s `μ±`,
   the channel ratio is *any* element of the field — with positivity preserved over `ℝ`,
   so the escape is not an artefact of admitting unphysical negative weights. In
   particular the measured two-nucleon asymmetry `33.7055` is attainable
   (`measured_asymmetry_attainable`).

**Why this is worth stating.** Bean `qou-brng` (2026-09-04) records the equal-scalars
hypothesis as *"the residue"* of the channel-asymmetry question and names its next step
as *"a witness for D9 would make the equal-scalars question decidable for the first
time."* Two shape facts bear on that, and both are checkable rather than argued:

* `fSpin` and `fIso` are **arbitrary functions on arbitrary types**. The projector
  scalars `μ₊ = (z + q⁻¹)/(q + q⁻¹)`, `μ₋ = (q − z)/(q + q⁻¹)` appear in the theorem's
  *docstring*, never in its *statement*. Nothing in the type ties either function to the
  corpus's `H₂` Wedderburn weights `y₂`, `y₁₁` — that identification lives in a different
  section of the same file (`weight_eq_proj_scalar`, `WeightsDetermineZ`), about
  different variables.
* The theorem has **no application site**. Measured over every tracked file, with Lean
  comments stripped (nested block comments included) before the name is searched for.
  Quoted against **`origin/main` as of 2026-09-06**, which is the tree the claim is
  *about* — not against this branch, which cites the name in four files of its own and so
  cannot be its own denominator:

      1 declaration, 0 applications, 28 prose citations in 13 files
      16 .md · 8 .py docstrings · 2 witness/ledger JSON · 2 Lean docstrings
      (isospin-from-canonical-bowtie.lean, TensorCouplingCannotUnbindSinglet.lean)

  On this branch the same command reads **41 in 17 files**. The whole increase is this
  PR's own four files — verified by set difference against `origin/main`, which adds no
  file and removes none, so no sibling contributed one. **The load-bearing figure is the
  `0`**, which is identical on both trees; the guard reports the prose count but gates
  only on the applications:
  [`scripts/separable-interface-instantiation-audit.py`](../../../../../../scripts/separable-interface-instantiation-audit.py).

So `hplus`/`hminus` are not a claim *about the corpus* that a witness could settle; they
are the antecedent of a statement universally quantified over every possible pair of
scalar assignments. Making them a claim about the corpus requires *instantiating* the
theorem at the corpus's own constructions — which nothing does.

**And that instantiation is not merely absent — one of its two arguments does not
exist.** Measured 2026-09-06 over every `.lean` in the tree:

* **`fIso` IS available.** The isospin scalars are `μ₊ = (z + q⁻¹)/(q + q⁻¹)` and
  `μ₋ = (q − z)/(q + q⁻¹)` (`InterfaceScalar.mu_sum_eq_one`,
  `mu_singlet_lt_mu_triplet`). At the proton pin under convention D they evaluate to
  `0.75270211325196540159377935162` and `0.24729788674803459840622064838` — which are,
  to all 30 digits, the corpus's own Wedderburn weights `y₍₂₎` and `y₍₁,₁₎` at `n = 2`
  (`y-lambda-at-q0.witness.json`), exactly as `weight_eq_proj_scalar` says they must be.
  **This is a re-measurement, not a discovery:** bean `qou-kj4v` recorded the same
  identity at 50 dps (agreement to `3.3e-52`) on 2026-08-09. Cited because the agreement
  is worth having twice from two directions, not because it is new here.
* **`fSpin` is NOT.** There is no spin-side projector-scalar pair anywhere. The two
  spin-side carriers assert something else entirely: `BringFiberAction` (D10) builds
  `A5Irrep → IcosahedralRotation` with an injectivity field, and `SpinFromSo3Fiber`
  constrains `levelCoeff : ℕ → R`, the `h^(2n)` Wedderburn coefficients of the
  three-strand Borromean trace (`levelCoeff 1 = 0`, `levelCoeff 2 = −3/4`). Neither is a
  two-element scalar on the spin channel. Read from the carriers' own field lists, not
  from their names.

**🛑 "un-instantiable" would be too strong, and this paragraph said it before the beans
path of the corpus-grep came back.** Someone *has* instantiated it: bean `qou-5d6k`
(2026-08-25) evaluates the Pauli-locked interface at 50 dps by using `μ±` for **both**
`SU(2)`s and gets

    μ(³S₁) = μ₊^spin · μ₋^iso = 0.18614164195799085217
    μ(¹S₀) = μ₋^spin · μ₊^iso = 0.18614164195799085217

— `separable_interface_degenerate`'s conclusion, measured, to the last digit. So the
statement is not that the identification cannot be written down; it is that **the only
way anyone has written it down is by positing `μ±` on the spin side, which assumes
`hplus`/`hminus` rather than checking them.** That is why "instantiate it at the corpus's
own constructions" is empty as a next step: no *construction* supplies `fSpin`, and the
one instantiation that exists supplies it by assumption.

The distinction matters because the two readings send a reader to different places. "It
cannot be instantiated" invites building a spin scalar. "It has only ever been
instantiated by assuming the answer" says the missing thing is a *derivation* of the spin
projector weights from the D10 side — which is a statement about `BringFiberAction`, not
about this theorem.

**A route that this observation might seem to open is already closed — do not walk into
it.** The tempting next move is to drop the missing spin factor and read the channel
asymmetry off the isospin scalars alone. Their log-ratio at the proton pin is
`B(T=0)/B(T=1) = 4.9181`, against a measured `33.7055` — but the shortfall is beside the
point, because the whole class is excluded by a stronger argument that needs no candidate:
the *total* `B(T=1) + B(T=0) = −α·log(μ₊μ₋)` is invariant under every T-odd rescaling
`(μ₊, μ₋) ↦ (μ₊t, μ₋/t)`, and `μ₊ + μ₋ = 1` floors it at `α·log 4 = 5.8030` against
nature's `2.1510`. Route 7 of
[`2026-08-16-two-nucleon-sector-final-state-eight-closures.md`](../../../../../../docs/audits/2026-08-16-two-nucleon-sector-final-state-eight-closures.md),
Lean, scope-(b), landed 2026-08-16. The `4.9181` is recorded here only so the next reader
does not re-derive it as though it were news.

There is a second, independent reason, and it is sharper: bean `qou-4g4a` proves the
admissible interface band `[z − h, z] = [0.40362773835082593616, 0.61268803714646525160]`
lies **strictly between** the two isospin weights — `μ₋` is 63.22 % below the floor and
`μ₊` 22.85 % above the ceiling, with a 7.56 % margin on the tighter of the two `q`
conditions, so it is not a knife-edge and not fixable by a better `q`. Using an isospin
projector *as* the interface is therefore not merely unmotivated but **unavailable**: the
two mechanisms compute on disjoint sets. (That separation on the lower side is a
convention-**D** phenomenon; under C, `μ₋ = 0.303675` sits inside the band.)

**What this does NOT say.** It does not refute `separable_interface_degenerate`, which is
correct and sorry-free, nor the physics reading of the Pauli lock, nor anything about
whether the two `SU(2)`s in fact carry equal scalars — that stays exactly as unestablished
as its converse. It is scope-(a) throughout: a statement about what the Lean asserts, with
the invariant named where it becomes (b) — see `asymmetry_attainable_with_distinct_scalars`,
whose content is that the conclusion is *unconstrained* once the antecedent is dropped.

**Base ring (§7c).** Everything here is generic — `CommRing`, `CommMonoid`, `Field` —
with the non-degeneracy `(5 : R) ≠ 6` carried as a hypothesis rather than obtained from an
ordering. The archimedean half (positivity of the projector weights, and the measured
asymmetry as a real numeral) lives in the sibling
`SeparableInterfaceHypothesesHaveContentReal.lean` and consumes these results at
`R := ℝ`, per §7c's rule that the specialisation goes in its own file.

-- Ref: [leitner2026] quantum-observable-universe/lean/QOU/QBeta/InterfaceScalar.lean
-/

namespace QOU.QBeta.SeparableInterfaceContent

/-! ## 1. The hypotheses do work -/

/-- **The separability conclusion is false without `hplus`/`hminus`.**

Index the two channels by `Bool`. With `fSpin = (2, 1)`, `fIso = (5, 3)` (reading
`true ↦` the first slot) and a unit space factor, the two sides are `5` and `6`.

The only thing the ring must supply is that those two are different — carried as the
hypothesis `(5 : R) ≠ 6` rather than deduced from an ordering, so the statement stays on
the generic side of the §7c wall. Its `R := ℝ` instance is in the sibling file.

This is the `gate_has_content` pattern this arc uses elsewhere: a theorem whose
hypotheses could be dropped without changing the conclusion asserts nothing, and the
cheapest way to know which kind you have is to exhibit a failure. -/
theorem separability_hypotheses_have_content {R : Type*} [CommRing R] (hne : (5 : R) ≠ 6) :
    ∃ (fSpin fIso : Bool → R) (fSpace : Unit → R),
      fSpin true * fIso false * fSpace () ≠ fSpin false * fIso true * fSpace () := by
  refine ⟨fun b => if b then 1 else 2, fun b => if b then 3 else 5, fun _ => 1, ?_⟩
  have h6 : (2 : R) * 3 = 6 := by norm_num
  simpa [h6] using hne

/-! ## 2. With the hypotheses, the residual mathematics is commutativity -/

/-- **What `separable_interface_degenerate` proves, once its antecedent is applied.**

Rewriting by `hplus` and `hminus` replaces both spin scalars by isospin ones, and the
two sides then differ by the order of a product. So the closure's mathematical content
is `mul_comm`; its physical content is entirely in the identification the hypotheses
make. Stated here separately so that this is visible without reading a proof term. -/
theorem degeneracy_is_commutativity {R : Type*} [CommMonoid R] (a b : R) :
    a * b = b * a := mul_comm a b

/-! ## 3. Releasing the identification releases the conclusion -/

/-- **Distinct scalars reach every ratio.**

If the spin `SU(2)` carries `(μ₊, μ₋)` and the isospin `SU(2)` carries a *different*
pair `(ν₊, ν₋)`, the channel ratio `r` defined by `μ₊ ν₋ = r · (μ₋ ν₊)` is unconstrained:
for every `r` there is such a pair. So no bound on the achievable asymmetry survives the
loss of `hplus`/`hminus` — not a weakened bound, none at all.

Scope (b) on the conjunction {separable interface, distinct scalar pairs}, invariant
named: a field has no nontrivial multiplicative constraint between two free elements. -/
theorem asymmetry_attainable_with_distinct_scalars {R : Type*} [Field R]
    (μp μm r : R) (hμp : μp ≠ 0) :
    ∃ νp νm : R, μp * νm = r * (μm * νp) := by
  refine ⟨1, r * μm / μp, ?_⟩
  field_simp

end QOU.QBeta.SeparableInterfaceContent
