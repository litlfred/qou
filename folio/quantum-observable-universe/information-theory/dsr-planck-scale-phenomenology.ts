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
});
