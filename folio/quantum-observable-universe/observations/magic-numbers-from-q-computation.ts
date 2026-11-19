import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:magic-numbers-from-q",
  label: "rem:magic-numbers-from-q-computation",
  title: "Magic numbers from $q$: computation, $q$-dependence, and homological route",
  tags: ["magic-numbers", "hoefsmit", "shell-closure", "computation"],
  authorNotes: [
    {
      kind: "note",
      body: "Witness shell-closure.witness.json records delta^2 Phi(Z) for Z = 1..30 at K = 10; the block-diagonal optimized producer is shell_closure_compute.py.",
    },
  ],
});
