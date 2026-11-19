import { remark } from "../../schema/builders";

export default remark({
  label: "rem:benzene-molecular-braid-remark",
  title: "Strand count and iterative construction of benzene",
  interprets: "def:benzene-molecular-braid",
  tags: ["definition-commentary"],
  uses: [
    "def:benzene-molecular-braid",
    "prop:benzene-threading-emergence",
  ],
});
