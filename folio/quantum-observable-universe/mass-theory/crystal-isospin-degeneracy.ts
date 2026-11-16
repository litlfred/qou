import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:crystal-isospin-degeneracy",
  title:
    "Crystal-limit isospin degeneracy: $S_{\\mathrm{crystal}}$ is invariant under $\\sigma_i \\leftrightarrow \\sigma_i^{-1}$",
  lean: {
    ref: "qou:QOU.BraidKnot.crystal_isospin_degeneracy",
    validation: "not_checked",
  },
  uses: [
    "conj:crystal-graph-realization",
    "prop:content-scaling-correspondence",
    "prop:spin-involution-lp-dual-invariance",
  ],
  tags: [
    "crystal-limit",
    "term-7",
    "isospin",
    "tritium",
    "helium-3",
    "shadow-price",
    "q-curvature",
    "shell-correction",
  ],
  cites: ["kashiwara1991", "lecouvey2007"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The proof previously derived $\\sigma_i^{-1} = \\sigma_i$ on each SYT line from the Hecke relation at $q = 0$. That step was false: $q^{-1}$ is undefined at $q = 0$, and at generic $q$ the eigenvalues of $\\sigma_i$ and $\\sigma_i^{-1}$ differ. The equality is an input of the crystal model (the `abs(i)` reduction), so the proposition is a statement about that model, not about $H_n(q)$. The statement previously said the limit cannot distinguish proton from neutron 'inside the bare Hecke algebra'; corrected to 'inside the crystal model'. The bridge `CrystalGraphRealization ⟹ CrystalEigenlineSignBlind` is not proved.",
    },
    {
      kind: "status",
      body: "This proposition is **conditional on**\n[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)\n(the conjectural identification of the $q \\to 0$ limit of\n$\\chi^\\lambda$ with the signed-permutation action on\n$\\mathrm{SYT}(\\lambda)$ used by\n[`term7_alpha5_crystal_derivation.py`](../../../computations/term7_alpha5_crystal_derivation.py)).\nThe Lean formalisation extracts only the per-eigenline content of\nthis conjecture into a smaller class\n$[\\mathrm{CrystalEigenlineSignBlind}\\;R]$ (`crystal-isospin-degeneracy.lean`),\nwhich axiomatises the *single* fact required for this proposition\n— that on every SYT eigenline, the $q = 0$ actions of $\\sigma_i$\nand $\\sigma_i^{-1}$ agree.  The class\n$[\\mathrm{CrystalGraphRealization}\\;R\\;q]$ (Lake-tracked in\n`QOU.BraidKnot.CrystalGraphRealization`) implies\n$[\\mathrm{CrystalEigenlineSignBlind}\\;R]$, so this proposition is\na *downstream consequence* of `conj:crystal-graph-realization`\nunder AGENTS.md §3b-cond conditional-class semantics.  Modulo the\nupstream conjecture, the equality\n$S_{\\mathrm{crystal}}(T) = S_{\\mathrm{crystal}}({}^3\\mathrm{He})$\nis **exact** under the legacy disjoint-product convention, and\nthe proposition itself is a fully verified Lean theorem.",
    },
  ],
});
