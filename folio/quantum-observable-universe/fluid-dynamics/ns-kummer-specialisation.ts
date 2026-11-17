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
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**OPEN — trace identity.** The Kummer divisibility `n | chi(A)` is read off the obstruction class. If `chi(A)` means `chi_eu(M_0)` (the Euler-class integral) the statement is about the genus and survives a rename; if it means `tr(id_A)` it is undefined until a regularisation is fixed. Which reading the proof uses is not settled here. Under the owner ruling of 2026-09-15, `tr(id_A) = dim_q(A)` is a q-dependent quantum dimension, and `-6` is `chi_eu(M_0)`, the topological Euler characteristic of the base curve (`rem:three-euler-characteristics`). Flagged open on owner instruction 2026-11-17 (Bring foundations cleanup); the bare `chi(A)` here was not renamed because the step uses a trace identity, not only the genus. Bean `qou-qhcr`.",
    },
  ],
});
