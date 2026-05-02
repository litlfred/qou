import { remark } from "../../schema/builders";

export default remark({
  label: "rem:calibration-inputs",
  title: "Calibration inputs and predictive content",
  interprets: "def:mass-identity",
  // Earlier versions listed `conj:mass-endomorphism` in `uses[]`,
  // which transitively typed every block citing this remark as
  // downstream of an open conjecture (see
  // `docs/audits/conjecture-cones.md` "Methodology" footnote — case
  // (2) cleanup). The three-calibration discipline does **not**
  // depend on the closed-form mass endomorphism: it only needs the
  // categorical mass framework (`def:mass-identity`,
  // `prop:categorical-mass-markov`), both already provable. The
  // conjectural reference moves to prose only.
  uses: [
    "def:mass-identity",
    "prop:categorical-mass-markov",
    "def:categorical-action",
    "def:quantum-observable-universe",
  ],
  tags: [
    "calibration",
    "mass",
    "prediction",
    "endomorphism",
    "substrate-parameter",
    "falsifiability",
  ],
});
