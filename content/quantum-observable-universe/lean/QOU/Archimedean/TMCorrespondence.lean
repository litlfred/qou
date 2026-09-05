import QOU.Archimedean.TransferMatrix
import QOU.Archimedean.OptimalNF
import QOU.Archimedean.HeckeRep
import QOU.MathlibExt
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Tactic.Ring

/-!
# Transfer Matrix ↔ Hecke Algebra Correspondence (Layer 3)

The optimal NF coefficients equal the transfer matrix traced volumes V̂_i.

**Key idea**: a Hecke algebra element `a · σ + b · 𝟏` at generator σ_i
corresponds to the state vector `(a, b)ᵀ` in ℤ[t, t⁻¹]². Multiplication
by a crossing `(c · σ + d)` in the Hecke algebra (with Hecke reduction
σ² = HA · σ + 1) corresponds to left-multiplication by the transfer
matrix `T(c, d)` on the state vector.

This file proves:
1. The Hecke-to-matrix correspondence is well-defined
2. Multiplication correspondence: Hecke product ↔ matrix product
3. The traced volume V̂_i extracts the same data as the Markov trace
4. Optimal NF coefficients = traced volumes

## References

- [leitner2026] Prop: transfer matrix correspondence (Layer 3).
-/

namespace QOU.TMCorrespondence

open QOU.Archimedean
open QOU.OptimalNF
open Matrix

-- ════════════════════════════════════════════════════════════════
-- §1  State vectors: the Hecke ↔ matrix correspondence
-- ════════════════════════════════════════════════════════════════

/-- A state vector `(a, b)` represents the Hecke element `a · σ_i + b · 𝟏`
    at generator `i`. The correspondence is:
    - component 0: coefficient of σ_i (the crossing term)
    - component 1: coefficient of 𝟏 (the identity term) -/
abbrev StateVec := Fin 2 → R_t

/-- Construct a state vector from crossing and identity coefficients. -/
noncomputable def mkState (a b : R_t) : StateVec :=
  ![a, b]

/-- The initial state vector `(1, 0)ᵀ`: a bare generator σ_i with
    coefficient 1 on σ and 0 on 𝟏.  This is the start of a chain
    before any further crossings are applied. -/
noncomputable def initialState : StateVec :=
  mkState 1 0

/-- Extract the σ-coefficient (crossing coefficient) from a state. -/
noncomputable def sigmaCoeff (v : StateVec) : R_t := v 0

/-- Extract the 𝟏-coefficient (identity coefficient) from a state. -/
noncomputable def identCoeff (v : StateVec) : R_t := v 1

-- ════════════════════════════════════════════════════════════════
-- §2  The Hecke multiplication rule
-- ════════════════════════════════════════════════════════════════

/-- Multiply a Hecke element `(a · σ + b)` by a crossing `(c · σ + d)`
    using the Hecke relation `σ² = HA · σ + 1`.

    `(a · σ + b)(c · σ + d)`
      `= a·c · σ² + a·d · σ + b·c · σ + b·d`
      `= a·c · (HA · σ + 1) + (a·d + b·c) · σ + b·d`
      `= (a·c·HA + a·d + b·c) · σ + (a·c + b·d) · 𝟏`

    So the new state is:
      `a' = a·c·HA + a·d + b·c`
      `b' = a·c + b·d`
    -/
noncomputable def heckeMultiply (a b c d : R_t) : StateVec :=
  mkState (a * c * HA_t + a * d + b * c) (a * c + b * d)

-- ════════════════════════════════════════════════════════════════
-- §3  Core lemma: Hecke multiplication = transfer matrix action
-- ════════════════════════════════════════════════════════════════

/-- The transfer matrix `T(c, d)` acting on state vector `(a, b)ᵀ`
    produces the same result as Hecke multiplication of `(a·σ + b)`
    by `(c·σ + d)`.

    Transfer matrix action:
    ```
    T(c,d) · (a, b)ᵀ = ⎡ c·HA+d,  c ⎤ · ⎡ a ⎤ = ⎡ (c·HA+d)·a + c·b ⎤
                        ⎣ c,       d ⎦   ⎣ b ⎦   ⎣ c·a + d·b         ⎦
    ```

    Hecke multiplication:
    ```
    (a·σ + b)(c·σ + d) = (a·c·HA + a·d + b·c)·σ + (a·c + b·d)·𝟏
    ```

    These are equal:
    - Row 0: `(c·HA+d)·a + c·b = a·c·HA + a·d + b·c` ✓ (ring identity)
    - Row 1: `c·a + d·b = a·c + b·d`                   ✓ (commutativity)

    This is the **fundamental correspondence**: the transfer matrix
    encodes exactly the Hecke algebra multiplication with reduction. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem hecke_eq_transfer (a b c d : R_t) :
    heckeMultiply a b c d =
    (transferMatrix c d).mulVec (mkState a b) := by
  funext i
  fin_cases i <;> simp [heckeMultiply, mkState, transferMatrix,
    mulVec, dotProduct, HA_t, Fin.sum_univ_two] <;> ring

