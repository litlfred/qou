import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:vdw-pskew-isolation",
  title:
    "Van der Waals as the bar-odd ($P_{\\mathrm{skew}}$, sinh) channel",
  lean: {
    ref: "qou:QOU.VdwPskew.hopf_bar_even_odd_decomposition",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "computations/vdw_pskew_sinh_probe.py",
    witness: [
      "computations/vdw-pskew-sinh-probe.witness.json",
    ],
  },
  uses: [
    "prop:hopf-link-symmetric-decomposition",
    "def:van-der-waals-hopf-channel",
    "prop:crossing-energy-decomposition",
    "def:bar-involution",
    "rem:im-q-vs-p-skew",
    "prop:alpha-em-habiro-bar-involution",
    "thm:em-spectral-completeness",
    "cor:gauge-coupling-uniqueness",
    "prop:alpha-em-categorical-trace-ratio",
  ],
  tags: [
    "van-der-waals",
    "bar-involution",
    "p-skew",
    "sinh-cosh",
    "hopf-link",
    "rapidity",
    "narrowed-probe",
  ],
});
