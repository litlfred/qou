import { proof } from "../../schema/builders";

export default proof({
  label: "prf:borromean-hopf-energy-crossover",
  title: "Proof of borromean hopf energy crossover",
  uses: ["prop:borromean-hopf-energy-crossover"],
  computation: {
    engine: "mpmath",
    script: "computations/snappy_borromean_volume.py",
    witness: "computations/snappy-borromean-volume.witness.json",
    status: "verified",
  },
});
