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
  uses: ["def:gravitational-constant"],
  cites: [
    "bowen1979",
    "ruelle1982",
    "mcmullen1998",
    "shishikura1998",
  ],
});
