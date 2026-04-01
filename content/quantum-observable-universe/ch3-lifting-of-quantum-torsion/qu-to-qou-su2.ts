import { example } from "../../schema/builders";

export default example({
  interprets: "thm:qu-to-qou",
  label: "ex:qu-to-qou-su2",
  title:
    "From quantum universe to QOU: $\\mathrm{SU}(2)$ verification",
  tags: ["su2", "main-theorem", "qou", "descent"],
  uses: ["thm:qu-to-qou", "ex:yekutieli-lifting-su2"],
});
