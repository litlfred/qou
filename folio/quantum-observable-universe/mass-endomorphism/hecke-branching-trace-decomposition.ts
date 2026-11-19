import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-branching-trace-decomposition",
  title:
    "Hecke branching trace decomposition: $\\mathrm{tr}_{V_\\lambda}(\\rho_\\lambda(\\beta_1 I \\beta_2)) = \\sum_{\\mu,\\nu} \\mathrm{tr}\\,A^\\lambda_{\\mu,\\nu}(I) \\cdot (\\rho_\\mu(\\beta_1) \\otimes \\rho_\\nu(\\beta_2))$",
  lean: {
    ref: "qou:QOU.MassEndomorphism.branch_trace",
    validation: "not_checked",
  },
  uses: [
    "prop:hoefsmit-seminormal-form",
    "prop:wenzl-bridge-applicability-qou",
  ],
  cites: [
    "halverson_ram_1998",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "hecke",
    "branching-rule",
    "littlewood-richardson",
    "wedderburn-decomposition",
    "hoefsmit-seminormal",
    "trace-decomposition",
    "operator-valued",
  ],
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
