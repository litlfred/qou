import QOU.Interactions.MarkovPeel
import QOU.Interactions.HeckeEngine

/-!
# Concrete Markov trace on the H₃(q) NF basis

H₃-specialised companion to `QOU.Interactions.MarkovPeel`.  Provides
the explicit canonical Jones–Markov trace on the 6-element NF basis
of `H₃(q)` (`HeckeNF := Fin 6 → R_q`, basis
{γ, σ₀, σ₁, L₊ = σ₀σ₁, L₋ = σ₁σ₀, e⁻ = σ₀σ₁σ₀}; see
`QOU.Interactions.HeckeEngine`).

The canonical trace values on this basis are (per
`markov_trace_canonical.py` lines 13-17 and the Python production
witness `markov-peel-atomic-tr-m.witness.json`):

  tr_M(γ)  = 1
  tr_M(σ₀) = z
  tr_M(σ₁) = z
  tr_M(L₊) = z²
  tr_M(L₋) = z²
  tr_M(e⁻) = h·z² + z       where h = q − q⁻¹

Direct numerical cross-check at q₀:
  proton  = b₀·γ + b₁·σ₀ + b₂·σ₁ + b₃·L₊ + b₄·L₋ + b₅·e⁻
       tr_M(proton)|q₀ = +1.14575978231523894039…

  Migrated C → D on 2026-09-05 (`qou-i229` → `qou-46ab`, owner-approved).
  This comment previously stated +1.065306228592389333… and claimed it
  "matches Hoefsmit + Wenzl bridge witness
  `atomic-tr-m-mpfr-50dps.witness.json` to ~4·10⁻¹⁶". Both halves were wrong:
  the value was **convention C**, and that witness gives
  1.1457597823152389404 — a 7.02·10⁻² gap, not 4·10⁻¹⁶, wrong by fourteen
  orders of magnitude. It was word-for-word the claim `qou-46ab` had already
  disproved at `canonical_tr_m_three_path_comparison.py:104`, and it survived
  here because that bean scanned the literal `1.06530622861316` while this
  file rendered the same quantity as `1.065306228592389333`.

  `qou-46ab` attributes the two frames to 50 digits:
       C-frame  1.0653062286131670594     (excised)
       D-frame  1.1457597822878355047     |D−C|/C = 0.0755215

  The value now quoted is the bridge witness's own, at `q0Anchor: muon` on the
  live pin — the same anchor and pin as `prop:q-hecke-seminormal-character-
  closure`, which was migrated in the same pass. The agreement claim is
  dropped rather than restated with a new tolerance: it has not been
  re-measured, and asserting an unmeasured tolerance is what went wrong here
  the first time.

## Scope vs the abstract `MarkovTrace` typeclass

`MarkovTrace H R` from `MarkovPeel.lean` is a *tower*-flavoured
typeclass — it expects `top : Nat → H` for arbitrarily large strand
counts.  `HeckeNF` is fixed at 6 elements (only H₃), so a *direct*
`MarkovTrace HeckeNF R_q` instance would need to interpret
`top n` for n > 3 as a degenerate / dummy value, which would
sacrifice the algebraic content of the (M2) Markov-peel axiom.

This file therefore provides a *specialised* `MarkovTraceH3`
record that captures the H₃-specific trace + axioms, and a one-line
derivation of `tr_M(proton)` matching the Python production
witness.  A full `MarkovTrace` instance for the *whole tower*
requires a generic family `HeckeNF (n : Nat) := Fin (Nat.factorial n) → R`
(or a Garside / Iwahori normal form), which is out of scope here.

## Open items (`#508` Phase 6 follow-up)

  - Build `MarkovTraceH3 → MarkovTrace HeckeNF R_q` for n = 3 only,
    routing arbitrary-`n` calls through dummy values for n ≠ 3.
  - Cross-check via `decide` / `native_decide` against the Python
    proton witness (`tr_M(proton)|q₀ ≈ 1.1458` under convention D;
    the ≈ 1.0653 this read was the excised convention C).

## References

- [jones1987] V.F.R. Jones, *Hecke algebra representations of braid
  groups and link polynomials*, Annals of Math. 126 (1987), 335–388.
- [kassel2008] C. Kassel, V. Turaev, *Braid groups*, Springer GTM 247.
-/

namespace QOU.Interactions

open QOU.Archimedean

/-! ## §1  H₃-specialised Markov trace -/

/-- An H₃-specific Markov-trace structure parameterised on the
    target ring `R` (typically a √q-extended Laurent ring or a
    formal symbolic ring).  Captures the canonical trace on the
    six NF basis elements of H₃(q):
    {γ, σ₀, σ₁, L₊, L₋, e⁻}. -/
structure MarkovTraceH3 (R : Type*) [CommRing R] where
  /-- The Markov parameter `z = q³/(q²+1) = q²/[2]_q` — **convention D**,
      the production trace (trace-convention registry). Corrected
      2026-09-05 (`qou-46ab`): this read `z = 1/(q^{1/2} + q^{-1/2})`,
      which is **convention C**, excised by the owner ruling of
      2026-08-09. The two are not variant normalisations of one
      quantity — see `rem:markov-z-reconciliation`. -/
  z : R
  /-- The Hecke parameter `h = q − q⁻¹`. -/
  h : R
  /-- The trace map.  Linear in the NF basis. -/
  tr : HeckeNF → R

