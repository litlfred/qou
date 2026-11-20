import { conjecture } from "../../schema/builders";

/**
 * §3b-cond conjecture class for the proton's Borromean mass assembly.
 *
 * The class axiomatisation lives in the `qou` Lake library at
 * folio/quantum-observable-universe/lean/QOU/AppendixQValues/ProtonBorromeanAssembly.lean
 * (class `ProtonBorromeanAssembly`); no sibling `.lean` here, so it does not
 * shadow the library class. The downstream `prop:proton-mass-substrate-identity`
 * takes this class as an explicit `[Instance]` hypothesis and DERIVES the
 * published flat identity from it (sorry-free modulo the class instance).
 */
export default conjecture({
  label: "conj:proton-borromean-assembly",
  title:
    "The proton's Borromean mass assembly: multiplicity $\\dim V_{(2,1)} = 2$ and binding count $|S_3| = 6$",
  lean: {
    ref: "qou:QOU.AppendixQValues.ProtonBorromeanAssembly",
  },
  uses: [
    "def:f-bor-borromean-observable",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The conjecture is axiomatised as the Lean class `QOU.AppendixQValues.ProtonBorromeanAssembly`: its fields are exactly these hypotheses (the two structural integers and the factored assembly law), and [Substrate evaluation](proton-mass-substrate-identity.md) derives the published flat identity from them, sorry-free modulo the class instance. Also: the transpose-pair identity \"is Lean-proved\"." },
    {
      kind: "note",
      date: "2026-05-25",
      body:
        "The Ocneanu leading-pole reading of $12$ (as $1/|-\\tfrac{1}{12}|$) was retracted on " +
        "2026-05-25 and re-confirmed refuted in the 2026-08-22 $F_{\\mathrm{Bor}}$ red-team " +
        "audit. The refutation itself is scholarly content and stays in the block; only its " +
        "dating and audit provenance live here.",
    },
    {
      kind: "status",
      date: "2026-08-23",
      body:
        "The section now titled *Established identifications and the residual bridge* was headed " +
        "**## Status: open categorical bridge**. The conditionality is carried by the block kind " +
        "(`conjecture`) and by the prose, which states what remains conjectural; the header does " +
        "not need to restate it.",
    },
  ],
  tags: [
    "proton",
    "borromean",
    "mass-assembly",
    "constituent-multiplicity",
    "ocneanu",
    "conditional-class",
  ],
});
