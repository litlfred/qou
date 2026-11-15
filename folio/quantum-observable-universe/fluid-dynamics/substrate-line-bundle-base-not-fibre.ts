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
        "**🟧 OWNER RULING 2026-09-15 settles the symbol: `tr(id_A)` is the quantum dimension `dim_q(A)`, the Euler characteristic of an object IN THE QOU CATEGORY — so it is q-DEPENDENT.** **This block's `chi(A) = tr(id_A)` bullet is WITHDRAWN as a direct consequence** and has been removed from the prose: under the ruling the categorical trace is exactly the q-dependent quantum dimension, so it cannot be listed among the quantities strictly independent of q. The four sibling bullets are untouched — `Hom(1, Ad(A))`, `c_1(Ad(A))`, `c_2(Ad(A))` and the Euler class `e(xi)` are each a class or a hom-space, fixed by `(C, A, tau)` alone. The block's thesis that the QOU structure anchors to the base is unaffected; only the trace moves off the list. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
  ],
});
