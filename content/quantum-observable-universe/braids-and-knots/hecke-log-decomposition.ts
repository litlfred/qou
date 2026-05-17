import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-log-decomposition",
  lean: {
    ref: "qou:QOU.Information.HeckeLogDecomposition",
    validation: "not_checked",
  },
  title: "Decomposition of log(1/h) into thermal + skein normalisation",
  tags: ["hecke-deformation", "boltzmann", "skein", "log-identity"],
  uses: ["rem:beta-decay-energy-scale", "prop:boltzmann-constant"],
});
