import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bring-embeddable-knots",
  title:
    "Bring-embeddable knots: genus-bounded table and per-knot B1 witness targets",
  interprets: "rem:knot-exhaustiveness",
  uses: [
    "rem:knot-exhaustiveness",
    "prop:knot-eigenbasis-complete",
    "conj:gb-depth-period-correspondence",
    "prop:explicit-central-idempotent",
    "conj:bring-figure-eight-depth-2-witness",
  ],
  cites: ["thurston1978"],
  tags: [
    "bring-embeddable",
    "genus-bound",
    "torus-knot-generators",
    "principled-atlas",
    "falsifiability-targets",
    "graded-mikusinski",
  ],
});
