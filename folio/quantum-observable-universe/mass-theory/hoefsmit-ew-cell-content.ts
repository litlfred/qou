import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hoefsmit-ew-cell-content",
  title:
    "Hoefsmit cell-content identification of the EW triplet inside $\\mathrm{End}_R(V^{\\otimes 6})$ (categorical existence)",
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
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Lean sibling made content-bearing (QA re-adjudication 2026-11-20).** The sibling previously carried `EWIdempotentsIdentified : Prop := True` and two predicates that were only index inequalities closed by `decide`, with an unused `q`. It now proves, sorry-free over a generic `CommRing R` with $q$ and $[2]_q$ invertible: the carrier strand pairs $\\{1,2\\},\\{3,4\\},\\{5,6\\}$ are pairwise disjoint and cover $\\{1,\\dots,6\\}$; in any commutative $R$-algebra containing three Hecke generators the eight pure-pattern projectors are idempotent, pairwise orthogonal and sum to $1$; the six single/double-flip patterns sum to $1 - E_{sss} - E_{aaa}$ (`hoefsmit_ew_cell_content`, axioms `propext, Classical.choice, Quot.sound`). The idempotent algebra reuses `QOU.Conjectures.WeakSpectralCompleteness`. The `True` field is removed, not replaced: that the six patterns are the $W^\\pm, Z^\\pm, H^\\pm$ carriers is a naming, not a Lean claim. `lean.ref` previously named the generic `HoefsmitSeminormalBasis` class; it now names this block's own theorem. `uses[]` cannot list `conj:electroweak-higgs-torus-link-triplet` or `prop:weak-spectral-completeness` without a cycle (both depend on this block). Whether this block should stay a `theorem` is put to the owner in `docs/audits/2026-11-20-qa-fails-proposals.md`.",
    },
    {
      kind: "status",
      body: "**Open.** The Hoefsmit cell-content arithmetic is correct\n(verified by the witness enumeration); the open inputs are:\n\n1. **The $W \\leftrightarrow \\sigma_1^4$, $Z \\leftrightarrow \\sigma_3^6$,\n $H \\leftrightarrow \\sigma_5^8$ identification** — currently a\n structural proposal motivated by disjoint-strand-pair commutativity\n plus matching twist parameters $k = 2, 3, 4$ to the EW link triplet.\n Needs a categorical-physics block (the \"categorical Higgs mechanism\"\n item from\n `conj:force-carrier-knot-vs-link-dichotomy`\n §Status) discharging the boson-to-strand-pair assignment.\n2. **The non-uniform Plancherel weight derivation** — the\n multiplicities $(2, 1, 3, 3, 1, 2)$ are read off from the\n tableaux enumeration; promoting them to a closed-form\n $q$-rational requires identifying their generating function in\n the Hoefsmit cell-content arithmetic.\n3. **Refinement of upstream blocks** — the existing\n [`prop:weak-spectral-completeness`](#prop:weak-spectral-completeness)\n and\n [`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)\n should be edited to reference this $n = 6$ formulation.",
    },
  ],
});
