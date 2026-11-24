import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cfs-comparison-summary",
  title:
    "External comparison: Causal Fermion Systems share carrier and universality class with QOU but are a distinct continuum theory",
  interprets: "rem:non-commutative-probability-dictionary",
  cites: [
    "finster2021",
    "finster2022",
    "finster2024",
    "biane1998",
  ],
  tags: [
    "causal-fermion-systems",
    "external-comparison",
    "free-probability",
    "summary",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Adjudicated qou-0irt: removed unused `dappiaggi2024` (PDF not held in `library/`) from `cites` and wired explicit `\\cite` calls for `finster2021`, `finster2022`, `finster2024`, and `biane1998` in the block prose.",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Bean qou-vfl4: separated external CFS definitions from QOU's own comparison reconstruction. `finster2021`, `finster2022`, and `finster2024` source the finite-rank spinor operator representation on H and the eigenvalue-difference causal Lagrangian on x*y; `biane1998` sources large-rank symmetric-group Plancherel free-probability asymptotics; the normalized finite type II_1 tracial comparison framing and the elementary variance identity (1/(4n^2)) sum_{i,j} (|lambda_i| - |lambda_j|)^2 = G_2(x,y) - ||x*y||_1^2 are QOU's own algebraic translation.",
    },
  ],
});
