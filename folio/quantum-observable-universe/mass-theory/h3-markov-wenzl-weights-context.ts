import { remark } from "../../schema/builders";

export default remark({
  label: "rem:h3-markov-wenzl-weights-context",
  title:
    "Scope, Borromean corollary, chirality, and notation for the H_3 Wenzl weights",
  interprets: "prop:h3-markov-wenzl-weights",
  tags: [
    "markov-trace",
    "wenzl-weights",
    "jones-polynomial",
    "borromean",
    "chirality",
  ],
  uses: ["prop:h3-markov-wenzl-weights"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `lem:feynman-eigenbasis-decomposition` puts the row cap ..., and `markovWeights_eq_jones_of_threeRow_eq_zero` then makes $z = q^3/(q^2+1)$ the unique faithful normalised Markov trace. ... entering as `trM_borromean` $\\to$ `F_Bor` $\\to$ `canonical_mass`." },
    {
      kind: "deprecated",
      date: "2026-08-09",
      body: "**Convention C excised (owner ruling, 2026-08-09).** Until then a *second*\ntrace ran in the binding channel: the full-Hecke Ocneanu trace, **convention\nC**, $z = 1/(q^{1/2}+q^{-1/2})$, with Wedderburn weights from the Wenzl\nSchur-principal specialisation and three-row weight\n$y_{(1^3)}(q) \\neq 0$ for $q \\neq 1$. It was pinned by\n[`rem:markov-axioms-primitive`](../braids-and-knots/markov-axioms-primitive.md),\nwhich described its own $z$ as \"a stipulation of this definition, not a\nconsequence of it\".\n\nIt is gone because the selection turned out to be **forced**:\n`lem:feynman-eigenbasis-decomposition` already puts the row cap\n$\\ell(\\lambda) \\leq 2$ in the mass channel's decomposition, giving\n$y_{(1^3)} = 0$, and `markovWeights_eq_jones_of_threeRow_eq_zero`\nthen makes $z = q^3/(q^2+1)$ the unique faithful normalised Markov trace.\n\n**Not decided by experimental match, and the numbers say so.** Switching the\nbinding channel to D makes the aggregate *worse* — mean $|{\\rm err}|$ over\n$\\{{}^2$H, $^3$H, $^3$He, $^4$He, $^6$Li, $^7$Li$\\}$ moves $37.39\\% \\to\n43.85\\%$. What it fixes is structural: under C the deuteron was\n**unreachable**, $B_{\\rm AME} = 2.2246$ lying $30.4\\%$ below the whole\nadmissible band $[2.9072, 5.1780]$ MeV; under D the band is $[2.0507, 3.7978]$\nand AME sits inside it. ${}^2$H itself improves $+74.85\\% \\to +27.36\\%$.\n\nThe mass channel was already on D in production, so the $m_e$-scaled\nrenderings of $m_p$ and $m_n$ are **unchanged** (verified: $938.27208943$,\n$939.56542276$).\n\nPath A (ladder linear system) $=$ Path B (Wenzl Schur) as a\n$\\mathbb{Z}$-Laurent identity remains proven for C in the\n$y_\\lambda$–$\\mathrm{tr}_M$ equivalence proof; that identity is\nabout C and is now historical.",
    },
    {
      kind: "refined-framing",
      body: "**Correction note.** An earlier draft of this proposition claimed the\n$q = 1$ weights were *uniform* ($y_\\lambda(1) = 1/4$ for all\n$\\lambda \\vdash 3$) via a bar-involution argument. That claim was\nwrong — caught in review — for the reason documented in the chirality\nsection above: the Jones trace is not sign-twist invariant. The\ncorrected weights $(\\tfrac12, \\tfrac14, 0)$ are verified three ways:\nSchur orthogonality on the $q = 1$ cycle-counting trace, the exact\n$q$-dependent closed forms above, and canonical reproduction of the\nBorromean closed form at 30 digits.",
    },
    {
      kind: "refined-framing",
      body: "**Correction note (scope).** An earlier draft of the scope note above stated\nthat the framework's *mass and binding* computations use the full-Hecke\nOcneanu trace, and that the two traces coincide on writhe-$0$,\n$\\pi=\\mathrm{id}$ braids, \"which is why every physical mass prediction is\ninsensitive to the distinction\". Both parts were wrong. The production mass\nchannel is on convention D, not C; and writhe $0$ makes only the\n$y_{(3)}$–$y_{(1^3)}$ *split* invisible, not $y_{(2,1)}$, so the two\nconventions differ on $\\beta_{\\mathrm{Bor}}$ — which is writhe $0$ with\n$\\pi = \\mathrm{id}$ — by $195.8$ ppm exactly. The corrected statements are\nabove; the trace-convention registry is now the machine-checked source of\ntruth for which channel uses which trace.",
    },
  ],
});
