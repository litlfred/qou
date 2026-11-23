import { remark } from "../../schema/builders";

export default remark({
  label: "rem:aromaticity-as-symmetric-projection",
  interprets: "prop:assembly-projector-exists",
  title: "Aromaticity, stability, and why breaking a ring releases a lot",
  uses: [
    "def:molecular-assembly-projector",
    "conj:ring-closure-barrier",
    "def:threading-link",
  ],
  tags: [
    "aromaticity",
    "stability",
    "binding-energy",
    "resonance",
    "irreducibility",
    "ring-closure",
  ],
});
