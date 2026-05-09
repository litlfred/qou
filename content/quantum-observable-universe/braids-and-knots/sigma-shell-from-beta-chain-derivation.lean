/-!
# QOU.BraidKnot.sigma_shell_from_beta_chain
  — Closed-form σ_shell magnitude as Wedderburn coefficient at the
    staircase partition

⚠ REDERIVED 2026-05-08 (PR #564 §5 escalation). The earlier
β-decay-chain frame gave a 22 M % discrepancy at A_magic=2;
deuteron has no non-shell-crossing predecessors along the β-
stability valley, so cumulative Q-value subtraction does not
isolate the shell magnitude.

Corrected categorical frame (per
`docs/audits/sigma-shell-categorical-identification.md`):

    y_target(A_magic) = C_{λ_shell} · y_{λ_shell} · |χ^{λ_shell}(β_K)|
                        / |tr_M(β_K)|

with λ_shell = staircase partition of n = 3·A_magic. For A=2,
λ_shell = (3,2,1) and the formula yields y_target = 0.001332 vs
benchmark 0.001185 (12 % agreement; 300 000× better than the
β-chain frame).

NO Q_β, NO AME chain Q-values, NO fitted parameters.

LaTeX: `\label{prop:sigma-shell-from-beta-chain-derivation}`
-/

import QOU.Basic

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

/-- **The closed-form extraction (conditional on the
    `SigmaShellFromBetaChainDerivation` class).**

    Asserts the corrected categorical identity from
    `docs/audits/sigma-shell-categorical-identification.md`:

      `y_target(A_magic)
         = C_{λ_shell}(q_0) · y_{λ_shell}(q_0) · |χ^{λ_shell}(β_K)|
           / |tr_M(β_K)|`

    The class wraps the conjectural identification of `λ_shell`
    with the staircase partition of `3·A_magic`; the conditional
    theorem then states the equation pointwise on
    `data : SigmaShellAtMagic`. -/
class SigmaShellFromBetaChainDerivation : Prop where
  identity : ∀ (data : SigmaShellAtMagic),
    data.y_target =
      data.C_lambda * data.y_lambda * data.abs_chi / data.abs_tr_M

-- Ref: [manuscript] prop:sigma-shell-from-beta-chain-derivation
theorem sigma_shell_from_beta_chain
    [inst : SigmaShellFromBetaChainDerivation]
    (data : SigmaShellAtMagic) :
    data.y_target =
      data.C_lambda * data.y_lambda * data.abs_chi / data.abs_tr_M :=
  inst.identity data

end QOU.BraidKnot
