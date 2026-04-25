import { remark } from "../../schema/builders";

export default remark({
  label: "rem:commutative-crossing-energy",
  title:
    "Commutative-limit crossing energy: $i$ from quarter-turn travel " +
    "on the $\\mathrm{U}(1)$ phase tube",
  tags: [
    "crossing-energy",
    "commutative-limit",
    "u1",
    "phase-tube",
    "branch-phase",
    "isospin",
    "mass-tower",
    "interpretation",
  ],
  uses: [
    "def:crossing-energy",
    "def:commutative-qou",
    "prop:u1-equivariant-reduction",
    "rem:u1-phase-tube",
    "def:hyperelliptic-quintic",
  ],
  interprets: "def:crossing-energy",
  cites: ["satula1997"],
});
