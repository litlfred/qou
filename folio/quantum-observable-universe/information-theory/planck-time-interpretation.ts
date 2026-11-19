import { remark } from "../../schema/builders";

export default remark({
  label: "rem:planck-time-interpretation",
  title: "Planck time: Reeb-circuit reading, regimes, field realisations, and the Planck length",
  interprets: "def:planck-time",
  tags: ["planck-time", "discrete-time", "reeb-flow", "planck-length", "information-theory"],
  uses: [
    "def:planck-time",
    "ex:q-reeb-flow",
    "rem:julia-set-reeb",
    "prop:local-substrate-q",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/binding_heat_kernel_canonical_time_probe.py",
    witness: "computations/binding-heat-kernel-canonical-time.witness.json",
    status: "verified",
  },
});
