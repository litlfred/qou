import { example } from "../../schema/builders";

export default example({
  interprets: "def:involutive-structure",
  label: "ex:dagger-su2",
  title: "Involutive structure on $\\mathrm{Rep}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2Dagger", validation: "not_checked" },
  uses: [
    "prop:positive-definite-dagger",
    "ex:frobenius-su2",
  ],
  tags: ["su2", "involutive"],
});
