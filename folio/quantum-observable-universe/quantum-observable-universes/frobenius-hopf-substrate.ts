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
    { kind: "note", date: "2026-10-11", body: "Relocated from the block prose by the paper-voice commentary audit: An earlier version of this definition opened *\"Let $\\mathbf{C}$ be a rigid monoidal category\"* and phrased axioms 4--5 as *\"the induced map $A \\to A^\\vee$ is an isomorphism\"*. That notation presupposes an ambient dual $A^\\vee$, which made this definition unusable at the level that actually invokes it: `def:quantum-universe` requires a Frobenius--Hopf object while explicitly stating that rigidity of $\\mathbf{C}$ is *not* required there. The formalization never assumed rigidity either --- `FrobeniusHopfData` is stated over a bare monoidal category and derives self-duality from $\\mathrm{coev}$ plus the snake identities, exactly as axiom 4 now does." },
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
        "Audit: `docs/audits/2026-09-14-frobenius-bialgebra-collapse.md`. " +
        "**Superseded the next day — see the note below: over a field the " +
        "non-unital corner is empty, so this is not an open option either.**",
    },
    {
      kind: "caveat",
      date: "2026-09-15",
      body:
        "**Over a field this definition has NO non-trivial model.** The note " +
        "above treats a non-unital counit as the surviving corner for a " +
        "non-trivial substrate. It is not one. Write " +
        "$\\sigma = \\eta \\circ \\varepsilon$ for the scalar " +
        "$\\varepsilon(1)$. Then axiom 3 plus the antipode condition of " +
        "axiom 2 give, with no further hypothesis, that $\\mathrm{id}_A$ " +
        "factors through a morphism carrying $\\sigma$ in the middle " +
        "(`id_factors_through_unitCounit`). So if $\\sigma$ is **invertible**, " +
        "$A$ is a retract of $\\mathbf{1}$ (`retract_of_unit_of_isIso`); and if " +
        "$\\sigma = 0$, then $\\mathrm{id}_A = 0$ and $A$ is a zero object " +
        "(`id_eq_zero_of_unitCounit_eq_zero`). A field has no element that is " +
        "neither, so in any preadditive monoidal category with field scalars — " +
        "$\\mathbf{Mod}_k$, $\\mathbf{FdRep}_k(G)$, any $k$-linear abelian " +
        "monoidal category with simple unit — **every** model has " +
        "$\\dim A \\le 1$ (`dichotomy_of_scalars_field`, sorry-free, in " +
        "`FrobeniusHopfModelDichotomy.lean`). " +
        "**Two limits, both real.** The zero branch needs " +
        "`MonoidalPreadditive`, so a *bare* monoidal category is untouched and " +
        "whether one admits a non-trivial model is open (`qou-aawz`). And " +
        "\"retract of $\\mathbf{1}$\" is \"$\\cong \\mathbf{1}$\" only where the " +
        "unit is indecomposable. " +
        "**Why this is the classical fact rather than a defect:** a " +
        "finite-dimensional Hopf algebra *is* Frobenius, but its Frobenius " +
        "comultiplication is not its Hopf comultiplication. Axiom 3 pins " +
        "$\\Delta$ to the Frobenius one and axiom 2 then asks for an antipode " +
        "against *that* $\\Delta$; the collapse is the price of forcing them to " +
        "coincide. The group algebra is the worked case: with the dual-basis " +
        "$\\Delta(1) = \\sum_h h \\otimes h^{-1}$, no linear map at all — not " +
        "merely $g \\mapsto g^{-1}$ — satisfies the antipode condition for " +
        "$|G| > 1$, verified by exact rational elimination on the full " +
        "$|G|^2$ system for $\\mathbb{Z}/2, \\mathbb{Z}/3, \\mathbb{Z}/4, S_3$. " +
        "Audit: `docs/audits/2026-09-15-frobenius-hopf-has-no-nontrivial-linear-model.md`. " +
        "**Acted on the same day — see the note below: the convolution condition " +
        "was replaced, so this block no longer carries an axiom with no models.**",
    },
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**Axiom 3 replaced: the antipode is now an involutive anti-automorphism, " +
        "not a convolution inverse** (owner decision). Until today axiom 2 asked " +
        "for $\\mu \\circ (S \\otimes \\mathrm{id}) \\circ \\Delta = " +
        "\\eta \\circ \\varepsilon$. The note above proves that condition has " +
        "**no non-trivial model over a field**, so it is not an axiom one can keep. " +
        "It now asks instead that $S$ reverse $\\mu$ and $\\Delta$, fix $\\eta$, " +
        "preserve $\\varepsilon$ and $\\lambda$, and square to the identity. " +
        "**What this buys, measured:** $k[G]$ with the Frobenius comultiplication " +
        "and the classical $S(g) = g^{-1}$ **is a model**, verified for " +
        "$\\mathbb{Z}/1..4$, $V_4$, $S_3$ and $D_4$ by exact integer arithmetic " +
        "(`computations/probes/frobenius_hopf_intermediate_axioms_probe.py`, 7/7). " +
        "**What it costs, and this is not hidden:** $S$ is *constrained* but no " +
        "longer *determined*. Uniqueness came only from the convolution identity, " +
        "which is exactly the one with no models — the two cannot both be had. On a " +
        "non-commutative $A$ the anti-algebra law does exclude the vacuous " +
        "$S = \\mathrm{id}_A$ (measured: excluded on $S_3$ and $D_4$, not on any " +
        "abelian group), which is what stops $S$ being decoration. " +
        "**Why $S^2 = \\mathrm{id}$ is not carried alone:** it pins nothing — " +
        "$S = \\mathrm{id}_A$ satisfies it on every group tested, non-abelian " +
        "included. It earns its place only beside the anti-algebra law. " +
        "**New requirement:** $\\mathbf{C}$ is now braided, since \"reverses\" is " +
        "not expressible without a way to exchange tensor factors. That is not a new " +
        "demand on the framework: `def:quantum-universe` is braided monoidal, and its " +
        "Lean carrier already supplied the instance. " +
        "The three theorems recording the collapse are **not** deleted — they now " +
        "take the convolution condition as an explicit hypothesis " +
        "(`ConvolutionLeft` / `ConvolutionRight`), which is strictly stronger than " +
        "reading it off a field. Audit: " +
        "`docs/audits/2026-09-15-antipode-anti-automorphism-package.md`.",
    },
    {
      kind: "status",
      date: "2026-10-13",
      body:
        "**Axiom 2 no longer asks for a multiplicative counit** (owner decision, " +
        "bean `qou-aj49`). The sentence " +
        "$\\varepsilon \\circ \\mu = u \\circ (\\varepsilon \\otimes \\varepsilon)$ " +
        "is removed. Reason, proved sorry-free: the right Frobenius relation, the " +
        "right counit law and a multiplicative counit force " +
        "$x = \\varepsilon(x) \\cdot 1$ for every $x$, over any commutative ring " +
        "and **with no antipode** (`MultiplicativeCounitCollapse.eq_counit_smul_one`, " +
        "`surjective_algebraMap`). So the definition as previously written had " +
        "only models spanned by the unit. **Consequence for the note above:** the " +
        "$k[G]$ probe (`frobenius_hopf_intermediate_axioms_probe.py`) uses " +
        "$\\varepsilon = \\delta_e$, which is not multiplicative, and never " +
        "tested multiplicativity; its 7/7 held only with the removed sentence " +
        "ignored. With the sentence removed, its claim applies to the definition " +
        "as now stated, for the axioms the probe checks. The Lean carriers " +
        "(`FrobeniusHopfData`, `FrobeniusHopfSubstrate`) never had this field, " +
        "so no proof changes.",
    },
  ],
});
