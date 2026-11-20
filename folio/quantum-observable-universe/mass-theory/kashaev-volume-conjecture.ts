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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ### Lean axiomatisation\n\nKVC is\nencoded in Lean as a **typeclass**\n\n```\nclass VolumeConjecture (q : ℝ) where\n  hypVolume       : Braid → ℝ\n  kashaevLimit    : Braid → ℝ\n  kvc_holds       : ∀ β, hypVolume β = kashaevLimit β\n  hypVolume_nonneg : ∀ β, 0 ≤ hypVolume β\n```\n\nThe class fields encode the conjectural identification of hyperbolic\nvolume with the Kashaev limit. Any instance of `VolumeConjecture` is\n**conjecture-bearing**: the `kvc_holds` field plays the role of\n`sorry`, but as an axiomatised class field rather than a tactic\nfailure. Downstream results that depend on KVC take it as an\n`[VolumeConjecture q]` typeclass argument and are then **fully\nverified** by Lean — the only unproved input is the class instance.\n\nThis is the same pattern used for `MassEvaluation` in\n[mass endomorphism tower](#prop:mass-endomorphism-tower): the\ncanonical computation is axiomatised so that the algebraic tower\nidentities are machine-checked.\n\n### Rationale for a class rather than an axiom\n\nThree reasons:\n\n1. **Locality.** A typeclass instance can be supplied per knot family\n   (figure-eight, torus, etc.) where KVC is actually proved; downstream\n   theorems then specialise to verified ground.\n\n2. **Compositionality.** A bridge theorem of the form\n   $\\Phi_q(V_S) = \\rho_q \\cdot \\mathrm{Vol}(K_S)$ depends only on KVC\n   restricted to $K_S$; the typeclass scope makes that dependency\n   visible in the type signature.\n\n3. **No global axiom pollution.** Mathlib's axiom audit\n   (`#print axioms`) records typeclass dependencies but does not flag\n   them as global axioms; the conditional nature of every downstream\n   result is preserved.\n\nThe conjecture itself remains open at the level of $\\pi_0$ —\nno claim of proof is made by introducing the class." },
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
