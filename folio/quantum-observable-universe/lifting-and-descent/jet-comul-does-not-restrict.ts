import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jet-comul-does-not-restrict",
  title: "The comultiplication does not restrict to the Kähler differentials",
  interprets: "lem:jet-prolongation-categorical-jet",
  uses: ["lem:jet-prolongation-categorical-jet"],
  lean: { ref: "qou:QOU.LiftingDescent.kahlerOmega_eq_bot_of_comul_restricts" },
  tags: ["kahler-differential", "jet-bundle", "bialgebra", "counterexample"],
});
