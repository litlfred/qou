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
    "rem:julia-set-reeb",
    "def:operational-entropy",
    "def:gravitational-constant",
    "def:planck-time",
  ],
});
