import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:infinitesimal-frobenius",
  title:
    "Infinitesimal Frobenius pairing: $\\int_A \\circ \\mu = \\mathrm{id} + O(\\varepsilon)$",
  lean: { ref: "qou:QOU.AppendixSurreals.InfinitesimalFrobenius", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "frobenius",
    "infinitesimal",
    "axiom-relaxation",
    "open-problem",
  ],
  uses: ["conj:archimedean-stpart"],
  cites: ["robinson1966"],
  authorNotes: [
    {
      kind: "status",
      body: "**Open.** Constructing a non-trivial example in\n$\\mathrm{Rep}_{\\mathbf{No}}(\\mathrm{SU}_q(2))$ would establish (2);\nabsence of such examples (i.e. every $\\varepsilon$-Frobenius\nalgebra is gauge-equivalent to a strict one) would refute it.\n\nThe matter is delicate because the $\\mathrm{Rep}(\\mathrm{SU}_q(2))$\ncategory has rigid Frobenius structure\n([fibre functor rigidity](#rem:fibre-functor-rigidity)) — every\nsmall deformation is trivial. So the candidate examples must lie\n*outside* this rigid regime, in larger or non-rigid Frobenius\nalgebras.",
    },
  ],
});
