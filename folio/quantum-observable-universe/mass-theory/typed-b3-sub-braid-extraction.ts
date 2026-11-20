import { remark } from "../../schema/builders";

export default remark({
  label: "rem:typed-b3-sub-braid-extraction",
  title:
    "Typed-$B_3$ sub-braid extraction reduces to the 2-strand chain via a single focused combinatorial axiom (`DominantSubBraidAtEps6`); composes to fully Lean-proved $c_3 = -2$",
  interprets: "prop:q-beta-c3-hopf-three-fold-markov",
  uses: ["rem:braid-link-types"],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-n-strand",
    "typed-b3",
    "sub-braid-extraction",
    "axiomatic-reduction",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_q_beta_operator_valued_N3.py",
    witness: [
      "computations/q-beta-operator-valued-N3.witness.json"
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): narrowing the open axiomatic content to a SINGLE focused\ncombinatorial fact.\n\n[...]\n\nβ_p (uud) and β_n (udd). The companion Lean development:\n\n1. Defines `TypedBraidWord3` matching the Python framework's\n   `atomic_braid_to_crossings` format.\n2. Defines `beta_p_typed`, `beta_n_typed` as explicit Lean lists.\n3. Proves both have length 11 (matching the Python recipe).\n4. Defines `subBraid` extraction by selecting crossing indices.\n5. Encodes the FINAL substantive axiom as a focused class field\n   `DominantSubBraidAtEps6` and **proves c_3 = -2 conditionally** on it.\n\n[...]\n\nUnder the single axiomatic input, the full chain is Lean-proved:\n\n[...]\n\nThe composed theorem `composed_track_C_c_3_eq_neg_two` is closed by\n`closure2_jones_at_one_sigma_sq_eq_neg_two` (already proved in\n[Concrete Lean braid and link types](#rem:braid-link-types)).\n\n[...]\n\n## The remaining axiom\n\nThe single open axiom is:\n\n> `DominantSubBraidAtEps6.dominant_subbraid_is_2_strand_2_crossings`:\n> the dominant\n\n[...]\n\nThe Lean discharge of this axiom requires:\n\n1. **`BraidGroup n` perturbative-expansion infrastructure**: define\n\n[...]\n\nSteps 1, 2, 4 are mechanical Lean infrastructure. Step 3 is the\nsubstantive combinatorial content.\n\n[...]\n\n## Cumulative atoms\n\nAfter this file:\n\n| step | content | Lean status |\n|---|---|---|\n| **Step C (canonical-equivalence axiom)** | exact arithmetic match | closed (item 2) |\n| **Step B (axiomatic closure map)** | two atomic axioms | closed |\n| **Step A 2-strand (concrete types)** | $\\sigma^2 \\to$ Hopf $\\to -2$ | closed |\n| **Step A n-strand (sub-braid extraction)** | composed under 1 axiom | closed conditionally |\n| **Remaining**: dominant-sub-braid combinatorial fact | empirically verified | open Lean-engineering |\n\nThe single remaining axiomatic content is a **specific combinatorial\nfact** about typed-braid sub-braid extraction, not a research-level\ncategorical question. Discharging it is substantial Lean work but no\nlonger at the categorical-frontier level." },
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "Lean stub: **no `sorry`s**. The chain is fully proved conditionally on\nthe single remaining axiom (`DominantSubBraidAtEps6`). All other\nsubstantive content is Lean-theorem-closed.",
    },
  ],
});
