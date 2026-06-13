import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:delta-lambda-closure",
  title: "$\\Delta_\\lambda$ closure ansätze (Track-A blocker — open gate)",
  uses: [
    "rem:term6-binding-density",
    "conj:crystal-graph-realization",
  ],
  computation: {
    engine: "python+mpmath",
    script: "folio-assistant/computations/option_e_v9_all_symmetries.py",
    status: "experimental",
  },
  tags: [
    "mba",
    "sidecar",
    "delta-lambda",
    "open-gate",
    "option-e",
    "crystal-graph",
  ],
});