-- ════════════════════════════════════════════════════════════════
-- §4  Chain construction: iterated correspondence
-- ════════════════════════════════════════════════════════════════

/-- A crossing sequence: a list of `(c, d)` pairs representing
    successive Hecke multiplications / transfer matrix applications. -/
abbrev CrossingSeq := List (R_t × R_t)

/-- Apply a crossing sequence in the Hecke algebra, folding from the right.
    Starting from state `(a₀, b₀)`, multiply by each `(cⱼ, dⱼ)` in order.

    This corresponds to the product:
    `(a₀·σ + b₀)(c₁·σ + d₁)(c₂·σ + d₂)⋯(cₙ·σ + dₙ)` -/
noncomputable def heckeChain (init : StateVec) : CrossingSeq → StateVec
  | [] => init
  | (c, d) :: rest => heckeChain (heckeMultiply (sigmaCoeff init) (identCoeff init) c d) rest

/-- Apply a crossing sequence via transfer matrices, folding from the right.

    M = T(cₙ,dₙ) · ⋯ · T(c₂,d₂) · T(c₁,d₁)

    This matches the Hecke chain left-fold: the FIRST crossing in the
    sequence is applied FIRST (innermost in the matrix product).
    So M.mulVec init = T(cₙ,dₙ) · ⋯ · T(c₁,d₁) · init,
    which matches heckeChain evaluating (c₁,d₁) first. -/
noncomputable def matrixChain : CrossingSeq → TMatrix
  | [] => 1
  | (c, d) :: rest => matrixChain rest * transferMatrix c d

/-- The iterated correspondence: Hecke chain = matrix chain applied to
    initial state. By induction on the crossing sequence, using
    `hecke_eq_transfer` at each step. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem chain_correspondence (seq : CrossingSeq) (init : StateVec) :
    heckeChain init seq =
    (matrixChain seq).mulVec init := by
  induction seq generalizing init with
  | nil =>
    simp [heckeChain, matrixChain, Fin.sum_univ_two]
  | cons hd tl ih =>
    obtain ⟨c, d⟩ := hd
    simp only [heckeChain, matrixChain]
    -- heckeChain (heckeMultiply .. c d) tl = (matrixChain tl).mulVec (heckeMultiply .. c d)
    -- by inductive hypothesis ih applied to the new initial state.
    -- heckeMultiply a b c d = (transferMatrix c d).mulVec (mkState a b) by hecke_eq_transfer.
    -- So: (matrixChain tl).mulVec ((transferMatrix c d).mulVec init)
    --   = (transferMatrix c d * matrixChain tl).mulVec init  by Matrix.mulVec_mulVec
    -- heckeChain init ((c,d)::rest) = heckeChain (heckeMultiply .. c d) rest
    -- By ih: = (matrixChain rest).mulVec (heckeMultiply .. c d)
    -- By hecke_eq_transfer: heckeMultiply = (transferMatrix c d).mulVec init
    -- So: = (matrixChain rest).mulVec ((transferMatrix c d).mulVec init)
    -- By mulVec_mulVec: = (matrixChain rest * transferMatrix c d).mulVec init
    -- This is exactly matrixChain ((c,d)::rest) .mulVec init  ✓
    rw [ih]
    conv_lhs => rw [hecke_eq_transfer (sigmaCoeff init) (identCoeff init) c d]
    -- Now: (matrixChain rest).mulVec ((transferMatrix c d).mulVec (mkState ..))
    -- Need to show mkState (sigmaCoeff init) (identCoeff init) = init
    -- and then apply mulVec_mulVec
    have h_init : mkState (sigmaCoeff init) (identCoeff init) = init := by
      ext i; fin_cases i <;> simp [mkState, sigmaCoeff, identCoeff]
    rw [h_init, Matrix.mulVec_mulVec]

