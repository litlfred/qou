import { example } from "../../schema/builders";

export default example({
  interprets: "lem:volume-from-rigidity",
  label: "ex:su2-volume-from-rigidity",
  title: "$\\mathrm{SU}(2)$ volume form from the lemma",
  uses: ["lem:volume-from-rigidity", "ex:qou-su2"],
  tags: ["su2", "volume"],
});
