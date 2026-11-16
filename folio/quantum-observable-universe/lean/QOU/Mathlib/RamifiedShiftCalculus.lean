import Mathlib.Tactic
import QOU.Brings.RamificationParityMonodromy
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.Mathlib.RamifiedShiftCalculus — shift-operator symbol calculus at a ramified pole

Infrastructure for walls **W1/W2** of
`docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md`: the
q-D-module symbol calculus at a simple ramification point `z = z_c + t²`, in the
coefficient model `f : ℤ → R` of a local Laurent expansion `Σ_e f(e) tᵉ` that
`QOU.Brings.RamificationParityMonodromy` already uses.

## The object

A **shift operator** is a pair (shift `k : ℤ`, multiplier `c : ℤ → R`):

  `shiftOp k c f = fun e => c e * f (e + k)`

— the coefficient at `tᵉ` is read from `t^{e+k}` with weight `c e`. Every
derivative-like operator on the chart is one of these:

| operator | shift `k` | multiplier `c e` | annihilates constants? |
|---|---|---|---|
| classical `d/dz = (1/2t) d/dt` (`ddz`) | 2 | `e + 2` | yes, `c(−2) = 0` |
| naive q-deformation of `d/dz` | 2 | `[e+2]_q` | yes, `[0]_q = 0` |
| Jackson `D_{q,t}` in the local coordinate | 1 | `[e+1]_q` | yes, `[0]_q = 0` |
| a zeroth-order / connection term | 0 or 1 | arbitrary | **no** when `c(−k) ≠ 0` |

The pair `(k, c)` *is* the operator's symbol on the punctured `t`-disk, and
symbols compose: `shiftOp k c ∘ shiftOp l d = shiftOp (k+l) (c · d(· + k))`
(`shiftOp_comp`). That composition law, with its iterate `shiftOp_iterate`, is
the calculus W2 asks for at the level of leading Laurent data.

## What it proves — the W1 prune

The keystone needs the jet tower to produce a **nonzero period** (residue at the
`t^{−2}` slot, since `λ = X^{(n)}·2t dt`) and to carry the **`(−1)^n` bar-parity
residual** (Door-v). Two exact necessary conditions on any single-shift
prolongation follow, with no reference to the C1 kernel coefficients (W3):

1. **Residue.** For a seed supported in `t`-degrees `≥ 0` (a power series — the
   colour-cubic branch is one), a shift-1 or shift-2 operator that **annihilates
   constants** (`c(−k) = 0`) has vanishing residue slot at every jet level
   (`residue_slot_zero_shift_two`, `residue_slot_zero_shift_one`). Every
   derivative — classical, or q-deformed in either q-integer convention, in `z`
   or in `t` — annihilates constants. So **no derivative-like prolongation of
   shift 1 or 2 can produce the binding period**; only a term with `c(−k) ≠ 0`,
   i.e. a genuine zeroth-order (connection-matrix) component, can.
2. **Parity.** An even shift commutes with the covering monodromy `t ↦ −t`; an
   **odd** shift anti-commutes (`shiftOp_anticomm_mono_of_odd`), so its jet
   tower's monodromy eigenvalue alternates as `(−1)^n`
   (`odd_shift_jet_monodromy_alternates`) — the positive counterpart to
   `classical_jet_monodromy_constant`. The `(−1)^n` residual therefore needs an
   **odd** shift component.

Together: the sought `D_q` must have an **odd shift** and a **non-derivative
component** that does not annihilate constants. Both are derived from the local
geometry of `Σ` (square-root branch ⇒ the coefficient model) and the two
measured target properties — never from the binding terms.

This does **not** construct `D_q` (W1 stays a wall) and does not identify its
symbol with C1 (W3 stays). It narrows the class exactly.

Ground ring: generic `[CommRing R]` throughout (§7c); `[Field R]` only where a
q-integer is instantiated.

## References

- [leitner2026] docs/audits/2026-07-20-zgeometric-prolongation-symbol-scoping.md
- [ramis-sauloy-zhang2013] q-difference formal classification / Stokes

LaTeX label: (library module — no content block)
-/

namespace QOU.Mathlib.RamifiedShiftCalculus

open QOU.Brings.RamificationParityMonodromy Finset

variable {R : Type*} [CommRing R]

/-! ## The symbol: shift operators and their composition -/

/-- **Shift operator** with shift `k` and multiplier `c`: the coefficient at `tᵉ`
is read from `t^{e+k}` with weight `c e`. The pair `(k, c)` is the operator's
symbol on the punctured `t`-disk. -/
def shiftOp (k : ℤ) (c : ℤ → R) (f : ℤ → R) : ℤ → R := fun e => c e * f (e + k)