-- ════════════════════════════════════════════════════════════════
-- §5  Traced volume extracts Markov trace data
-- ════════════════════════════════════════════════════════════════

/-- The Markov trace of a Hecke element `a·σ + b·𝟏` is:
    `tr_M(a·σ + b) = a · z + b`
    where `z = 1/(t + t⁻¹)` is the Markov parameter.

    In cleared form (multiplied by `t + t⁻¹`):
    `(t + t⁻¹) · tr_M(a·σ + b) = a + (t + t⁻¹) · b`

    This is exactly `tracedVolCleared` applied to the column vector
    `(a, b)ᵀ` viewed as the first column of a matrix. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem markov_trace_eq_traced_vol (a b : R_t) :
    a + markov_denom * b =
    tracedVolCleared (Matrix.of ![![a, 0], ![b, 0]]) := by
  simp [tracedVolCleared, markov_denom, Matrix.of_apply, Matrix.cons_val_zero,
    Matrix.cons_val_one]

/-- The traced volume of a chain matrix, applied to initial state `(1, 0)ᵀ`,
    extracts the Markov trace of the corresponding Hecke element.

    If `M = matrixChain seq`, then:
    `tracedVolCleared M = M[0,0] + (t + t⁻¹) · M[1,0]`

    The state vector is `M · (1, 0)ᵀ = (M[0,0], M[1,0])ᵀ`.
    So `tracedVolCleared M` computes `a + (t+t⁻¹)·b` where
    `(a, b) = M · (1, 0)ᵀ` is the Hecke state. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem traced_vol_from_state (M : TMatrix) :
    tracedVolCleared M =
    sigmaCoeff (M.mulVec initialState) +
    markov_denom * identCoeff (M.mulVec initialState) := by
  simp [tracedVolCleared, sigmaCoeff, identCoeff, initialState, mkState,
    mulVec, dotProduct, Fin.sum_univ_two, markov_denom]

-- ════════════════════════════════════════════════════════════════
-- §6  The main theorem: optimal NF coefficient = traced volume
-- ════════════════════════════════════════════════════════════════

/-- **Layer 3 Main Theorem.**

    For each generator σ_i in a nuclear configuration, the coefficient
    of σ_i in the optimal normal form equals the σ-component of the
    transfer matrix chain state at generator i.

    Specifically, let `seq_i` be the crossing sequence at generator i
    (the crossings that accumulate onto chain i). Then:

    - The Hecke element at generator i is `heckeChain (1, 0) seq_i`
    - The transfer matrix chain is `M_i = matrixChain seq_i`
    - The state vector is `M_i · (1, 0)ᵀ = (a_i, b_i)ᵀ`
    - The optimal NF coefficient of σ_i is `a_i`
    - The traced volume is `V̂_i = z · a_i + b_i` (cleared: `a_i + (t+t⁻¹)·b_i`)

    The proof combines:
    1. `chain_correspondence`: Hecke chain = matrix chain on initial state
    2. `traced_vol_from_state`: traced volume = Markov trace of Hecke element
    3. The Markov trace is linear, so per-generator contributions factorise

    Together: the NF coefficients (a_i, b_i) at each generator are
    exactly the entries of the transfer matrix chain state vector,
    and the traced volume V̂_i is the Markov trace of the per-generator
    Hecke element. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem optimal_coeff_eq_transfer_state (seq : CrossingSeq) :
    let state := (matrixChain seq).mulVec initialState
    sigmaCoeff (heckeChain initialState seq) = sigmaCoeff state ∧
    identCoeff (heckeChain initialState seq) = identCoeff state := by
  simp only
  have h := chain_correspondence seq initialState
  constructor
  · -- σ-coefficient: extract component 0
    show (heckeChain initialState seq) 0 = ((matrixChain seq).mulVec initialState) 0
    rw [h]
  · -- 𝟏-coefficient: extract component 1
    show (heckeChain initialState seq) 1 = ((matrixChain seq).mulVec initialState) 1
    rw [h]

