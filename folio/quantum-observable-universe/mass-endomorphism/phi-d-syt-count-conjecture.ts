import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-d-syt-count-conjecture",
  interprets: "rem:chi-per-irrep-cyclotomic-closed-forms",
  title:
    "Conjecture: per-irrep character differences factor via $\\Phi_{4 f_\\lambda}(q)$, where $f_\\lambda$ is the SYT count — verified at $n=3$ for $V_{(3)}, V_{(2,1)}, V_{(1,1,1)}$; predicts cyclotomic structure at all $n$",
  uses: ["rem:chi-per-irrep-cyclotomic-closed-forms"],
  cites: [
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
    "kassel1995",
  ],
  tags: [
    "lean-infrastructure",
    "conjecture",
    "cyclotomic",
    "syt-count",
    "per-wedderburn-block",
    "generalization",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
    {
      kind: "status",
      body: "**n = 3 fully verified** in Lean (`chi_V3_numerator_matches`, `chi_V21_numerator_matches`, `chi_V111_numerator_matches`, `PhiD4FConjecture`, `phiDConj_V3`, `phiDConj_V21`, `phiDConj_V111`). **n $\\ge$ 4 open** — concrete next\nprobe is the B_4 typed-braid character difference at each of the\nfive irreps, testing whether the predicted $\\Phi_4, \\Phi_{12}, \\Phi_8$\nfactors appear.",
    },
  ],
});
