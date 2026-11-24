import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:fiber-adjoint-involution",
  label: "rem:archimedean-realisations",
  title: "Archimedean realisations of categorical structures",
  tags: ["archimedean", "realisations"],
  uses: [
    "ex:c-quantum-observable-universe",
    "prop:fiber-adjoint-involution",
    "prop:variational-equations",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-24",
      body: "Relocated from block prose (paper-commentary-audit drain): the reduction of the categorical Einstein equation to $\\mathrm{Ric}_{g_\\varTheta} = T^{(q)}$ in item 3 is not formalised in Lean.",
    },
  ],
});
