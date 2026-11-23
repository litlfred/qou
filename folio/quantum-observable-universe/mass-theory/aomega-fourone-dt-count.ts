import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:aomega-fourone-dt-count",
  title:
    "The figure-eight Stokes integer $A_\\omega(4_1) = 3$ is a BPS/DT count (conditional on the Stokes--DT--BPS bridge)",
  lean: {
    ref: "qou:QOU.QBeta.aomega_fourOne_dt_count",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/probes/aomega_bps_sector_nondegeneracy.py",
    witness: "computations/probes/aomega-bps-sector-nondegeneracy.witness.json",
    status: "verified",
  },
  uses: ["conj:stokes-dt-bps-bridge"],
  cites: [
    "garoufalidis-gu-marino2023peacock",
    "gukov-pei-putrov-vafa2017",
  ],
  tags: [
    "a-omega",
    "stokes-constant",
    "donaldson-thomas",
    "bps-states",
    "figure-eight",
    "conditional-on-class",
    "g3-keystone",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): $W_{-1}(0)$ in [`QOU.QBeta.StokesQZeroDTCount`](#conj:im-q-physical-role). Composing," },
    {
      kind: "status",
      date: "2026-08-02",
      body:
        "**Conditional theorem (§3b-cond), sorry-free.** Lean " +
        "`QOU.QBeta.aomega_fourOne_dt_count` derives `bpsDim(4₁) = 3` through " +
        "the two `StokesDTBPSBridge` fields plus the bridge-independent " +
        "certified q→0 Stokes datum `S⁺(0)₀₁ = 3` " +
        "(`QOU.QBeta.StokesQZeroDTCount.stokes_qzero_offdiagonal`). The class " +
        "supplies the identifications (inputs); the value 3 comes from the " +
        "certified computation, not a class field — non-degenerate. lean-direct " +
        "exit 0. NOT wired to production (L2 / Q_β untouched). Internal " +
        "derivation of 3 from the QOU categorical drivers remains open " +
        "(`qou-qnnq`).",
    },
    {
      kind: "status",
      date: "2026-10-10",
      body:
        "**Scope corrected: conditional for 4₁ too.** The earlier status read " +
        "\"theorem for 4₁\" on the ground that GGM proved peacock Conjecture 3 " +
        "for the figure-eight. The held paper (library/arxiv-2012.00062v3) keeps " +
        "Conjecture 3, including (d), a conjecture; it proves Conjecture 5 for " +
        "4₁ and 5₂ (Theorem 6) and verifies Conjecture 4 by computation. No " +
        "bridge instance is discharged, so the result is conditional for every " +
        "knot. The Lean (conditional on the class) is unchanged. Owner-approved " +
        "2026-10-10; bean qou-3ent.",
    },
  ],
});
