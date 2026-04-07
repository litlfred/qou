import { definition } from "../../schema/builders";

export default definition({
  label: "def:briggs-klein-chart",
  lean: { decl: "QOU.BriggsKleinChart", validation: "not_checked" },
  title: "Briggs--Klein affine chart",
  tags: ["brings-surface", "coordinate-chart"],
  uses: ["def:brings-surface"],
});
