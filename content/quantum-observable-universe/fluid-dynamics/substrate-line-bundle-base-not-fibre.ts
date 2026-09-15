import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-line-bundle",
  label: "rem:substrate-line-bundle-base-not-fibre",
  title: "The QOU structure is the base, not the fibre",
  uses: ["def:substrate-line-bundle"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**The q-independence of `chi(A) = tr(id_A)` asserted here is in direct conflict with two other live sites.** `lem:brings-euler-characteristic`'s proof recovers its value as *\"the quantum dimension specialised at the Descartes substrate parameter q_0\"* -- which presupposes q-dependence -- and `prf:knot-operator-selection` gives `tr(id_A) = [2]_q = q + q^-1`, manifestly q-dependent. Either those two are about a different object (plausible: `[2]_q` is `dim_q` of the fundamental `V_1`, not of the base algebra) or this bullet is too strong. Not resolved here. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
  ],
});
