import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electroweak-higgs-torus-link-triplet",
  title:
    "$(W^\\pm, Z, H) \\leftrightarrow (T(2,4), T(2,6), T(2,8))$ — non-Bring even-twist 2-component torus-link triplet",
  lean: {
    ref: "qou:QOU.ParticleInteractions.EWHiggsTorusLinkTriplet",
    validation: "not_checked",
  },
  uses: [
    "prop:electroweak-triplet-bring-embedding",
    "thm:ew-triplet-far-commuting-minimal",
    "thm:ew-triplet-charge-spin-from-involution",
    "def:spin-involution",
    "prop:force-carrier-bring-uniqueness",
    "prop:torus-knot-genus-four-unique",
    "conj:n-v-bring-action",
    "def:hecke-normal-form",
    "rem:hecke-algebra-from-braiding",
    "def:coulomb-charge",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): As formalized in [`QOU/StandardModel/ElectroweakBringSchwingerBridge.lean`](../lean/QOU/StandardModel/ElectroweakBringSchwingerBridge.lean) and verified at 50 dps in [`electroweak_bring_schwinger_bridge_probe.py`](../../../computations/probes/electroweak_bring_schwinger_bridge_probe.py): | `ewFixedPoint_iff_cubic` | conditional on `ElectroweakVevFixedPointClass` | the first-principles derivation of `ElectroweakVevFixedPointClass`" },
    {
      kind: "status",
      date: "2026-07-05",
      body:
        "Top node of the electroweak identification conjecture lattice, " +
        "NARROWED 2026-07-05 (Lean file: four §3b classes — C1 selection " +
        "[primary, physics postulate only], C2 enumeration [dependent on C1], " +
        "C_sector sector assignment [primary], C_top identification " +
        "[dependent on C1/C_sector]). The genus / enumeration / far-commuting " +
        "minimality half is discharged to the sorry-free " +
        "`prop:electroweak-triplet-bring-embedding` + " +
        "`thm:ew-triplet-far-commuting-minimal`. Charge and spin (the former " +
        "C3, C4 — previously two independent open primary conjectures) are now " +
        "PROVED consequences of the single sector postulate via " +
        "`thm:ew-triplet-charge-spin-from-involution` (spin involution " +
        "def:spin-involution: H in A+ => scalar+neutral; W± in A- => vector " +
        "T3=±1; Z in A- vector neutral via Weinberg mixing). Residual: C1 " +
        "selection (strong corpus grounding, genus-4 saturation of " +
        "{T(2,9),T(3,5)}) + the sector assignment + bare label map.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "σ₅⁸ = B vs H bar-grading is now DERIVED-FROM-SPIN, not merely stated " +
        "(Task 2, 2026-07-05). The slot σ₅⁸ (= T(2,8)) carries BOTH gauge " +
        "bosons, bar-graded: Higgs BOSON H = A+ (bar-even, scalar), B (U(1)_Y " +
        "hypercharge) = A- (bar-odd, vector). Formerly an owner ruling, this is " +
        "now the sorry-free `ew_sigma5_bargrade_forced` in " +
        "thm:ew-triplet-charge-spin-from-involution: the sector→spin map is " +
        "injective and inverts (spin ⇒ sector), so H scalar (spin 0) ⇒ A+ and " +
        "B vector (spin 1) ⇒ A- are FORCED. Residual postulate: only that both " +
        "inhabit the one σ₅⁸ slot. weinberg-angle-categorical (reads A- = B) and " +
        "this block (reads A+ = H) agree by derivation. 4₁ in " +
        "self-dual-higgs-real-volume is the Higgs MASS MECHANISM (muon scale " +
        "m_μ/m_e = Vol(4₁)/ℏ_q²), NOT the 125-GeV boson H = T(2,8) = A+.",
    },
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Task 1 (which-slot-is-W) HONEST — W = σ₁⁴ is a FREE LABEL, not forced. " +
        "Corpus has no crossing→charge principle that selects the neutral slot: " +
        "def:coulomb-charge Q = ½·writhe on σ₁^{2k} gives Q = k > 0 for all " +
        "three carriers (makes W,Z,H all charged); writhe→Y falsified " +
        "(2026-06-02-u1-hypercharge-assignment.md; only writhe→I₃ survives). " +
        "Proved sorry-free: which_slot_is_W_free (two labelings W=σ₁⁴ and " +
        "mirror W=σ₃⁶ both admissible). The crossing→isospin label is now an " +
        "explicit content-bearing free-label field `t3Label` on EWSectorAssignment " +
        "(w_charged: t3Label 2 = 1 is the paper's choice; z_neutral, higgs_neutral). " +
        "Paper's W=σ₁⁴ rests only on mass ordering 4<6<8 (necessary, not " +
        "sufficient). Forcing it needs a genuine crossing/linking→T₃ map the " +
        "framework does not yet supply.",
    },
  ],
  computation: {
    engine: "python",
    script: "computations/probes/ew_higgs_sdp_probe.py",
    witness: "computations/probes/ew-higgs-sdp-probe.witness.json",
    status: "verified",
  },
  tags: [
    "electroweak",
    "higgs",
    "torus-link",
    "non-bring",
    "psd-feasibility",
    "weak-sector",
    "force-carrier",
    "open-problem",
  ],
});
