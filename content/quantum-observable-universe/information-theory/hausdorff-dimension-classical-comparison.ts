import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:julia-set-reeb",
  label: "rem:hausdorff-dimension-classical-comparison",
  title:
    "Classical Hausdorff dimension $d_H$ of the Julia set vs. the $q$-deformed $d_{H,q}$",
  tags: [
    "hausdorff-dimension",
    "julia-set",
    "information-theory",
    "transfer-operator",
    "ruelle",
  ],
  uses: ["rem:hausdorff-dimension-recurrence"],
  cites: [
    "bowen1979",
    "ruelle1982",
    "mcmullen1998",
    "shishikura1998",
  ],
});
