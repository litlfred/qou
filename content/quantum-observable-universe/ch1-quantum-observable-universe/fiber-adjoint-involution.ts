import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fiber-adjoint-involution",
  lean: { decl: "QOU.FiberAdjointInvolution" },
  title: "Fiber--adjoint-fiber involution",
  uses: ["def:quantum-observable-universe", "def:frobenius-pairing", "def:projective-line-object"],
  proofs: ["prf:fiber-adjoint-involution"],
  examples: ["ex:fiber-adjoint-su2"],
  tags: ["involution", "adjoint"],
});
