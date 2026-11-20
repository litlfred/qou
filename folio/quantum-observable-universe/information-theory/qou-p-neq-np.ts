import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qou-p-neq-np",
  title:
    "$\\mathrm{P} \\neq \\mathrm{NP}$ at non-torsion $q \\in \\mathbb{G}_m$",
  lean: { ref: "qou:QOU.Information.QouPNeqNp", validation: "stub" },
  tags: [
    "tier:famous",
    "P-vs-NP",
    "Gm-torsion",
    "obstruction",
    "millennium-problem",
    "substrate-parameter",
    "computational-horizon",
  ],
  uses: [
    "conj:p-vs-np-boundary",
    "ex:chi-minus-six-derivation",
    "prf:qou-obstruction-reduction",
  ],
  cites: ["jaeger1990", "aharonov2009", "freedman2003", "cook1971"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean carrier makes the conditioning explicit: `qou_implies_p_neq_np` derives the QOU-scoped separation `PNeqNPInQOU` *from* a `QouPNeqNp` instance (the QOU faithfulness hypothesis) — it never concludes a bare $\\mathrm{P} \\neq \\mathrm{NP}$.\n\ntogether they are the open, un-instantiated `faithful` field of the Lean carrier [`QouPNeqNp`](../lean/QOU/Information/QouPNeqNp.lean) — which is itself (the gap is carried as a *class hypothesis*, never an `axiom` or `instance`; a fabricated instance would launder the conjecture into a proof):\n\nThis genericity is itself Lean-proved, in the companion module [`ObstructionGenericity`](../lean/QOU/Information/ObstructionGenericity.lean): a nonzero\n\nformalized in the companion module [`PNeqNpEquivalence`](../lean/QOU/Information/PNeqNpEquivalence.lean) (the class `ResidueFaithfulness` carries *soundness* $\\mathrm{P} \\neq \\mathrm{NP} \\Rightarrow \\mathrm{res} \\neq 0$ and *faithfulness* $\\mathrm{res} \\neq 0 \\Rightarrow \\mathrm{P} \\neq \\mathrm{NP}$ as separate hypotheses, and the equivalence is derived from them). Given the derived non-vanishing, three facts are machine-checked:\n\n$\\mathrm{P}$, $\\mathrm{NP}$ remain an opaque proposition pending a formal complexity-theory layer.\n\nThese enter the formalization as the cited hypothesis class `JonesComplexityCitations` (carried in the type, never instantiated — a fabricated instance would launder literature into a proof). Modulo that class and the residue--semisimplicity bridge, the reachable companion faithfulness is machine-checked:\n\nrequires exactly two open inputs, displayed as the hypotheses of `faithfulness_of_transfer`:\n\nits parameter side is done: `WenzlGeneric` formalizes \"$q^k \\neq 1$ for $2 \\leq k \\leq n$\" over a generic monoid, `wenzlGeneric_of_one_lt` proves every real $q > 1$ satisfies it at every rank, and `counting_faithfulness_of_one_lt` composes end-to-end — for the substrate $q_0 > 1$, given $\\mathrm{FP} \\neq \\#\\mathrm{P}$, exact Jones evaluation is not polynomial-time, conditional only on the two cited classes.\n\nStage 2 advances this on the Schur-element side ([`WenzlSchurElement`](../lean/QOU/MathlibExt/WenzlSchurElement.lean) infrastructure): semisimplicity is governed by non-vanishing of the Schur elements of the symmetrizing trace, and `schurElement_ne_zero` proves — on\n\nThe Geck--Pfeiffer criterion enters as the cited class `SchurElementCriterion`, and `semisimple_of_substrate` discharges semisimplicity at every rank with the Schur leg computed rather than assumed.\n\nit is proved in [`WenzlSchurElement`](../lean/QOU/MathlibExt/WenzlSchurElement.lean), and the surviving blocks\n\n`substrate_avoids_tl_locus` proves $X \\leq 0 \\Rightarrow X \\neq Q^{-N}$ for every $N$,\n\nThe reachable counting statement `counting_faithfulness_of_one_lt` consumes only\n\nthe pair displayed by `faithfulness_of_transfer`.\n\nThis physical-intractability theorem is proved (`QOU.Information.qou_physical_intractability_unconditional`; the exponential-domination fact it rests on is proved, `superPoly_two_pow`).\n\none shared object, `QOU.Information.SkeinObservationSystem`, on which the P-side is `PolyObservable` and the boundary" },
    {
      kind: "refined-framing",
      body: "Earlier drafts stated the G_m-torsion dichotomy backwards.",
    },
  ],
});
