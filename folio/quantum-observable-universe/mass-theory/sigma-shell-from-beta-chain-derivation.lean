import QOU.Basic


/-!
# QOU.BraidKnot.SigmaShellFromBetaChainDerivation
  — Staircase closed form for the σ_shell magnitude (CONJECTURE carrier)

Status (2026-11-15, owner decision S1): demoted from proposition to
conjecture. The block `conj:sigma-shell-from-beta-chain-derivation`
proposes

    y_target(A_magic) = C_{λ_shell} · y_{λ_shell} · |χ^{λ_shell}(β_K)|
                        / |tr_M(β_K)|

with λ_shell = the staircase partition of n = 3·A_magic.

Under production convention D (z = q³/(q²+1)) the right-hand side is
identically zero: every such staircase has at least three rows, and
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`
(sorry-free, general n) makes y_{λ_shell} = 0. At A_magic = 2 this gives
y_target = 0 against the benchmark B(D)/(2·m_p) ≈ 0.0012, a scope-(b)
exclusion of this construction under D. The 12 % agreement recorded
earlier was a convention-C computation on the superseded grouped
deuteron word.

The former theorem `sigma_shell_from_beta_chain := inst.identity data`
was a self-assuming projection of the class field and is removed. The
class below is the conjecture carrier and has no instance.

LaTeX: `\label{conj:sigma-shell-from-beta-chain-derivation}`
-/

namespace QOU.BraidKnot

/-- **Per-magic-anchor σ_shell data tuple.**

    Encodes the inputs and output of the corrected categorical
    closed-form: the Wedderburn coefficient `C_{λ_shell}(q_0)`,
    the central weight `y_{λ_shell}(q_0)`, the absolute character
    `|χ^{λ_shell}(β_K)|`, the absolute Markov trace `|tr_M(β_K)|`,
    and the extracted shell magnitude `y_target(A_magic)`. -/
structure SigmaShellAtMagic where
  /-- Magic anchor (one of {2, 8, 20, 28, 50, 82, 126}). -/
  A_magic   : ℕ
  /-- Wedderburn coefficient at the staircase partition. -/
  C_lambda  : Float
  /-- Jones-Markov central coefficient `y_{λ_shell}(q_0)`. -/
  y_lambda  : Float
  /-- `|χ^{λ_shell}(β_K)|` at q_0. -/
  abs_chi   : Float
  /-- `|tr_M(β_K)|` at q_0. -/
  abs_tr_M  : Float
  /-- Extracted σ_shell magnitude. -/
  y_target  : Float

/-- **The closed-form extraction (conjecture carrier; no instance).**

    Asserts the corrected categorical identity from
    `docs/audits/sigma-shell-categorical-identification.md`:

      `y_target(A_magic)
         = C_{λ_shell}(q_0) · y_{λ_shell}(q_0) · |χ^{λ_shell}(β_K)|
           / |tr_M(β_K)|`

    The class wraps the conjectural identification of `λ_shell`
    with the staircase partition of `3·A_magic`; the field states the equation pointwise on
    `data : SigmaShellAtMagic`. Under convention D the identity forces
    `y_target = 0` at every magic staircase (see the module header). -/
class SigmaShellFromBetaChainDerivation : Prop where
  identity : ∀ (data : SigmaShellAtMagic),
    data.y_target =
      data.C_lambda * data.y_lambda * data.abs_chi / data.abs_tr_M

end QOU.BraidKnot
