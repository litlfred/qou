import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:one-dim-qou-channel",
  label: "rem:photon-propagation-1d",
  title: "Photon modes and bar-even $q$-dispersion in a 1D channel",
  lean: {
    ref: "qou:QOU.Information.BarEvenVacuumDispersionAndLorentzParity.barEven_zero_ir_and_quadratic_dispersion_summary",
  },
  tags: [
    "optical-fibre",
    "photon",
    "dispersion",
    "mode-quantization",
    "information-theory",
  ],
  uses: [
    "def:one-dim-qou-channel",
    "def:information-speed-of-light",
  ],
});
