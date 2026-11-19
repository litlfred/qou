import { remark } from "../../schema/builders";

export default remark({
  label: "rem:breit-wheeler-observation",
  title: "Breit--Wheeler process: observation and comparison with the model selection rule",
  interprets: "rem:pair-creation-energy",
  uses: [
    "rem:breit-wheeler-vertex",
    "rem:pair-creation-energy",
  ],
  tags: [
    "breit-wheeler", "pair-creation", "polarisation",
    "STAR", "ATLAS",
    "cos2phi", "azimuthal-asymmetry",
  ],
  cites: ["star2021bw", "atlas2021bw"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-15",
      body:
        "**False comparison removed (owner F1(a), bean `qou-ccst`, PR #7825).** This block said the STAR/ATLAS anisotropy " +
        "was consistent with, and followed from, the Hecke selection rule, quoted a cos(2φ) amplitude of 10–15 %, and said " +
        "E₀ ≈ 2.27 MeV equals 2m_e plus ℏ_q ≈ 1.25 MeV. STAR (arXiv:1910.12400) reports cos 4Δφ = (16.8 ± 2.5) %, reproduced " +
        "by lowest-order QED (16.5 %), and QED gives nonzero parallel-polarisation pair production; ℏ_q = (q−1)/q ≈ 0.0991 " +
        "is dimensionless. The ATLAS sentence was not re-checked against the paper. The `testable` / `first-testable` tags " +
        "were dropped (owner H3). The bibliography title of `star2021bw` may not match PRL 127, 052302; not changed here.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/q_pinning_50_digit.py",
    witness: "computations/q-pinning-50-digit.witness.json",
    status: "verified",
  },
});
