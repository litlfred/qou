import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:quantum-peter-weyl",
  label: "rem:quantum-peter-weyl-interpretation",
  title: "Closing the completeness gap and recovering the Kelvin dispersion",
  uses: [
    "thm:quantum-peter-weyl",
    "prop:q-spectral-sobolev",
    "prop:kelvin-dispersion-derivation",
  ],
});