/-- The corpus's `shift2` is the shift-2 member. -/
theorem shift2_eq_shiftOp (c f : ℤ → R) : shift2 c f = shiftOp 2 c f := by
  funext e; simp [shift2, shiftOp, smul_eq_mul]

/-- The classical prolongation `d/dz` is shift 2 with multiplier `e + 2`. -/
theorem ddz_eq_shiftOp (f : ℤ → R) : ddz f = shiftOp 2 (fun e => ((e + 2 : ℤ) : R)) f :=
  shift2_eq_shiftOp _ f

/-- **Symbols compose**: shifts add, multipliers multiply along the shift. -/
theorem shiftOp_comp (k l : ℤ) (c d : ℤ → R) (f : ℤ → R) :
    shiftOp k c (shiftOp l d f) = shiftOp (k + l) (fun e => c e * d (e + k)) f := by
  funext e
  simp only [shiftOp]
  rw [add_assoc]
  ring

/-- Linearity in the seed. -/
theorem shiftOp_smul (k : ℤ) (c : ℤ → R) (r : R) (f : ℤ → R) :
    shiftOp k c (r • f) = r • shiftOp k c f := by
  funext e; simp only [shiftOp, Pi.smul_apply, smul_eq_mul]; ring

theorem shiftOp_neg (k : ℤ) (c : ℤ → R) (f : ℤ → R) :
    shiftOp k c (-f) = -shiftOp k c f := by
  funext e; simp [shiftOp]