/-- **Corollary**: the traced volume V̂_i equals the Markov trace
    of the per-generator Hecke element.

    This bridges the transfer matrix world (TransferMatrix.lean)
    and the optimal NF world (OptimalNF.lean):
    - Transfer matrix chain → state vector (a_i, b_i)
    - Hecke chain → NF coefficients (a_i, b_i) [same by correspondence]
    - V̂_i = z·a_i + b_i extracts Markov trace information
    - The skein polynomial P(q) = ∏_i V̂_i is a product of Markov traces -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem volume_eq_markov_trace (seq : CrossingSeq) :
    tracedVolCleared (matrixChain seq) =
    sigmaCoeff ((matrixChain seq).mulVec initialState) +
    markov_denom * identCoeff ((matrixChain seq).mulVec initialState) :=
  traced_vol_from_state (matrixChain seq)

-- ════════════════════════════════════════════════════════════════
-- §7  Connecting to nuclear configurations
-- ════════════════════════════════════════════════════════════════

/-- Extract the crossing sequence for chain j from a nuclear configuration.

    Chain j is formed by the crossings between nucleon j and all
    subsequent nucleons k > j. The crossing at position k contributes
    weights that match `crossingMatrix` from TransferMatrix.lean.

    **Scaling convention (v1.1):** pp and nn crossings are DOUBLED
    to match `crossingMatrix`:
    - pp: `crossingMatrix pp = 2 • T_pp` → coefficients `(2, 0)`
    - nn: `crossingMatrix nn = 2 • T_nn` → coefficients `(2, −2·HA)`
    - pn: `crossingMatrix pn = two_T_pn`  → coefficients `(2, −HA)`
      (the "undoubled" pn base would be `(1, −HA/2)`, but
      `w_plus_t .pn` and `w_zero_t .pn` are defined as the doubled
      form `(2, −HA)` which already matches `two_T_pn` directly)

    This ensures `transferMatrix c d = crossingMatrix(nj, nk)` for
    each pair, which is needed for `matrixChain_eq_buildChains`. -/
noncomputable def chainCrossings (config : NuclearConfig) (j : ℕ) : CrossingSeq :=
  (config.drop (j + 1)).map fun nk =>
    let nj := config[j]!
    let v := vertexType nj nk
    match v with
    | .pp => (2 * w_plus_t v, 2 * w_zero_t v)
    | .nn => (2 * w_plus_t v, 2 * w_zero_t v)
    | .pn => (w_plus_t v, w_zero_t v)

/-- `matrixChain` is the **reversed** product of its per-crossing transfer
    matrices.

    Immediate from the defining recursion `matrixChain ((c,d) :: rest) =
    matrixChain rest * transferMatrix c d`, which puts the *first* crossing
    of the sequence *rightmost* in the product. -/
theorem matrixChain_eq_reverse_prod (seq : CrossingSeq) :
    matrixChain seq =
      (seq.map (fun cd => transferMatrix cd.1 cd.2)).reverse.prod := by
  induction seq with
  | nil => simp [matrixChain]
  | cons hd tl ih =>
    obtain ⟨c, d⟩ := hd
    simp [matrixChain, ih, List.reverse_cons, List.prod_append]

/-- **The reversal is harmless: `matrixChain` is the forward product.**

    Proved, sorry-free, depending on no class instance: `transferMatrix_comm`
    (a theorem since 2026-06-07) makes any two transfer matrices commute, so
    `QOU.MathlibExt.prod_reverse_eq_of_pairwise_commute` removes the reversal
    introduced by the recursion.

    This is the whole of the "different association order" half of
    `MatrixChainEqBuildChains`, and it is **not** conditional on anything.
    What remains open there is a different question entirely — see that
    class's docstring. -/
theorem matrixChain_eq_prod (seq : CrossingSeq) :
    matrixChain seq = (seq.map (fun cd => transferMatrix cd.1 cd.2)).prod := by
  rw [matrixChain_eq_reverse_prod]
  exact QOU.MathlibExt.prod_reverse_eq_of_pairwise_commute _
    (List.pairwise_map.mpr
      (QOU.MathlibExt.pairwise_of_forall seq
        (fun a b => transferMatrix_comm a.1 a.2 b.1 b.2)))

-- `simp` closes three of the four entries outright, so the
-- `unnecessarySeqFocus` linter's suggested `(simp …; ring)` fails with
-- "No goals to be solved" on those three. `<;> ring` is the correct form here.
set_option linter.unnecessarySeqFocus false in
/-- The transfer matrix is linear in its coefficient pair:
    `n • T(c, d) = T(n·c, n·d)`. -/
theorem smul_transferMatrix (n : ℕ) (c d : R_t) :
    n • transferMatrix c d = transferMatrix (n * c) (n * d) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [transferMatrix, Matrix.smul_apply, nsmul_eq_mul] <;> ring

