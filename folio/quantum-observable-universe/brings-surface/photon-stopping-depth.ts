import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:photon-stopping-depth",
  title: "The photon stopping depth is $\\lfloor n^2/4 \\rfloor$",
  uses: ["prop:photon-filtration-depth-bounds"],
  tags: ["photon", "hecke-algebra", "filtration", "open-problem", "conjectural-framing"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Evidence: exact modular rank in $H_n(q)$ for $n = 3, 4, 5, 6$ gives $L(n) = 2, 4, 6, 9 = \\lfloor n^2/4 \\rfloor$ (two primes, random $q$; full rank certified, non-fullness one step earlier probabilistic). $L(3) = 2$ is proved in Lean. Pre-registered as P14/P15 in the audit §12.0 before computing.",
    },
  ],
});
