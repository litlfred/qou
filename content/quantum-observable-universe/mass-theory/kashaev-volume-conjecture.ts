import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-volume-conjecture",
  title: "Kashaev volume conjecture (axiomatised as Lean class)",
  lean: {
    ref: "qou:QOU.Kashaev.VolumeConjecture",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-as-archimedean-realization",
    "def:quantum-bloch-group",
  ],
  cites: ["kashaev1997", "murakami-murakami2001", "zagier1986", "neumann-zagier1985"],
  tags: [
    "tier:famous",
    "kashaev",
    "volume-conjecture",
    "archimedean",
    "phi-q",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-26",
      body:
        "The **figure-eight instance** of this conjecture is now " +
        "machine-proved sorry-free in-repo: " +
        "`(2π/N)·log⟨4₁⟩_N → 2·Cl₂(π/3) = Vol(4₁)` " +
        "(`QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol`, " +
        "`FigureEightVolumeSqueeze.lean`, milestone qou-cpfn) — an " +
        "elementary Riemann-sum squeeze against the Clausen primitive, no " +
        "Borel resummation. The 4₁-specific class `VolumeConjecture41` " +
        "carries a sorry-free instance. The GENERAL conjecture stated by " +
        "this block (all hyperbolic knots) remains open; the per-family " +
        "typeclass rationale below is exactly the mechanism that lets the " +
        "proved 4₁ instance discharge downstream results while the general " +
        "class stays conjectural.",
    },
  ],
});
