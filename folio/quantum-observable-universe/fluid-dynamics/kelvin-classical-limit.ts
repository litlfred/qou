import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:kelvin-dispersion-derivation",
  label: "rem:kelvin-classical-limit",
  title: "Classical limit of the $q$-Kelvin dispersion",
  uses: ["prop:kelvin-dispersion-derivation"],
  tags: ["classical-limit", "kelvin-wave", "self-induction"],
});
