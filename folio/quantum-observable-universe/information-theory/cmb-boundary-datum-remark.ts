import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cmb-boundary-datum-remark",
  title: "Jet content of the CMB boundary datum",
  interprets: "def:cmb-boundary-datum",
  tags: ["definition-commentary"],
  uses: [
    "def:cmb-boundary-datum",
  ],
});
