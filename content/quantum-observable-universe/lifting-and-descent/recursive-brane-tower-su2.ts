import { example } from "../../schema/builders";

export default example({
  interprets: "def:recursive-brane-tower",
  label: "ex:recursive-brane-tower-su2",
  title: "Brane tower for $\\mathrm{SU}(2)$",
  tags: ["su2", "brane-tower", "jet-bundle"],
  uses: ["def:recursive-brane-tower", "ex:jet-prolongation-su2"],
});
