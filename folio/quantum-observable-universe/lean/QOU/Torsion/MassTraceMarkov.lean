import QOU.IwahoriHecke.JonesNormalisation

/-!
# The Markov trace of a braid is a trace of its multiplicative integral

`QOU.Torsion.MassTraceIdentity` proved the mass identity with the categorical trace of
the Frobenius algebra `A` on itself, and recorded that this functional is the *regular*
trace, which is not a Markov trace (`tr(σ₁σ₂) = h²/6` against `(tr σ₁)² = h²/4` on
`H₃(q)`). This file states the identity with the trace that *is* a Markov trace: the
site-weighted (quantum) trace on `V^{⊗(m+1)}`, `V = R²`, through Jimbo's R-matrix.

## Statement

A braid word is a list of letters `(a, ε)`, `a : Fin m` a strand and `ε` the sign of the
crossing. Its *transport* is the R-matrix acting at strands `a, a+1` of `V^{⊗(m+1)}`:

    T(a, +) = Ř_a,        T(a, −) = Ř_a − (q − q⁻¹) = Ř_a⁻¹.

The discrete multiplicative integral of the word is the ordered product of its transports,
`Hol(ℓ₁ ⋯ ℓ_k) = T(ℓ₁) ⋯ T(ℓ_k)`. The theorems are:

1. `braidTrace_wordBraid` (the mass identity, Markov form):

       tr_M(β_ℓ) = wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ)),

   where `β_ℓ` is the braid the word spells, `tr_M` is the normalised Markov trace
   `QOU.IwahoriHecke.BraidGroup.braidTrace`, `K = diag(w₀, w₁)` is the site weight and
   `wi` is the inverse of `w₀ + w₁`.
2. `jonesFn_wordBraid`: the framing-corrected trace of
   `QOU.IwahoriHecke.JonesNormalisation` is the same functional of `Hol(ℓ)`, times
   `A^{m+1} · B^{writhe}`, with the writhe read off the word as the signed letter count.

The weight is not chosen here. `QOU.IwahoriHecke.MarkovPeel.peel_forces_physical_weight`
shows the peel exists only for `w = (1, q²)` up to scale, and `MarkovNormalized` shows
the normalised peel scalar is then `q³/(q²+1)` (convention D). The two theorems hold for
every weight; the Markov property holds only for that one.

## What this does not say

* **Not a link invariant.** `jonesFn` is invariant under both Markov moves and under
  conjugation, but descending it to links needs Markov's theorem, which this corpus does
  not prove (`JonesNormalisation`, §"One gap remains").
* **Not the categorical trace of `A`.** That is `MassTraceIdentity`, and it is the regular
  trace. This file replaces it; it does not identify the two.
* **Not the continuous holonomy.** `Hol` is the ordered product of finitely many
  transports. That a KZ / Drinfeld–Kohno holonomy along a path of configurations equals
  such a product is a cited theorem, not proved here.
* **Not the abstract Markov trace.** The Ocneanu-weight trace on `H_n(q)` being this
  functional is bean `qou-0fmb`.

**Base ring (§7c).** `R` is any commutative ring; `q⁻¹` and `(w₀ + w₁)⁻¹` are carried as
`qi`, `wi` with witnessing equations. No order, norm or root is used.

## References

- Ref: [turaev2010] https://doi.org/10.1515/9783110221831 — enhanced Yang–Baxter operators;
  the functional `α^{-w} β^{-n} Tr(ρ(b) ∘ μ^{⊗n})` is this one with `μ = K`.
- Ref: [jones1987] https://doi.org/10.2307/1971403 — Hecke algebra representations of
  braid groups and link polynomials.
- Ref: [jimbo1986] https://doi.org/10.1007/BF00704588 — the R-matrix.
-/

namespace QOU.Torsion.MassTraceMarkov

open QOU.IwahoriHecke.Balanced QOU.IwahoriHecke.TensorEmbed QOU.IwahoriHecke.QuantumTrace
open QOU.IwahoriHecke.MarkovNormalized QOU.IwahoriHecke.BraidGroup
open QOU.IwahoriHecke.JonesNormalisation QOU.MathlibExt.SkeinRelation

variable {R : Type*} [CommRing R] (q qi : R) {m : ℕ}

/-- The braid generator of a letter, with the sign of the crossing. -/
def letterBraid (ℓ : Fin m × Bool) : BraidGroupN m :=
  if ℓ.2 then braidGen (coxA m) ℓ.1 else (braidGen (coxA m) ℓ.1)⁻¹

/-- The braid a word spells. -/
def wordBraid (ℓs : List (Fin m × Bool)) : BraidGroupN m :=
  (ℓs.map letterBraid).prod

