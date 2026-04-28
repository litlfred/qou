import { definition } from "../../schema/builders";

export default definition({
  label: "def:briggs-klein-chart",
  lean: { ref: "qou:QOU.BriggsKleinChart", validation: "not_checked" },
  title: "Briggs--Klein affine chart",
  tags: ["brings-surface", "coordinate-chart"],
  uses: ["def:brings-surface"],
});
