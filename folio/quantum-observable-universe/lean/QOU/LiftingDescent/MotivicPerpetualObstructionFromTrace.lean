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

/-- Two-term Habiro prime-ideal collapse functional evaluated at a prime-indexed
    root residue `u_res p : ℤ`:
    `a₀(u_p) + a₁(u_p) · (1 − u_p)`.
    When `(u;u)_m ≡ 0 (mod 𝔭)` for `m ≥ 2` and `u ≡ u_res p (mod 𝔭)`, the
    Habiro series `∑_m a_m(u) (u;u)_m` truncates to its `m = 0, 1` terms. -/
def habiroPrimeCollapse (a0 a1 : ℤ → ℤ) (u_res : Nat.Primes → ℤ)
    (p : Nat.Primes) : ℤ :=
  a0 (u_res p) + a1 (u_res p) * (1 - u_res p)

/-- At `u_res p = -1` (the `q = ζ_{2p}` reduction modulo `𝔭 = (1 - ζ_p)`),
    the two-term Habiro prime-ideal collapse evaluates to `a₀(-1) + 2·a₁(-1)`. -/
theorem habiroPrimeCollapse_at_neg_one (a0 a1 : ℤ → ℤ)
    (u_res : Nat.Primes → ℤ) (p : Nat.Primes) (hu : u_res p = -1) :
    habiroPrimeCollapse a0 a1 u_res p = a0 (-1) + 2 * a1 (-1) := by
  unfold habiroPrimeCollapse
  rw [hu]
  ring

/-- Canonical `m = 0` Habiro numerator coefficient for the proton (`a₀(u) = 8`). -/
def protonA0 : ℤ → ℤ := fun _ => 8

/-- Canonical `m = 1` Habiro numerator coefficient for the proton (`a₁(u) = 0`). -/
def protonA1 : ℤ → ℤ := fun _ => 0

/-- Canonical `m = 0` Habiro numerator coefficient for the neutron (`a₀(u) = 2`). -/
def neutronA0 : ℤ → ℤ := fun _ => 2

/-- Canonical `m = 1` Habiro numerator coefficient for the neutron (`a₁(u) = 0`). -/
def neutronA1 : ℤ → ℤ := fun _ => 0

/-- Canonical `m = 0` Habiro numerator coefficient for the deuteron (`a₀(u) = 192`). -/
def deuteronA0 : ℤ → ℤ := fun _ => 192

/-- Canonical `m = 1` Habiro numerator coefficient for the deuteron (`a₁(u) = 0`). -/
def deuteronA1 : ℤ → ℤ := fun _ => 0

/-- When a prime-indexed trace `trace : Nat.Primes → ℤ` collapses at every prime
    to a constant integer `C` with `|C| > 1`, the perpetual obstruction holds
    with an empty exception set `S = ∅` (`∀ p ∉ S, ¬IsUnit (trace p)`).

    Restated (bean `qou-lrnd`) so the conclusion `¬IsUnit (trace p)` genuinely
    depends on the quantified prime `p` and exception set `S` via
    `perpetual_obstruction_from_trace`. -/
theorem perpetual_obstruction_from_collapse_invariant
    (trace : Nat.Primes → ℤ) (C : ℤ) (hC : 1 < C.natAbs)
    (h_collapse : ∀ p : Nat.Primes, trace p = C) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S → ¬IsUnit (trace p) := by
  refine perpetual_obstruction_from_trace trace 0 (fun p _ => ?_)
  rw [h_collapse p]
  exact hC

/-- **The Habiro prime-collapse trace for the proton is not a unit at any prime.**

    For any prime-indexed residue map `u_res : Nat.Primes → ℤ` satisfying
    `u_res p = -1`, the proton Habiro collapse trace
    `habiroPrimeCollapse protonA0 protonA1 u_res p = a₀(-1) + 2·a₁(-1) = 8`
    is a non-unit in `ℤ` for every prime `p ∉ S` (with `S = ∅`).

    Restated (bean `qou-lrnd`) from the former constant conclusion `¬IsUnit (8 : ℤ)`
    so that the conclusion genuinely evaluates the `p`-indexed Habiro collapse
    functional at `p`.

    Ref: [thm:motivic-perpetual-obstruction]
    Ref: [def:motivic-galois-character]
    Ref: bean qou-86gm, qou-lrnd -/
theorem qou_proton_perpetual_obstruction
    (u_res : Nat.Primes → ℤ) (hu : ∀ p : Nat.Primes, u_res p = -1) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S →
      ¬IsUnit (habiroPrimeCollapse protonA0 protonA1 u_res p) := by
  refine perpetual_obstruction_from_collapse_invariant
    (habiroPrimeCollapse protonA0 protonA1 u_res) 8 (by decide) (fun p => ?_)
  rw [habiroPrimeCollapse_at_neg_one protonA0 protonA1 u_res p (hu p)]
  rfl

/-- **The Habiro prime-collapse trace for the neutron is not a unit at any prime.**
    `C = a₀(-1) + 2·a₁(-1) = 2`, and `|2| > 1` (bean `qou-lrnd`). -/
theorem qou_neutron_perpetual_obstruction
    (u_res : Nat.Primes → ℤ) (hu : ∀ p : Nat.Primes, u_res p = -1) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S →
      ¬IsUnit (habiroPrimeCollapse neutronA0 neutronA1 u_res p) := by
  refine perpetual_obstruction_from_collapse_invariant
    (habiroPrimeCollapse neutronA0 neutronA1 u_res) 2 (by decide) (fun p => ?_)
  rw [habiroPrimeCollapse_at_neg_one neutronA0 neutronA1 u_res p (hu p)]
  rfl

/-- **The Habiro prime-collapse trace for the deuteron is not a unit at any prime.**
    `C = a₀(-1) + 2·a₁(-1) = 192`, and `|192| > 1` (bean `qou-lrnd`). -/
theorem qou_deuteron_perpetual_obstruction
    (u_res : Nat.Primes → ℤ) (hu : ∀ p : Nat.Primes, u_res p = -1) :
    ∃ S : Finset ℕ, ∀ p : Nat.Primes, (p : ℕ) ∉ S →
      ¬IsUnit (habiroPrimeCollapse deuteronA0 deuteronA1 u_res p) := by
  refine perpetual_obstruction_from_collapse_invariant
    (habiroPrimeCollapse deuteronA0 deuteronA1 u_res) 192 (by decide) (fun p => ?_)
  rw [habiroPrimeCollapse_at_neg_one deuteronA0 deuteronA1 u_res p (hu p)]
  rfl

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

    Unlike the older constant-conclusion encoding, the conclusion here is about
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
