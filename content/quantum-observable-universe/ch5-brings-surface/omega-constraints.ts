import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:quaternionic-spectral-resolvents",
  label: "rem:omega-constraints",
  title: "Algebraic constraints in the $\\omega_k$ basis",
  uses: ["def:quaternionic-spectral-resolvents", "ex:self-dual-curvature"],
});