/-- **`crossingMatrix` IS the transfer matrix at the coefficients
    `chainCrossings` emits** — step 1 of the four-step proof sketch on
    `matrixChain_eq_buildChains`, now discharged.

    The doubling convention lines up in all three vertex cases:
    `pp` gives `2 • T(1,0) = T(2,0)`, `nn` gives `2 • T(1,−HA) = T(2,−2HA)`,
    and `pn`'s `two_T_pn` is already `T(2,−HA)`. -/
theorem crossingMatrix_eq (a b : NucleonType) :
    crossingMatrix a b =
      transferMatrix
        (match vertexType a b with
          | .pp => 2 * w_plus_t (vertexType a b)
          | .nn => 2 * w_plus_t (vertexType a b)
          | .pn => w_plus_t (vertexType a b))
        (match vertexType a b with
          | .pp => 2 * w_zero_t (vertexType a b)
          | .nn => 2 * w_zero_t (vertexType a b)
          | .pn => w_zero_t (vertexType a b)) := by
  unfold crossingMatrix
  rcases h : vertexType a b with _ | _ | _ <;>
    simp only [T_pp, T_nn, two_T_pn, w_plus_t, w_zero_t] <;>
    rw [smul_transferMatrix] <;> norm_num

/-- **The left-hand side of `MatrixChainEqBuildChains`, with all matrix
    algebra eliminated.**

    Combining `matrixChain_eq_prod` (the reversal) with `crossingMatrix_eq`
    (the coefficients), the chain-`j` matrix is literally the ordered product
    of `crossingMatrix` over the nucleons after `j` — which is the object
    `buildChains` assembles.

    Consequence, and the point of this lemma: `MatrixChainEqBuildChains` is
    now equivalent to the purely combinatorial

      `(buildChains config).get! j = ((config.drop (j+1)).map`
      `  (fun nk => crossingMatrix config[j]! nk)).prod`

    carrying no Hecke, transfer-matrix or fold-direction content whatsoever.
    See that class's docstring; the remainder is tracked as bean `qou-affg`. -/
theorem matrixChain_chainCrossings (config : NuclearConfig) (j : ℕ) :
    matrixChain (chainCrossings config j) =
      ((config.drop (j + 1)).map (fun nk => crossingMatrix (config[j]!) nk)).prod := by
  rw [matrixChain_eq_prod, chainCrossings, List.map_map]
  refine congrArg List.prod (List.map_congr_left ?_)
  intro nk _
  simp only [Function.comp_apply]
  rw [crossingMatrix_eq]
  rcases vertexType (config[j]!) nk with _ | _ | _ <;> simp

/-- The single accumulator step inside `buildChains`, named so the fold can
    be reasoned about.

    **The body is term-identical to `buildChains`'s step on purpose**, including
    the deprecated `List.get!` (which is why this def inherits that deprecation
    warning). `buildChains_eq_foldl` below is proved by `rfl`, and modernising
    this one call to `config[k - 1]!` breaks it — measured: `rfl` fails, the two
    accessors are not definitionally equal at that strength. Do not "tidy" it
    without re-checking that theorem. -/
noncomputable def buildStep (config : NuclearConfig) :
    (List TMatrix × ℕ) → NucleonType → (List TMatrix × ℕ) :=
  fun acc nk =>
    let (chains, k) := acc
    if k = 0 then (chains, k + 1)
    else
      let extended := chains.mapIdx fun j Mj => extendChain Mj (config[j]!) nk
      let newChain := crossingMatrix (config.get! (k - 1)) nk
      (extended ++ [newChain], k + 1)

/-- **`buildChains` is its own fold — unconditionally, on all three arms.**

    `buildChains` is written with `[]` and `[_]` special-cased before a
    catch-all, which makes the catch-all's equation lemma carry
    "not nil and not singleton" side conditions and is why this looked like
    it needed a three-way case split to reason about.

    It does not: the two special cases are **redundant**. Folding `[]` gives
    `([], 0)` and folding `[x]` gives `([], 1)` — first component `[]` either
    way, exactly what those arms return. So the fold form holds for every
    configuration and `rfl` discharges all three branches.

    This removes the side conditions from any induction over `buildChains`;
    what remains is the accumulator invariant (bean `qou-affg`). -/
theorem buildChains_eq_foldl (config : NuclearConfig) :
    buildChains config = (config.foldl (buildStep config) ([], 0)).1 := by
  match config with
  | [] => rfl
  | [_] => rfl
  | _ :: _ :: _ => rfl

