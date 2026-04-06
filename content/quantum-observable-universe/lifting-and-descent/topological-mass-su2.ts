import { example } from "../../schema/builders";

export default example({
  interprets: "thm:topological-mass",
  label: "ex:topological-mass-su2",
  title: "Topological mass decomposition for $\\mathrm{SU}(2)$",
  tags: ["su2", "topological-mass", "hopf", "euler-characteristic"],
  uses: ["thm:topological-mass", "ex:descent-eigenspaces-su2"],
});
