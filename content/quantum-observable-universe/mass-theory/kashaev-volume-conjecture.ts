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
        "TWO instances of this conjecture are now machine-proved " +
        "sorry-free in-repo. **Figure-eight**: " +
        "`(2π/N)·log⟨4₁⟩_N → 2·Cl₂(π/3) = Vol(4₁)` " +
        "(`QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol`, " +
        "`FigureEightVolumeSqueeze.lean`, milestone qou-cpfn). " +
        "**Borromean rings**: `(2π/N)·log⟨𝓑₃⟩_N → 8·Cl₂(π/2) = 8G = " +
        "Vol(𝓑₃)` (`tendsto_log_borromeanKashaev_vol`, " +
        "`BorromeanVolume.lean`, bricks B1–B5, bean qou-jor3; carrier " +
        "defined by the Habiro root-of-unity positive sum, GL2011 App. A " +
        "— the diagrammatic identification is the cited input). Both are " +
        "elementary Riemann-sum squeezes against the Clausen primitive — " +
        "no Borel resummation. Per-link classes `VolumeConjecture41` / " +
        "`VolumeConjectureBorromean` carry sorry-free instances. The " +
        "GENERAL conjecture stated by this block remains open (8₁₁ is the " +
        "corpus's one remaining open instance); the per-family typeclass " +
        "rationale below is exactly the mechanism that lets proved " +
        "instances discharge downstream results while the general class " +
        "stays conjectural.",
    },
  ],
});
