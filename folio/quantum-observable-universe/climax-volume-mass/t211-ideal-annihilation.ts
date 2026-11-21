import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Representation-theoretic refinement.** The privileged role of $T_{2,3}$ and $T_{2,5}$ atop the embedding table attains a representation-theoretic footing under the weight identification of [prop:x5-bring-weight-identification](#prop:x5-bring-weight-identification). Passing to the hyperelliptic quintic $\\mathcal{X}_5$ of [thm:hyperelliptic-z5-classification](#thm:hyperelliptic-z5-classification), the non-trivial $\\mathbb{Z}_5$-isotypical part of $H^1(\\mathcal{X}_5, \\mathbb{Q})$ manifests exactly as the 4-dim character sum $\\chi_1 \\oplus \\chi_2 \\oplus \\chi_3 \\oplus \\chi_4$. The Seifert surface of $T_{2,5}$ fills this representation completely ($g(T_{2,5}) = 2 = \\dim_{\\mathbb{C}} J(\\mathcal{X}_5)$), while $T_{2,3}$ occupies only a 2-dim sub-isotype. See [rem:weight-identification-consequences](#rem:weight-identification-consequences) for details." },
  ],
  interprets: "prop:vertex-algebra-jet-relations",
  label: "rem:t211-ideal-annihilation",
  title: "Behaviour of $T_{2,11}$ on the jet bundle ideals",
  tags: [
    "torus-knot", "genus-bound", "spectral-filter",
    "hecke-algebra", "knot-coordinates", "ideal",
  ],
  uses: [
    "prop:genus-filtration-ideal",
    "prop:vertex-algebra-jet-relations",
    "prop:shell-structure-eigenvalues",
    "prop:x5-bring-weight-identification",
    "thm:hyperelliptic-z5-classification",
  ],
  cites: ["kassel1995", "jones1987"],
});
