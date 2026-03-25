import { example } from "../../schema/builders";

export default example({
  label: "ex:jet-prolongation-su2",
  title: "Jet prolongation of $\\mathcal{O}(\\mathrm{SU}(2))$",
  tags: ["su2", "jet-bundle", "frobenius-hopf", "prolongation"],
  uses: ["prop:jet-prolongation", "ex:yekutieli-lifting-condition-su2"],
});
