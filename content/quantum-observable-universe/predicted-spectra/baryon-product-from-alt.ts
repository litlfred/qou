import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:baryon-product-from-alt",
  title:
    "The baryon integrand $\\prod_k dc_k/dz$ is the $\\mathrm{Alt}^3$-isotype of the color-tube Jacobian",
  cites: ["fulton1997", "macdonald1995"],
  uses: ["prop:atom-knot-mass-derivation"],
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
});
