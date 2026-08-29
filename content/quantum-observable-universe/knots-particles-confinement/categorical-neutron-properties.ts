import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-neutron-properties",
  interprets: "def:categorical-neutron",
  title: "Neutron: NF construction, mass, transition, and charge",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: [
    "def:categorical-neutron",
    "def:categorical-proton",
    "def:up-quark",
    "def:down-quark",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-29",
      body:
        "**Crossing count corrected 13 \u2192 11 (owner-authorised).** This block " +
        "previously read that the integer LP dual selects $L_+ \\to L_-$ " +
        "(*two* Hopf links, 4 gluon crossings) for a total of 13 crossings, " +
        "and that the neutron needs more gluon crossings than the proton " +
        "(4 versus 2). Two pieces of the block's **own** evidence contradict " +
        "that. First, the paragraph immediately above states that *a single* " +
        "Hopf link $L_- = \\sigma_1\\sigma_0$ restores structural stability. " +
        "Second, building the block's own recipe gives the k-ladder " +
        "9 crossings \u2192 0.788010, **11 \u2192 0.7975664**, 13 \u2192 1.235859: the " +
        "$+0.7976$ this block prints is the *eleven*-crossing value, and " +
        "1.235859 appears nowhere in the corpus. The 4-versus-2 asymmetry " +
        "claim does not survive and has been dropped; the $\\mathrm{tr}_M$ " +
        "depth comparison it rested on is kept, being a separate " +
        "measurement. Probe: `qbeta_delta_net_four_values_probe.py` (19/19). " +
        "This settles `qou-im4m` (#5892), which established the prose/code " +
        "mismatch but left open which side was wrong \u2014 it is the prose.",
    },
    {
      kind: "caveat",
      date: "2026-08-29",
      body:
        "**Not settled here: whether two gluon crossings suffice at all.** " +
        "Evaluating Frobenius positivity as $(\\mathrm{G}x)_\\gamma = " +
        "\\mathrm{tr}_M(e_\\gamma \\cdot T_w)$ \u2014 a reading that reproduces " +
        "this chapter's own claim that the bare 9-crossing element violates " +
        "positivity, with exactly one negative channel \u2014 no adjunction of " +
        "two gluon crossings is feasible for the *proton*; the minimum is " +
        "three. That rests on a reading of the predicate rather than on the " +
        "corpus's arithmetic, so it is deliberately **not** written into " +
        "this block. Bean `qou-vtlj`; adjudication belongs to `qou-bg3w`.",
    },
  ],
});
