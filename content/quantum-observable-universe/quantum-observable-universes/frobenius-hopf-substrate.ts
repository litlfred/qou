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
        "of $\\mu$ — do not transfer to it. **This is not a gap to be filled: see " +
        "the next note, which proves the axiom must not be added.**",
    },
    {
      kind: "note",
      date: "2026-09-14",
      body:
        "**The bialgebra compatibility is EXCLUDED, not merely absent.** The note " +
        "above left it as an open option. It is not one. One of the four bimonoid " +
        "axioms *on its own* — $\\Delta \\circ \\eta = \\eta \\otimes \\eta$, " +
        "Mathlib's `BimonObj.one_comul` — collapses this definition to the tensor " +
        "unit. Proved sorry-free in `QOU.FrobeniusHopfData.counit_comp_unit` " +
        "(`FrobeniusBialgebraCollapse.lean`): the Frobenius relation of axiom 3 " +
        "makes $\\Delta$ a map of $A$-bimodules, hence determined by $\\Delta(1)$; " +
        "the bimonoid axiom sets $\\Delta(1) = 1 \\otimes 1$, which is degenerate; " +
        "the counit law of axiom 2 then forces $x = \\varepsilon(x) \\cdot 1$ for " +
        "every $x$, i.e. $\\varepsilon \\circ \\eta = \\mathrm{id}_A$. With the " +
        "second unit-side axiom $\\eta \\circ \\varepsilon = \\mathrm{id}$ this is " +
        "an isomorphism $A \\cong \\mathbf{1}$ (`isoUnit`). The usable form is the " +
        "contrapositive `not_one_comul_of_nontrivial`: if $A$ is not the trivial " +
        "object, the bimonoid unit axiom fails. " +
        "**Why this is expected rather than alarming:** a finite-dimensional Hopf " +
        "algebra *is* Frobenius, but its Frobenius comultiplication is not its " +
        "Hopf comultiplication; forcing the two to coincide is what collapses. " +
        "Axiom 3 fixes $\\Delta$ as the Frobenius one, so this substrate is a " +
        "Frobenius monoid carrying an antipode, not a Hopf monoid. Nothing here " +
        "argues against a Hopf structure on $A$ borne by a *different* " +
        "comultiplication — that is a separate object the corpus does not have.",
    },
    {
      kind: "caveat",
      date: "2026-09-15",
      body:
        "**The antipode axiom of this block excludes counit-unitality.** Sharper " +
        "than the note above, and with *no* extra hypothesis: axiom 2's Hopf " +
        "condition together with axiom 3's Frobenius relation forces " +
        "$\\varepsilon(1) \\cdot x = \\varepsilon(x) \\cdot 1$ for every $x$ — " +
        "`QOU.FrobeniusHopfData.scalar_id_eq_counit_unit` " +
        "(`FrobeniusBialgebraCollapse.lean`, sorry-free, no `Classical.choice`). " +
        "The Frobenius relation makes $\\Delta$ a right $A$-module map, so the " +
        "convolution $S * \\mathrm{id}$ is left multiplication by the single " +
        "element $(S * \\mathrm{id})(1)$; the Hopf condition says that same " +
        "convolution is $\\varepsilon(-) \\cdot 1$. Consequently, if " +
        "$\\varepsilon(1) = 1$ — the ordinary normalisation of a counit, and " +
        "Mathlib's `BimonObj.one_counit` — then $A \\cong \\mathbf{1}$ " +
        "(`isoUnitOfUnital`). The usable form is the contrapositive " +
        "`counit_not_unital_of_nontrivial`: **a non-trivial substrate has a " +
        "non-unital counit.** " +
        "So both of the two unit-side bimonoid axioms are individually excluded " +
        "for a non-trivial $A$ — $\\Delta(1) = 1 \\otimes 1$ by the note above, " +
        "$\\varepsilon(1) = 1$ by this one. " +
        "**Scope:** $\\varepsilon(1) = 1$ is not an axiom of this block, so this " +
        "is *not* a proof that the stated axioms force $A = \\mathbf{1}$; it is " +
        "the identity above plus its contrapositive. Whether the framework wants " +
        "a substrate whose counit is non-unital is an open question for the " +
        "author, bean `qou-aawz`; nothing here is a reason to revert axiom 2. " +
        "Audit: `docs/audits/2026-09-14-frobenius-bialgebra-collapse.md`.",
    },
  ],
});
