import Mathlib.Tactic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Finset.Basic

namespace QOU.LiftingDescent

/-- In ℤ, the only units are ±1. If |trace| > 1 then it's not a unit.
    This is the Route A proof: bypass the abstract Mhat and work in ℤ. -/
theorem galois_trace_not_unit (n : ℤ) (h : 1 < n.natAbs) : ¬IsUnit n := by
  intro hu
  have h1 : n.natAbs = 1 := Int.isUnit_iff_natAbs_eq.mp hu
  omega

/-- Given a trace function and a bound N past which the trace is large, 
    the trace is not a unit almost everywhere. -/
theorem perpetual_obstruction_from_trace
    (trace : Nat.Primes → ℤ)
    (N : ℕ)
    (h_bound : ∀ p : Nat.Primes, (p : ℕ) ≥ N → 1 < (trace p).natAbs) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit (trace p) := by
  refine ⟨Finset.range N, ?_⟩
  intro p hpS
  have hpN : N ≤ (p : ℕ) := by
    by_contra hlt
    push_neg at hlt
    exact hpS (Finset.mem_range.mpr hlt)
  exact galois_trace_not_unit (trace p) (h_bound p hpN)

/-- **The collapse invariant for the proton/neutron is not a unit.**

    C = a₀(-1) + 2·a₁(-1) = 8 for the proton, and |8| > 1.

    (This said "= 4 for the proton and neutron" until 2026-08-23. Both halves
    were wrong: `a₀` is 8 for the proton and **2** for the neutron, so they do
    not share a numerator constant. Bean `qou-lrnd`.)

    NOTE (2026-08-22, bean `qou-lrnd`): read the TYPE. The conclusion is
    `¬IsUnit (4 : ℤ)`, which mentions neither `p` nor `S`, and the proof term
    discards both binders and takes `S = ∅`. So what this proves is that 4 is
    not a unit in ℤ — not that the Frobenius is a non-unit at every prime.
    The statement carrying that is `qou_proton_frobenius_not_unit` below,
    whose conclusion is `¬ IsUnit (frob p)`. Kept because it is cited, and
    because the ∃/∀ shape is what makes it compose with
    `perpetual_obstruction_from_trace`.

    Derivation: at q = ζ_{2p}, the prime ideal 𝔭 = (1-ζ_p) satisfies
    q ≡ -1 (mod 𝔭), and (q;q)_m ≡ 0 (mod 𝔭) for m ≥ 2. Therefore
    Frob_p ≡ a₀(-1) + a₁(-1)·(1-(-1)) = 8 + 0 = 8 (mod 𝔭).
    CORRECTION (2026-08-23, bean `qou-lrnd`): this paragraph previously
    continued "The Galois norm N(Frob_p) ≡ 4^{p-1} (mod p), which is never ±1
    for p ≥ 3". That is wrong twice: by Fermat 4^{p-1} ≡ 1 (mod p) whenever
    p ∤ 4, and 1 ≡ +1, so the congruence is *satisfied* by a unit rather than
    excluded by one. The claim is removed rather than repaired -- see
    `HabiroCollapse.lean`, where the inference it was standing in for is shown
    not to hold at all.

    This proof uses only the STRUCTURE of the Habiro expansion, not
    🛑 **C IS 8, NOT 4** (2026-08-23, bean `qou-lrnd`). This read "The value
    C=4 is an exact algebraic identity: a₀(u) evaluated at u=-1 gives 4, and
    a₁(-1)=0." Half of that holds — `a₁(-1) = 0` — but `a₀` is the **constant
    8** for the proton (and 2 for the neutron, 192 for the deuteron), so no
    evaluation point yields 4. Measured from the canonical coefficients witness
    in `computations/probes/habiro_collapse_constant_probe.py`. The statement
    below is re-stated at 8; `1 < natAbs` is unaffected.

    And `tr_M` carries a denominator: dividing through, proton and neutron
    both collapse to `1/2` and the deuteron to `1/8` — not integers, and the
    collapse does not separate proton from neutron.

    Ref: [thm:motivic-perpetual-obstruction]
    Ref: [def:motivic-galois-character]
    Ref: bean qou-86gm (symbolic derivation) -/
theorem qou_proton_perpetual_obstruction :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit (8 : ℤ) :=
  ⟨∅, fun _ _ => galois_trace_not_unit 8 (by norm_num)⟩

/-- **The collapse invariant for the deuteron is not a unit.**
    C = a₀(-1) + 2·a₁(-1) = 192, and |192| > 1.

    🛑 This said `-32` until 2026-08-23. The deuteron's `a₀` is the constant
    **192** and `a₁(-1) = 0`, so C = 192 (bean `qou-lrnd`; probe as above).

    Same reading as the proton above: the conclusion is `¬IsUnit (192 : ℤ)`,
    a fact about one integer. `qou_deuteron_frobenius_not_unit` is the
    statement about the Frobenius. -/
theorem qou_deuteron_perpetual_obstruction :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit (192 : ℤ) :=
  ⟨∅, fun _ _ => galois_trace_not_unit 192 (by norm_num)⟩

