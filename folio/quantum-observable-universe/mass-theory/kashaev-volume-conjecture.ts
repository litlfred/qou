import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-volume-conjecture",
  title: "Kashaev volume conjecture (axiomatised as Lean class)",
  lean: {
    ref: "qou:QOU.Kashaev.VolumeConjecture",
    validation: "not_checked",
  },
  uses: [
    "def:archimedean-realization-functor",
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
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the conjecture is `class VolumeConjecture (q : ℝ)` with fields `hypVolume`, `kashaevLimit`, `kvc_holds`, `hypVolume_nonneg`; downstream results take `[VolumeConjecture q]`; the same pattern is `MassEvaluation`.",
    },
    {
      kind: "status",
      date: "2026-08-02",
      body:
        "THREE instances of this conjecture are now machine-proved " +
        "sorry-free in-repo. **Figure-eight**: " +
        "`(2π/N)·log⟨4₁⟩_N → 2·Cl₂(π/3) = Vol(4₁)` " +
        "(`QOU.Knot.FigureEightVolume.tendsto_log_kashaev_vol`, " +
        "`FigureEightVolumeSqueeze.lean`, milestone qou-cpfn). " +
        "**Borromean rings**: `(2π/N)·log⟨𝓑₃⟩_N → 8·Cl₂(π/2) = 8G = " +
        "Vol(𝓑₃)` (`tendsto_log_borromeanKashaev_vol`, " +
        "`BorromeanVolume.lean`, bricks B1–B5, bean qou-jor3; carrier " +
        "defined by the Habiro root-of-unity positive sum, GL2011 App. A " +
        "— the diagrammatic identification is the cited input). " +
        "**Whitehead 2-belt chain** `W_{a,2,1,0}`: " +
        "`(2π/(2M+1))·log P_M → 4·Cl₂(π/2) = 4G = Vol(𝓑₃)/2` (one " +
        "regular ideal octahedron; " +
        "`tendsto_log_whiteheadKashaev_vol`, `WhiteheadChainVolume.lean`, " +
        "bricks W1–W5, milestone qou-k49o; carrier is van der Veen's " +
        "Lemma-1 phase-free positive sum at odd N, arXiv:math/0611181, " +
        "anchor-verified transcription — the diagrammatic identification " +
        "is the cited input; the b=1 Whitehead link proper still needs " +
        "vdV's Lemma-4 Gaussian non-cancellation and remains open " +
        "in-repo). All three are elementary Riemann-sum squeezes against " +
        "the Clausen primitive — no Borel resummation. Per-link classes " +
        "`VolumeConjecture41` / `VolumeConjectureBorromean` / " +
        "`VolumeConjectureWhiteheadChain` carry sorry-free instances. The " +
        "GENERAL conjecture stated by this block remains open (8₁₁ is the " +
        "corpus's one remaining open instance); the per-family typeclass " +
        "rationale below is exactly the mechanism that lets proved " +
        "instances discharge downstream results while the general class " +
        "stays conjectural.",
    },
  ],
});
