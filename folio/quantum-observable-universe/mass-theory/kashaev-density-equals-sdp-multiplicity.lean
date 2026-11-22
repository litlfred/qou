import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum

/-!
# QOU.Kashaev.DensityEqualsSDPMultiplicity — the ρ_F = ν_SDP conjecture carrier

**Sibling-resolution carrier** for content block
[`conj:kashaev-density-equals-sdp-multiplicity`](kashaev-density-equals-sdp-multiplicity.md):
*the Kashaev density prefactor equals the joint-tower SDP Wedderburn multiplicity*.

Per AGENTS.md §3b the class instance is the **conjectural witness** (sorry = conjecture),
not a missing proof; downstream results take `[KashaevDensityEqualsSdpMultiplicity …]` as an
explicit `[Instance]` hypothesis. **No instance is provided** — that is the honest open state.

## 2026-09-05 — this carrier used to assert nothing

It read, in full:

```lean
class KashaevDensityEqualsSdpMultiplicity where
  holds : Prop
```

A field typed `: Prop` is a field whose *type* is the universe of propositions, so an
instance supplies **a proposition, not a proof of one**: `instance := ⟨True⟩` type-checks and
discharges the class. Every `[KashaevDensityEqualsSdpMultiplicity]`-conditional result was
therefore conditional on nothing. This is the shape AGENTS.md §3b-tax forbids (*"class fields
must carry the conjecture's content … never a bare `True` or an empty body"*).

The old docstring also pointed at `../lean/QOU/Kashaev/DensityEqualsSDPMultiplicity.lean` as
the place where the real axiomatisation lived, marked *"(file pending)"*. That directory does
not exist and never has; there is no library twin under any capitalisation (checked before
this rewrite, as the D11 mis-ref case `WignerSu4FromSpinIsospin` requires — PR #6711). So this
sibling is the only carrier and the content belongs here.

## Prior work — the defect CLASS was known; this fixes one carrier in it

**`holds : Prop` is not a new finding.** Bean `qou-tsnp` states it in the same words —
*"GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing"* — and is the
corpus-wide census and drain queue;
[`docs/audits/2026-08-23-free-prop-field-census.md`](../../../docs/audits/2026-08-23-free-prop-field-census.md)
is the measurement behind it. It was named earlier still in
`2026-06-07-klr-gs-order-formalization-plan.md` and `2026-06-24-devils-advocate-wave10.md`.
This carrier was `UNPINNED-EMPTY` in that census's taxonomy: nothing else in the class could
pin the free `Prop`. What is new here is the repair for this one carrier, not the diagnosis.

Companion repairs of the same defect, same shape: `isospin-from-canonical-bowtie.lean` (D9,
PR #6671) and `../nuclear-interactions/spin-from-so3-fiber.lean` (D10, PR #6683).

## What is encoded below

The block's falsifiable arithmetic content, in the producer's own form:

    B_pred(K_w) = ρ_F · m_e · Vol_hyp(K_w)        with   ρ_F = ν_SDP(K_w) ∈ ℤ_{>0}

Read from the producer [`computations/mass_table_ppb.py`](../../../computations/mass_table_ppb.py),
not from the glyphs:

| symbol | producer | note |
|---|---|---|
| `ν_SDP` | `ATOM_ASSIGN[…]["nu_sdp"]`, lines 156–163 | a plain `int` field, **hardcoded** per atom |
| `B_pred` | `nu * ME * vol` (kashaev rule) and `nu * ME * A * VOL_BORROMEAN` (magic rule) | one shape; the magic rule is the same product with `Vol := A·8G` |
| `ρ_F` | has **no** separate name in the producer — `rho_factor` was renamed to `nu_sdp` | the identity is asserted by the *renaming*, which is precisely what this class states |

Everything is a class **parameter supplied by the caller**, following the rule recorded in
`QOU/AlgebraicSubstrate/ConditionalClasses.lean` after that file's own retraction — an `∃`
over a quantity the class itself chooses cannot be false, whereas a `∀` about a quantity the
caller supplies can be. So the class **is refutable**, and `kashaev_density_eq_sdp_multiplicity_refutable`
below discharges that as a theorem rather than asserting it in prose.

## What is NOT encoded, and why — the honest half

**1. `ν_SDP` itself is not defined here, and cannot yet be.** The block defines it as *"the
dimension of the saturating projection in the irreducible-block decomposition
`H_n(q) ≅ ⊕_{λ⊢n} End(V_λ)`"*. The corpus carries no Lean type for a Hecke Wedderburn SDP
solution, nor for the dimension of its saturating projection, so there is nothing to state
that against. Inventing one would encode a different claim than the block makes. `nuSdp` is
therefore a **parameter**, and this file does *not* claim it is any SDP construct — it states
only that the prefactor is a positive integer and that the binding is that integer multiple.

This is the `qou-tsnp` guard outcome (*"if a conjecture's claim cannot yet be stated against
existing types, say so and name what must grow first"*) applied to one half of the claim.
**What must grow first:** a Hecke-algebra Wedderburn decomposition with an SDP feasible set
and a `saturatingProjection` whose rank is computable.

**2. The categorical-home claim is not encoded.** *"ν_SDP is a MacMahon-style partition-algebra
count"* is an identification of the same missing object, and follows once (1) exists.

**3. It would be wrong to read (1) as merely unformalised.** Per
[`2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md`](../../../docs/audits/2026-06-21-nu-sdp-saturation-obstruction-and-critical-distance.md)
and
[`2026-06-20-he4-nu-sdp-not-computed-definition-gate.md`](../../../docs/audits/2026-06-20-he4-nu-sdp-not-computed-definition-gate.md),
**no operational definition of ν_SDP in the corpus reproduces the confirmed `1, 2, 2`.** Six
routes were computed and none matches; the values in
`joint_tower_sdp_solver_v2.py` carry methodology `"manual-historical-volume-match"`, i.e. they
are hand-assigned inputs. So the missing Lean type is missing because the *mathematics* is
open, not because nobody has typed it. Formalising `nuSdp` as a parameter is the faithful
encoding of that state, not a shortcut around it.

**4. Not claimed: that the identity is derived.** It is a numerical coincidence on three atoms
promoted to a conjecture under owner-authorised Rule-14 adoption (2026-05-24,
[`2026-05-24-rule14-kashaev-density.md`](../../../docs/audits/2026-05-24-rule14-kashaev-density.md)).
Axiomatising it here is the §3b conjecture pattern, not a derivation
(AGENTS.md §"Axiomatization is NOT a Proof").

## A staleness flag raised by writing this, NOT acted on here

The block's §Evidence table opens with `²H → knot 6₂ → ρ_F = ν_SDP = 1`. **Owner ruling A of
2026-08-29 retires that assignment**: the deuteron knot is the canonical braid closure
(trefoil / Hopf, `Vol = 0`) and the deuteron binding is *not* a hyperbolic-volume term
([`2026-08-29-deuteron-knot-owner-decision.md`](../../../docs/audits/2026-08-29-deuteron-knot-owner-decision.md),
Bloch volume leg proved 0 in PR #5242). At `Vol = 0` the block's formula gives `B_pred = 0`
for any `ρ_F`, so the deuteron row cannot pin a prefactor at all. `vol_pos` below therefore
excludes it, which scopes the class to the genuinely hyperbolic atoms. Whether the block's
evidence table should be rewritten is an editorial question about the physics and is left for
the author; this file records the tension rather than silently resolving it.

**Archimedean.** Stated over `ℝ`. Binding energies in MeV, an electron mass scale and a
hyperbolic volume are archimedean quantities compared against AME2020, so §7c's generic-`R`
default does not apply.

-- Ref: [leitner2026] quantum-observable-universe/mass-theory/kashaev-density-equals-sdp-multiplicity.ts
-/

namespace QOU.Kashaev

/-- **CONJECTURE.** The Kashaev density prefactor equals the joint-tower SDP Wedderburn
multiplicity: `ρ_F = ν_SDP ∈ ℤ_{>0}`, and the predicted binding is that integer multiple of
`m_e · Vol_hyp`.

`Atom` indexes the census atoms; `rhoF`, `nuSdp`, `bindingPred`, `vol` and `mE` are all
supplied **by the caller**, so the class is false at values that violate its fields — which is
the point (see the header). `nuSdp` is a bare `ℕ`-valued parameter and is **not** claimed to
be any SDP construct; the corpus has no type for the saturating projection whose dimension it
is meant to be.

**No instance is provided.** Downstream results consume this as
`[KashaevDensityEqualsSdpMultiplicity Atom rhoF nuSdp bindingPred vol mE]` and are genuinely
conditional on it.

-- Ref: [leitner2026] conj:kashaev-density-equals-sdp-multiplicity -/
class KashaevDensityEqualsSdpMultiplicity
    (Atom : Type*) (rhoF : Atom → ℝ) (nuSdp : Atom → ℕ)
    (bindingPred vol : Atom → ℝ) (mE : ℝ) : Prop where
  /-- The electron mass scale is a genuine scale (CAL-1 is positive). -/
  mE_pos : 0 < mE
  /-- Scope: the atoms carrying a *hyperbolic* census knot. This is what excludes the
  deuteron under owner ruling A of 2026-08-29 (`Vol = 0` for the canonical braid closure);
  see the header. -/
  vol_pos : ∀ a, 0 < vol a
  /-- `ν_SDP` is a **strictly positive** integer multiplicity — `ℤ_{>0}` in the block, not
  `ℤ_{≥0}`. The strictness carries content: without it `ν_SDP ≡ 0` satisfies the identity for
  any zero prefactor and the class is back where it started. -/
  nuSdp_pos : ∀ a, 0 < nuSdp a
  /-- **The content.** `ρ_F(K_w) = ν_SDP(K_w)` — the prefactor is that integer exactly. -/
  identity : ∀ a, rhoF a = (nuSdp a : ℝ)
  /-- **The formula the identity feeds**, in the producer's form:
  `B_pred(K_w) = ρ_F · m_e · Vol_hyp(K_w)`. The magic-`A` closure is the same product with
  `vol a := A · 8G`. -/
  binding_formula : ∀ a, bindingPred a = rhoF a * mE * vol a

/-- A prefactor strictly between two consecutive naturals refutes the class, because
`identity` forces the prefactor to be a natural-number cast.

This is the block's own `⁴He` negative, stated as a Lean obstruction: the AME2020-pinned
prefactor there is `B_AME / (m_e · A · 8G) = 28.295673 / (0.51099895 · 4 · 8G) = 1.88917`
([`he4_nu_sdp_binding_arbiter.py`](../../../computations/probes/he4_nu_sdp_binding_arbiter.py)),
which lies strictly between `1` and `2` — so **no** choice of `ν_SDP` satisfies the identity
at the doubly-magic point, and rounding `1.889 → 2` is a choice with no derived origin. -/
theorem not_of_prefactor_strictly_between
    {Atom : Type*} {rhoF : Atom → ℝ} {nuSdp : Atom → ℕ} {bindingPred vol : Atom → ℝ} {mE : ℝ}
    (a : Atom) (k : ℕ) (h₁ : (k : ℝ) < rhoF a) (h₂ : rhoF a < (k : ℝ) + 1)
    (hc : KashaevDensityEqualsSdpMultiplicity Atom rhoF nuSdp bindingPred vol mE) : False := by
  have hid := hc.identity a
  rw [hid] at h₁ h₂
  have hk₁ : k < nuSdp a := by exact_mod_cast h₁
  have hk₂ : nuSdp a < k + 1 := by exact_mod_cast h₂
  omega

/-- The class is **refutable**, which the previous `holds : Prop` carrier was not.

The refuting instantiation is the `⁴He` datum in miniature: `ρ_F = 1889/1000`, with `m_e` and
`Vol` normalised to `1` and `B_pred` chosen so that `binding_formula`, `mE_pos` and `vol_pos`
all *hold*. So the class fails on `identity` **alone** — the prefactor's non-integrality, not
an inconsistent binding, is what refutes it, and it does so for every `ν_SDP` whatsoever.

Stated as a `theorem` rather than left implicit because "the carrier asserts something" is
exactly the property that was missing, and a reader should be able to see it discharged rather
than take the docstring's word. -/
theorem kashaev_density_eq_sdp_multiplicity_refutable (nuSdp : Unit → ℕ) :
    ¬ KashaevDensityEqualsSdpMultiplicity Unit (fun _ => 1889 / 1000) nuSdp
        (fun _ => 1889 / 1000) (fun _ => 1) 1 :=
  fun hc => not_of_prefactor_strictly_between () 1 (by norm_num) (by norm_num) hc

/-- …and the class is not refutable *vacuously*: it has a model, so it is a genuine
constraint rather than a contradiction that every parameter tuple falsifies. Refutability
alone would not distinguish those two, and a contradictory hypothesis class would make every
downstream conditional result vacuously true — the failure mode this rewrite exists to remove,
wearing the opposite sign.

**This is emphatically NOT a witness for the conjecture**, and it is deliberately a `theorem`
rather than an `instance` so that instance search can never find it. The tuple is a toy:
`Atom = Unit`, `m_e` and `Vol` normalised to `1`, and the prefactor set to the integer `2` by
hand. Nothing here computes a `ν_SDP` from an SDP, which is the open half (see the header). -/
theorem kashaev_density_eq_sdp_multiplicity_satisfiable :
    Nonempty (KashaevDensityEqualsSdpMultiplicity Unit (fun _ => 2) (fun _ => 2)
      (fun _ => 2) (fun _ => 1) 1) :=
  ⟨{ mE_pos := by norm_num
     vol_pos := fun _ => by norm_num
     nuSdp_pos := fun _ => by norm_num
     identity := fun _ => by norm_num
     binding_formula := fun _ => by norm_num }⟩

end QOU.Kashaev
