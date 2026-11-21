import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:homological-shell-condensation",
  title:
    "Homological shell condensation: BB-stratified $E_\\infty^{p,>0}(n) = 0$ at magic $n$",
  lean: {
    ref: "qou:QOU.ShellCondensation.HomologicalConjecture",
    validation: "not_checked",
  },
  uses: [
    "ex:brane-tower-levels",
    "prop:gb-spectral-sequence",
    "prop:graded-trace-residue-split",
  ],
  cites: [
    "bialynicki1973",
    "yekutieli2010",
    "ariki1996",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "Formalize-first derivation (`QOU.ShellCondensation.SelectorPrune`, sorry-free). (i) `offDiag_vanish_iff_pure`: the statement is equivalent to purity of the induced filtration on cohomology, every $H^k$ sitting in filtration degree $k$; it is not the vanishing of $H^{\\geq 1}$. (ii) `not_upward_closed` / `not_downward_closed`: no predicate on $n$ that is preserved by $n \\mapsto n+1$, or by its reverse, matches the magic set on $0..126$. Semisimplicity of $H_n$ at a root of unity is upward closed in $n$, so it cannot be the selector. Open readings: Hochschild with a chosen coefficient module, and the Bring-surface lattices of `conj:magic-numbers-bring`. Bean `qou-6qbv`.",
    },
    {
      kind: "note",
      date: "2026-11-20",
      body: "Under the Hecke reading (algebra $H_n(R, q)$ with $n$ the nucleon count, Coxeter-length filtration, Hochschild cohomology) the vanishing is proved for every $n$: `cor:hecke-length-limit-page-vanishing`. That reading does not single out the magic numbers, so this conjecture stays open until a reading is named under which some non-magic $n$ fails (owner, option 1; bean `qou-6qbv`; `docs/audits/2026-11-20-homological-shell-condensation-well-posedness.md`).",
    },
    {
      kind: "caveat",
      date: "2026-11-20",
      body: "**Citation mismatch (bean `qou-6qbv`).** The Setup cites `prop:gb-spectral-sequence` for a spectral sequence on the Białynicki-Birula filtration of the jet algebra $A_n$. That proposition is about the Hochschild complex of $H_n(R, q)$ filtered by Coxeter length, a different filtration on a different algebra, so it does not supply the sequence used here. This block's own $E_2$ statement is about its BB sequence and is not affected by the $H_3$ result ($d_2, d_4 \\neq 0$ for the length-filtered Hochschild sequence). The block was typed `proposition` while its statement is a conjecture; retyped to `conj:` on owner instruction the same day.",
    },
  ],
  tags: [
    "magic-numbers",
    "shell-closure",
    "spectral-sequence",
    "BB-stratification",
    "brane-tower",
    "homological-condensation",
    "open-problem",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([prop:graded-trace-residue-split](#prop:graded-trace-residue-split))" },
  ],
});
