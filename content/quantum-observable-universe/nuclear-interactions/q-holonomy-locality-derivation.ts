import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-holonomy-locality-derivation",
  title:
    "Derivation: locality from flatness of the KZ connection",
  interprets: "conj:lifted-crossing-locality",
  tags: [
    "kz-connection",
    "flatness",
    "monodromy",
    "quantum-group",
    "kohno-drinfeld",
    "locality-derivation",
  ],
  uses: ["rem:soft-confinement-at-q0"],
  cites: ["kohno1987"],
});
