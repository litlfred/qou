import { prose } from "../../schema/builders";

export default prose({
  label: "prose:sm-open-problems",
  title: "Open problems",
  cites: ["todorov2018"],
  tags: ["appendix", "standard-model", "open-problem", "epistemic-status"],
  authorNotes: [
    {
      kind: "note",
      body: "Lean backing for obstructions and proved items in this ledger: `QOU/StandardModel/TwistBatteryVacuity.lean` (collapse of the first-generation twist battery to `T = 3Q` per flavour), `QOU/StandardModel/QuarkBraidChargeObstruction.lean` (anti-up vs down braid-element charge collision), and continuant divisibility `b_a | b_n <-> a | n`.",
    },
  ],
});
