import { example } from "../../schema/builders";

export default example({
  interprets: "prop:categorical-self-duality",
  label: "ex:self-dual-curvature",
  title: "Self-duality of the curvature",
  tags: ["self-duality", "archimedean"],
  lean: { ref: "qou:QOU.self_dual_curvature",
    validation: "leanok",
  },
  uses: ["prop:categorical-self-duality", "ex:c-quantum-observable-universe"],
});
