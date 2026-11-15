import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:substrate-parameter-exists",
  title: "Existence of the substrate parameter",
  lean: {
    decl: "QOU.SubstrateParameter.ofReebDecomposition",
    validation: "not_checked",
  },
  uses: ["def:substrate-parameter"],
  proofs: ["prf:substrate-parameter-exists"],
  tags: ["existence", "substrate", "deformation"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/substrate-parameter-exists-0.svg", blockIndex: 0, hash: "4aa896a3cce4" },
  ],

});
