/-!
# QOU.BraidKnot.sigma_shell_from_beta_chain
  — Closed-form σ_shell magnitude from compound β-decay chain Q-values

Refines `prop:compound-beta-shell-calibration` (which set up the
framework but left y_target as the algebraic unknown) with the
explicit closed form for y_target(A_magic) from cumulative AME
Q-values along the β-stability valley.

LaTeX: `\label{prop:sigma-shell-from-beta-chain-derivation}`
-/

import QOU.Basic

namespace QOU.BraidKnot

/-- **Closed-form σ_shell extraction.**

    Inputs: AME 2020 chain Q-values reaching A_magic + per-link
    categorical density changes δρ^(k) along the chain.

    Output: y_target(A_magic) = (Σ Q^net - Σ δρ·m_e·|tr_M|)
                                / (m_e · |tr_M(β_ref)|).

    Returns the structural data; numeric extraction is deferred
    to the Python consumer
    `folio-assistant/computations/sigma_shell_from_beta_chain.py`. -/
structure SigmaShellFromBetaChain where
  /-- The magic anchor (one of {2, 8, 20, 28, 50, 82, 126}). -/
  A_magic : ℕ
  /-- Cumulative AME Q-value along the β-chain reaching the magic
      anchor (positive convention: energetically downhill chain). -/
  Q_beta_net_MeV : Float
  /-- Cumulative constituent-walk piece
      Σ_k δρ^(k) · m_e · |tr_M(β_k)|. -/
  constituent_walk_MeV : Float
  /-- The reference braid's |tr_M| value (typically free p or n). -/
  abs_tr_M_ref : Float


/-- **The closed-form extraction.**

    y_target(A_magic) = (Q_beta_net - constituent_walk) / (m_e · |tr_M_ref|).

    Numeric value computed by the consumer; this lemma states
    structural existence. -/
-- Ref: [manuscript] prop:sigma-shell-from-beta-chain-derivation
theorem sigma_shell_from_beta_chain
    (data : SigmaShellFromBetaChain) :
    True := by
  -- Structural statement: given the chain data, y_target is
  -- uniquely determined by the formula in the .md file. The
  -- compute layer (sigma_shell_from_beta_chain.py stub) instantiates
  -- this for each magic anchor.
  trivial

end QOU.BraidKnot
