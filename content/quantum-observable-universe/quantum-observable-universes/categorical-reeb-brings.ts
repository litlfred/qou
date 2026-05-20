import { example } from "../../schema/builders";

export default example({
  interprets: "thm:categorical-reeb-exists",
  label: "ex:categorical-reeb-brings",
  title:
    "Constructive Reeb derivation on Bring's coordinate ring",
  tags: ["brings-surface", "reeb", "constructive", "maurer-cartan"],
  uses: [
    "thm:categorical-reeb-exists",
    "ex:reeb-su2",
    "def:brings-coordinate-ring",
    "ex:weight-decomposition-su2",
  ],
  cites: [
    "woronowicz1989",
  ],
});
