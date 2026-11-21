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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; they are recorded — labelled as a structural/phenomenological\nmodel, **not** a parameter-free derivation — in the interpreting remark\n[Model G: a phenomenological $\\alpha$-cluster binding closure](#rem:alpha-cluster-model-g-closure)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean structure\n\nAll four parts are formalized (generic commutative ring where the\nstatement permits):\n\n- **(1)–(2)** `QOU.Mass.MilnorIndeterminacyGate` —\n  `gate_kills_hopf_spectator` ($|\\ell_{ij}|=1 \\Rightarrow\n  \\mathrm{Subsingleton}\\,(\\mathbb{Z}/\\Delta\\mathbb{Z})$) and\n  `gate_open_iff_brunnian` ($\\Delta = 0 \\iff$ all $\\ell_{ij}=0$), with the\n  structure-level `ClusterTriple.residue_nontrivial_of_brunnian`.\n- **(3)** `QOU.Mass.MilnorSignRepObstruction.equivariant_linearMap_eq_zero`\n  (Schur-lemma vanishing of the $\\Sigma_3$ sign-rep coupling over any\n  `CommRing`), with `coupling_vanishes_on_charge_bilinears`.\n- **(4)** `QOU.Mass.BondChannelClassSelection.wplane_term_eq_zero_of_vol_eq_zero`\n  ($\\mathrm{Vol}=0 \\Rightarrow \\mathfrak{m}_e\\,\\mathrm{Vol}\\,q = 0$). The\n  companion CAL-3 class-selection statement\n is a *conditional* result on\n  the `BindingVolumeLedger` class (no instance declared — the ledger is an open\n  input, not part of this proposition's proved content)." },
  ],
});
