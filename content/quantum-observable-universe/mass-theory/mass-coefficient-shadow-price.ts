import { proposition } from "../../schema/builders";

/**
 * Each QOU mass-formula coefficient is a shadow price (LP dual
 * variable) of a Frobenius positivity constraint on a single
 * Wedderburn block, not a fitted parameter.
 *
 * This closes the derivation loop:
 *   operator-selection-lp → shadow prices → mass coefficients
 *   mass-categorical-descent → partition structure → scaling functions
 *   wedderburn-trace-identity → normalization → trace budget
 *
 * At each Hecke level k, the mass-formula coefficient for
 * partition λ ⊢ k is c_λ = y_λ^* · m_e, where y_λ^* is the
 * optimal dual variable of the Frobenius constraint
 * ⟨Φ, π_λ⟩_F ≥ 0.  The factorisation y_λ^* = C_λ · S_λ(Z,N,A)
 * with q-integer C_λ and content-sum-driven S_λ gives every
 * QOU mass coefficient (across all six terms of
 * thm:six-term-mass-formula-complete) as an algebraic q-rational
 * — no AME-style fitted parameters.
 *
 * History: the block was originally titled
 * `prop:mass-coefficient-shadow-price` framing the claim around
 * the empirical Bethe-Weizsäcker formula.  Renamed 2026-05-18
 * to align with the QOU six-term-mass-formula production
 * framework (the BW framing was superseded by the 2026-05-11
 * plancherel-usage audit which moved the BW-named compute
 * scripts to `_deprecated/`).  The structural claim — shadow
 * price = mass coefficient — is unchanged.
 */
export default proposition({
  label: "prop:mass-coefficient-shadow-price",
  title:
    "Mass-formula coefficients as shadow prices of the Frobenius positivity constraints",
  lean: { ref: "qou:QOU.BraidKnot.MassCoefficientShadowPrice",
    validation: "validated",
  },
  uses: [
    "prop:mass-categorical-descent",
    "prop:wigner-coefficient-derivation",
  ],
  tags: [
    "mass-formula",
    "shadow-price",
    "lp-duality",
    "frobenius-positivity",
    "wedderburn",
    "derived-coefficient",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-22",
      body:
        "The charge-type scaling function $S_\\lambda$ (left here as \"Z-dependent\") is identified — formalize-first, no fit — with the free-vs-atom **$H_{3A}$ q-Reeb phase** $|\\Delta\\theta_\\lambda|$, not a partition-only $Z(Z-1)$ count. The bare $\\sum_{\\text{charge}} C_\\lambda\\,Z(Z-1)\\,m_e$ misses the $^3$H$-^3$He split by $22.6\\times$ (the GAP-A-4 $H_3$-collapse obstruction: $p\\equiv n\\equiv{}^3$He at $H_3$); the atomic q-Reeb phase reproduces it to $\\sim118\\%$ (right order). The Coulomb channel $\\sinh(\\log q)=h/2$ is already the factor in $C_\\lambda=\\tilde w_\\lambda\\,h/2$. See `docs/audits/2026-06-22-charge-slambda-reeb-phase-crack.md`.",
    },
  ],
});
