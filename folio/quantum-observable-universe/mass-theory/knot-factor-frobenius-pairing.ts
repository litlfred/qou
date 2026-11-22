import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:knot-factor-frobenius-pairing",
  title:
    "Knot factor as Frobenius self-pairing ratio",
  lean: { ref: "qou:QOU.BraidKnot.HeckeFunctional.markovKnotFactor",
    validation: "not_checked",
  },
  uses: [
    "conj:nuclear-knot-classification",
    "rem:fibre-functor-rigidity",
    "conj:confinement-frobenius-reciprocity",
    "def:q-casimir",
    "rem:adjoint-trace",
    "def:q-heat-equation",
      ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "Markov instance proved: the Markov trace is now a linear functional on `QOU.Hecke.IwahoriHecke K q n` (`heckeMarkovTrace`, via σ_i ↦ s σ_i with s² = q, s h = q − 1), and `markovKnotFactor` / `markov_trace_eq_tau_mul_knotFactor` give tr_M x = τ(x κ) with κ central, for q ≠ 0 and every splitting (block `prop:markov-trace-hecke-functional`, sorry-free). `lean.ref` now points at that instance. The braid half of this conjecture is therefore a theorem for the Markov trace. The binding half (comparison against AME2020) is still open.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-22",
      body: "The braid-level half is now a theorem: for every cyclic trace t on H_n(q), q ≠ 0, and every splitting, t(x) = τ(x·κ) with the unique central knot factor κ = Σ_λ y_λ s_λ e_λ (`QOU.Hecke.KnotFactor`, sorry-free; the Lean carrier `QOU.BraidKnot.KnotFactorFrobeniusPairing` was retyped to an algebra element on owner approval). The Markov instance has since been proved (see the 2026-11-22 status note). The binding half is a definition (`QOU.Conjectures.bindingDefect`) plus a comparison point against AME2020 (dashboard `B_can⁰`); the statement still open here is that comparison. With the γγ-selected interface bond the difference form gives ⁴He ≈ −1.6 keV (`computations/probes/he4_gg_all_pairs/`).",
    },
  ],
  cites: ["yekutieli2015", "kassel1995"],
  tags: [
    "tier:keystone",
    "frobenius-pairing",
    "self-duality",
    "knot-factor",
    "rigid-monoidal",
    "categorical-binding",
    "reciprocity",
  ],
});
