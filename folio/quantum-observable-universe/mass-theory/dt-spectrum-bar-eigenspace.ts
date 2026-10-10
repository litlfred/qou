import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:dt-spectrum-bar-eigenspace",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoDTSpectrumSplit",
    validation: "validated",
  },
  title:
    "The DT-spectrum split is the bar-eigenspace decomposition of the $q\\to0$ Stokes constants",
  uses: [],
  cites: ["garoufalidis-gu-marino2021"],
  tags: [
    "g3-aomega",
    "route-c",
    "bar-parity",
    "dt-invariant",
    "chirality",
    "stokes-constant",
  ],
});
