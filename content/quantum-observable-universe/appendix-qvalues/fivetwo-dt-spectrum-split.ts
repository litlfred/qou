import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fivetwo-dt-spectrum-split",
  lean: {
    ref: "qou:QOU.QBeta.FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality",
    validation: "not_checked",
  },
  title:
    "The $5_2$ DT spectrum $\\{3,4\\}$ splits across chirality, and no $\\tau$-symmetric scalar can recover the ordered datum",
  tags: [
    "five-two",
    "stokes-matrix",
    "dt-spectrum",
    "chirality",
    "bar-grading",
    "amphichiral",
    "structural-exclusion",
  ],
  uses: ["prop:fivetwo-trace-field", "rem:fivetwo-bar-odd-arithmetic-home"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-19",
      body:
        "**Proved sorry-free** — Lean " +
        "`QOU.QBeta.FiveTwoDTSpectrumSplit.symmetric_scalar_blind_to_chirality`, " +
        "universally quantified over every $\\tau$-symmetric integer reading " +
        "$g$. The supporting members are `decide`-discharged facts about " +
        "concrete integer matrices: `splus0_carries_four`, " +
        "`sminus0_carries_three`, `fourone_carries_three` (the $4_1$ " +
        "contrast), `readings_all_distinct`, `dtPair52_chiral`, and the " +
        "$\\mathbb{Z}/2$ grading lemmas `barSwap_involutive`, " +
        "`barGrading_faithful`. Finite and decidable throughout — no analysis.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**Leading order only, and locating is not evaluating.** Every " +
        "statement is about the $q \\to 0$ coefficient matrices; nothing is " +
        "claimed about the full $q$-series beyond leading order. The grading " +
        "says *where* the bar-odd datum lives and that it is nonzero; it " +
        "supplies no bar-odd action value, and none is claimed.",
    },
    {
      kind: "caveat",
      date: "2026-08-19",
      body:
        "**The $7$ is the $\\tau$-even sum $4+3$, not $\\det(5_2)$.** The " +
        "block says so explicitly because the coincidence is inviting and " +
        "this lane has already lost a claim to exactly that kind of " +
        "conflation: the retracted 2026-07-18 audit read the invariant trace " +
        "field off $\\det(5_2) = 7$ (bean `qou-ynff`). The Lean is careful " +
        "here too — `chirality_sum_seven` is used only as one of four " +
        "*distinct* readings in `readings_all_distinct`, and makes no " +
        "identification with the determinant.",
    },
    {
      kind: "note",
      date: "2026-08-19",
      body:
        "Read positively this is Route C milestone M0 (`docs/audits/" +
        "2026-08-11-route-c-bps-cohomology-scoping.md`): it turns the proved " +
        "\"no scalar\" negative into the statement that the DT count is a " +
        "**bar-graded** object, connecting the split to the bar-parity " +
        "programme (`c1-ggm-bar-parity-faces`, `OhtsukiTowerBarParity`). " +
        "\"No scalar serves the datum\" and \"the bar-odd part is nonzero\" " +
        "are the same statement.",
    },
  ],
});