/-- **The iterate**: `n` applications read the coefficient from `e + n·k` with the
product of the multipliers met along the way. -/
theorem shiftOp_iterate (k : ℤ) (c : ℤ → R) (f : ℤ → R) (n : ℕ) (e : ℤ) :
    (shiftOp k c)^[n] f e = (∏ i ∈ range n, c (e + (i : ℤ) * k)) * f (e + (n : ℤ) * k) := by
  induction n generalizing e with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    show c e * (shiftOp k c)^[n] f (e + k) = _
    rw [ih, prod_range_succ']
    have hf : e + k + (n : ℤ) * k = e + ((n + 1 : ℕ) : ℤ) * k := by push_cast; ring
    have hp : ∏ i ∈ range n, c (e + k + (i : ℤ) * k)
        = ∏ i ∈ range n, c (e + ((i + 1 : ℕ) : ℤ) * k) := by
      apply prod_congr rfl; intro i _; congr 1; push_cast; ring
    rw [hf, hp]
    simp only [Nat.cast_zero, zero_mul, add_zero]
    ring

/-! ## The residue slot -/

/-- The residue of `X^{(n)} · 2t dt` sits at `t^{−2}`; a single shift reads it from
`t^{k−2}` with weight `c(−2)`. -/
theorem shiftOp_residue_slot (k : ℤ) (c : ℤ → R) (f : ℤ → R) :
    shiftOp k c f (-2) = c (-2) * f (-2 + k) := rfl

/-- A seed with no negative `t`-powers — a power series, which the colour-cubic
branch `X(t)` is. -/
def PowerSeriesSupported (f : ℤ → R) : Prop := ∀ e : ℤ, e < 0 → f e = 0

/-- **Annihilating constants** is the property `c(−k) = 0`: the constant term
`t⁰` (`monomialCoeff 0`) lands at slot `−k` with weight `c(−k)`. Every derivative
has it; a zeroth-order term does not. -/
def AnnihilatesConstants (k : ℤ) (c : ℤ → R) : Prop := c (-k) = 0

theorem shiftOp_monomial_zero_apply (k : ℤ) (c : ℤ → R) :
    shiftOp k c (monomialCoeff 0) (-k) = c (-k) := by
  simp [shiftOp, monomialCoeff]

theorem shiftOp_monomial_zero_off (k : ℤ) (c : ℤ → R) (e : ℤ) (he : e ≠ -k) :
    shiftOp k c (monomialCoeff 0) e = 0 := by
  have : e + k ≠ 0 := by omega
  simp [shiftOp, monomialCoeff, this]

/-- The characterisation: the operator kills the constant term iff `c(−k) = 0`. -/
theorem annihilatesConstants_iff (k : ℤ) (c : ℤ → R) :
    AnnihilatesConstants k c ↔ shiftOp k c (monomialCoeff 0) = 0 := by
  constructor
  · intro h; funext e
    by_cases he : e = -k
    · subst he; simpa [shiftOp_monomial_zero_apply] using h
    · exact shiftOp_monomial_zero_off k c e he
  · intro h
    simpa [AnnihilatesConstants, shiftOp_monomial_zero_apply] using congrFun h (-k)

/-! ## The W1 prune: derivative-like shift-1 / shift-2 operators cannot produce a residue -/

/-- **Shift 2.** If `c(−2) = 0` the residue slot is dead at every jet level `n ≥ 1`,
for **every** seed: the `i = 0` factor of the iterate product is `c(−2)`. This is
the classical `d/dz` and every q-deformation of its multiplier. -/
theorem residue_slot_zero_shift_two (c : ℤ → R) (hc : AnnihilatesConstants 2 c)
    (f : ℤ → R) (n : ℕ) (hn : 0 < n) :
    (shiftOp 2 c)^[n] f (-2) = 0 := by
  rw [shiftOp_iterate]
  have h0 : c (-2 + ((0 : ℕ) : ℤ) * 2) = 0 := by simpa [AnnihilatesConstants] using hc
  rw [prod_eq_zero (mem_range.mpr hn) h0, zero_mul]

/-- **Shift 1.** If `c(−1) = 0` and the seed is a power series, the residue slot is
dead at every jet level: at `n = 0, 1` the seed's own support kills it, and for
`n ≥ 2` the `i = 1` factor is `c(−1)`. This is the Jackson operator in the local
coordinate and every derivative-like shift-1 operator. -/
theorem residue_slot_zero_shift_one (c : ℤ → R) (hc : AnnihilatesConstants 1 c)
    (f : ℤ → R) (hf : PowerSeriesSupported f) (n : ℕ) :
    (shiftOp 1 c)^[n] f (-2) = 0 := by
  rw [shiftOp_iterate]
  rcases n with _ | _ | n
  · simp [hf (-2) (by norm_num)]
  · simp [hf (-1) (by norm_num)]
  · have h1 : c (-2 + ((1 : ℕ) : ℤ) * 1) = 0 := by simpa [AnnihilatesConstants] using hc
    rw [prod_eq_zero (mem_range.mpr (by omega : 1 < n + 2)) h1, zero_mul]

/-! ## Instantiations: the naive q-deformations all annihilate constants -/

section QDeformed
variable {K : Type*} [Field K]
open QOU.QInteger

/-- The naive q-deformation of `d/dz`: keep shift 2, replace the multiplier
`e + 2` by the canonical balanced q-integer `[e+2]_q`. -/
noncomputable def qddz (q : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 2 (fun e => qIntBalZ q (e + 2)) f

/-- The Jackson q-derivative in the local coordinate `t`: shift 1, multiplier `[e+1]_q`. -/
noncomputable def jacksonT (q : K) (f : ℤ → K) : ℤ → K :=
  shiftOp 1 (fun e => qIntBalZ q (e + 1)) f

theorem qddz_annihilatesConstants (q : K) :
    AnnihilatesConstants 2 (fun e : ℤ => qIntBalZ q (e + 2)) := by
  simp [AnnihilatesConstants]

theorem jacksonT_annihilatesConstants (q : K) :
    AnnihilatesConstants 1 (fun e : ℤ => qIntBalZ q (e + 1)) := by
  simp [AnnihilatesConstants]

/-- **q-deforming `d/dz` does not rescue the residue**, for any `q`. -/
theorem qddz_residue_slot_zero (q : K) (f : ℤ → K) (n : ℕ) (hn : 0 < n) :
    (qddz q)^[n] f (-2) = 0 :=
  residue_slot_zero_shift_two _ (qddz_annihilatesConstants q) f n hn

/-- **Nor does the Jackson operator in the local coordinate**, on a power-series seed. -/
theorem jacksonT_residue_slot_zero (q : K) (f : ℤ → K) (hf : PowerSeriesSupported f) (n : ℕ) :
    (jacksonT q)^[n] f (-2) = 0 :=
  residue_slot_zero_shift_one _ (jacksonT_annihilatesConstants q) f hf n

end QDeformed

/-! ## Parity: odd shifts anti-commute with the covering monodromy -/

theorem shiftOp_comm_mono_of_even (k : ℤ) (hk : Even k) (c f : ℤ → R) :
    shiftOp k c (mono f) = mono (shiftOp k c f) := by
  funext e
  simp only [shiftOp, mono]
  have : Even (e + k) ↔ Even e := by
    rw [Int.even_add]; exact ⟨fun h => h.mpr hk, fun h => ⟨fun _ => hk, fun _ => h⟩⟩
  by_cases h : Even e
  · rw [if_pos h, if_pos (this.mpr h)]
  · rw [if_neg h, if_neg (fun hh => h (this.mp hh))]; ring

/-- **An odd shift anti-commutes with `t ↦ −t`**: it swaps the bar-even and bar-odd
sectors. -/
theorem shiftOp_anticomm_mono_of_odd (k : ℤ) (hk : Odd k) (c f : ℤ → R) :
    shiftOp k c (mono f) = -mono (shiftOp k c f) := by
  funext e
  simp only [shiftOp, mono, Pi.neg_apply]
  have hke : Even (e + k) ↔ ¬ Even e := by
    rw [Int.even_add, ← Int.not_odd_iff_even (n := k)]
    constructor
    · intro h he; exact (h.mp he) hk
    · intro h; exact ⟨fun he => absurd he h, fun hk' => absurd hk hk'⟩
  by_cases h : Even e
  · rw [if_pos h, if_neg (fun hh => (hke.mp hh) h)]; ring
  · rw [if_neg h, if_pos (hke.mpr h)]; ring

/-- **The positive counterpart to `classical_jet_monodromy_constant`.** Under an
odd-shift prolongation, a fixed-parity seed's monodromy eigenvalue alternates as
`(−1)^n ε` along the jet tower — exactly the Door-v `(−1)^n` residual. So carrying
that residual requires an **odd** shift component. -/
theorem odd_shift_jet_monodromy_alternates (k : ℤ) (hk : Odd k) (c : ℤ → R)
    (X : ℤ → R) (ε : R) (hX : mono X = ε • X) (n : ℕ) :
    mono ((shiftOp k c)^[n] X) = ((-1 : R) ^ n * ε) • (shiftOp k c)^[n] X := by
  induction n with
  | zero => simpa using hX
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    have h := shiftOp_anticomm_mono_of_odd k hk c ((shiftOp k c)^[n] X)
    rw [ih, shiftOp_smul] at h
    -- h : ((-1)^n * ε) • shiftOp k c (iter) = - mono (shiftOp k c (iter))
    have : mono (shiftOp k c ((shiftOp k c)^[n] X))
        = -(((-1 : R) ^ n * ε) • shiftOp k c ((shiftOp k c)^[n] X)) := by
      rw [h, neg_neg]
    rw [this, ← neg_smul]
    congr 1
    ring

/-! ## Non-vacuity: an operator that does NOT annihilate constants does produce a residue -/

/-- A shift-1 operator with a nonzero zeroth-order weight reaches the residue slot
from the constant term in two steps with weight `c(−2)·c(−1)`; with `c ≡ 1` that is
`1`. So the prune is a statement about derivative-*like* operators, not about all
of them — which is the whole point. -/
theorem constant_weight_shift_one_residue (f : ℤ → R) :
    (shiftOp 1 (fun _ => (1 : R)))^[2] f (-2) = f 0 := by
  rw [shiftOp_iterate]; norm_num

/-- **Additivity of `shiftOp` in the Laurent series seed.** -/
theorem shiftOp_add (k : ℤ) (c : ℤ → R) (f g : ℤ → R) :
    shiftOp k c (f + g) = shiftOp k c f + shiftOp k c g := by
  funext e
  have hfg : (f + g) (e + k) = f (e + k) + g (e + k) := rfl
  show c e * (f + g) (e + k) = c e * f (e + k) + c e * g (e + k)
  rw [hfg, mul_add]

/-- **Under an even-shift prolongation, a fixed-parity seed retains its monodromy
eigenvalue `ε` at every jet level `n`.** -/
theorem even_shift_jet_monodromy_invariant (k : ℤ) (hk : Even k) (c : ℤ → R)
    (X : ℤ → R) (ε : R) (hX : mono X = ε • X) (n : ℕ) :
    mono ((shiftOp k c)^[n] X) = ε • (shiftOp k c)^[n] X := by
  induction n with
  | zero => simpa using hX
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    rw [← shiftOp_comm_mono_of_even k hk c ((shiftOp k c)^[n] X)]
    rw [ih, shiftOp_smul]

/-- **General two-step shift-1 residue formula**: two applications of `shiftOp 1 c`
read the residue slot `t⁻²` from the constant term `f 0` with weight `c(-2) · c(-1)`. -/
theorem shift_one_two_step_residue_eq (c : ℤ → R) (f : ℤ → R) :
    (shiftOp 1 c)^[2] f (-2) = c (-2) * c (-1) * f 0 := by
  rw [shiftOp_iterate]
  rw [prod_range_succ, prod_range_one]
  norm_num
  ring

end QOU.Mathlib.RamifiedShiftCalculus
