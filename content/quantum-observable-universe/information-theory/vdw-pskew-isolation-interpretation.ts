import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vdw-pskew-isolation",
  label: "rem:vdw-pskew-isolation-interpretation",
  title:
    "Van der Waals is the discarded sinh residual, the same Hopf channel as $\\alpha_{EM}$",
  computation: {
    engine: "python",
    script: "computations/vdw_pskew_sinh_probe.py",
    witness: [
      "computations/vdw-pskew-sinh-probe.witness.json"
    ],
    status: "verified",
  },
  uses: [
    "prop:vdw-pskew-isolation",
    "prop:crossing-energy-decomposition",
    "def:bar-involution",
    "rem:im-q-vs-p-skew",
    "thm:em-spectral-completeness",
    "cor:gauge-coupling-uniqueness",
    "prop:alpha-em-categorical-trace-ratio",
    "prop:alpha-em-habiro-bar-involution",
  ],
});
