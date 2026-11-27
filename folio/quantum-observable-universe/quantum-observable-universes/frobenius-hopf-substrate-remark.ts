import { remark } from "../../schema/builders";

export default remark({
  label: "rem:frobenius-hopf-aether-remark",
  renamedFrom: ["rem:frobenius-hopf-substrate-remark"],
  title: "The counit, the antipode and self-duality of the aether",
  interprets: "def:frobenius-hopf-aether",
  uses: ["def:frobenius-hopf-aether", "def:quantum-universe", "def:quantum-observable-universe"],
  tags: ["frobenius", "hopf-algebra", "substrate", "vacuum"],
});
