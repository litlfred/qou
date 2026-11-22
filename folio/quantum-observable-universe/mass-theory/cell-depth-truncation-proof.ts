import { proof } from "../../schema/builders";

export default proof({
  label: "prf:cell-depth-truncation",
  title: "Proof of the cell-depth truncation statements",
  uses: ["prop:cell-depth-truncation"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Lean.** `stratum_eq_zero_of_gt`, `tower_stable`, `tower_total` and `kstar_eq_of_max_in_supp` (items 1–4, for an arbitrary depth function on a finite index set, with the vanishing derived from the definition of the support rather than assumed), and `phiTrunc_succ_ne`, `no_stable_phi_tower`, `witness_hyp` (item 5) in the sibling file. The Hecke algebra, the Kazhdan–Lusztig basis and the cell–irreducible correspondence are not formalised; they are cited [Kazhdan–Lusztig 1979] and were checked exactly for $n\\le5$ (probe recorded on issue #8094). Sorry-free, lean-direct exit 0. $\\blacksquare$" },
  ],
});
