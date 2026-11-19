import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:information-speed-of-light",
  label: "rem:dsr-planck-scale-phenomenology",
  title:
    "Doubly special relativity and Planck-scale phenomenology: bar-even parity and GRB bounds",
  lean: {
    ref: "qou:QOU.Information.BarEvenVacuumDispersionAndLorentzParity.barEvenGroupVelocity_quadratic_dispersion_bound",
  },
  tags: [
    "dispersion",
    "lorentz-invariance",
    "planck-scale",
    "phenomenology",
    "information-theory",
  ],
  uses: [
    "def:information-speed-of-light",
    "rem:photon-propagation-1d",
    "def:one-dim-qou-channel",
  ],
  cites: [
    "amelinocamelia2001",
    "amelinocamelia1998",
    "abdo2009",
    "amelinocamelia2013",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probes/bar_even_grb_dispersion_and_lorentz_null_probe.py",
    witness: "computations/probes/bar-even-grb-dispersion-and-lorentz-null.witness.json",
    status: "verified",
  },
});
