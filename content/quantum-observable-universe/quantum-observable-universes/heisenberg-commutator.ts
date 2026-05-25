import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:heisenberg-commutator",
  label: "rem:heisenberg-commutator",
  title: "Heisenberg commutator and the Reeb fibre",
  tags: ["heisenberg", "uncertainty", "reeb", "fibre-coordinate"],
  uses: ["prop:heisenberg-commutator"],
  cites: [
    "heisenberg1958",
  ],
});
