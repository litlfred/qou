import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:chirality-from-frobenius-self-pairing",
  label: "rem:chirality-from-frobenius-self-pairing-scope",
  title:
    "Scope, structural value, and open ribbon-closure derivation of the chirality factor",
  uses: [
    "prop:chirality-from-frobenius-self-pairing",
    "thm:frobenius-codim-universal",
  ],
  tags: ["chirality", "frobenius", "scope", "ribbon-category", "open-problem"],
});
