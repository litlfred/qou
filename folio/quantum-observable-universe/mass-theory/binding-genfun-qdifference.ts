import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:binding-genfun-qdifference",
  lean: {
    ref: "qou:QOU.Mass.binding_qdifference_recurrence",
    validation: "validated",
  },
  title: "The binding generating function's q-difference equation gives a depth-d recurrence",
  uses: [
    // conj:binding-manybody-eq-jet-filtration removed (qou-tm3c): items (1)-(2) hold for any q-difference kernel R; the conjecture only names the terms B_n.
    "prop:sw-period-residue-sum",
  ],
  proofs: ["prf:binding-genfun-qdifference"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): named by\n> [The q-difference kernel R is the jet-prolongation symbol, carried by the binding q-lift module](#conj:qdifference-kernel-prolongation-symbol)" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): > ([`QOU.Mass.QDifferenceConfluentObstruction.no_bounded_depth_first_order_kernel`](../lean/QOU/Mass/QDifferenceConfluentObstruction.lean)).\n\n> Formalized in\n> [`QOU.Mass.BindingScalarKernelParityExclusion`](../lean/QOU/Mass/BindingScalarKernelParityExclusion.lean)." },
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Corrected 2026-11-16 (QA finding: da-non-sequitur, critical).** The block said " +
        "$G(qx) = RG$ gives a recurrence $B_{n+d} = \\sum_j a_j(q) B_{n+j}$ with constant " +
        "$a_j$, and that the '$\\rho\\cdot A$' scale rule is its solution. The coefficients " +
        "depend on $n$ through $q^n$ (counterexample $R = 1 - x$, $B_n = 1/(q;q)_n$). The Lean " +
        "structure now carries position-dependent coefficients. **Mass-derivation flag:** " +
        "`BindingRecurrenceSpectral.lean` studies the constant-$\\tau$ recurrence " +
        "$a_{n+2} = \\tau a_{n+1} - a_n$ as if it came from $R = x^2 - \\tau x + 1$; it does " +
        "not, and its docstring now says so. No compute changes.",
    },
  ],
});
