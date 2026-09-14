import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-hopf-substrate",
  title: "The quantum vacuum as a Frobenius--Hopf algebra",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.FrobeniusHopfSubstrate",
    validation: "not_checked",
  },
  uses: ["def:frobenius-pairing"],
  tags: ["frobenius", "hopf-algebra", "substrate", "vacuum"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-14",
      body:
        "**Antipode axiom added (owner decision).** Until this date axiom 2 read " +
        "*\"with antipode $S \\colon A \\to A$ satisfying the Hopf compatibility " +
        "$\\varepsilon \\circ \\mu = u \\circ (\\varepsilon \\otimes \\varepsilon)$\"* — " +
        "a sentence that names $S$ on the left of \"satisfying\" and puts it on " +
        "neither side of the equation that follows. That equation is " +
        "multiplicativity of the *counit*. $S$ was therefore constrained by nothing: " +
        "free data, about which no property is derivable and none refutable. " +
        "`S^2 = \\mathrm{id}$ was consequently **independent** of this definition — " +
        "neither open nor false. The Hopf condition " +
        "$\\mu \\circ (S \\otimes \\mathrm{id}) \\circ \\Delta = \\eta \\circ \\varepsilon$ " +
        "is now stated, which makes $S$ the convolution inverse of $\\mathrm{id}_A$ " +
        "and hence unique. The unit / counit / associativity / coassociativity laws " +
        "that axioms 1--2 assert in prose were also absent from the Lean and are now " +
        "carried, because the uniqueness argument is exactly what spends them. " +
        "Machine-checked record of the prior state: `QOU.AntipodeIndependence`; " +
        "uniqueness: `QOU.FrobeniusHopfData.antipode_unique`. Beans `qou-c64q`, " +
        "`qou-qjhc`; found in prose by the block's own QA sidecar " +
        "(`trap-nonspeakable`, reviewer `agent:d02`).",
    },
    {
      kind: "caveat",
      date: "2026-09-14",
      body:
        "**Still not asserted: the bialgebra (bimonoid) compatibility** " +
        "$\\Delta \\circ \\mu = (\\mu \\otimes \\mu) \\circ \\tau \\circ (\\Delta \\otimes \\Delta)$. " +
        "Axiom 2 asks only for a coalgebra object, and the Frobenius relation of " +
        "axiom 3 is a different compatibility that does not imply it. So this " +
        "substrate is not a Hopf *monoid* in Mathlib's sense " +
        "(`CategoryTheory.HopfObj`), and results proved there — notably " +
        "`antipode_antipode`, i.e. $S^2 = \\mathrm{id}$ under braided-commutativity " +
        "of $\\mu$ — do not transfer to it. Recorded, not acted on: adding a " +
        "bialgebra axiom is a further change to this definition.",
    },
  ],
});
