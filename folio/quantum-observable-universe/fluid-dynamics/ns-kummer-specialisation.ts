import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ns-kummer-specialisation",
  lean: { ref: "qou:QOU.FluidDynamics.ns_kummer_specialisation", validation: "not_checked" },
  title:
    "Kummer specialisation: the NS obstruction survives $q = 1$ for $\\gcd(\\chi(A), n) \\neq n$",
  uses: [
    "rem:substrate-gm-torsion",
    "prop:ns-obstruction-computation",
    "conj:qou-p-neq-np",
    "thm:ns-singularity-descartes",
    "rem:skein-filtration-trichotomy",
  ],
  cites: ["aaronsonwigderson2009", "grochow2017"],
  tags: [
    "kummer",
    "specialisation",
    "etale",
    "obstruction",
    "divisibility",
    "euler-characteristic",
  ],
});
