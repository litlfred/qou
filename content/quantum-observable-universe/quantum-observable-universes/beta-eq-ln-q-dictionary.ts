import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-02",
      body:
        "R1 of the partition-function unification: the Frobenius/Markov trace $\\mathrm{tr}_M = \\sum_{\\lambda} y_\\lambda(q)\\,\\chi_\\lambda$ read as a statistical-mechanics partition function, with Wedderburn blocks as microstates and $\\beta = \\ln q$. Lean sibling `QOU.Thermo` (archimedean over $\\mathbb{R}$, AGENTS.md §7c): `boltzmann_energyOf` (read-off correct), `energyOf_unique` (unique energy), `energyOf_le_iff` (order-reversing: dominant block = ground state), `partition_sum_eq` ($\\sum d_\\lambda e^{-\\beta E_\\lambda} = \\sum d_\\lambda y_\\lambda$). Sorry-free; axioms `propext, Classical.choice, Quot.sound` only. Scope: takes the weights $y_\\lambda>0$ as given (they are supplied by Schur--Weyl); closes no physics observable, since energies are relative to the weights.",
    },
  ],
  label: "prop:beta-eq-ln-q-dictionary",
  title: "The $\\beta = \\ln q$ partition-function dictionary",
  tags: ["partition-function", "markov-trace", "temperature", "wedderburn", "categorical"],
  lean: { ref: "qou:QOU.Thermo.boltzmann_energyOf", validation: "not_checked" },
  uses: ["prop:q-exp-entire"],
});
