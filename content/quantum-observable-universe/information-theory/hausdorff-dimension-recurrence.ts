import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:julia-set-reeb",
  label: "rem:hausdorff-dimension-recurrence",
  title: "Discrete recurrence of the Hausdorff dimension",
  tags: [
    "hausdorff-dimension",
    "julia-set",
    "recurrence",
    "information-theory",
    "cosmological-arrow",
    "gravitational-constant",
  ],
  uses: [
    "def:gravitational-constant",
    "rem:hausdorff-dimension-classical-comparison",
  ],
});
