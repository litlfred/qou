import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:jet-prefix-gb-filtration",
  title:
    "Jet-level prefix formula via Gröbner–Shirshov filtration (candidate Term 6)",
  lean: {
    ref: "qou:BraidKnotOctonion.jet_prefix_gb_filtration",
    validation: "not_checked",
  },
  uses: [
    "conj:confinement-grading-correspondence",
  ],
  tags: [
    "jet-level",
    "prefix-formula",
    "gb-filtration",
    "groebner-shirshov",
    "term-6",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-are-inhabited-by-zero.lean` inhabits `QOU.BraidKnot.JetPrefixGbFiltrationContext` at `Unit` and `0 = 0`.",
      see: "docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean",
    },
    { kind: "status", date: "2026-11-21", body: "Demoted from `conj:jet-prefix-gb-filtration` (owner, #8526, 2026-11-21; bean qou-tm3c). The evaluation formula for $a_k$ is not proved: the Lean names it as a proposition and does not assert it. A proof needs the Gröbner–Shirshov filtration of $H_{3A}(q)$, the symbol map and the partial Markov trace, none of which is formalised. The previously listed `conj:confinement-grading-correspondence` was not used." },
  ],
});
