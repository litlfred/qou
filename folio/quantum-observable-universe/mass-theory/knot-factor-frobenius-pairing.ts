import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:knot-factor-frobenius-pairing",
  title:
    "Knot factor as Frobenius self-pairing ratio",
  lean: { ref: "qou:QOU.BraidKnot.KnotFactorFrobeniusPairing",
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
      kind: "refined-framing",
      date: "2026-11-22",
      body: "The braid-level half is now a theorem: for every cyclic trace t on H_n(q), q ≠ 0, and every splitting, t(x) = τ(x·κ) with the unique central knot factor κ = Σ_λ y_λ s_λ e_λ (`QOU.Hecke.KnotFactor`, sorry-free; the Lean carrier `QOU.BraidKnot.KnotFactorFrobeniusPairing` was retyped to an algebra element on owner approval). The Markov trace is not yet a linear functional on that Hecke type, so the Markov instance waits on that definition. The binding half is a definition (`QOU.Conjectures.bindingDefect`) plus a comparison point against AME2020 (dashboard `B_can⁰`); the statement still open here is that comparison. With the γγ-selected interface bond the difference form gives ⁴He ≈ −1.6 keV (`computations/probes/he4_gg_all_pairs/`).",
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
