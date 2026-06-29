import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:zeta8-witness-level2-su2",
  title:
    "Level-2 SU(2) Verlinde witness at $q = \\zeta_8$: " +
    "$(\\zeta_8;\\zeta_8)_7 = 8$, $\\mathrm{ord}(\\sigma_i) = 8$, " +
    "$[4]_q = 0$, and the Wenzl annihilator",
  lean: {
    ref: "qou:QOU.BraidKnot.Zeta8Witness.qInt_four_at_zeta8",
  },
  uses: [
    "prop:cyclotomic-strand-doubling",
    "prop:habiro-pochhammer-bridge",
  ],
  cites: [
    "wenzl1987",
    "jones1987",
    "witten1989",
  ],
  tags: [
    "habiro-ring",
    "hecke",
    "wenzl-projector",
    "level-2-su2",
    "verlinde-truncation",
    "1ppQ",
    "categorical-witness",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-01",
      body: "The companion audit doc `docs/audits/2026-06-01-qbeta-habiro-phi8-interpretation.md` landed via PR #1579 (now on `main`).",
    },
  ],
});
