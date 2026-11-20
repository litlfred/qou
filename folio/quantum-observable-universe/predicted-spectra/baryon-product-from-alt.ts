import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:baryon-product-from-alt",
  title:
    "The baryon integrand $\\prod_k dc_k/dz$ is the $\\mathrm{Alt}^3$-isotype of the color-tube Jacobian",
  cites: ["fulton1997", "macdonald1995"],
  uses: ["conj:atom-knot-mass-derivation"],
  defines: [],
  tags: [
    "schur-weyl",
    "alternating-representation",
    "wedderburn",
    "frobenius-pairing",
    "color-tube",
    "vandermonde",
    "baryon",
    "categorical",
    // Was `chapter: "archimedean-universe"`, a PRE-SPLIT declaration that the
    // restructure made stale. `archimedean-universe` was a real chapter: the
    // top manifest still records the plan -- "Phase 4+5 (TBD) will split
    // braids-and-knots and archimedean-universe into focused destination
    // chapters" -- and `e32d978dbf` (2026-05-25) carried it out, "split
    // archimedean-universe into brings-surface + predicted-spectra".
    //
    // So this block is already IN one of the two destinations, and
    // `predicted-spectra` is annotated in the manifest as "split from
    // archimedean-universe". The placement is the outcome of the split; the
    // declaration is what the split left behind. It survived because
    // `chapter:` is on no schema -- the key was stripped before anything
    // downstream saw it, so no rename pass and no validator ever touched it.
    //
    // The archimedean provenance is real and worth keeping, so it moves to
    // the field that carries it here (cf. brings-surface/archimedean-leptons.ts,
    // which tags it the same way). `lean.ref` still points at
    // QOU.Archimedean.baryonProductFromAlt. qou #5115 / beans `qou-j3m4`.
    "archimedean-universe",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.baryonProductFromAlt",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-20",
      body: "**Demoted to `conjecture` (owner, 2026-11-20, bean `qou-6qbv`; W8, full cascade).** `terms-2-6-higher-operations` and `spectral-sequence-h3-explicit` (formerly `prop:`) state open research claims (the Term 2/6 Wedderburn/residue identifications; the explicit $d_1, d_2$ on $H_3$) whose Lean siblings carried them on context-class fields any instance could satisfy. Both were demoted, and by the conjectural-propagation rule (AGENTS.md §3b) so was every provable block whose `uses[]` cone reaches them. The owner chose the full cascade over dropping citational edges. Label prefix changed to `conj:`. Nothing in the mathematics or the Lean of this block changed.",
    },
  ],
});
