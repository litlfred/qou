import { example } from "../../schema/builders";

export default example({
  interprets: "prop:fiber-adjoint-involution",
  label: "ex:fiber-adjoint-su2",
  title: "Fiber--adjoint-fiber involution for $\\mathrm{SU}(2)$",
  lean: { ref: "qou:QOU.Examples.su2FiberAdjoint", validation: "not_checked" },
  uses: ["prop:fiber-adjoint-involution", "ex:projective-line-su2"],
  tags: ["su2", "involution"],
});
