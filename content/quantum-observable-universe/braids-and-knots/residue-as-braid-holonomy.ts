import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gb-residue-spectral-sum",
  label: "rem:residue-as-braid-holonomy",
  title:
    "Each residue is the holonomy of a braid loop around a singular fibre",
  tags: [
    "holonomy",
    "residue",
    "spectral-sum",
    "filtration",
    "gauge-theory",
    "interpretation",
  ],
  uses: ["prop:gb-residue-spectral-sum"],
});
