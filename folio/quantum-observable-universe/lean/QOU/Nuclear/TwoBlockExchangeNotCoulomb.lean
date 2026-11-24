import Mathlib.Data.Rat.Defs
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith

/-!
# Photon exchange between two nucleon blocks is not a charge–charge term

Pre-registered in
`computations/probes/np_splitting/np_two_block_photon_exchange_preregistration.md`; the exact
symbolic probe is `np_two_block_photon_exchange_probe.py` in the same directory.

Setup. Six strands carry the level-2 Jimbo braiding
`Ř = [[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]]`, `h = q − q⁻¹`, and `K = diag(q, q⁻¹)`, with
`u` = bit `0`. Block `A` is strands `0–2`, block `B` is strands `3–5`, and each carries the
ruled nucleon core `V³ = (σ_iσ_{i+1}⁻¹)³` (`i = 0` and `i = 3`). The block charge is
`Q = (number of u bits on the block) − 1`, so `p` has `Q = 1` and `n` has `Q = 0`. For an
insertion `X`,

`T_X(a, b) = Tr(K^{⊗6} · (Π_a ⊗ Π_b) · V_A³ V_B³ X)`,  `ΔE_X(a, b) = T_X(a, b)/T_1(a, b)`.

A Coulomb pair term is `ΔE_X(a, b) = c + κ·Q_a·Q_b`; then a neutral block feels only the
constant, so `ΔE_X(p, n) = ΔE_X(n, n)`. An isospin term `c + κ·W_aW_b`, `W = 2Q − 1`, forces
`ΔE_X(p, p) = ΔE_X(n, n)`.

What is proved. At `q = 2`, for each photon monomial that touches both blocks
(`σ₂`, `σ₂⁻¹`, `σ₁σ₂⁻¹`, `σ₂σ₃⁻¹`), neither form holds on the four nucleon pairs. A form that held
as an identity in `q` would hold at `q = 2`, so this refutes both identities; it says nothing
about the size of the miss at the proton `q₀` (the probe reports it there).

Arithmetic. At `q = 2` the matrices `2Ř`, `2Ř⁻¹` and `2K` are integral, so the traces are
computed exactly in `ℤ` by `decide` (kernel evaluation of the definitions below; no
`native_decide`). The scale factor `2^{6 + 12 + |X|}` is put back in `dE`.
-/

namespace QOU.QBeta.TwoBlockExchange

set_option maxRecDepth 100000

/-- Bit `k` of a six-strand basis state `s`; strand `0` is the most significant bit. -/
def bit (s k : ℕ) : ℕ := (s / 2 ^ (5 - k)) % 2

/-- `s` with strands `i, i+1` set to the two bits of `c = 2·b_i + b_{i+1}`. -/
def setPair (s i c : ℕ) : ℕ :=
  s - bit s i * 2 ^ (5 - i) - bit s (i + 1) * 2 ^ (4 - i)
    + (c / 2) * 2 ^ (5 - i) + (c % 2) * 2 ^ (4 - i)

/-- `2·Ř` at `q = 2` (`h = 3/2`), entry `(row, col)` on the basis `00, 01, 10, 11`. -/
def r2 : ℕ → ℕ → ℤ
  | 0, 0 => 4 | 1, 2 => 2 | 2, 1 => 2 | 2, 2 => 3 | 3, 3 => 4 | _, _ => 0

/-- `2·Ř⁻¹` at `q = 2`. -/
def r2i : ℕ → ℕ → ℤ
  | 0, 0 => 1 | 1, 1 => -3 | 1, 2 => 2 | 2, 1 => 2 | 3, 3 => 1 | _, _ => 0

/-- `(2Ř)(2Ř⁻¹) = 4`: the two tables are inverse up to the scale. -/
theorem r2_mul_r2i : ∀ i ∈ List.range 4, ∀ k ∈ List.range 4,
    ((List.range 4).map fun j => r2 i j * r2i j k).sum = if i = k then 4 else 0 := by decide

/-- A letter `(i, inv)`: `2σ_i` or `2σ_i⁻¹` on strands `i, i+1`. -/
def act (l : ℕ × Bool) (v : List ℤ) : List ℤ :=
  (List.range 64).map fun t =>
    let row := 2 * bit t l.1 + bit t (l.1 + 1)
    (List.range 4).foldl
      (fun acc c => acc + (if l.2 then r2i row c else r2 row c) * v.getD (setPair t l.1 c) 0) 0

/-- `W·v` for the word `W = g₁ g₂ ⋯ g_L` (list order). -/
def applyWord (w : List (ℕ × Bool)) (v : List ℤ) : List ℤ := w.foldr act v

/-- Basis vector `e_s`. -/
def e (s : ℕ) : List ℤ := (List.range 64).map fun t => if t = s then 1 else 0

