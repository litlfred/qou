import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cosimplicial-crossed-groupoid",
  title: "Proof of Cosimplicial crossed groupoid",
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "def:ccg-cosimplicial-identities",
    "lem:ccg-crossed-module-structure",
  ],
});
