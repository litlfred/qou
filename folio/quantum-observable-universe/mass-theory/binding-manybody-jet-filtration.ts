import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:binding-manybody-eq-jet-filtration",
  title:
    "Binding many-body series equals the jet-order filtration: $B(K)=\\sum_n m_e\\,a_D^{(n)}$",
  lean: {
    ref: "qou:QOU.Mass.BindingManyBodyJetFiltration",
    validation: "validated",
  },
  uses: [
    "lem:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
    "prop:magic-A-binding-formula",
  ],
  tags: [
    "binding",
    "many-body",
    "jet-order-filtration",
    "seiberg-witten",
    "q-difference",
    "step-9b",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/binding_n3_forcing_probe.py, computations/coulomb_energy.py, docs/audits/2026-08-26-n3-body-order-forcing.md.",
    },
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/d_from_scratch.py",
    witness: "computations/d-from-scratch.witness.json",
    status: "verified",
  },
});
