import QOU.BraidsAndKnots.NucleonWeightSpaceTraces

/-!
# Two exclusions for the neutron–proton splitting (Bridge B)

Setting as in `NucleonWeightSpaceTraces`: level-2 Jimbo braiding on `(C²)^{⊗3}`, `h = q - q⁻¹`,
proton-type weight space `(2,1)` and neutron-type weight space `(1,2)`.

**1. Signed braid words.** `NucleonWeightSpaceTraces.trace_word_eq` covers words in the positive
letters `σ₁, σ₂` only. The γγ nucleon word `V³ = (σ₁σ₂⁻¹)³` uses inverse letters. By the Hecke
relation `σ⁻¹ = σ - h`, so the intertwiner `P` also intertwines the inverse letters, and the plain
traces agree for every signed word (`trace_sword_eq`). The quantum trace restricted to the two
weight spaces then differs only by the pivot scalar: `q` on `(2,1)` and `q⁻¹` on `(1,2)`, so
`T_p = q² · T_n` for every braid word (`restrictedTrace_ratio`). The braid word contributes no
proton/neutron difference.

**2. Same/different-quark rules are blind to `u ↔ d`.** A rule that decorates each crossing using only
whether the two crossing quarks carry the same label produces the same decorated word for a labelling
and for its complement (`decorate_compl`). The proton `uud` and neutron `udd` labellings with the odd
quark on strand `k` are complements of each other (`proton_eq_compl_neutron`), so any such rule
gives them identical words, hence identical traces.

**3. General form.** The intertwiner `P` is `q⁻¹` times the block of the total lowering operator
`F₃` between the two weight spaces (`lowerBlock_eq`). So any pair of operators intertwined by `F₃`,
that is, the two weight blocks of any weight-preserving operator commuting with the quantum-group
lowering operator, has equal plain traces and restricted quantum traces in ratio `q²`
(`commutant_trace_eq`, `commutant_restrictedTrace_ratio`). Breaking `n = p` beyond the pivot needs
an operator that does not commute with `F₃`.

Scope: all three are scope-(b) exclusions inside this setting, resting on the intertwiner and on the
`u ↔ d` complement symmetry. No numerical value enters.
-/

namespace QOU.BraidsAndKnots.NucleonIsospinExclusions

open Matrix QOU.BraidsAndKnots.NucleonWeightSpaceTraces

variable {R : Type*} [Field R]

/-! ## 1. Signed words -/

/-- The inverse letter, from the Hecke relation `σ⁻¹ = σ - h`. -/
def inv (q : R) (X : Matrix (Fin 3) (Fin 3) R) : Matrix (Fin 3) (Fin 3) R := X - (q - q⁻¹) • 1

