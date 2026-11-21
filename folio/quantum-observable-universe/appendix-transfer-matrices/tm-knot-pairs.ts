import { prose } from "../../schema/builders";

export default prose({
  label: "tm-knot-pairs",
  title: "Transfer matrices of knot pairs",
  uses: ["def:transfer-matrix-operator"],
  tags: [
    "transfer-matrix",
    "knot",
    "nuclear",
    "electromagnetic",
    "photon",
    "trivial",
    "appendix",
    "catalogue",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-20", body: "Owner ruling 2026-11-20 (option B of `docs/audits/2026-11-20-up-quark-electron-knot-clash.md`): a quark is an unknot strand of the pure Borromean braid $\\mathcal{B}_3$ (`def:up-quark`); $T_{2,3}$ and $T_{2,3}^{\\sigma}$ are the lepton partners of $\\mathfrak{u}$ and $\\mathfrak{d}$, not their knot types. The identification in this block was reworded on that date; its mathematics was not changed. Assumed: §2 and §4b–4c labelled each quark strand by its lepton partner's torus knot. Still valid: the matrices use only the crossing coefficients $(c, d)$ and no trefoil invariant, and $T_{nn} = T_{pp} - (q - q^{-1})\\mathbb{I}$ is the Hecke relation $\\sigma_i^{-1} = \\sigma_i - (q - q^{-1})$, so $T_{pp}$, $T_{nn}$, $T_{\\mathrm{mix}}$ read directly as the crossing letters $\\sigma_i$, $\\sigma_i^{-1}$ and their midpoint. Needs re-scoping: the derivation of $(c, d)$ in §2 from the trefoil pair, and the generation-2/3 pair labels in §4b–4c ($\\mathfrak{b}$ has lepton partner $T_{2,7}^{\\sigma}$ in the dictionary, not $T_{2,5}$)." },
  ],
});
