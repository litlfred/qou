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
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Two quantities are both called N_v (owner chose to record this, 2026-11-20).** `conj:electroweak-higgs-torus-link-triplet` and `ElectroweakBringSchwingerBridge.lean` define $N_v = v/m_p \\approx 262.418$ ($q\\,\\tfrac{[2]_q}{2}[4]_q[6]_q[8]_q + 1/\\pi$ minus the 1-loop term), with no $\\mathcal{N}_{\\rm sym}$ factor. `computations/n_sym_numerical_anchor.py` defines $N_v = v/(E_\\times \\mu_0) = 3v/m_e \\approx 1.4455 \\times 10^6$ and divides by $\\prod_{k=2,3,4} [2k]_q^2/[2]_q \\approx 6782.9$ to get the anchor $\\mathcal{N}_{\\rm sym}(q_0) \\approx 213.11$. Under the block's $N_v$ the same quotient is $\\approx 0.0387$. So 213.11 exists only under the script's definition; it is also back-solved from $G_F$, so it is a fit either way. No numbers are changed here.",
      see: "computations/n_sym_numerical_anchor.py",
    },
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
