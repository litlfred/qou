import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The replacement value must be read off a regenerated `toffoli-lp-stability.witness.json`; it is not to be hand-edited, and the producer needs three fixes (convention, trace rule, precision) before it can be re-run.\n\n([`toffoli_nf_coordinates_and_lp_feasibility.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_nf_coordinates_and_lp_feasibility.py))\n\nFormalized in `QOU.Information.toffoliFlip_mul_coneCoord_nonpos`, with the symbolic cross-check in [`toffoli_sign_inversion_is_structural.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_sign_inversion_is_structural.py) (7/7).\n\n**Every sign and zero claim above is Lean-proved.** Nothing in this arc rests on evaluation at a single anchor:\n\n| claim | theorem |\n|---|---|\n| $P_{7,7} > 0$ on $q > 0$, no positive root | `toffoliDiagonal_pos` |\n| $P_{6,6} > 0$ on $q > 0$ | `toffoliP66_pos` |\n| $P_{7,6}$'s only positive zero is $q = 1$ | `toffoliFlip_eq_zero_iff` |\n| $P_{7,6} < 0$ on $q > 1$, the substrate side | `toffoliFlip_neg_of_one_lt` |\n| $P_{7,6} > 0$ on $0 < q < 1$ | `toffoliFlip_pos_of_lt_one` |\n| $P_{6,7} + P_{7,6} = q(q-1)^2(q+1)^2/2(q^2+1)$ | `toffoli_antisymmetry_defect` |\n| the flip channel is **not** antisymmetric | `toffoli_not_antisymmetric` |\n| $W_{\\mathrm{std}} > 0$ and $P_{7,7}W_{\\mathrm{std}} > 0$ | `wStd_pos`, `toffoliDiagonal_mul_wStd_pos` |\n| $\\mathrm{sign}\\,P_{7,6} = -\\mathrm{sign}\\,\\hbar_\\times$ | `toffoliFlip_mul_coneCoord_nonpos` |\n\nAll use only the axioms `propext`, `Classical.choice` and `Quot.sound`.\n\nSymbolic cross-check: [`toffoli_amplitude_sign_claims.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_amplitude_sign_claims.py), 9/9.\n\n— validated against the production `gram_matrix_mp` at five values of $q$ —\n\nProved without the intermediate value theorem and without $q_c$'s value in `cone_sign_change_unexplained_by_factors`:\n\nFormalized in `QOU.Information.cone_eq_quadratic_in_amplitudes`, with `coneCoordRow5_pos_iff` carrying the sign from the numerator to the constraint.\n\nMeasurement: [`toffoli_cone_in_entry_subring.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_cone_in_entry_subring.py), 8/8.\n\nFormalized in `QOU.Information.cone_eq_markov_hecke_polynomial`.\n\nThe relation is in `QOU.Information.markov_hecke_relation`; it is a fact\n\nand the corpus already carries that as a table, `QOU.Machinery.MarkovTraceH4.TRM`, whose entries 9 and 13 are $\\hbar_\\times z^2 + z = \\mathrm{tr}(\\sigma_0\\sigma_1\\sigma_0)$.\n\nMeasurement: [`toffoli_cone_in_markov_hecke_parameters.py`](https://github.com/litlfred/qou/blob/main/computations/probes/toffoli_cone_in_markov_hecke_parameters.py), 13/13." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:toffoli-lp-stability",
  title:
    "LP-dual stability of the $q$-Toffoli braid and the golden-ratio threshold",
  tags: [
    "toffoli",
    "lp-duality",
    "stability",
    "gram-matrix",
    "golden-ratio",
    "substrate-q",
    "hecke-algebra",
    "q-AND",
  ],
  lean: { ref: "qou:QOU.Information.toffoli_lp_stable",
    validation: "not_checked",
  },
  uses: [
    "prop:toffoli-transfer-matrix",
    "prop:lp-dual-stability",
  ],
  computation: {
    engine: "python",
    script: "computations/toffoli-lp-stability.py",
    witness: "computations/toffoli-lp-stability.witness.json",
    status: "verified",
  },
});
