/-
Copyright (c) 2026 litlfred. All rights reserved.

# Q_β odd-channel: ζ₄-residue exclusion + R₁₂ trace-cubic reduction (Lean certificate)

Formalize-first certificate for the **scope-(b) structural exclusion** recorded
in `docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md` (bean `0zr0`),
which closed the ζ₄-**residue** route for the Q_β odd channel at the
fibre-Laurent level. The refuted-declaration discipline (AGENTS.md §"Before
declaring refuted/ruled out") requires a scope-(b) exclusion to **cite/prove
the invariant**; until now that invariant lived only in a sympy witness
(`qbeta-zeta4-fibre-cyclotomic.witness.json`). These lemmas are its exact,
kernel-checked certificate.

The object is the bar-odd part of the net decay-width Laurent polynomial
`Δ_net(q) = Δ(neutron) − Δ(proton)`; its numerator (over `4q⁷`) is

  `num(q) = q¹⁴ − 5q¹² + 10q¹⁰ − 16q⁸ + 16q⁶ − 10q⁴ + 5q² − 1`.

**Results (all exact, division-free over any `CommRing`):**

1. `numOdd_factor` — the **cyclotomic content is exactly `q²−1`**:
   `num = (q²−1)·R₁₂`, with `R₁₂` the palindromic degree-12 cofactor.
2. `numOdd_phi4_quot` / `numOdd_at_phi4_root` — **`Φ₄ = q²+1` does NOT divide
   `num`**: exact division `num + 64 = (q²+1)·Q`, so `num ≡ −64 (mod Φ₄)`; at
   any root of `Φ₄` (e.g. `q = i` over `ℂ`) `num = −64 ≠ 0`. This is the
   scope-(b) invariant: the ζ₄=i **residue** (Φ₄ divisibility) is *absent* —
   the odd carrier is not a root-of-unity object.
3. `R12_eq_trace_cubic_shift` (division-free) / `R12_eq_cubic_trace` (`Field`) —
   what **survives**: `R₁₂ = q⁶·C(q²+q⁻²)` with the irreducible cubic
   `C(y) = y³ − 4y² + 3y − 2` in the **bar-even loop-trace variable**
   `y = q²+q⁻² = 2cosh 2λ` (S₃ Galois, disc `−152`). The surviving odd-channel
   content lives in `ℚ[y]`, degree 3 — NOT in a cyclotomic factor.

Derives **no** `c_k` value, wires **nothing**, changes **no** registry tier
(flip-flop guard, registry §8). It hardens an existing refutation and pins the
one surviving open object (`C(y)`). Generic `CommRing` per AGENTS.md §7c; the
one `Field` lemma is the literal `q⁻²` restatement only.

Sorry-free.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

namespace QOU.QBeta.Zeta4Residue

variable {R : Type*} [CommRing R]

/-- Numerator of the bar-odd part of the net decay-width carrier
    `Δ_odd(q) = num(q) / (4q⁷)`. -/
def numOdd (q : R) : R :=
  q ^ 14 - 5 * q ^ 12 + 10 * q ^ 10 - 16 * q ^ 8 + 16 * q ^ 6
    - 10 * q ^ 4 + 5 * q ^ 2 - 1

/-- The palindromic degree-12 cofactor `R₁₂` (the non-cyclotomic substance of
    the odd carrier). -/
def R12 (q : R) : R :=
  q ^ 12 - 4 * q ^ 10 + 6 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1

/-- The surviving cubic in the bar-even trace variable: `C(y) = y³−4y²+3y−2`. -/
def cubicC (y : R) : R := y ^ 3 - 4 * y ^ 2 + 3 * y - 2

/-! ## §1. Cyclotomic content of the odd carrier is exactly `q²−1` -/

/-- **The only cyclotomic content of `num` is the trivial `q²−1`.**
    `num = (q²−1)·R₁₂` — the `Φ₁·Φ₂` factor, with the rest carried by the
    non-cyclotomic palindromic `R₁₂`. -/
theorem numOdd_factor (q : R) : numOdd q = (q ^ 2 - 1) * R12 q := by
  unfold numOdd R12; ring

/-! ## §2. `Φ₄ = q²+1` does NOT divide `num` (the ζ₄-residue exclusion) -/

/-- **Exact division of `num` by `Φ₄ = q²+1` leaves the nonzero constant
    remainder `−64`.** `num + 64 = (q²+1)·Q` with `Q` the explicit degree-12
    quotient. Since the remainder is a nonzero constant, `Φ₄ ∤ num`: the
    ζ₄ = i **residue** is absent from the odd carrier. -/
theorem numOdd_phi4_quot (q : R) :
    numOdd q + 64 =
      (q ^ 2 + 1) *
        (q ^ 12 - 6 * q ^ 10 + 16 * q ^ 8 - 32 * q ^ 6 + 48 * q ^ 4
          - 58 * q ^ 2 + 63) := by
  unfold numOdd; ring

/-- **`num` evaluates to the constant `−64` at every root of `Φ₄`** (e.g.
    `q = i` over `ℂ`, where `q²+1 = 0`). Hence `num` has no `Φ₄` factor: the
    scope-(b) exclusion of the ζ₄-residue route, cited invariant. (Over a ring
    where `(64 : R) ≠ 0` — e.g. `ℤ, ℚ, ℝ, ℂ` — this is a genuine non-vanishing;
    the value `−64` itself holds over any `CommRing`.) -/
theorem numOdd_at_phi4_root (q : R) (hq : q ^ 2 + 1 = 0) : numOdd q = -64 := by
  have h := numOdd_phi4_quot q
  rw [hq, zero_mul] at h
  linear_combination h

/-! ## §3. What survives: `R₁₂ = q⁶·C(q²+q⁻²)`, a cubic in the trace variable -/

/-- **Division-free trace-cubic form of `R₁₂`.** `R₁₂ = q⁶·C(q²+q⁻²)` with
    `C(y) = y³−4y²+3y−2`, written without inverses by clearing `q⁶`:
    `R₁₂ = (q⁴+1)³ − 4q²(q⁴+1)² + 3q⁴(q⁴+1) − 2q⁶` (each `q⁶·yᵏ` becomes a
    genuine polynomial via `q²·(q²+q⁻²) = q⁴+1`). The odd carrier's surviving
    content is a **degree-3 object in the bar-even trace variable**, not a
    cyclotomic factor. -/
theorem R12_eq_trace_cubic_shift (q : R) :
    R12 q =
      (q ^ 4 + 1) ^ 3 - 4 * q ^ 2 * (q ^ 4 + 1) ^ 2
        + 3 * q ^ 4 * (q ^ 4 + 1) - 2 * q ^ 6 := by
  unfold R12; ring

/-- **Literal trace-cubic form (`Field`, `q ≠ 0`):** `R₁₂ = q⁶·C(q²+q⁻²)` with
    the trace variable `y = q²+q⁻²` written explicitly. The `Field`/`q ≠ 0`
    hypothesis is only to admit `q⁻²`; the content is the division-free
    `R12_eq_trace_cubic_shift`. -/
theorem R12_eq_cubic_trace {F : Type*} [Field F] (q : F) (hq : q ≠ 0) :
    R12 q = q ^ 6 * cubicC (q ^ 2 + q⁻¹ ^ 2) := by
  unfold R12 cubicC
  field_simp
  ring

/-! ## §4. `C(y)` is a degree-3 obstruction: no rational root, missed by every
       quadratic substrate anchor

`C(y) = y³ − 4y² + 3y − 2` is **monic with constant term −2**, so by the
rational root theorem any rational root is an integer dividing `2`, i.e.
`y ∈ {±1, ±2}`. The four evaluations below are all nonzero, so `C` has **no
rational root** and (being a monic integer cubic) is **irreducible over ℚ** —
its root generates a genuine **degree-3 field** (S₃ splitting, disc `−152`).

Consequence for the c_3 odd channel: every substrate **quadratic** anchor sits
at a rational trace value `y = q²+q⁻²` — golden `φ ↦ y = 3`, silver `1+√2 ↦
y = 6`, classical `q = 1 ↦ y = 2` — and `C` is nonzero at each. A degree-≤2
substrate number can never be a root of an irreducible cubic, so **no
quadratic-anchor / real-q closure can resolve the odd carrier**; this is the
structural reason those closures (KC-refuted class) keep failing. (Numerical
aside, NOT a structural claim: `C(3) = −2` coincides with the `c_3 → −2` q=1
shadow value; flagged as a coincidence pending any derivation.) -/

/-- **RRT candidate `y = 1`:** `C(1) = −2 ≠ 0`. -/
theorem cubicC_one : cubicC (1 : R) = -2 := by unfold cubicC; norm_num

/-- **RRT candidate `y = −1`:** `C(−1) = −10 ≠ 0`. -/
theorem cubicC_neg_one : cubicC (-1 : R) = -10 := by unfold cubicC; norm_num

/-- **RRT candidate `y = 2` (also the classical `q = 1` trace value):**
    `C(2) = −4 ≠ 0`. -/
theorem cubicC_two : cubicC (2 : R) = -4 := by unfold cubicC; norm_num

/-- **RRT candidate `y = −2`:** `C(−2) = −32 ≠ 0`. -/
theorem cubicC_neg_two : cubicC (-2 : R) = -32 := by unfold cubicC; norm_num

/-- **Golden-anchor trace value `y = φ²+φ⁻² = 3`:** `C(3) = −2 ≠ 0` — the golden
    substrate anchor is not a root of the odd-channel cubic. -/
theorem cubicC_golden : cubicC (3 : R) = -2 := by unfold cubicC; norm_num

/-- **Silver-anchor trace value `y = (1+√2)²+(1+√2)⁻² = 6`:** `C(6) = 88 ≠ 0` —
    the silver substrate anchor is not a root of the odd-channel cubic. -/
theorem cubicC_silver : cubicC (6 : R) = 88 := by unfold cubicC; norm_num

/-- **No rational root (`ℚ`).** The four RRT candidates `{±1, ±2}` are the only
    possible rational roots of the monic integer cubic `C`; each is nonzero
    (`cubicC_one/neg_one/two/neg_two`), so `C` has no root in `ℚ` and is
    irreducible over `ℚ`. Stated as the disjunction of the certified
    non-vanishings that the rational root theorem reduces the claim to. -/
theorem cubicC_rrt_candidates_all_nonzero :
    cubicC (1 : ℚ) ≠ 0 ∧ cubicC (-1 : ℚ) ≠ 0 ∧
      cubicC (2 : ℚ) ≠ 0 ∧ cubicC (-2 : ℚ) ≠ 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;> · unfold cubicC; norm_num

/-! ## §5. Knot-sector decomposition: the degree-3 field is the **Hopf** sector

Where does the cubic field come from? The bar-odd part of the net decay-width
carrier `Δ_net = Δ(neutron) − Δ(proton)` on the H₃ normal-form basis
`{𝟏, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}` (sectors unknot / virtual / Hopf / electron word `e⁻`; the closure of `σ₀σ₁σ₀` on three
strands is the Hopf link, not the trefoil — owner ruling 2026-11-21: electron = σ₀σ₁σ₀, closure the Hopf link; the trefoil σ₀³ ∈ B₂ is the backup)
decomposes **exactly** by knot sector (reproducible exact Laurent arithmetic,
probe `qbeta_odd_carrier_sector_decomposition.py`, from
`free-neutron-decay.witness.json`):

- **virtual (σ₀, σ₁; 1 crossing) → 0** and **electron word (σ₀σ₁σ₀; 3 crossings) → 0**:
  the odd-crossing sectors are bar-EVEN, contributing nothing to the bar-odd
  carrier.
- **unknot (𝟏; identity) → a quadratic** `C_unknot(y) = 2y² − 7y + 4`
  (disc `17`, field `ℚ(√17)`), in `y = q²+q⁻²`.
- **Hopf (σ₀σ₁+σ₁σ₀; 2 crossings) → the cubic** `C_Hopf(y) = y³ − 6y² + 10y − 6`
  (irreducible over `ℚ`, disc `−76 = −2²·19`).

with `C = C_Hopf + C_unknot`. So the **degree-3 field of the odd channel is
sourced entirely by the Hopf-link (double-crossing) sector**; the identity adds
only a quadratic, and the odd-crossing sectors vanish. It is NOT a 3-dim
representation (H₃'s Wedderburn blocks are `1,2,1` — none is 3-dim) nor a single
knot invariant — it is specifically the 2-crossing amplitude in the isospin
difference (refines the KC18 identification of the odd channel with the Markov
crossing term). The discriminant prime `19` is shared by `C_Hopf` (`−76`) and
the total `C` (`−152 = −2³·19`) — the arithmetic fingerprint of the sector. -/

/-- Unknot/identity-sector contribution to the odd-channel cubic: the quadratic
    `C_unknot(y) = 2y² − 7y + 4` (disc `17`). -/
def cubicC_unknot (y : R) : R := 2 * y ^ 2 - 7 * y + 4

/-- Hopf/double-crossing-sector contribution: the **cubic** `C_Hopf(y) =
    y³ − 6y² + 10y − 6` — the source of the degree-3 field. -/
def cubicC_Hopf (y : R) : R := y ^ 3 - 6 * y ^ 2 + 10 * y - 6

/-- **Sector decomposition of the odd-channel cubic.** `C = C_Hopf + C_unknot`:
    the total cubic splits exactly into the Hopf-sector cubic plus the
    unknot-sector quadratic. The `y³` term — hence the degree-3 field — lives
    entirely in the Hopf (double-crossing) summand. -/
theorem cubicC_sector_decomp (y : R) :
    cubicC y = cubicC_Hopf y + cubicC_unknot y := by
  unfold cubicC cubicC_Hopf cubicC_unknot; ring

/-- **The Hopf-sector cubic has no rational root** (RRT candidates = divisors of
    `6`, i.e. `{±1, ±2, ±3, ±6}`, all nonzero: `C_Hopf` = `−1, −23, −2, −58, −3,
    −117, 54, −498`), so it is irreducible over `ℚ`: the double-crossing sector
    alone already carries an irreducible cubic field (disc `−76 = −2²·19`). -/
theorem cubicC_Hopf_rrt_candidates_all_nonzero :
    cubicC_Hopf (1 : ℚ) ≠ 0 ∧ cubicC_Hopf (-1 : ℚ) ≠ 0 ∧
      cubicC_Hopf (2 : ℚ) ≠ 0 ∧ cubicC_Hopf (-2 : ℚ) ≠ 0 ∧
      cubicC_Hopf (3 : ℚ) ≠ 0 ∧ cubicC_Hopf (-3 : ℚ) ≠ 0 ∧
      cubicC_Hopf (6 : ℚ) ≠ 0 ∧ cubicC_Hopf (-6 : ℚ) ≠ 0 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> · unfold cubicC_Hopf; norm_num

/-! ## §6. Classical (q=1) shadow: the Hopf cubic reproduces the c_3 shadow

At the classical trace point `q = 1` the trace variable is `y = q²+q⁻² = 2`.
The c_3 q=1 shadow is `−2` (registry KC10, `= J_Hopf(q=1)`). The Hopf-sector
cubic reproduces it exactly — a carrier-side confirmation that the c_3→−2 shadow
lives in the Hopf (double-crossing) sector (KC20/§5).

**Scope (STRICT).** This is a **shadow-level** (q=1) identity only. It does NOT
extend to the substrate: `C_Hopf` at the substrate trace value is anchor-rigid
while the physical `c_3` swings 2.375% across anchors, so the cubic does not
determine `c_3` off `q=1` — the swing lives in the crossing weight `w(q)`
(registry KC19). See
`docs/audits/2026-07-07-hopf-cubic-vs-crossing-weight-shadow-bridge.md`. The
total carrier gives `C(2) = −4 = C_Hopf(2) + C_unknot(2)`; the shadow `−2`
matches the per-sector Hopf value `J_Hopf(1)`, not the total. -/

/-- **Shadow identity.** `C_Hopf(2) = −2` — the Hopf-sector cubic at the
    classical trace value `y = 2` (`q = 1`) equals the c_3 q=1 shadow
    `−2 = J_Hopf(1)` (KC10). -/
theorem cubicC_Hopf_classical_shadow : cubicC_Hopf (2 : R) = -2 := by
  unfold cubicC_Hopf; norm_num

/-- **Unknot-sector value at the classical point.** `C_unknot(2) = −2` — the
    identity sector coincidentally also equals `−2` at `y = 2`; recorded so the
    shadow match is not mis-read as Hopf-exclusive. The total is
    `C(2) = C_Hopf(2) + C_unknot(2) = −4` (`cubicC_two`). -/
theorem cubicC_unknot_classical : cubicC_unknot (2 : R) = -2 := by
  unfold cubicC_unknot; norm_num

/-! ## §8. Discriminants (upgrade of the KC20 symbolic-exact tier)

Registry row KC20 recorded the two discriminants — `disc C = −152 = −2³·19`
and `disc C_Hopf = −76 = −2²·19` — at symbolic-exact tier (witness, not
Lean). The certificates below close that gap: the coefficient readings tie
the generic monic-cubic discriminant to `cubicC` / `cubicC_Hopf`, the
evaluations are `norm_num`-exact over any `CommRing`, and the shared prime
`19` (the arithmetic fingerprint the two sectors have in common) is
certified over `ℤ`. -/

/-- Discriminant of a monic cubic `y³ + p·y² + q·y + r`. -/
def cubicDisc (p q r : R) : R :=
  18 * p * q * r - 4 * p ^ 3 * r + p ^ 2 * q ^ 2 - 4 * q ^ 3 - 27 * r ^ 2

/-- Coefficient reading of the total carrier cubic: `C = y³ − 4y² + 3y − 2`
    is monic with `(p, q, r) = (−4, 3, −2)`. -/
theorem cubicC_coeffs (y : R) :
    cubicC y = y ^ 3 + (-4) * y ^ 2 + 3 * y + (-2) := by
  unfold cubicC; ring

/-- Coefficient reading of the Hopf-sector cubic: `(p, q, r) = (−6, 10, −6)`. -/
theorem cubicC_Hopf_coeffs (y : R) :
    cubicC_Hopf y = y ^ 3 + (-6) * y ^ 2 + 10 * y + (-6) := by
  unfold cubicC_Hopf; ring

/-- **`disc C = −152`.** With the `cubicC_coeffs` reading, the discriminant
    of the total carrier cubic evaluates exactly. -/
theorem cubicC_disc : cubicDisc (-4 : R) 3 (-2) = -152 := by
  unfold cubicDisc; norm_num

/-- **`disc C_Hopf = −76`.** With the `cubicC_Hopf_coeffs` reading, the
    discriminant of the Hopf-sector cubic evaluates exactly. -/
theorem cubicC_Hopf_disc : cubicDisc (-6 : R) 10 (-6) = -76 := by
  unfold cubicDisc; norm_num

/-- **Shared prime `19`.** `−152 = −(2³·19)` and `−76 = −(2²·19)`: the two
    sector discriminants differ by a factor of `2` and share the prime `19` —
    the arithmetic fingerprint recorded in the 2026-07-07 audit, now
    certified over `ℤ`. -/
theorem disc_shared_prime_19 :
    (-152 : ℤ) = -(2 ^ 3 * 19) ∧ (-76 : ℤ) = -(2 ^ 2 * 19) := by
  norm_num

end QOU.QBeta.Zeta4Residue