/-- The prime-ideal-collapse invariant C is a rational integer derived
    from the Habiro expansion: C = a₀(-1) + 2·a₁(-1). When |C| > 1,
    the perpetual obstruction follows with an EMPTY exception set
    (i.e., the Frobenius is non-unit at EVERY prime, not just
    "almost every"). -/
theorem perpetual_obstruction_from_collapse_invariant
    (C : ℤ) (hC : 1 < C.natAbs) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit C :=
  ⟨∅, fun _ _ => galois_trace_not_unit C hC⟩

/-- Non-unitness transfers backwards along a ring map: a ring hom carries
    units to units, so a non-unit image forces a non-unit source. -/
theorem not_isUnit_of_image {R : Type*} [CommRing R]
    (φ : R →+* ℤ) (x : R) (h : ¬ IsUnit (φ x)) : ¬ IsUnit x :=
  fun hx => h (hx.map φ)

/-- **The perpetual obstruction, with the prime in the statement.**

    `frob p` is the Frobenius at `p` — `f(u)|_{u = ζ_{2p}}` from the Habiro
    expansion, living in `ℤ[ζ_{2p}]` — and `reduce p` is reduction modulo the
    prime ideal `𝔭 = (1 - ζ_p)`. The collapse identity `reduce p (frob p) = C`
    is the content the symbolic derivation supplies: at `q = ζ_{2p}` one has
    `q ≡ -1 (mod 𝔭)` and `(q;q)_m ≡ 0 (mod 𝔭)` for `m ≥ 2`, so the expansion
    collapses to `a₀(-1) + 2·a₁(-1) = C`.

    Unlike `qou_proton_perpetual_obstruction`, the conclusion here is about
    `frob p` rather than about a constant, so `p` is not decoration.

    🛑 **The hypotheses have no instantiation at the ring the paragraph above
    describes** (2026-08-23, bean `qou-lrnd`). The theorem is true and
    sorry-free for an arbitrary family `R` carrying a hom to `ℤ` — that is not
    in question — but it does not reach the QOU Frobenius, for two independent
    reasons, both checked exactly in
    `computations/probes/cyclotomic_residue_four_unit_probe.py`:

    * `reduce p : R p →+* ℤ` cannot be reduction mod `𝔭`. That map lands in
      `O/𝔭 ≅ 𝔽_p`. And no hom `ℤ[ζ_2p] →+* ℤ` sends `ζ ↦ -1` — it would force
      `Φ_2p(-1) = 0`, whereas `Φ_2p(-1) = p`. (None exists at all.)
    * With the correct target `𝔽_p`, the residue `C` is a **unit** for every
      `p ∤ C`, so `not_isUnit_of_image` — which needs the *residue* to be a
      non-unit — runs the wrong way. This is not a gap awaiting a proof: the
      cyclotomic unit `u₄ = 1 + ζ + ζ² + ζ³` is a unit of `ℤ[ζ_p]` with
      residue exactly `4 (mod 𝔭)`, so `Frob_p ≡ 4 (mod 𝔭)` is *compatible
      with `Frob_p` being a unit*.

    The collapse half is fine and is now proved in general, with no cyclotomic
    input: `QOU.LiftingDescent.map_habiro_expansion`. What is missing is a
    different obstruction argument entirely, not a discharge of `h_collapse`. -/
theorem habiro_frobenius_not_unit
    {R : Nat.Primes → Type*} [∀ p, CommRing (R p)]
    (frob : ∀ p, R p) (reduce : ∀ p, R p →+* ℤ)
    (C : ℤ) (hC : 1 < C.natAbs)
    (h_collapse : ∀ p, reduce p (frob p) = C) :
    ∀ p : Nat.Primes, ¬ IsUnit (frob p) := by
  intro p
  refine not_isUnit_of_image (reduce p) (frob p) ?_
  rw [h_collapse p]
  exact galois_trace_not_unit C hC

/-- **QOU proton/neutron instance**, C = a₀(-1) + 2·a₁(-1) = 8.
    (Was stated at 4 until 2026-08-23; `a₀` is the constant 8. Bean
    `qou-lrnd`.) Note this instance does NOT separate proton from neutron —
    after the `tr_M` denominator both collapse to `1/2`. -/
theorem qou_proton_frobenius_not_unit
    {R : Nat.Primes → Type*} [∀ p, CommRing (R p)]
    (frob : ∀ p, R p) (reduce : ∀ p, R p →+* ℤ)
    (h_collapse : ∀ p, reduce p (frob p) = 8) :
    ∀ p : Nat.Primes, ¬ IsUnit (frob p) :=
  habiro_frobenius_not_unit frob reduce 8 (by norm_num) h_collapse

/-- **QOU deuteron instance**, C = a₀(-1) + 2·a₁(-1) = 192.
    (Was stated at -32 until 2026-08-23. Bean `qou-lrnd`.) -/
theorem qou_deuteron_frobenius_not_unit
    {R : Nat.Primes → Type*} [∀ p, CommRing (R p)]
    (frob : ∀ p, R p) (reduce : ∀ p, R p →+* ℤ)
    (h_collapse : ∀ p, reduce p (frob p) = 192) :
    ∀ p : Nat.Primes, ¬ IsUnit (frob p) :=
  habiro_frobenius_not_unit frob reduce 192 (by norm_num) h_collapse

end QOU.LiftingDescent
