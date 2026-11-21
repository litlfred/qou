import { proposition } from "../../schema/builders";

/**
 * The H2 covalent bond word under the one gamma-gamma rule.
 *
 * Re-derived 2026-11-15 (owner ruling: bonds follow gamma-gamma +
 * reading 3): the bond letter is V^3 when the constituents pass
 * reading 3 alone; the inverse trefoil is not a gamma-gamma word.
 */
export default proposition({
  label: "prop:ilp-covalent-bond",
  lean: { ref: "qou:QOU.Molecular.inverse_trefoil_not_gammaGamma" },
  title: "The $H_2$ bond word is $V^3$ under the $\\gamma\\gamma$ rule",
  tags: [
    "covalent-bond",
    "gamma-gamma",
    "reading-3",
    "knot-operator",
    "molecular",
    "zero-parameters",
  ],
  computation: {
    engine: "python",
    script: "computations/probes/h2_gg_electron/h2_gg_electron_probe.py",
    witness: [
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-15",
      body:
        "Re-derived on owner instruction under the one-rule ruling (bonds follow " +
        "gamma-gamma + reading 3). The previous statement selected the inverse " +
        "trefoil from a list of knots; that word has odd length and is excluded " +
        "by `gammaGamma_length_even`. Its Lean (`length = 3 := rfl`, and an " +
        "`axiom` asserting only `∃ E, 0 < E ∧ E < 5`) is replaced. The selection " +
        "data come from the `h2-gg-electron` witness of PR #7741, so #7741 must " +
        "land first for the computation path to resolve. The constituent " +
        "condition (electron passes reading 3 alone) was ruled by the owner on 2026-11-15: each particle must pass reading 3 on its own strands, so V^3 is unique.",
    },
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "The proposition is a computation at the single point q = q0 (proton pin), " +
        "evaluated in 40-digit arithmetic; no other q is tested (owner chose to name q0 " +
        "in the statement, 2026-11-15). The Lean ref `inverse_trefoil_not_gammaGamma` " +
        "encodes only the side remark that the inverse trefoil has odd length and so is " +
        "not a gamma-gamma word; the selection result itself is not formalized.",
    },
  ],
});
