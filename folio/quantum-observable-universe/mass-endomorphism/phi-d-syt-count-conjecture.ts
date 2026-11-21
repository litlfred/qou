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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Lean theorems exported\n\n| Theorem | Content |\n|---|---|\n| `chi_V3_numerator_matches` | Conjecture's $V_{(3)}$ numerator equals proved closed-form numerator |\n| `chi_V21_numerator_matches` | Conjecture's $V_{(2,1)}$ numerator equals proved closed-form numerator |\n| `chi_V111_numerator_matches` | Conjecture's $V_{(1,1,1)}$ numerator equals proved closed-form numerator |\n| `class PhiD4FConjecture (n λ_syt_count q)` | Abstract conjecture class with $d_\\lambda$ field and residual (no instances) |\n\nThese theorems are closed by `ring` after unfolding." },
    {
      kind: "status",
      body: "**n = 3 fully verified** in Lean. **n $\\ge$ 4 open** — concrete next\nprobe is the B_4 typed-braid character difference at each of the\nfive irreps, testing whether the predicted $\\Phi_4, \\Phi_{12}, \\Phi_8$\nfactors appear.",
    },
  ],
});