theorem A₁_mul_inv (q : R) (hq : q ≠ 0) : A₁ q * inv q (A₁ q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [inv, A₁, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp

theorem A₂_mul_inv (q : R) (hq : q ≠ 0) : A₂ q * inv q (A₂ q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [inv, A₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp

theorem B₁_mul_inv (q : R) (hq : q ≠ 0) : B₁ q * inv q (B₁ q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [inv, B₁, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp

theorem B₂_mul_inv (q : R) (hq : q ≠ 0) : B₂ q * inv q (B₂ q) = 1 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [inv, B₂, Matrix.mul_apply, Fin.sum_univ_three, Matrix.one_apply] <;> field_simp

/-- An intertwining relation passes to the inverse letters. -/
theorem intertwine_inv (q : R) {Pm X Y : Matrix (Fin 3) (Fin 3) R} (h : Pm * X = Y * Pm) :
    Pm * inv q X = inv q Y * Pm := by
  simp only [inv, Matrix.mul_sub, Matrix.sub_mul, Matrix.mul_smul, Matrix.smul_mul,
    Matrix.mul_one, Matrix.one_mul, h]

/-- A letter: generator (`true` = `σ₁`) and sign (`true` = positive). -/
abbrev Letter := Bool × Bool

/-- The matrix of one letter. -/
def letter (q : R) (X Y : Matrix (Fin 3) (Fin 3) R) : Letter → Matrix (Fin 3) (Fin 3) R
  | (g, s) => let M := if g then X else Y; if s then M else inv q M

/-- A signed braid word, evaluated on a pair of generator matrices. -/
def sword (q : R) (X Y : Matrix (Fin 3) (Fin 3) R) : List Letter → Matrix (Fin 3) (Fin 3) R
  | [] => 1
  | l :: w => letter q X Y l * sword q X Y w

theorem intertwine_letter (q : R) (hq : q ≠ 0) (l : Letter) :
    P q * letter q (A₁ q) (A₂ q) l = letter q (B₁ q) (B₂ q) l * P q := by
  obtain ⟨g, s⟩ := l
  cases g <;> cases s <;> simp only [letter, Bool.false_eq_true, if_false, if_true]
  · exact intertwine_inv q (intertwine₂ q hq)
  · exact intertwine₂ q hq
  · exact intertwine_inv q (intertwine₁ q hq)
  · exact intertwine₁ q hq

theorem intertwine_sword (q : R) (hq : q ≠ 0) (w : List Letter) :
    P q * sword q (A₁ q) (A₂ q) w = sword q (B₁ q) (B₂ q) w * P q := by
  induction w with
  | nil => simp [sword]
  | cons l w ih =>
    simp only [sword]
    rw [← mul_assoc, intertwine_letter q hq l, mul_assoc, ih, mul_assoc]

/-- **Equal plain traces for every signed braid word.** -/
theorem trace_sword_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    trace (sword q (A₁ q) (A₂ q) w) = trace (sword q (B₁ q) (B₂ q) w) := by
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  have key : sword q (B₁ q) (B₂ q) w = P q * sword q (A₁ q) (A₂ q) w * (P q)⁻¹ := by
    rw [intertwine_sword q hq w, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  rw [key, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hdet, one_mul]

/-- Proton-type restricted quantum trace: `K^{⊗3}` acts on `(2,1)` by the scalar `q`. -/
def Tp (q : R) (w : List Letter) : R := q * trace (sword q (A₁ q) (A₂ q) w)

/-- Neutron-type restricted quantum trace: `K^{⊗3}` acts on `(1,2)` by the scalar `q⁻¹`. -/
def Tn (q : R) (w : List Letter) : R := q⁻¹ * trace (sword q (B₁ q) (B₂ q) w)

/-- **The whole proton/neutron difference is the pivot.** For every signed braid word,
`T_p = q² · T_n`. -/
theorem restrictedTrace_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (w : List Letter) :
    Tp q w = q ^ 2 * Tn q w := by
  simp only [Tp, Tn, trace_sword_eq q hq hq2 w]
  field_simp

/-- The γγ nucleon word `V³ = (σ₁ σ₂⁻¹)³`. -/
def V3 : List Letter := [(true, true), (false, false), (true, true), (false, false),
  (true, true), (false, false)]

/-- The γγ nucleon word is an instance: its proton and neutron restricted traces differ by `q²`. -/
theorem V3_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) : Tp q V3 = q ^ 2 * Tn q V3 :=
  restrictedTrace_ratio q hq hq2 V3

/-! ## 2. Same/different-quark rules -/

/-- Decorate a list of crossings (pairs of quark identities, tracked through the braid) using a rule
that sees only whether the two quark labels agree. -/
def decorate {n : ℕ} {α : Type*} (rule : Bool → α) (l : Fin n → Bool)
    (crossings : List (Fin n × Fin n)) : List α :=
  crossings.map fun c => rule (decide (l c.1 = l c.2))

/-- Complementing every label leaves the decorated word unchanged. -/
theorem decorate_compl {n : ℕ} {α : Type*} (rule : Bool → α) (l : Fin n → Bool)
    (crossings : List (Fin n × Fin n)) :
    decorate rule (fun i => !l i) crossings = decorate rule l crossings := by
  simp [decorate]

/-- Proton labelling (`true` = u) with the odd quark `d` on strand `k`. -/
def proton (k : Fin 3) : Fin 3 → Bool := fun i => decide (i ≠ k)

/-- Neutron labelling with the odd quark `u` on strand `k`. -/
def neutron (k : Fin 3) : Fin 3 → Bool := fun i => decide (i = k)

theorem proton_eq_compl_neutron (k : Fin 3) : proton k = fun i => !neutron k i := by
  funext i; simp [proton, neutron]

/-- **Exclusion 2.** For every placement of the odd quark and every same/different rule, the
proton and neutron decorated words coincide. -/
theorem decorate_proton_eq_neutron {α : Type*} (rule : Bool → α) (k : Fin 3)
    (crossings : List (Fin 3 × Fin 3)) :
    decorate rule (proton k) crossings = decorate rule (neutron k) crossings := by
  rw [proton_eq_compl_neutron, decorate_compl]

/-! ## 3. The general no-go: anything commuting with the total lowering operator

`P` is not an ad hoc matrix. With the coproduct `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F` (the one that commutes
with the Jimbo `Ř`), the three-fold coproduct `F₃ = F⊗1⊗1 + K⁻¹⊗F⊗1 + K⁻¹⊗K⁻¹⊗F` maps the
proton-type weight space to the neutron-type one, and in the bases above its block is
`lowerBlock q = q • P q` (checked symbolically in
`computations/probes/bridge_b/h3_lowering_block_probe.py`, and proved here as `lowerBlock_eq`).

So the statement below is the general form of exclusions 1 and 2: **any** pair of weight-space
operators intertwined by the total lowering operator — that is, the two weight blocks of any
weight-preserving operator commuting with `F₃` — has the same plain trace on the two spaces, and
the restricted quantum traces differ by exactly the pivot factor `q²`. Braid words are one
instance (`intertwine_sword`). Breaking `n = p` beyond the pivot therefore needs an operator
that does not commute with `F₃`. -/

/-- The block of the total lowering operator `F₃` from the `(2,1)` to the `(1,2)` weight space. -/
def lowerBlock (q : R) : Matrix (Fin 3) (Fin 3) R := !![q⁻¹, 1, 0; 1, 0, 1; 0, 1, q]

theorem lowerBlock_eq (q : R) (hq : q ≠ 0) : lowerBlock q = q • P q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [lowerBlock, P] <;> field_simp

/-- **General no-go.** If the lowering block intertwines `X` (on the proton-type space) with `Y`
(on the neutron-type space), the plain traces agree. -/
theorem commutant_trace_eq (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    {X Y : Matrix (Fin 3) (Fin 3) R} (h : lowerBlock q * X = Y * lowerBlock q) :
    trace X = trace Y := by
  have hP : P q * X = Y * P q := by
    have h' : q • (P q * X) = q • (Y * P q) := by
      rw [← Matrix.smul_mul, ← Matrix.mul_smul, ← lowerBlock_eq q hq, h]
    exact smul_right_injective _ hq h'
  have hdet : IsUnit (P q).det := by
    rw [det_P q hq]
    exact isUnit_iff_ne_zero.mpr (div_ne_zero (neg_ne_zero.mpr hq2) (pow_ne_zero 4 hq))
  have key : Y = P q * X * (P q)⁻¹ := by
    rw [hP, mul_assoc, Matrix.mul_nonsing_inv _ hdet, mul_one]
  rw [key, Matrix.trace_mul_cycle, Matrix.nonsing_inv_mul _ hdet, one_mul]

/-- **General no-go, quantum-trace form.** For any such pair the restricted quantum traces differ
only by the pivot: `q · tr X = q² · (q⁻¹ · tr Y)`. -/
theorem commutant_restrictedTrace_ratio (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    {X Y : Matrix (Fin 3) (Fin 3) R} (h : lowerBlock q * X = Y * lowerBlock q) :
    q * trace X = q ^ 2 * (q⁻¹ * trace Y) := by
  rw [commutant_trace_eq q hq hq2 h]
  field_simp

/-- Braid words are an instance of the general no-go. -/
theorem lowerBlock_intertwine_sword (q : R) (hq : q ≠ 0) (w : List Letter) :
    lowerBlock q * sword q (A₁ q) (A₂ q) w = sword q (B₁ q) (B₂ q) w * lowerBlock q := by
  rw [lowerBlock_eq q hq, Matrix.smul_mul, Matrix.mul_smul, intertwine_sword q hq w]

end QOU.BraidsAndKnots.NucleonIsospinExclusions
