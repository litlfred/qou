import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:stokes-dt-bps-bridge",
  title:
    "Resurgent Stokes constants are Donaldson--Thomas / BPS degeneracies (the closed-sector state-integral bridge, GGM Conjecture 3(d) + GPPV)",
  lean: {
    ref: "qou:QOU.QBeta.StokesDTBPSBridge",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/probes/aomega_bps_sector_nondegeneracy.py",
    witness: "computations/probes/aomega-bps-sector-nondegeneracy.witness.json",
    status: "verified",
  },
  uses: ["conj:im-q-physical-role"],
  cites: [
    "garoufalidis2013",
    "bridgeland2016",
    "garoufalidis-gu-marino2023peacock",
    "gukov-pei-putrov-vafa2017",
    "dimofte-gaiotto-gukov2013",
    "dimofte-gaiotto2011",
    "murakami-y2022",
    "gukov-stosic2012",
    "kucharski-reineke-stosic-sulkowski2017",
    "singh-physrevd108106023",
  ],
  tags: [
    "tier:famous",
    "stokes-constant",
    "donaldson-thomas",
    "bps-states",
    "3d-3d-correspondence",
    "a-omega",
    "conditional-adoption",
    "axiom-class",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the bridge is `class QOU.QBeta.StokesDTBPSBridge (Knot)` with fields `stokesConstant`, `dtInvariant`, `bpsDim`, `stokes_eq_dt`, `dt_eq_bps`; no instance is supplied; downstream results take `[StokesDTBPSBridge Knot]`.",
    },
    {
      kind: "status",
      date: "2026-08-02",
      body:
        "**Adopted conjecture (Vol-conjecture-style), theorem for 4₁.** GGM " +
        "peacock (`garoufalidis-gu-marino2023peacock`, 2012.00062) " +
        "Conjecture 3(d) — *the Stokes constants are integers corresponding " +
        "to the Donaldson–Thomas invariants and the BPS degeneracies* — is a " +
        "**theorem for the figure-eight 4₁**; GPPV " +
        "(`gukov-pei-putrov-vafa2017`) realise that DT/BPS count as the graded " +
        "dimension of the BPS Hilbert space of T[M₃]. Adopting this identifies " +
        "the G3 Stokes integer A_ω=3 as a BPS/DT count (see " +
        "[`thm:aomega-fourone-dt-count`](aomega-fourone-dt-count.md)). NOT " +
        "wired to production (L2 / Q_β untouched); the general conjecture (all " +
        "hyperbolic knots) is open.",
    },
    {
      kind: "caveat",
      date: "2026-08-02",
      body:
        "**This is the CLOSED / state-integral BPS sector, NOT the open-HOMFLY " +
        "Gukov–Stošić bridge.** Non-degeneracy check (this PR, witness " +
        "`aomega-bps-sector-nondegeneracy`): the *open* BPS-states bridge of " +
        "Gukov–Stošić (`gukov-stosic2012`, 1112.0030 — knot homology = open " +
        "BPS states on the conormal Lagrangian) gives, via the knots–quivers " +
        "correspondence (`kucharski-reineke-stosic-sulkowski2017`), a 4₁ count " +
        "of det(4₁)=5 (five HOMFLY generators / five quiver nodes; trefoil " +
        "calibration = 3 = det 3₁). 5 ∉ {3,4}, so the open-HOMFLY bridge does " +
        "NOT reproduce the GGM resurgent-Stokes spectrum {3,4} and does NOT " +
        "license A_ω=3. The two BPS sectors (open HOMFLY vs closed Ẑ / " +
        "state-integral) are distinct. Only the closed-sector bridge above " +
        "reproduces {3,4}/reduced-3.",
    },
  ],
});
