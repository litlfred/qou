import { example } from "../../schema/builders";

export default example({
  interprets: "prop:descent-eigenspaces",
  label: "ex:descent-eigenspaces-su2",
  title: "Descent eigenspaces for $\\mathrm{SU}(2)$",
  tags: ["su2", "descent", "eigenspaces", "involution"],
  uses: ["prop:descent-eigenspaces", "ex:descent-involution-su2"],
});
