import { definition } from "../../schema/builders";

export default definition({
  label: "def:ns-regular-qou",
  title: "NS-regular quantum observable universe",
  // Was `qou:QOU.FluidDynamics.NSRegularQOU`. Neither that namespace nor that
  // declaration exists anywhere in the tree, and the canonical resolver returns
  // unresolved for it. `QOU.GaugeFieldFluidDynamics.BoundaryObservability`
  // carries this block's own `\label{def:ns-regular-qou}` — the label is the
  // evidence, the ref's name was not. Same repair as `thm:su2-emergence`
  // (PR #5222) and `def:mass-identity` (bean `qou-qc6s`).
  //
  // Why nothing caught this: the block has a co-located sibling
  // `ns-regular-qou.lean`, and `walkBlocks` resolves the sibling FIRST. So the
  // checkers audited the stub and passed, while the library ref sat dead and
  // the real declaration went unchecked. A sibling stub MASKS a broken library
  // ref — see bean `qou-2u26`.
  lean: {
    ref: "qou:QOU.GaugeFieldFluidDynamics.BoundaryObservability",
    validation: "not_checked",
  },
  uses: ["def:q-navier-stokes"],
  tags: [
    "definition",
    "navier-stokes",
    "obstruction",
    "euler-characteristic",
    "categorical",
  ],
});
