import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cellular-depth-filtration",
  title: "Proof of the cell-depth filtration properties",
  uses: ["prop:cellular-depth-filtration"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** The sibling file works with any commutative algebra $Z$ and orthogonal idempotents $e:\\iota\\to Z$: `F_mono`, `mul_mem_F`, `mul_mem_F_add`, `one_mem_F_iff`, `one_not_mem_F_zero` (item 1); `map_mem_F_comp`, `map_mem_F_of_perm` (item 2); `aDepth_transpose`, `aDepth_add_transpose`, `maxHookDepth_transpose`, `rows_transpose` on Mathlib Young diagrams; `map_gen_eq_self_iff`, `map_gen_add`, `map_gen_sub` (item 3); `odd_component_eq_zero_of_intertwines_of_parity`, `component_swap_of_intertwines_of_parity`, `odd_component_ne_zero_iff_of_intertwines_of_parity` (item 4). The input $\\#(e_\\lambda)=e_{\\lambda'}$ is a hypothesis (`hφ`), cited from [Mathas 1999, Ch. 3] and [Dipper–James 1986]. The count of self-conjugate partitions and the $a$-function identification are not formalised. Sorry-free, lean-direct exit 0. $\\blacksquare$" },
  ],
});
