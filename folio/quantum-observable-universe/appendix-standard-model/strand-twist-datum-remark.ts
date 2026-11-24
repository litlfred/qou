import { remark } from "../../schema/builders";

export default remark({
  label: "rem:strand-twist-datum-remark",
  title: "Properties of the per-strand framing datum and the hypercharge candidate",
  interprets: "def:strand-twist-datum",
  tags: ["framing", "hypercharge"],
  uses: [
    "def:strand-twist-datum",
    "def:gauge-action-groupoid",
    "def:coulomb-charge",
    "conj:sm-hypercharge-invariant",
  ],
});
