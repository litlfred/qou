import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:integer-stability",
  label: "rem:q-stability-ranges",
  title:
    "Stability of $n_{\\mathrm{pred}}$ under local variations in $q$",
  tags: [
    "stability",
    "substrate-parameter",
    "robustness",
    "light-nuclei",
  ],
  uses: [
    "prop:integer-stability",
    "prop:beta-stability",
    "def:substrate-parameter",
    "prop:local-substrate-q",
  ],
});
