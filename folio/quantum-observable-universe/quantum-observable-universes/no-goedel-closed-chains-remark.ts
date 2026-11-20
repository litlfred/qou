import { remark } from "../../schema/builders";

/**
 * Why a Gödel-type universe is excluded once time order is defined as
 * crossing application.
 *
 * Words: every tick is a ≺_c-step, and a well-founded relation has no closed
 * chains, for any braiding. States: the writhe forbids closed chains in the
 * braid group, while a crossing of finite order (c² = id is order two) puts
 * every state on one. This is where the non-symmetry hypothesis of
 * prop:braiding-induced-ordering does real work.
 */
export default remark({
  interprets: "prop:braiding-induced-ordering",
  label: "rem:no-goedel-closed-chains",
  title: "No closed causal chains: why a Gödel universe is excluded",
  lean: {
    ref: "qou:QOU.Chronology.braid_no_closedChainAt",
    sorryFree: true,
    validation: "not_checked",
  },
  uses: [
    "prop:braiding-induced-ordering",
    "prf:braiding-induced-ordering",
  ],
  cites: ["goedel1949"],
  tags: [
    "arrow-of-time",
    "causality",
    "well-ordering",
    "closed-timelike-curves",
    "goedel-universe",
    "scope-limit",
    "writhe",
    "symmetric-braiding",
  ],
});
