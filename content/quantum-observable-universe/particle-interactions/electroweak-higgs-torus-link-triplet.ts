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
  ],
  authorNotes: [
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
      kind: "caveat",
      date: "2026-07-05",
      body:
        "TENSION FLAGGED FOR OWNER (σ₅⁸ = B vs H). weinberg-angle-categorical " +
        "reads σ₅⁸ as the U(1)_Y singlet B (pre-mixing); this block reads σ₅⁸ " +
        "(= T(2,8)) as H. Both bar-even/A+ singlet-like, but B and H are " +
        "distinct particles. Needs an owner ruling; not silently resolved.",
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
