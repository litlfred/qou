import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:q-collatz",
  title:
    "The $q$-Collatz conjecture: Skein-module crossing resolution",
  lean: { ref: "qou:QOU.AppendixSurreals.QCollatz", validation: "stub" },
  uses: [
    "rem:substrate-gm-torsion",
    "thm:qou-obstruction-reduction",
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
  cites: ["collatz1937", "lagarias2010"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-18",
      body:
        "Domain-stability refinement backing: computations/qcollatz_divergence_probe.py + .witness.json. Forward-orbit census (6045 positive Laurent seeds, window q^-3..q^5): 6042 escape the domain {P(-1)∈{0,-1}} (5369 after one step, max in-domain prefix 4), 0 divergent, 0 rogue cycles; the only convergents are the fundamental 2-cycle {q^-1,1+q^-1} and its backward-tree preimages. Motivates the domain-stable cone. Cycle half: qcollatz_cycle_census (period<=18).",
    },
  ],
});
