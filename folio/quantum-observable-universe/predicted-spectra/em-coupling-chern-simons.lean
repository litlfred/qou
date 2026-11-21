/-
  Fine structure constant — Chern–Simons descent correction (CONJECTURE,
  `κ` unproved).

  Companion: em-coupling-chern-simons.md

  The live claim of the block (its `.md`):

    1/α_EM = q · [9]_q · [10]_q · (1 + δ_CS / (1 − δ_CS · κ))

    δ_CS = (CS(T_{2,9}) + CS(T_{3,5})) · ([2]_q/2) · ℏ_q² / (q [9]_q [10]_q),
    ℏ_q = 1 − q⁻¹,  CS(T_{m,n}) = π²(m²−1)(n²−1)/(12mn),
    κ  = det G^cl_CS / det G^q_CS  (Gram-determinant ratio of the classical
         and q-deformed Chern–Simons pairing on Bring's surface).

  History (bean `qou-aemx` → `qou-08zf`, 2026-09-03).  Until this
  revision the file formalised a DIFFERENT formula from its own `.md`:
  the superseded PSLQ-empirical gluon-octet form
  `45·[3]_q·(1 + δ + 8q·δ²)`, with `κ := 8q` hard-coded, wrapped in a
  class whose only field was a CODATA literal
  (`|alphaEmInvCorrected q − 137.035999177| < 1e-6`); and the
  Chern–Simons class wrapped an `opaque` Prop nobody could state.  The
  `.md`'s live formula reproduces `meson_em_sinh_closed_form.py` exactly
  and is what the L2 dashboard consumes; the two forms differ by 470 ppb
  (`docs/audits/2026-08-29-em-coupling-block-md-lean-divergence.md`).

  Now: the Lean states the `.md`'s formula; `κ` is the determinant ratio
  of an explicit classical pairing against a q-deformed pairing `Gq`
  carried as a PARAMETER (which q-deformation is the open question — the
  `.md` enumerates 16 readings, none of which closes); the conjecture
  class is content-bearing and has NO instance; and no CODATA value
  appears in any statement (the numerical comparison lives in the
  witness `alpha-em-form-comparison` and the `.md`).  The superseded
  gluon-octet form is kept as a plain definition for provenance only.

  Tower status (owner ruling 2026-09-03): ORDER-ZERO-ONLY.  The object is
  the single force-carrier pair `{T(2,9), T(3,5)}` at fixed strand count;
  the δ_CS tower is resummed to all orders in δ_CS, but this is not the
  full `H_n(q)` tower.
-/

import QOU.Archimedean.EmCouplingProjection
import QOU.Mass.QHookDimensionBalanced
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.LinearAlgebra.Matrix.Notation

namespace QOU.ArchimedeanUniverse

open QOU.Mass.QHookDimensionBalanced (qIntBal)

/-! ## Which `q`-integer? — resolved by the file's own target (bean `qou-pjfu`)

The balanced `[k]_q = (q^k − q^{−k})/(q − q^{−1})` (AGENTS.md §7a,
`Mass.QHookDimensionBalanced.qIntBal`), not the geometric `∑_{j<k} q^j`:
evaluated at the substrate anchor the geometric convention lands 9.8 % off
the target while the balanced one lands within ppb.  The number was used
only as a **fingerprint** to recover which function the author meant — the
legitimate use of a known value; it appears in no statement below.

-- Ref: [leitner2026] bean `qou-pjfu`
-/

/-- Chern–Simons invariant of the torus knot `T_{m,n}`:
    `CS(T_{m,n}) = π²(m²−1)(n²−1)/(12mn)`. -/
noncomputable def chernSimons (m n : ℕ) : ℝ :=
  Real.pi ^ 2 * ((m ^ 2 - 1) * (n ^ 2 - 1)) / (12 * m * n)

/-- Self-linking `s = (m−1)(n−1)` of `T_{m,n}` (the `.md`'s Gram-matrix
    diagonal datum). -/
def selfLinking (m n : ℕ) : ℕ := (m - 1) * (n - 1)

/-- Crossing product `c = m·n` of `T_{m,n}`. -/
def crossingProduct (m n : ℕ) : ℕ := m * n

/-- Linking number `ℓ = |m₁n₂ − m₂n₁|` of the carrier pair
    `(T_{2,9}, T_{3,5})`. -/
def carrierLinking : ℕ := 17

/-- `ℓ = |2·5 − 3·9| = 17` — the recorded integer is the formula's value. -/
theorem carrierLinking_eq : ((3 * 9 : ℤ) - 2 * 5).natAbs = carrierLinking := by
  decide

/-- **The classical Chern–Simons Gram pairing** of the `.md` for the
    configuration `(T_{2,9}, T_{3,5})` on Bring's surface:

        G_CS = [ CS₁ + π² s₁²/c₁² ,  π² ℓ²/(c₁c₂) ;
                 π² ℓ²/(c₁c₂)    ,  CS₂ + π² s₂²/c₂² ]

    with `s_i = (m_i−1)(n_i−1)`, `c_i = m_i n_i`, `ℓ = 17`. -/
noncomputable def csGramClassical : Matrix (Fin 2) (Fin 2) ℝ :=
  !![chernSimons 2 9 + Real.pi ^ 2 * (selfLinking 2 9 : ℝ) ^ 2 / (crossingProduct 2 9 : ℝ) ^ 2,
       Real.pi ^ 2 * (carrierLinking : ℝ) ^ 2 / ((crossingProduct 2 9 : ℝ) * crossingProduct 3 5);
     Real.pi ^ 2 * (carrierLinking : ℝ) ^ 2 / ((crossingProduct 2 9 : ℝ) * crossingProduct 3 5),
       chernSimons 3 5 + Real.pi ^ 2 * (selfLinking 3 5 : ℝ) ^ 2 / (crossingProduct 3 5 : ℝ) ^ 2]

/-- The Gram-determinant ratio `κ = det G^cl_CS / det G^q_CS` against a
    q-deformed pairing `Gq`.  Which `Gq` — the reading of *"replace `m, n`
    by `[m]_q, [n]_q`"* — is the open identification, so `Gq` is a
    parameter here, not a definition. -/
noncomputable def gramDetRatio (Gq : Matrix (Fin 2) (Fin 2) ℝ) : ℝ :=
  csGramClassical.det / Gq.det

/-- `κ` is basis-independent: a congruence `G ↦ Bᵀ G B` multiplies both
    determinants by `(det B)²`, which cancels in the ratio (the `.md`'s
    first "source of freedom" is not one).  Stated for a common change of
    basis `B` with `det B ≠ 0`. -/
theorem gramDetRatio_congr (Gq B : Matrix (Fin 2) (Fin 2) ℝ) (hB : B.det ≠ 0)
    (hG : Gq.det ≠ 0) :
    (B.transpose * csGramClassical * B).det / (B.transpose * Gq * B).det = gramDetRatio Gq := by
  unfold gramDetRatio
  rw [Matrix.det_mul, Matrix.det_mul, Matrix.det_mul, Matrix.det_mul, Matrix.det_transpose]
  have hB2 : B.det * B.det ≠ 0 := mul_ne_zero hB hB
  field_simp

/-- `ℏ_q = 1 − q⁻¹` (the mass-chain convention the `.md`'s `δ_CS` uses). -/
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- The bare prefactor `q · [9]_q · [10]_q` — Layer 2 of
    `prop:em-coupling-projection` normalised by the force-carrier
    `q`-dimensions (Layer 3). -/
noncomputable def emBarePrefactor (q : ℝ) : ℝ := q * qIntBal q 9 * qIntBal q 10

/-- The Chern–Simons correction `δ_CS` of the `.md`:
    `(CS(T_{2,9}) + CS(T_{3,5})) · ([2]_q/2) · ℏ_q² / (q [9]_q [10]_q)`. -/
noncomputable def deltaCS (q : ℝ) : ℝ :=
  (chernSimons 2 9 + chernSimons 3 5) * (qIntBal q 2 / 2) * hbarQ q ^ 2 / emBarePrefactor q

/-- The resummed correction factor `1 + δ/(1 − δκ)`. -/
noncomputable def csResummedFactor (δ κ : ℝ) : ℝ := 1 + δ / (1 - δ * κ)

/-- **The conjectured inverse fine-structure constant** in the `.md`'s live
    form, with `κ` a parameter:
    `1/α_EM(q, κ) = q [9]_q [10]_q · (1 + δ_CS/(1 − δ_CS κ))`. -/
noncomputable def alphaEmInvChernSimons (q κ : ℝ) : ℝ :=
  emBarePrefactor q * csResummedFactor (deltaCS q) κ

/-! ## The resummation, proved

What separates the block's live form from the one its `.md` supersedes is not a
value of `κ` — it is whether the correction tower may be summed in closed form at
all. That question needs no `κ`, no CODATA and no anchor, so it is settled here
rather than deferred with the rest.  Unconditional, sorry-free, no fitted input. -/

/-- **The correction tower resums.** For `|δκ| < 1`,
    `Σ_{j≥1} δ^j κ^{j-1} = δ / (1 - δκ)`.  The closed form is not an
    approximation of the tower, it **is** the tower, so there is no
    truncation order to choose — a chosen truncation order is a free
    parameter, and the superseded form had one. -/
theorem csTower_resums (δ κ : ℝ) (h : |δ * κ| < 1) :
    ∑' j : ℕ, δ ^ (j + 1) * κ ^ j = δ / (1 - δ * κ) := by
  have hnorm : ‖δ * κ‖ < 1 := by rwa [Real.norm_eq_abs]
  have hterm : ∀ j : ℕ, δ ^ (j + 1) * κ ^ j = δ * (δ * κ) ^ j := by
    intro j; rw [mul_pow, pow_succ]; ring
  rw [tsum_congr hterm, tsum_mul_left, tsum_geometric_of_norm_lt_one hnorm,
    div_eq_mul_inv]

/-- **The superseded form is the tower's second partial sum.** The order-`δ²`
    expression `δ + κδ²` is exactly `Σ_{j=1}^{2} δ^j κ^{j-1}`. -/
theorem csTower_partialSum_two (δ κ : ℝ) :
    ∑ j ∈ Finset.range 2, δ ^ (j + 1) * κ ^ j = δ + κ * δ ^ 2 := by
  simp [Finset.sum_range_succ]
  ring

/-! ## The conjecture -/

/-- **Chern–Simons-correction conjecture** (primary, content-bearing,
    NO instance; `conj:em-coupling-chern-simons`).

    For the substrate `q > 1`, a q-deformed Chern–Simons Gram pairing
    `Gq` and the inverse fine-structure constant `alphaInv`, the class
    asserts the `.md`'s identity with `κ` the Gram-determinant ratio:

        alphaInv = q [9]_q [10]_q · (1 + δ_CS/(1 − δ_CS κ)),
        κ = det G^cl_CS / det Gq,

    together with the non-degeneracy of `Gq` and the convergence of the
    tower (`|δ_CS κ| < 1`) that makes the resummed form the tower.

    **What is open.**  Which q-deformation of the classical pairing is
    `Gq` — the `.md` enumerates the 16 readings of *"replace `m,n` by
    `[m]_q,[n]_q`"*, the shipped producer picks one (`κ ≈ 1.7216`), and
    none of the 16 makes the identity hold at the physical value (the
    residual is `−468 ppb`; exact closure would need `κ ≈ 1.9153`).  So
    `Gq` is a parameter, and the class is falsified for every reading
    enumerated so far.  A parameter-free `Gq` is GAP bean territory.

    No instance is provided; supplying one asserts the conjecture.
    (History: this class previously wrapped an `opaque` Prop, and before
    that was discharged by an `axiom` installed as a global instance —
    both removed, not completed.) -/
-- Ref: [leitner2026] conj:em-coupling-chern-simons
-- Ref: [witten1989] https://doi.org/10.1007/BF01217730
class ChernSimonsCorrectionConjecture (q : ℝ) (hq : 1 < q)
    (Gq : Matrix (Fin 2) (Fin 2) ℝ) (alphaInv : ℝ) : Prop where
  /-- The q-deformed pairing is non-degenerate. -/
  gram_nondegenerate : Gq.det ≠ 0
  /-- The tower converges: `|δ_CS · κ| < 1`. -/
  tower_convergent : |deltaCS q * gramDetRatio Gq| < 1
  /-- **The identity — the conjecture's claim.** -/
  identity : alphaInv = alphaEmInvChernSimons q (gramDetRatio Gq)

/-- **Conditional consequence (§3b-cond).**  *If* the conjecture holds,
    the inverse coupling is the bare prefactor times the **full** correction
    tower `1 + Σ_{j≥1} δ_CS^j κ^{j−1}` — derived from the class's identity
    and convergence fields through `csTower_resums`, so the tower form and
    the closed form are provably one statement, not two. -/
theorem alphaInv_eq_bare_mul_tower
    {q : ℝ} {hq : 1 < q} {Gq : Matrix (Fin 2) (Fin 2) ℝ} {alphaInv : ℝ}
    [inst : ChernSimonsCorrectionConjecture q hq Gq alphaInv] :
    alphaInv =
      emBarePrefactor q * (1 + ∑' j : ℕ, deltaCS q ^ (j + 1) * gramDetRatio Gq ^ j) := by
  rw [inst.identity]
  unfold alphaEmInvChernSimons csResummedFactor
  rw [csTower_resums _ _ inst.tower_convergent]

/-! ## The superseded gluon-octet form — provenance only

`1/α = 45·[3]_q·(1 + δ + 8q·δ²)`, `δ = ℏ_q⁴·[5]_q`, is the PSLQ-empirical form
the block **previously** displayed (`rem:alpha-em-derivation-open-problems`
records it as ruled out: single-point fit, `κ = 8q` post-hoc).  It is kept as a
definition so that the historical figures remain reproducible from the Lean;
it carries no conjecture class and no numerical claim. -/

/-- The superseded correction `ℏ_q⁴ · [5]_q` (balanced `[·]_q`). -/
noncomputable def deltaCS_gluonOctet (q : ℝ) : ℝ :=
  ((1 - 1/q) ^ 4) * qIntBal q 5

/-- The superseded coefficient `κ = 8q`.  The corpus's exact reading of the
    `8` is `Vol(𝓑₃)/G` (Borromean volume over Catalan's constant), not
    `dim su(3)`; either way the combination `q·8` was never derived and the
    live `.md` uses the torus-knot Chern–Simons pairing instead. -/
noncomputable def gluonOctetKappa (q : ℝ) : ℝ := 8 * q

/-- The superseded gluon-octet form (second-order truncation). -/
noncomputable def alphaEmInvGluonOctet (q : ℝ) : ℝ :=
  45 * qIntBal q 3 *
    (1 + deltaCS_gluonOctet q + gluonOctetKappa q * deltaCS_gluonOctet q ^ 2)

/-- The superseded form is the second partial sum of its own tower —
    the concrete instance of `csTower_partialSum_two`. -/
theorem alphaEmInvGluonOctet_eq_partialSum (q : ℝ) :
    alphaEmInvGluonOctet q =
      45 * qIntBal q 3 *
        (1 + ∑ j ∈ Finset.range 2,
          deltaCS_gluonOctet q ^ (j + 1) * gluonOctetKappa q ^ j) := by
  unfold alphaEmInvGluonOctet
  rw [csTower_partialSum_two]
  ring

end QOU.ArchimedeanUniverse
