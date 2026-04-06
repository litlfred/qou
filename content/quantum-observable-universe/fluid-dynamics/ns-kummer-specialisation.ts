import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-kummer-specialisation",
  title:
    "Kummer specialisation: the NS obstruction survives $q = 1$ for $\\gcd(\\chi(A), n) \\neq n$",
  uses: [
    "rem:substrate-gm-torsion",
    "prop:ns-obstruction-tower",
    "prop:ns-obstruction-computation",
    "thm:qu-to-qou",
    "def:quantum-characteristic-classes",
    "conj:levi-degeneracy",
  ],
  tags: [
    "kummer",
    "specialisation",
    "etale",
    "obstruction",
    "divisibility",
    "euler-characteristic",
  ],
});
