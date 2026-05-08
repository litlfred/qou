import { example } from "../../schema/builders";

export default example({
  interprets: "thm:tannaka-krein-isomorphism",
  label: "ex:tannaka-krein-su2",
  title:
    "Constructive Tannaka--Krein reconstruction for $\\mathrm{SU}_q(2)$",
  tags: ["su2", "tannaka-krein", "constructive", "reconstruction"],
  uses: [
    "thm:tannaka-krein-isomorphism",
    "ex:substrate-parameter-su2",
    "ex:substrate-parameter-brings",
    "ex:categorical-reeb-brings",
  ],
});
