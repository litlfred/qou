import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-scattering-pipeline",
  title:
    "From Hoefsmit scattering weights to physical mass via the observation frame",
  lean: {
    decl: "QOU.BraidKnot.hoefsmit_scattering_pipeline",
    validation: "not_checked",
  },
  uses: [
    "prop:hoefsmit-seminormal-form",
    "prop:wedderburn-trace-identity",
    "prop:universal-braid-branching",
    "prop:topological-mass-formula",
    "prop:geom-yekutieli-alignment",
    "prop:figure-eight-bw-coefficients",
  ],
  cites: ["hoefsmit1974", "wenzl1988"],
  tags: [
    "hoefsmit",
    "r-matrix",
    "scattering",
    "markov-trace",
    "jones-polynomial",
    "observation-frame",
    "pipeline",
  ],
});