/-- Number of `u` bits (zeros) on strands `lo, lo+1, lo+2`. -/
def zerosOn (s lo : ℕ) : ℕ := 3 - (bit s lo + bit s (lo + 1) + bit s (lo + 2))

/-- The two nucleon cores `V_A³ V_B³`, `V = σ_iσ_{i+1}⁻¹`. -/
def core : List (ℕ × Bool) :=
  [(0, false), (1, true), (0, false), (1, true), (0, false), (1, true),
   (3, false), (4, true), (3, false), (4, true), (3, false), (4, true)]

/-- `2^{6+12+|X|}·T_X(a, b)` at `q = 2`, with `a, b` the block charges plus one (`p ↦ 2`,
`n ↦ 1`), i.e. the number of `u` bits on each block. -/
def T (X : List (ℕ × Bool)) (za zb : ℕ) : ℤ :=
  ((List.range 64).filter fun s => zerosOn s 0 = za ∧ zerosOn s 3 = zb).foldl
    (fun acc s => acc + 4 ^ (zerosOn s 0 + zerosOn s 3) * (applyWord (core ++ X) (e s)).getD s 0) 0

/-- The pair shift `ΔE_X(a, b)` at `q = 2`, with `za, zb` the `u`-bit counts. -/
def dE (X : List (ℕ × Bool)) (za zb : ℕ) : ℚ :=
  (T X za zb : ℚ) / (2 ^ X.length * T [] za zb)

theorem T_one_pp : T [] 2 2 = 582932736 := by decide
theorem T_one_pn : T [] 2 1 = 145733184 := by decide
theorem T_one_np : T [] 1 2 = 145733184 := by decide
theorem T_one_nn : T [] 1 1 = 36433296 := by decide

/-- The insertion `σ₂`. -/
def X_s2 : List (ℕ × Bool) := [(2, false)]

theorem T_s2_pp : T X_s2 2 2 = 1635713024 := by decide
theorem T_s2_pn : T X_s2 2 1 = 667952128 := by decide
theorem T_s2_np : T X_s2 1 2 = 474667264 := by decide
theorem T_s2_nn : T X_s2 1 1 = 109282304 := by decide

/-- The insertion `σ₂⁻¹`. -/
def X_s2i : List (ℕ × Bool) := [(2, true)]

theorem T_s2i_pp : T X_s2i 2 2 = -113085184 := by decide
theorem T_s2i_pn : T X_s2i 2 1 = 230752576 := by decide
theorem T_s2i_np : T X_s2i 1 2 = 37467712 := by decide
theorem T_s2i_nn : T X_s2i 1 1 = -17584 := by decide

/-- The insertion `σ₁σ₂⁻¹ (photon on strands 1–3)`. -/
def X_s1s2i : List (ℕ × Bool) := [(1, false), (2, true)]

theorem T_s1s2i_pp : T X_s1s2i 2 2 = -143875072 := by decide
theorem T_s1s2i_pn : T X_s1s2i 2 1 = -110364416 := by decide
theorem T_s1s2i_np : T X_s1s2i 1 2 = -80716544 := by decide
theorem T_s1s2i_nn : T X_s1s2i 1 1 = 11688512 := by decide

/-- The insertion `σ₂σ₃⁻¹ (photon on strands 2–4)`. -/
def X_s2s3i : List (ℕ × Bool) := [(2, false), (3, true)]

theorem T_s2s3i_pp : T X_s2s3i 2 2 = 2660630528 := by decide
theorem T_s2s3i_pn : T X_s2s3i 2 1 = 1013641216 := by decide
theorem T_s2s3i_np : T X_s2s3i 1 2 = 751381504 := by decide
theorem T_s2s3i_nn : T X_s2s3i 1 1 = 175219712 := by decide

/-- A Coulomb pair term on the four nucleon pairs: `ΔE_X(a, b) = c + κ·Q_a·Q_b`,
with `Q = z − 1`. -/
def CoulombForm (X : List (ℕ × Bool)) : Prop :=
  ∃ c κ : ℚ, ∀ za ∈ [1, 2], ∀ zb ∈ [1, 2],
    dE X za zb = c + κ * ((za : ℚ) - 1) * ((zb : ℚ) - 1)

/-- An isospin pair term on the four nucleon pairs: `ΔE_X(a, b) = c + κ·W_a·W_b`,
`W = 2Q − 1`. -/
def IsospinForm (X : List (ℕ × Bool)) : Prop :=
  ∃ c κ : ℚ, ∀ za ∈ [1, 2], ∀ zb ∈ [1, 2],
    dE X za zb = c + κ * (2 * (za : ℚ) - 3) * (2 * (zb : ℚ) - 3)

