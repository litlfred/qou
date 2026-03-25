import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:double-slit-photon-pattern",
  lean: {
    decl: "QOU.Experimental.double_slit_photon_pattern",
    validation: "not_checked",
  },
  title: "Photon interference pattern via Julia-set envelope",
  uses: [
    "def:double-slit-q-phase",
    "def:exceptional-divisor",
    "def:chiral-sector-coords",
    "rem:julia-s1-photon-scatter",
  ],
  tags: ["double-slit", "interference", "photon", "julia-set", "exceptional-divisor"],
});
