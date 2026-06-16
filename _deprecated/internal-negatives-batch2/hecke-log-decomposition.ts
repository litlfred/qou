import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-log-decomposition",
  lean: {
    ref: "qou:QOU.Information.hecke_log_decomposition",
    validation: "not_checked",
  },
  title: "Decomposition of log(1/h) into thermal + skein normalisation",
  tags: ["hecke-deformation", "boltzmann", "skein", "log-identity"],
  uses: ["rem:beta-decay-energy-scale", "prop:boltzmann-constant"],
  computation: {
    engine: "mpmath",
    script: "computations/hecke_log_decomposition_probe.py",
    witness: "computations/hecke-log-decomposition-probe.witness.json",
    status: "verified",
  },
});
