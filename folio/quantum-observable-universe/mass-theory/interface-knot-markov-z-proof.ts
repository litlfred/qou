import { proof } from "../../schema/builders";

export default proof({
  label: "prf:interface-knot-markov-z",
  title: "Proof of interface knot markov z",
  uses: ["prop:interface-knot-markov-z"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `conj:constit-factor-2q-minus-1`" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Per-atom interface census (from `atom_braid_word_3A`):" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): is checked exactly in\n[`pn_interface_bar_structure_probe.py`](../../../computations/probes/pn_interface_bar_structure_probe.py)\n(17 assertions), and the four identities that are field-theoretic rather than\nsubstrate-specific — $\\overline{z} = z - h$, the bar-symmetriser form, the bar\ndefect $-(\\overline{\\varepsilon} + \\varepsilon)h$, and the bar-even-iff-offset-bar-odd\nequivalence — are formalised over an arbitrary characteristic-zero field in\n[`QOU/MassTheory/PnInterfaceBarStructure.lean`](../lean/QOU/MassTheory/PnInterfaceBarStructure.lean),\nusing only the axioms `propext`, `Classical.choice` and `Quot.sound`." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): is\nformalised over a generic commutative ring as\n`interface_knot_markov_z_bar_symmetric` (the $\\tfrac12$ normalisation is\ndeferred to the archimedean realisation, per the base-ring convention)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): `prop:averaging-resonance-rule`" },
    {
      kind: "note",
      date: "2026-10-10",
      body: "The verification table replaces one measured at the excised convention-C weight z = √q/(q+1) (bean qou-7xpx). Producer: computations/probes/interface_knot_markov_z_convention_d_probe.py.",
    },
  ],
});