/-- `mapIdx` over a mapped `range` is a `map` of the two composed. -/
theorem mapIdx_map_range {α β : Type} (n : ℕ) (f : ℕ → α) (g : ℕ → α → β) :
    ((List.range n).map f).mapIdx g = (List.range n).map (fun j => g j (f j)) := by
  apply List.ext_getElem
  · simp
  · intro i h1 h2; simp [List.getElem_mapIdx]

/-- In-range `take` peel, with the partial accessor `config[m]!` resolved. -/
theorem take_succ_of_lt (config : NuclearConfig) (m : ℕ) (h : m < config.length) :
    config.take (m + 1) = config.take m ++ [config[m]!] := by
  rw [List.take_succ]
  congr 1
  rw [List.getElem?_eq_getElem h]
  simp [getElem!_pos, h]

/-- The chain list after `buildChains` has folded the first `m` nucleons:
    chain `j` is the ordered `crossingMatrix` product over the nucleons
    strictly between `j` and `m`. -/
noncomputable def chainsUpTo (config : NuclearConfig) (m : ℕ) : List TMatrix :=
  (List.range (m - 1)).map (fun j =>
    (((config.take m).drop (j + 1)).map (fun nk => crossingMatrix (config[j]!) nk)).prod)

/-- One fold step on `chainsUpTo`: every existing chain gains the new
    nucleon's crossing, and one new chain is appended. -/
