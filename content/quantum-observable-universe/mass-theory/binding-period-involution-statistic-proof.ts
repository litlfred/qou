import { proof } from "../../schema/builders";

export default proof({
  label: "prf:binding-period-involution-statistic",
  title:
    "Proof that the balanced dimension sum is the $2\\,\\mathrm{maj} + \\mathrm{content} \\circ \\mathrm{RSK}$ involution generating function",
  uses: [
    "prop:binding-period-involution-statistic",
  ],
});
