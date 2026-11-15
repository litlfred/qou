import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:fiber-adjoint-involution",
  lean: { decl: "QOU.FiberAdjointInvolution" },
  title: "Fiber--adjoint-fiber involution",
  uses: [
    "def:frobenius-pairing",
    "def:projective-line-object",
  ],
  proofs: ["prf:fiber-adjoint-involution"],
  examples: ["ex:fiber-adjoint-su2"],
  tags: ["involution", "adjoint"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/fiber-adjoint-involution-0.svg", blockIndex: 0, hash: "6e7ee5806e2d" },
  ],

});
