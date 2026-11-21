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
  title: "The $H_2$ bond word among the powers of $V_s$ is $V_s^3$",
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
      "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
      "computations/probes/h2_ruled_electron/h2-ruled-electron.witness.json",
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
    {
      kind: "status",
      date: "2026-11-21",
      body:
        "Rescoped on owner instruction (issue #8821). Under the ruled electron " +
        "sigma0 sigma1 sigma0 (2026-11-21) and the ruled photon " +
        "1 + phi0 sigma0 + phi1 sigma1 + phi01 sigma0 sigma1^-1, the pre-registered probe " +
        "`computations/probes/h2_ruled_electron/` finds that V^3 is unique only among the " +
        "powers of V_s; with the photon's full term alphabet 37 (pe) / 32 (ep) of 155 bonds " +
        "pass, the cheapest being sigma5^2. The statement is narrowed to the V-power family " +
        "and the wider result is a remark. Which bond the full alphabet selects is an open " +
        "owner question. The two-term statement rests on the derived insertion of PR #8743, " +
        "not yet merged. Lean: `QOU/Molecular/H2RuledElectronBond.lean` (no sorry).",
    },
  ],
});
