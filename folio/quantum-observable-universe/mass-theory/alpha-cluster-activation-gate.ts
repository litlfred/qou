import { proposition } from "../../schema/builders";

/**
 * The proved-Lean α-cluster ACTIVATION GATE — a topological selection rule on
 * which inter-cluster bond channels contribute to the body-order binding.
 *
 * This block asserts ONLY the four Lean-proved, unconditional facts about
 * Milnor triple-linking indeterminacy + Σ₃ sign-rep obstruction + Vol=0
 * annihilation. It deliberately carries NO binding magnitudes, NO calibrated
 * coefficients, and NO isotope closure — the phenomenological Model G numbers
 * (cluster bases entering at measured AME values, b, g, the ≤0.31% fit) are
 * recorded, honestly labelled as a non-derivation, in the interpreting remark
 * `rem:alpha-cluster-model-g-closure`. Anti-laundering STRICT (owner directive
 * 2026-07-18): the fit is NOT presented in the paper as a parameter-free
 * derivation; only the proved gate mechanism is a proposition.
 *
 * Lean (all sorry-free, generic ring where applicable):
 *  - QOU.Mass.MilnorIndeterminacyGate.gate_open_iff_brunnian   (headline ref)
 *  - QOU.Mass.MilnorIndeterminacyGate.gate_kills_hopf_spectator
 *  - QOU.Mass.MilnorSignRepObstruction.equivariant_linearMap_eq_zero
 *  - QOU.Mass.BondChannelClassSelection.wplane_term_eq_zero_of_vol_eq_zero
 */
export default proposition({
  label: "prop:alpha-cluster-activation-gate",
  title:
    "The $\\alpha$-cluster activation gate: Milnor indeterminacy, sign-rep obstruction, and $\\mathrm{Vol}=0$ annihilation",
  lean: {
    ref: "qou:QOU.Mass.MilnorIndeterminacyGate.gate_open_iff_brunnian",
    validation: "not_checked",
  },
  cites: ["milnor1954"],
  uses: [],
  tags: [
    "binding",
    "alpha-cluster",
    "milnor",
    "brunnian",
    "activation-gate",
    "sign-rep-obstruction",
  ],
});
