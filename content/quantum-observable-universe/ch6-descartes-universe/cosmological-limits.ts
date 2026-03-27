import { example } from "../../schema/builders";

export default example({
  interprets: "def:quantum-observable-universe",
  label: "ex:cosmological-limits",
  title: "Cosmological limits of $q$",
  tags: ["cosmology", "limits"],
  uses: [
    "def:quantum-observable-universe",
    "def:frobenius-pairing",
    "def:substrate-parameter",
    "rem:hopf-non-cocommutativity",
  ],
});
