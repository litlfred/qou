import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:alpha-decay-gamow-tunneling",
  title:
    "Zero-parameter Gamow--Gurney--Condon $\\alpha$-decay tunneling and the $N=126$ shell-closure hindrance",
  lean: {
    ref: "qou:QOU.Observations.alpha_decay_gamow_tunneling",
    validation: "not_checked",
  },
  uses: [
    "def:aether-parameter",
    "def:categorical-q-ext-deriv",
    "def:quantum-planck-constant",
    "def:borromean-baryon",
  ],
  cites: ["gamow1928", "mayer1949"],
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.py",
    witness:
      "computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.witness.json",
    status: "verified",
  },
  tags: [
    "alpha-decay",
    "gamow-tunneling",
    "geiger-nuttall",
    "magic-shells",
    "n-126",
    "zero-parameter",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body: "Bean qou-i2jl: Lean sibling `QOU.Observations.alpha_decay_gamow_tunneling` carries both generic-field (`alpha_decay_pair_and_qvalue_generic`, `mayerJensenPairOverlap_po210_generic`, `two_mul_geigerNuttallExponentGeneric`) and archimedean `ℝ` statements per AGENTS.md §7c. All numerical figures are verified at 80 working dps (50 dps serialized, proton pin, zero float64) in `computations/probes/alpha_decay_n126_and_derived_qalpha/alpha_decay_n126_qalpha_probe.py` against pre-registration `PREREGISTRATION.md`.",
    },
  ],
});
