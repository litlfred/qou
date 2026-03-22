import { example } from "../../schema/builders";

export default example({
  label: "ex:self-dual-curvature",
  title: "Self-duality of the curvature",
  tags: ["self-duality", "archimedean"],
  lean: {
    decl: "QOU.self_dual_curvature",
    validation: "leanok",
  },
  uses: ["prop:categorical-self-duality", "ex:c-quantum-observable-universe"],
});