/-- A Coulomb form forces `ΔE(p, n) = ΔE(n, n)`: the neutral block sees only the constant. -/
theorem pn_eq_nn_of_coulomb {X : List (ℕ × Bool)} (h : CoulombForm X) :
    dE X 2 1 = dE X 1 1 := by
  obtain ⟨c, κ, hc⟩ := h
  rw [hc 2 (by simp) 1 (by simp), hc 1 (by simp) 1 (by simp)]
  norm_num

/-- An isospin form forces `ΔE(p, p) = ΔE(n, n)` (charge symmetry). -/
theorem pp_eq_nn_of_isospin {X : List (ℕ × Bool)} (h : IsospinForm X) :
    dE X 2 2 = dE X 1 1 := by
  obtain ⟨c, κ, hc⟩ := h
  rw [hc 2 (by simp) 2 (by simp), hc 1 (by simp) 1 (by simp)]
  norm_num

theorem not_coulomb_s2 : ¬ CoulombForm X_s2 := by
  intro h
  have := pn_eq_nn_of_coulomb h
  simp only [dE, T_s2_pn, T_s2_nn, T_one_pn, T_one_nn] at this
  norm_num [X_s2] at this

theorem not_isospin_s2 : ¬ IsospinForm X_s2 := by
  intro h
  have := pp_eq_nn_of_isospin h
  simp only [dE, T_s2_pp, T_s2_nn, T_one_pp, T_one_nn] at this
  norm_num [X_s2] at this

theorem not_coulomb_s2i : ¬ CoulombForm X_s2i := by
  intro h
  have := pn_eq_nn_of_coulomb h
  simp only [dE, T_s2i_pn, T_s2i_nn, T_one_pn, T_one_nn] at this
  norm_num [X_s2i] at this

theorem not_isospin_s2i : ¬ IsospinForm X_s2i := by
  intro h
  have := pp_eq_nn_of_isospin h
  simp only [dE, T_s2i_pp, T_s2i_nn, T_one_pp, T_one_nn] at this
  norm_num [X_s2i] at this

theorem not_coulomb_s1s2i : ¬ CoulombForm X_s1s2i := by
  intro h
  have := pn_eq_nn_of_coulomb h
  simp only [dE, T_s1s2i_pn, T_s1s2i_nn, T_one_pn, T_one_nn] at this
  norm_num [X_s1s2i] at this

theorem not_isospin_s1s2i : ¬ IsospinForm X_s1s2i := by
  intro h
  have := pp_eq_nn_of_isospin h
  simp only [dE, T_s1s2i_pp, T_s1s2i_nn, T_one_pp, T_one_nn] at this
  norm_num [X_s1s2i] at this

theorem not_coulomb_s2s3i : ¬ CoulombForm X_s2s3i := by
  intro h
  have := pn_eq_nn_of_coulomb h
  simp only [dE, T_s2s3i_pn, T_s2s3i_nn, T_one_pn, T_one_nn] at this
  norm_num [X_s2s3i] at this

theorem not_isospin_s2s3i : ¬ IsospinForm X_s2s3i := by
  intro h
  have := pp_eq_nn_of_isospin h
  simp only [dE, T_s2s3i_pp, T_s2s3i_nn, T_one_pp, T_one_nn] at this
  norm_num [X_s2s3i] at this

/-! ### KZ monodromy (audit §28)

`β_AB = (σ₂σ₁σ₀)(σ₃σ₂σ₁)(σ₄σ₃σ₂)` carries block `A` across block `B`; `M = β_AB²` is the full
twist of one block around the other, i.e. the monodromy of the KZ connection. On the nucleon
pairs it gives the same shift for `pp` and `nn`, so it is not Coulomb (where `pp ≠ nn` would be
needed with `pn = nn`). Proved here at `q = 2`. -/

/-- The block crossing `β_AB` followed by itself. -/
def X_M : List (ℕ × Bool) :=
  [(2, false), (1, false), (0, false), (3, false), (2, false), (1, false),
   (4, false), (3, false), (2, false),
   (2, false), (1, false), (0, false), (3, false), (2, false), (1, false),
   (4, false), (3, false), (2, false)]

theorem T_M_pp : T X_M 2 2 = 141244912971546624 := by decide +kernel
theorem T_M_nn : T X_M 1 1 = 8827807060721664 := by decide +kernel

theorem dE_M_pp_eq_nn : dE X_M 2 2 = dE X_M 1 1 := by
  simp only [dE, T_M_pp, T_M_nn, T_one_pp, T_one_nn]
  norm_num [X_M]

/-- A Coulomb form needs `pp − nn = κ`; the monodromy therefore has no charge–charge term. -/
theorem M_coulomb_kappa_zero (c κ : ℚ) (hpp : dE X_M 2 2 = c + κ) (hnn : dE X_M 1 1 = c) :
    κ = 0 := by
  have := dE_M_pp_eq_nn
  rw [hpp, hnn] at this
  linarith

end QOU.QBeta.TwoBlockExchange
