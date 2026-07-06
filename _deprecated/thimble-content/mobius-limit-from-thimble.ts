import { conjecture } from "../../schema/builders";

// CAL-4 caveat (2026-05-22): demoted prop → conj. The PL derivation
// was retracted on main (commit f86ea9d7a; witness labels (4-q)/(4q+3)
// as "← post-hoc"). The replacement algebraic-Galois Step 1 sources
// the constants {4, 3} from F(z,c)'s c²-coefficient and degree, but
// the color-tube cubic has coefficients in z only — so the VARIABLE q
// in the numerator and denominator is not sourced. Curve-fit twin of
// the literal LAMBDA_PROTON_DOC CAL-4 (cheat-sheet Migration Backlog #1).
export default conjecture({
  label: "conj:mobius-limit-from-thimble",
  title:
    "The integration limit $a(q) = (4-q)/(4q+3)$ — q-source open (CAL-4 caveat)",
  cites: ["witten2011", "pham1965", "arnold-gusein-zade-varchenko1988"],
  uses: [
    "rem:picard-lefschetz-thimble",
    "prop:mobius-golden-fixed-points",
    "rem:baryon-integration-limit",
  ],
  defines: [],
  tags: [
    "mobius-transformation",
    "integration-limit",
    "color-tube",
    "galois-data",
    "binomial-coefficients",
    "laurent-polynomial",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.mobiusLimitFromThimble",
    validation: "not_checked",
  },
  computation: {
    engine: "sympy",
    script: "computations/mobius_limit_from_thimble.py",
    witness: "computations/mobius-limit-from-thimble.witness.json",
    status: "not_run",
    requires: ["sympy", "mpmath"],
  },
});
