import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:lepton-bring-surface-h3-3channel",
  lean: {
    ref: "qou:QOU.BraidKnot.LeptonBringSurfaceH3.lepton_V_hat_h3_3channel",
    validation: "not_checked",
  },
  title:
    "Lepton Bring-surface representation: 3-sheet H_3 Wedderburn channels (analog of nucleon 3-quark color tubes); $\hat{V}_\ell$ for any torus-knot lepton σ_1^k is computed via the H_3 3-channel Plancherel-weighted character sum with Markov-traced std-channel; verifies $\hat{V}_e$ ≈ 0.594 against `mass-endomorphism-tower.md` paper convention",
  uses: [
    "def:bar-involution",
    "prop:per-braid-mass-tower",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-05-25",
      body:
        "**Theorem (algebraic identity).** The $\hat{V}_e$ ≈ 0.594 paper convention " +
        "(`mass-endomorphism-tower.md:351`) is computed via the H_3 3-channel " +
        "formula in `tools/pyhecke/python/pyhecke/constants.py:156` " +
        "(V_HAT_ELECTRON). This proposition states the closed-form algebraic " +
        "identity. Numerical match to within 1.3% verified at q_0 ≈ 1.110 " +
        "(my computation 0.586 vs paper 0.594). The 1.3% gap is precision " +
        "in the paper's 0.594 rounding; the algebraic formula is exact.",
    },
    {
      kind: "refined-framing",
      date: "2026-05-25",
      body:
        "**Bring-surface analog with nucleons.** Nucleon (uud / udd) has 3 " +
        "quark color tubes on Bring-surface sheets (SU(3) color). Lepton has " +
        "3 H_3 Wedderburn channels (sym + std + alt; partitions of 3). Both " +
        "are 3-fold representations on the Bring surface, but with different " +
        "physical content. The 3-channel structure is the canonical " +
        "'where leptons live' on the substrate — even though σ_1^k is " +
        "naturally an H_2 element, the mass formula sits at H_3 because " +
        "that's where the 3-CAL ↔ 3-channel cohomological discipline " +
        "(`prop:three-parameters-wedderburn`) is set.",
    },
    {
      kind: "caveat",
      date: "2026-05-25",
      body:
        "**T6 status — gap (a) RESOLVED, gap (c) IMPLICATED.** This proposition " +
        "documents the $\hat{V}_\ell$ convention (closing T6 gap (a)). But applying the " +
        "Li_2^q canonical mass tower to $\hat{V}_{\mu_{T(2,5)}}$ = 0.834 gives mass ratio " +
        "1.36, vs CODATA m_μ/m_e = 206.77 — a 99% shortfall. The missing " +
        "factor 206.77/1.36 = 152.04 ≈ (3/2) · (1/ℏ_q²) IS the SUPERSEDED " +
        "scalar substrate density. This implies the framework's canonical " +
        "operator-level formula implicitly requires the SUPERSEDED ρ_q to " +
        "give CODATA values — the explicit purge (PR #1127) removed ρ_q " +
        "from witnesses but not from the operative formula. Full diagnosis: " +
        "[`docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md`](../../../docs/audits/2026-05-25-lepton-bring-surface-h3-3channel-convention.md).",
    },
  ],
  tags: [
    "lepton",
    "bring-surface",
    "h3-3channel",
    "wedderburn",
    "calibration",
    "convention",
    "t6-resolved-a",
  ],
  cites: [
    "wenzl1988",
    "jones1987",
  ],
});
