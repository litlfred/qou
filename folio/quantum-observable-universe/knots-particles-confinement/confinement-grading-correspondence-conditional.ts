import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:confinement-grading-correspondence-conditional",
  title:
    "Confinement = KLR grading shift (conditional on Brundan–Kleshchev isomorphism + crystal-graph realisation)",
  lean: {
    ref:
      "qou:QOU.BraidsAndKnots.confinement_grading_correspondence_conditional",
    validation: "not_checked",
  },
  uses: ["conj:confinement-grading-correspondence"],
  cites: [
    "khovanovlauda2009",
    "brundankleshchev2009",
  ],
  tags: [
    "confinement",
    "klr",
    "grading",
    "filtration",
    "conditional-theorem",
    "conditional-on-class",
    "computational-shortcut",
  ],
  authorNotes: [
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:confinement-grading-correspondence-conditional` (owner, #8526, 2026-11-21; bean qou-tm3c). The block's display is that of `conj:confinement-grading-correspondence`, and the Lean class field `confinement_eq_klr_top_degree` is the conclusion (AGENTS.md §3b-cond item 5)." },
    {
      kind: "status",
      body: "Per AGENTS.md §3b, an unconditional theorem about a downstream\nconsequence of an open conjecture would constitute a propagation\nviolation. This block invokes the **conditional-class exception**\n(§3b-cond):\n\n1. **Class axiomatisation.** The upstream conjecture\n   [`conj:crystal-graph-realization`](#conj:crystal-graph-realization)\n   is axiomatised in\n   [`confinement-grading-correspondence-conditional.lean`](confinement-grading-correspondence-conditional.lean)\n   as the Lean class `CrystalGraphRealization n`.  Its single field\n   `crystal_klr_iso` carries the Brundan–Kleshchev intertwining;\n   any `sorry` lives inside the class instance, not in the proof\n   that follows from it.\n2. **Explicit hypothesis on the Lean side.** The theorem's\n   declaration carries the class as an explicit `[Instance]`\n   argument:\n   `theorem confinement_grading_correspondence_conditional [CrystalGraphRealization n] : ... := ...`\n   with no `sorry` inside the proof body.\n3. **Conditional banner.** The proposition statement above is\n   prefixed with \"**Theorem (conditional on\n   [`conj:crystal-graph-realization`](#conj:crystal-graph-realization))**\".\n4. **`uses[]` includes the conjecture.** The block's manifest\n   lists both `conj:crystal-graph-realization` and the original\n   unconditional [`conj:confinement-grading-correspondence`](#conj:confinement-grading-correspondence).\n\nBy §3b-cond this block represents a *rigorous conditional result*:\nfully verified by Lean modulo a single, named, class-axiomatised\nconjectural input. The `conjectural-propagation` audit will\nclassify it as `conditional-on-class` rather than as a violation.",
    },
  ],
});