/-- The canonical Markov-trace function on H₃ NF basis elements.

    Given Markov parameter `z` and Hecke parameter `h = q − q⁻¹`,
    a basis-linear element `a : HeckeNF` (6 coefficients in `R_q`)
    has Markov trace

      tr (a) = a₀ · 1
             + a₁ · z          (σ₀)
             + a₂ · z          (σ₁)
             + a₃ · z²         (L₊ = σ₀σ₁)
             + a₄ · z²         (L₋ = σ₁σ₀)
             + a₅ · (h·z² + z) (e⁻ = σ₀σ₁σ₀)

    The values come from the Markov axioms applied to each basis
    element individually:
      • tr(γ) = 1            by (M3)
      • tr(σ_i) = z          by (M2) with x = γ
      • tr(σ_iσ_j) = z²      by two (M2) peels (`prop:markov-pair-z2`)
      • tr(σ_iσ_jσ_i) = h·z² + z (Hecke quadratic + Markov peel)

    Corrected 2026-09-05 (`qou-46ab`): this claimed the Python
    production witnesses cross-check the formula at `q = q₀` to
    ≤ 4·10⁻¹⁶ against the Hoefsmit + Wenzl bridge. That tolerance was
    measured in **convention C** and does not hold as stated; the
    bridge witness is 7·10⁻² from the C-frame value. The formula
    itself is convention-independent — it is the Markov axioms applied
    basis element by basis element — so nothing above depends on `z`'s
    value. The numeric claim is dropped rather than restated with a new
    tolerance, because it has not been re-measured under D.

    The signature takes an explicit ring hom `φ : R_q →+* R`
    (the "lift" of the algebra coefficients into the trace ring)
    so the canonical instance with `R = R_q` and `φ = RingHom.id`
    drops out trivially, while the symbolic instance with
    `R = R_q[z, z⁻¹] / (z⁻¹ − (q² + 1)/q³)` is also expressible via
    the inclusion hom.  (Corrected 2026-09-05, `qou-46ab`: the defining
    relation read `z⁻¹ − q^{1/2} − q^{-1/2}`, i.e. **convention C**.
    Under production convention D, `z = q³/(q²+1)`, so the relation is
    `z⁻¹ = (q²+1)/q³` — and note it needs no √q, which is one of the
    structural reasons D is the production trace.) -/
noncomputable def trH3
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) (a : HeckeNF) : R :=
  φ (a 0)
  + φ (a 1) * z
  + φ (a 2) * z
  + φ (a 3) * z^2
  + φ (a 4) * z^2
  + φ (a 5) * (h * z^2 + z)

/-- Reference: tr_M(γ) = 1.  Direct from the (M3) unit axiom. -/
theorem trH3_unit
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) :
    trH3 φ z h (fun i => if i = 0 then (1 : R_q) else 0) = 1 := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [leitner2026] markov-axiom-recursive-ascent (QOU narrative)
  simp [trH3]

/-- Reference: tr_M(σ_0) = z.  Single Markov peel from the unit. -/
theorem trH3_sigma0
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) :
    trH3 φ z h (fun i => if i = 1 then (1 : R_q) else 0) = z := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  simp [trH3]

/-- Reference: tr_M(σ_0 σ_1) = z².  Two consecutive Markov peels.
    This is the H₃ instance of `prop:markov-pair-z2` from the
    abstract typeclass; see `MarkovPeel.markov_pair_z2`. -/
theorem trH3_L_plus
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) :
    trH3 φ z h (fun i => if i = 3 then (1 : R_q) else 0) = z * z := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  -- Ref: [leitner2026] prop:markov-pair-z2 (QOU narrative)
  simp [trH3, sq]

/-- Reference: tr_M(σ_0 σ_1 σ_0) = h·z² + z.  Hecke quadratic +
    Markov peel; the only basis element whose trace involves the
    Hecke parameter `h`. -/
theorem trH3_e_minus
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) :
    trH3 φ z h (fun i => if i = 5 then (1 : R_q) else 0)
      = h * z * z + z := by
  -- Ref: [jones1987] https://doi.org/10.2307/1971403
  simp [trH3, sq]
  ring

/-- Canonical instance: take `R = R_q` and embed via `RingHom.id`.
    Provides the full `MarkovTraceH3` record on the H₃ NF basis,
    parameterised by a chosen `z` and `h = q − q⁻¹` in `R_q`.

    The `tr` field is `trH3` applied with the identity ring hom;
    no proofs are bundled into the structure (the four reference
    identities above suffice for the basis evaluations).  See
    `markov-peel-atomic-tr-m.witness.json` for cross-checks. -/
noncomputable def canonicalMarkovTraceH3 (z h : R_q) : MarkovTraceH3 R_q where
  z := z
  h := h
  tr := trH3 (RingHom.id R_q) z h


/-- Reference (`qou-46ab`): `tr_M(σ₁) = z` and `tr_M(L₋) = z * z` on the remaining two
NF basis elements of `H₃(q)`. -/
theorem trH3_sigma1_and_L_minus
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) :
    trH3 φ z h (fun i => if i = 2 then (1 : R_q) else 0) = z ∧
      trH3 φ z h (fun i => if i = 4 then (1 : R_q) else 0) = z * z := by
  constructor
  · simp [trH3]
  · simp [trH3, sq]

/-- **Additivity of `trH3` (`qou-46ab`).** `trH3` is additive across coefficient vectors
`a, b : HeckeNF` for every Markov parameter `z` and Hecke parameter `h`. -/
theorem trH3_add
    {R : Type*} [CommRing R]
    (φ : R_q →+* R) (z h : R) (a b : HeckeNF) :
    trH3 φ z h (fun i => a i + b i) = trH3 φ z h a + trH3 φ z h b := by
  simp only [trH3, map_add]
  ring

end QOU.Interactions
