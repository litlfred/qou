import { remark } from "../../schema/builders";

/**
 * CO triple bond energy interpretation.
 */
export default remark({
  label: "rem:co-triple-bond-energy",
  title: "$CO$ triple bond energy from the Wedderburn invariants",
  interprets: "prop:co-lp-dual-binding",
  uses: ["def:co-molecular-braid"],
  tags: ["CO", "triple-bond", "binding-energy", "prediction"],
  computation: {
    engine: "python",
    script: "computations/co_bond_order_active_set.py",
    witness: [
      "computations/co-bond-order-active-set.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The witness file `co-molecular-binding.witness.json` records:" },
    {
      kind: "caveat",
      date: "2026-08-25",
      body: "**Provenance and scope (2026-08-25).** The witness cited below,\n`co-molecular-binding.witness.json`, is absent from the tree — it was added\n2026-04-13 in commit `a3e8c2c82d` under `folio-assistant/computations/` and\nleft with the platform code in the miga migration. Recovered and read\n([analysis](https://github.com/litlfred/qou/blob/main/docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md)), it does not support the surrounding text:\n\n- Its energy scale is **fitted**. `calibration_factor = 0.23879110765149733`\n  is exactly $4.478 / 18.753$, the ratio that makes the uncalibrated result\n  equal $\\mathrm{H}_2$'s *measured* bond energy — a fourth calibration, on a\n  molecular observable, outside CAL-1/2/3. The owner directive of 2026-08-25\n  is **no fitting**, so the resulting number is not admissible as a\n  parameter-free prediction.\n- Its three bonds are **not differentiated**. The text below says the\n  $\\sigma$ bond contributes the largest $\\lvert\\hat{V}\\rvert$ and the\n  $\\pi$ bonds smaller; in the witness all three carry the identical\n  $\\Delta\\Phi_1 = 0.687012518457808$, and the $k=3$ total is exactly three\n  times the $k=1$ value.\n- It records **no LP duals**. The list below claims shadow prices\n  $y_1, y_2, y_3$; `y0_star`, `y_star`, `active_set`, `primal_obj`,\n  `dual_obj` and `duality_gap` are all absent.\n\nIts own surviving assertion is \"CO triple bond within 25 % of observed\"\nagainst $D_0(\\mathrm{CO}) = 11.09$ eV; the computed $13.434$ eV is\n$+21.1\\%$ — inside a loose bar, reached via a scale fitted on a different\nmolecule. Do not cite this bond energy as derived.",
    },
  ],
});
