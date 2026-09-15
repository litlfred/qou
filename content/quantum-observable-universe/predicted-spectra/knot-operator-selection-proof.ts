import { proof } from "../../schema/builders";

export default proof({
  label: "prf:knot-operator-selection",
  title: "Proof of knot operator selection",
  uses: ["prop:knot-operator-selection"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**Scope: the `tr(id_A) = [2]_q` on this page is a DIFFERENT object from the `chi(A) = -6` of `lem:brings-euler-characteristic`.** `[2]_q = q + q^-1 = 2.0108968667` at the proton `q_0` is `dim_q` of the **fundamental** `V_1`; the Euler-characteristic reading is about the base algebra `A = O_q(SU(2))`. They share only the glyph, and this one is manifestly q-dependent while `rem:substrate-line-bundle-base-not-fibre` declares the other q-independent. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
  ],
});
