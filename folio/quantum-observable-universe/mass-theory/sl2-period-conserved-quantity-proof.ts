import { proof } from "../../schema/builders";

export default proof({
  label: "prf:sl2-period-conserved-quantity",
  title: "Proof of the depth-2 conserved first integral",
  uses: [
    "prop:sl2-period-conserved-quantity",
    "prop:sl2-prolongation-recurrence",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): This is the Lean theorem\n[`QOU.Mass.sl2Invariant_succ`](#prop:sl2-period-conserved-quantity): after\n`unfold sl2Invariant; rw [hrec n]`, the goal is the polynomial identity above,\ndischarged by `ring`. A straightforward induction on $n$ (base $H_0 = H_0$, step\n$H_{k+1} = H_k = H_0$) then gives $H_n = H_0$ for all $n$\n([`QOU.Mass.sl2Invariant_eq_zeroth`](#prop:sl2-period-conserved-quantity))." },
  ],
});
