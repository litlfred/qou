import { remark } from "../../schema/builders";

export default remark({
  label: "rem:canonical-braid-interface-composition-remark",
  title: "Closed forms and asymmetry of the interface composition",
  interprets: "def:canonical-braid-interface-composition",
  uses: [
    "def:canonical-braid-interface-composition",
    "prop:flavor-split-substrate",
  ],
});
