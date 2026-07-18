import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:benzene-threading-emergence",
  label: "rem:benzene-threading-selection",
  title: "Why the threading link is LP-optimal, and the resonance energy",
  uses: ["def:benzene-molecular-braid"],
  tags: ["benzene", "threading-link", "resonance", "LP-dual"],
  computation: {
    engine: "python",
    script: "computations/molecular_experimental_refs.py",
    witness: ["computations/molecular-experimental-refs.witness.json"],
    status: "experimental",
  },
});
