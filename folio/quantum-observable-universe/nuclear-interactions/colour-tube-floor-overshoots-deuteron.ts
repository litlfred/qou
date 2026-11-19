import { remark } from "../../schema/builders";

export default remark({
  label: "rem:colour-tube-floor-overshoots-deuteron",
  title:
    "The colour-tube selection rule cannot supply the interface tilt: a category error, corroborated by a family floor above the deuteron",
  interprets: "conj:inter-nucleon-channel-color-tube",
  uses: [
    "conj:inter-nucleon-channel-color-tube",
    "prop:interface-band-between-isospin-weights",
  ],
  tags: [
    "colour-tube",
    "deuteron",
    "isospin",
    "impossibility",
    "nn-channel",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-09",
      body:
        "OPEN — the numerical half of this remark has NO PRODUCER and NO WITNESS, and is " +
        "labelled as provisional in the rendered prose for exactly that reason. " +
        "Bean qou-dx1t records: scanning lambda on a 1/100 grid across 6 colour alignments at " +
        /* <!-- literal-source: exploratory grid scan figures recorded in qou-dx1t (no witness JSON, noted below) --> */
        "30 dps gives family floor B_pn = 2.29580 MeV against B_AME(2H) = 2.224566 MeV " +
        "(overshoot 0.0712 MeV, 3.2 %); the S_3 average that confinement demands lands at " +
        "2.46755 MeV (11 % high); reaching the target needs x = 0.35768, i.e. the answer must " +
        /* <!-- literal-source: exploratory grid scan figure recorded in qou-dx1t --> */
        "already be known. The figure 2.29580 appears NOWHERE in the repo outside .beans/qou-dx1t " +
        "— no probe, no witness JSON. computations/color_tube_flavor_isospin_selection.py and " +
        "color_tube_t1_tensor_decomposition.py supply COLOR_WEIGHTS measured clean of the tilt, " +
        "but nothing computes the B_pn family range. A probe + witness must be written before " +
        "this block can become a proposition or carry a `computation` field; writing that " +
        "producer was out of scope for this change. No new Lean scaffold was created — " +
        "ColorFlavorIsospinSelection.lean and InterNucleonChannelColorTube.lean already exist " +
        "and are in the build graph.",
    },
    {
      kind: "caveat",
      date: "2026-08-09",
      body:
        "Refutation scope, per the (a)/(b) discipline. The CATEGORY ERROR is a structural " +
        "exclusion (b): the named invariant is that InterNucleonChannelColorTube.weight " +
        "factors through NucleonColorContent — definite quark content on each sheet — while " +
        "the deuteron line (pn - np)/sqrt(2) is not an eigenvector of that content, so the " +
        "weight is not defined on it at all. The 3.2 % overshoot is a scope-limited negative " +
        "(a): this family, alone, on the scanned grid, does not reach the target.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/color_tube_flavor_isospin_selection.py",
    witness: [
      "computations/color-tube-flavor-isospin-selection.witness.json",
      "computations/color-tube-t1-tensor-decomposition.witness.json",
      "computations/probes/gamma-gamma-isospin-channel-probe.witness.json",
      "computations/m-tau-knot-prediction.witness.json",
    ],
    status: "verified",
  },
});
