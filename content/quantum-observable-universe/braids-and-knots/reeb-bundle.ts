import { definition } from "../../schema/builders";

export default definition({
  label: "def:reeb-bundle",
  lean: { ref: "qou:QOU.ReebBundle", validation: "not_checked" },
  title: "Reeb bundle over the exceptional divisor",
  tags: [
    "reeb-bundle", "exceptional-divisor", "hopf-fibration",
    "blow-up",
  ],
  uses: [
    "def:exceptional-divisor",
    "ex:q-reeb-vector-field",
  ],
});
