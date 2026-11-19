import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Skein-module crossing resolution",
  lean: { ref: "qou:QOU.AppendixSurreals.QCollatz", validation: "stub" },
  // Two entries removed 2026-08-15 to break editorial cycles.
  //
  // `rem:skein-filtration-trichotomy` synthesises across three problems of
  // which this conjecture is one, and lists this conjecture in its own
  // `uses[]`. A problem statement does not require the remark that discusses
  // it; the reader meets the conjecture first and the synthesis after.
  //
  // `prop:ns-kummer-specialisation` is cited here as a parallel, not a
  // prerequisite — "Compare the same caveat on … the Navier--Stokes leg" — and
  // it lists this conjecture transitively. A comparison is not a dependency.
  uses: [
    "rem:substrate-gm-torsion",
    "thm:qou-obstruction-reduction",
    "conj:qou-p-neq-np",
  ],
  tags: [
    "tier:famous",
    "collatz",
    "skein-module",
    "hecke-algebra",
    "number-theory",
    "q-deformation",
    "crossing-resolution",
    "convexity",
    "jones-polynomial",
    "markov-trace",
  ],
  cites: [
    "collatz1937",
    "lagarias2010",
    "aaronsonwigderson2009",
    "grochow2017",
    "razborovrudich1997",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-18",
      body:
        "Domain-stability refinement backing: computations/qcollatz_divergence_probe.py + .witness.json. Forward-orbit census (6045 positive Laurent seeds, window q^-3..q^5): 6042 escape the domain {P(-1)∈{0,-1}} (5369 after one step, max in-domain prefix 4), 0 divergent, 0 rogue cycles; the only convergents are the fundamental 2-cycle {q^-1,1+q^-1} and its backward-tree preimages. Motivates the domain-stable cone. Cycle half: qcollatz_cycle_census (period<=18).",
    },
    {
      kind: "refined-framing",
      date: "2026-08-15",
      body:
        "Lean references for the obstruction and length-filtration discussion: QOU/AlgebraicSubstrate/collatz_obstruction_link.lean (links kappa_C only to Kummer removability at n | chi(A)), QOU/Information/ObstructionGenericity.lean (cofinite non-vanishing locus in q), QOU/Information/SkeinCounterfactual.lean (halting set vs single-proposition scalar distinction, corrected 2026-08-15), QOU/Information/ObstructionVerdictCap.lean (independent verdicts across legs), and QOU.Information.SkeinObservationSystem (Halts / halts_of_len_descent).",
    },
  ],
});
