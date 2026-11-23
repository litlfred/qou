import { remark } from "../../schema/builders";

/**
 * The cyclotomic ground ring on which a Hecke-type quantum universe is
 * non-degenerate. Moved here from the Chapter 1 definition
 * (def:quantum-universe) on 2026-11-20 (voice drain, epic qou-d4kh, bean
 * qou-x4nh): it uses q, [n]_q and Phi_d, which Chapter 1 does not yet have.
 * The Chapter 1 block keeps the ring-independent half of the argument.
 */
export default remark({
  label: "rem:q-generic-ground-ring",
  interprets: "def:quantum-universe",
  title: "The q-generic ground ring",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.IsQGeneric",
    validation: "not_checked",
  },
  uses: ["def:quantum-universe", "def:substrate-parameter"],
  tags: ["substrate", "ground-ring", "cyclotomic", "hecke"],
});
