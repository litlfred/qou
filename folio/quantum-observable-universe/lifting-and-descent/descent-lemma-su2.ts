import { example } from "../../schema/builders";

export default example({
  interprets: "lem:descent",
  label: "ex:descent-lemma-su2",
  title: "Descent lemma for $\\mathrm{SU}(2)$",
  tags: ["su2", "descent", "surjectivity"],
  uses: ["lem:descent", "ex:recursive-brane-tower-su2"],
});
