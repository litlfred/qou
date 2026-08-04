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
    {
      kind: "status",
      date: "2026-08-02",
      body:
        "**Conditional theorem (§3b-cond), sorry-free; theorem for 4₁.** Lean " +
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
  ],
});