/-- The R-matrix transport of a letter: `Ř_a` for a positive crossing,
`Ř_a − (q − q⁻¹) = Ř_a⁻¹` for a negative one. -/
def transport (ℓ : Fin m × Bool) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  if ℓ.2 then strandBraid q qi ℓ.1 else negCrossing q qi (strandBraid q qi ℓ.1)

/-- The discrete multiplicative integral of a word: the ordered product of its transports. -/
def hol (ℓs : List (Fin m × Bool)) : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) R :=
  (ℓs.map (transport q qi)).prod

/-- A letter's braid, represented in the Hecke algebra and then on `V^{⊗(m+1)}`, is its
transport. -/
theorem heckeActionN_letter (hqi : q * qi = 1) (ℓ : Fin m × Bool) :
    heckeActionN q qi hqi
        ((heckeRep (coxA m) hqi coxA_symm (letterBraid ℓ) : (BalancedHecke (coxA m) q)ˣ)
          : BalancedHecke (coxA m) q)
      = transport q qi ℓ := by
  rcases ℓ with ⟨a, _ | _⟩
  · have hval : ((heckeRep (coxA m) hqi coxA_symm (braidGen (coxA m) a)⁻¹
          : (BalancedHecke (coxA m) q)ˣ) : BalancedHecke (coxA m) q)
        = negCrossing q qi (sigma (coxA m) q qi a) := by
      rw [map_inv, heckeRep_braidGen]
      rfl
    simp only [letterBraid, transport, Bool.false_eq_true, if_false]
    rw [hval, negCrossing, negCrossing, map_sub, AlgHom.commutes, heckeActionN_sigma]
  · simp only [letterBraid, transport, if_true]
    rw [heckeRep_braidGen_val, heckeActionN_sigma]

/-- The representation of a word's braid is the multiplicative integral of the word. -/
theorem heckeActionN_wordBraid (hqi : q * qi = 1) (ℓs : List (Fin m × Bool)) :
    heckeActionN q qi hqi
        ((heckeRep (coxA m) hqi coxA_symm (wordBraid ℓs) : (BalancedHecke (coxA m) q)ˣ)
          : BalancedHecke (coxA m) q)
      = hol q qi ℓs := by
  induction ℓs with
  | nil => simp [wordBraid, hol]
  | cons ℓ ℓs ih =>
    have hw : wordBraid (ℓ :: ℓs) = letterBraid ℓ * wordBraid ℓs := by
      simp [wordBraid]
    rw [hw, map_mul, Units.val_mul, map_mul, ih, heckeActionN_letter]
    simp [hol]

/-- **Mass identity, Markov form.** The normalised Markov trace of the braid a word spells
is the site-weighted trace of the word's multiplicative integral:
`tr_M(β_ℓ) = wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ))`. -/
theorem braidTrace_wordBraid (hqi : q * qi = 1) (w : Fin 2 → R) (wi : R)
    (ℓs : List (Fin m × Bool)) :
    braidTrace q qi hqi w wi (wordBraid ℓs)
      = wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs) := by
  rw [braidTrace, markovTr, qTrace, heckeActionN_wordBraid]

/-- The signed letter count of a word. -/
def signedLength : List (Fin m × Bool) → ℤ
  | [] => 0
  | ℓ :: ℓs => (if ℓ.2 then 1 else -1) + signedLength ℓs

/-- The writhe of the braid a word spells is the word's signed letter count. -/
theorem braidWritheZ_wordBraid (ℓs : List (Fin m × Bool)) :
    braidWritheZ (wordBraid ℓs) = signedLength ℓs := by
  induction ℓs with
  | nil => simp [wordBraid, signedLength, braidWritheZ]
  | cons ℓ ℓs ih =>
    have hw : wordBraid (ℓ :: ℓs) = letterBraid ℓ * wordBraid ℓs := by
      simp [wordBraid]
    rw [hw, braidWritheZ_mul, ih, signedLength]
    rcases ℓ with ⟨a, _ | _⟩
    · simp [letterBraid, braidWritheZ_inv, braidWritheZ_gen]
    · simp [letterBraid, braidWritheZ_gen]

/-- **The framing-corrected trace** of a word's braid is the same functional of its
multiplicative integral, times the strand and writhe factors. -/
theorem jonesFn_wordBraid (wi : R) (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (ℓs : List (Fin m × Bool)) :
    jonesFn q qi wi hqi w hw (wordBraid ℓs)
      = ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
          * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
          * (wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs)) := by
  rw [jonesFn, braidWritheZ_wordBraid, braidTrace_wordBraid]

end QOU.Torsion.MassTraceMarkov
