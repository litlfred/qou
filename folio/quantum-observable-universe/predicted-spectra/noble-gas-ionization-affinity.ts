import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:noble-gas-characterization",
  label: "rem:noble-gas-ionization-affinity",
  title: "Ionization energy and electron affinity of the noble gases",
  uses: ["prop:noble-gas-characterization"],
});