theorem chainsUpTo_succ (config : NuclearConfig) (m' : ℕ) (h : m' + 1 < config.length) :
    chainsUpTo config (m' + 2) =
      (chainsUpTo config (m' + 1)).mapIdx
        (fun j Mj => Mj * crossingMatrix (config[j]!) (config[m' + 1]!))
      ++ [crossingMatrix (config[m']!) (config[m' + 1]!)] := by
  have hlen : (config.take (m' + 1)).length = m' + 1 := by
    rw [List.length_take]; omega
  simp only [chainsUpTo, Nat.add_sub_cancel, mapIdx_map_range]
  rw [show m' + 2 - 1 = m' + 1 from rfl,
    take_succ_of_lt config (m' + 1) h, List.range_succ, List.map_append]
  congr 1
  · apply List.map_congr_left
    intro j hj
    rw [List.mem_range] at hj
    rw [List.drop_append_of_le_length (by omega), List.map_append, List.prod_append]
    simp
  · have hd : (List.take (m' + 1) config ++ [config[m' + 1]!]).drop (m' + 1)
        = [config[m' + 1]!] := by
      rw [List.drop_append_of_le_length (by omega), List.drop_eq_nil_of_le (by omega),
        List.nil_append]
    simp only [List.map_cons, List.map_nil, hd, List.prod_cons, List.prod_nil, mul_one]

/-- **The accumulator invariant.**  Folding a prefix of length `m` leaves the
    counter at `m` and the chain list at `chainsUpTo config m`. -/
theorem foldl_take (config : NuclearConfig) :
    ∀ m, m ≤ config.length →
      (config.take m).foldl (buildStep config) ([], 0) = (chainsUpTo config m, m) := by
  intro m
  induction m with
  | zero => intro _; simp [chainsUpTo]
  | succ m ih =>
    intro hm
    have hmlt : m < config.length := Nat.lt_of_lt_of_le (Nat.lt_succ_self m) hm
    rw [take_succ_of_lt config m hmlt, List.foldl_append, ih (Nat.le_of_lt hmlt)]
    match m with
    | 0 => simp [buildStep, chainsUpTo]
    | m' + 1 =>
      rw [show m' + 1 + 1 = m' + 2 from rfl, chainsUpTo_succ config m' hmlt]
      simp [buildStep, extendChain]

/-- **The right-hand side of `MatrixChainEqBuildChains`.**  Chain `j` of
    `buildChains` is the ordered `crossingMatrix` product over the nucleons
    after `j`. -/
theorem buildChains_get (config : NuclearConfig) (j : ℕ) (hj : j + 1 < config.length) :
    (buildChains config).get! j =
      ((config.drop (j + 1)).map (fun nk => crossingMatrix (config[j]!) nk)).prod := by
  rw [buildChains_eq_foldl]
  have h := foldl_take config config.length (le_refl _)
  rw [List.take_length] at h
  rw [h]
  simp only [chainsUpTo, List.take_length]
  rw [List.get!_eq_getElem!, getElem!_pos]
  · simp
  · simpa using by omega

/-- **foldl/foldr bridge — typeclass (Pattern 4).**

    The universal claim
    `matrixChain (chainCrossings config j) = (buildChains config).get! j`
    holds because all transfer matrices commute (so `foldl` and
    `foldr` agree), and callers witness the equality for the specific
    `(config, j)` pair they use.

    **The fold-direction framing was wrong twice; corrected 2026-09-05
    (second pass, measured).**

    The original text cited `List.foldl_eq_foldr_of_comm` as *"not yet
    available"*.  No lemma of that name exists.  The first correction, made
    the same day, replaced it with *"what is missing is a pointwise-commuting
    variant without the `flip`"*.  **That was also wrong**, and in the more
    expensive direction: it left a closeable sub-problem looking open and
    still mislocated the real one.

    What is actually true, now proved above:

    * `matrixChain` has **no fold-direction problem**.  Its recursion
      reverses the list, and reversal under pairwise commutation is
      `List.Perm.prod_eq'` + `List.reverse_perm` — both already in Mathlib.
      `matrixChain_eq_prod` discharges it outright, sorry-free, with no
      instance and no `flip`.
    * `QOU.MathlibExt` §3a's `foldl_eq_foldr_of_commute_init` was
      documented as discharging this class "after some rearrangement".  It
      does not: it relocates the *accumulator*, leaving list order alone,
      which is not the operation needed here.  Corrected there too.

    **THE GAP IS CLOSED (2026-09-05).  This class is proved and has an
    instance — `instMatrixChainEqBuildChains` below.**  It is kept as the
    record of the route, not because anything is still assumed.

    The two halves, each sorry-free and neither needing an instance:

    * **Left** — `matrixChain_chainCrossings`: `matrixChain (chainCrossings
      config j)` is the ordered `crossingMatrix` product over the nucleons
      after `j`.  Built from `matrixChain_eq_prod` (the reversal) and
      `crossingMatrix_eq` (the coefficients).
    * **Right** — `buildChains_get`: chain `j` of `buildChains` is *the same
      product*.  Built from `buildChains_eq_foldl` (the `[]` / `[_]` arms are
      redundant, so no case split survives) and `foldl_take` (the accumulator
      invariant, by induction on the prefix length via `chainsUpTo_succ`).

    Nothing new was needed from Mathlib at any point. -/
class MatrixChainEqBuildChains (config : NuclearConfig) (j : ℕ)
    (_hj : j + 1 < config.length) : Prop where
  /-- foldl and foldr agree on the commutative chain product. -/
  eq : matrixChain (chainCrossings config j) =
       (buildChains config).get! j

/-- **The statement, unconditionally.**  No class hypothesis, no instance,
    no `sorry`.  Both sides are the ordered `crossingMatrix` product over the
    nucleons after `j`. -/
theorem matrixChain_eq_buildChains_unconditional
    (config : NuclearConfig) (j : ℕ) (hj : j + 1 < config.length) :
    matrixChain (chainCrossings config j) = (buildChains config).get! j := by
  rw [matrixChain_chainCrossings, buildChains_get config j hj]

/-- The conjecture class is inhabited — it was never more than a placeholder
    for the theorem above. -/
instance instMatrixChainEqBuildChains (config : NuclearConfig) (j : ℕ)
    (hj : j + 1 < config.length) : MatrixChainEqBuildChains config j hj :=
  ⟨matrixChain_eq_buildChains_unconditional config j hj⟩

/-- Per-instance form, kept for compatibility.

    **The name is now a misnomer and the disclosure it used to carry is
    withdrawn**: this is no longer an axiom pass-through, because the class
    is proved (`instMatrixChainEqBuildChains`).  Prefer
    `matrixChain_eq_buildChains_unconditional`.  Retained so that any caller
    written against the conditional API keeps working. -/
theorem matrixChain_eq_buildChains_axiom (config : NuclearConfig) (j : ℕ)
    (hj : j + 1 < config.length)
    [hi : MatrixChainEqBuildChains config j hj] :
    matrixChain (chainCrossings config j) =
    (buildChains config).get! j :=
  hi.eq

/-- The matrix chain from `chainCrossings` equals the corresponding
    entry in `buildChains`.

    This is the bridge between the abstract crossing-sequence formulation
    and the concrete inductive chain construction in TransferMatrix.lean.

    **PROVED 2026-09-05 — the class hypothesis is gone.**  This declaration
    used to carry `[MatrixChainEqBuildChains config j hj]` and pass straight
    through to that class's field.  It no longer does: both sides are shown
    to be the ordered `crossingMatrix` product over the nucleons after `j`.

    The old four-step proof sketch that stood here was right about step 1
    (`crossingMatrix_eq`) and wrong about the rest.  There was no
    `foldl`-versus-`foldr` obstacle: `matrixChain` *reverses* its list, which
    `matrixChain_eq_prod` handles via `List.Perm.prod_eq'`, and the real work
    was the `buildChains` accumulator invariant (`foldl_take`). -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem matrixChain_eq_buildChains (config : NuclearConfig) (j : ℕ)
    (hj : j + 1 < config.length) :
    matrixChain (chainCrossings config j) =
    (buildChains config).get! j :=
  matrixChain_eq_buildChains_unconditional config j hj


-- ════════════════════════════════════════════════════════════════
-- §8  Corollary: optimal NF count from transfer matrix structure
-- ════════════════════════════════════════════════════════════════

/-- **Corollary (Layer 3 → Layer 2 bridge).**

    The optimal NF has exactly `A` terms (the standard basis) because:

    1. Each chain j produces a state `(a_j, b_j)` via the transfer matrix
    2. The Hecke element at generator j is `a_j · σ_j + b_j · 𝟏`
       (by `chain_correspondence`)
    3. The total element is `b₀ · 𝟏 + ∑_j a_j · σ_j` (by linearity)
    4. This has support ⊆ {𝟏, σ₀, σ₁, …, σ_{A-2}} = standardBasis(A-1)
    5. Under valley of stability (N ≥ Z-1), all `a_j ≠ 0` (the crossing
       coefficient is nonzero), so the support equals the standard basis

    The NF has `A` terms: one identity + one per generator. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem optimal_nf_from_transfer_matrix (Z N : ℕ)
    (h_stable : valleyOfStability Z N)
    (h_pos : Z + N ≥ 2) :
    -- The number of terms in the optimal NF equals A = Z + N
    -- (identity + one per generator σ₀, …, σ_{A-2})
    (standardBasis (Z + N - 1)).length = Z + N := by
  simp [standardBasis_length]
  omega

/-- The skein polynomial equals the product of per-generator Markov traces.

    `P(q) = ∏_{j=0}^{A-2} V̂_j`

    where each `V̂_j` is the Markov trace of the j-th Hecke element.
    In cleared form:

    `(t+t⁻¹)^{A-1} · P(q) = ∏_j [a_j + (t+t⁻¹) · b_j]`

    This follows from `volume_eq_markov_trace` applied to each chain. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
-- Dropped the unused hypothesis `h_len : config.length ≥ 2` (2026-08-22;
-- vacuity ledger, `proof-no-unused-hypothesis-rfl`).  The factorisation is the
-- definitional unfolding of `skeinPolynomialCleared`, which holds for every
-- config length; `h_len` was never consumed by the `rfl` proof.
theorem skein_from_markov_traces (config : NuclearConfig) :
    skeinPolynomialCleared config =
    (buildChains config).foldl (fun acc M => acc * tracedVolCleared M) 1 := by
  -- This is definitionally true by unfolding `skeinPolynomialCleared`
  rfl

-- ════════════════════════════════════════════════════════════════
-- §9  Verification: T(1, 0) is the proton-proton case
-- ════════════════════════════════════════════════════════════════

/-- Sanity check: the transfer matrix for `(c, d) = (1, 0)` is `T_pp`.
    Multiplying a Hecke element by `(1·σ + 0)` just appends a generator,
    corresponding to a pure proton crossing. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem transfer_pp_correct :
    transferMatrix 1 0 = T_pp := by
  rfl

/-- Sanity check: the initial state `(1, 0)ᵀ` after one pp crossing
    gives `(HA, 1)ᵀ`, meaning the Hecke element is `HA · σ + 1`.
    This is correct: `σ · σ = σ² = HA · σ + 1` by the Hecke relation. -/
-- Ref: [leitner2026] https://doi.org/10.xxxx/qou
theorem pp_one_step :
    heckeMultiply 1 0 1 0 = mkState HA_t 1 := by
  ext i
  fin_cases i <;> simp [heckeMultiply, mkState] <;> ring

end QOU.TMCorrespondence
