import { definition } from "../../schema/builders";

export default definition({
  label: "def:hecke-curvature-2-cocycle",
  title: "Hecke curvature 2-cocycle $F$",
  lean: {
    ref: "qou:QOU.WedderburnMass.heckeResidue",
    validation: "not_checked",
  },
  uses: [],
  cites: ["kassel1995"],
  tags: [
    "hecke",
    "curvature",
    "2-cocycle",
    "hochschild",
    "yang-baxter",
    "gb-filtration",
  ],
});
