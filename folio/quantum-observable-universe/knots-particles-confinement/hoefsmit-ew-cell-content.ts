import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell content of the far-commuting triple $(\\sigma_1, \\sigma_3, \\sigma_5)$: disjoint strand pairs and eight pure-pattern idempotents",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.hoefsmit_ew_cell_content",
    validation: "not_checked",
  },
  uses: ["def:braid-group", "prop:hoefsmit-seminormal-form"],
  tags: [
    "hoefsmit",
    "cell-content",
    "seminormal-form",
    "wedderburn-decomposition",
    "electroweak",
    "ew-triplet",
    "disjoint-strand-pair",
    "non-uniform-plancherel",
    "n-six",
    "closure-tier-b",
    "phase-2-sprint-5-discharge",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-21", body: "Moved out of the prose by the voice-leak drain (qou-d4kh, W14b, 2026-11-21): the counts are computed by the tableau and eigenvalue-class routines in `computations/probes/ew_interface_knot_probe.py`." },
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Statement cut to what the Lean proves (owner ruling 2026-11-20, option A of `docs/audits/2026-11-20-qa-fails-proposals.md` P1).** The theorem states four things, all proved sorry-free over a generic `CommRing R` with $q$ and $[2]_q$ invertible (`hoefsmit_ew_cell_content`, axioms `propext, Classical.choice, Quot.sound`): the strand pairs $\\{1,2\\},\\{3,4\\},\\{5,6\\}$ are pairwise disjoint and cover $\\{1,\\dots,6\\}$; the eight pure-pattern projectors are idempotent, pairwise orthogonal and sum to $1$; the six single/double-flip patterns sum to $1 - E(s,s,s) - E(a,a,a)$; and, for $k = 2,3,4$, the word $\\sigma^{2k}$ in $B_2$ has identity closure permutation (two closure components) and writhe $2k$ (`carrier_powers_closure_invariants`, via `QOU.Knot.BraidClosure`). The naming $W \\leftrightarrow \\sigma_1^4$, $Z \\leftrightarrow \\sigma_3^6$, $H \\leftrightarrow \\sigma_5^8$ and the torus-link reading $T(2,4), T(2,6), T(2,8)$ moved to `rem:hoefsmit-ew-cell-content-context`. That closure of $\\sigma^{2k}$ is $T(2,2k)$ is not stated as proved: the tree has no link-isotopy type with an independent torus-link construction (`QOU.BraidKnot.closure2` assigns `torusLink2` to $\\sigma^k$ by definition, and `QOU.Archimedean.RossoJonesGeneral` takes $T(r,s)$ to be the closure of $(s_0\\cdots s_{r-2})^s$), so against either it is the definition. The pattern multiplicities $(4,2,1,3,3,1,2,4)$ and the 20 pure tableaux are recorded as computed (re-run 2026-11-20 over the 76 standard tableaux of size 6, using the routines in `computations/probes/ew_interface_knot_probe.py`), not derived. The witness `computations/hoefsmit-ew-cell-content.witness.json` cited earlier does not exist in the tree.",
    },
    {
      kind: "status",
      body: "**Open.** The open inputs are: (1) the $W \\leftrightarrow \\sigma_1^4$, $Z \\leftrightarrow \\sigma_3^6$, $H \\leftrightarrow \\sigma_5^8$ identification, now a naming in `rem:hoefsmit-ew-cell-content-context` whose physical content is `conj:electroweak-higgs-torus-link-triplet` (and, for the boson-to-strand-pair assignment, `conj:categorical-higgs-mechanism`); (2) a closed-form generating function for the pure-pattern multiplicities; (3) refinement of `prop:weak-spectral-completeness` and `conj:weak-symmetric-normalization` to reference this $n = 6$ formulation.",
    },
  ],
});
