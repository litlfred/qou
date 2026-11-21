import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:brings-euler-characteristic",
  lean: { ref: "qou:QOU.ArchimedeanUniverse.brings_euler_characteristic",
    validation: "not_checked",
  },
  title: "Euler characteristic of Bring's surface",
  tags: ["euler-characteristic", "brings-surface", "categorical-trace", "descartes-substrate"],
  uses: ["prop:euler-char-stability", "rem:hkr-theorem"],
  foreshadows: ["rem:three-euler-characteristics", "rem:euler-characteristic-of-the-regular-representation"],
  proofs: ["prf:brings-euler-characteristic"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "**ENACTED (owner selection A, 'separate by name', 2026-09-15).** The statement no longer calls `-6` a categorical trace: it is `chi_eu(Sigma_4)`, the topological Euler characteristic of the base curve, with its Hochschild reading. The proof's sentence recovering `-6` as \"the quantum dimension specialised at q_0\" is withdrawn — under the ruling `tr(id_A) = dim_q(A)`, the Peter–Weyl series for `A = O_q(SU(2))` diverges and its regularised value is `0` (zeta) or `-1/(q-q^-1)^2` (Hadamard), never `-6` (`computations/audits/dimq_regularisation_schemes_probe.py`, 16/16). Analysis: `docs/audits/2026-09-15-chi-as-a-component-of-the-chern-character.md`. The Lean sibling `brings_euler_characteristic` still proves `2 - 2g = -6` from `g = 4` and is unaffected.",
    },
    {
      kind: "note",
      date: "2026-09-15",
      body:
        "**🟧 OWNER RULING 2026-09-15 settles the symbol: `tr(id_A)` is the quantum dimension `dim_q(A)`, the Euler characteristic of an object IN THE QOU CATEGORY — so it is q-DEPENDENT.** Consequence for this block: the `-6` here is a **topological** Euler characteristic `chi_eu(Sigma_4)`, a different object from the categorical trace, so it is not a competing value and is not wrong. But the `prop:euler-char-stability` bridge this block invokes is now a **substantive claim relating two different things** rather than a restatement — it equates a q-dependent quantity with a q-independent integer, which can hold at most on a locus in q. Whether that locus contains q_0 is open. And this block's own proof recovers -6 as *\"the quantum dimension specialised at q_0\"* — now the right register, but a quantum dimension of -6 is **negative**, while dim_q of an object in a rigid category with positive structure constants is positive (the fundamental gives +2.0109). So the -6 needs the Euler-characteristic-of-a-complex sense, an alternating sum, not a naive dim_q. Not decided here. Register entry in `notation/notation-collisions.md`; bean `qou-2uf0`.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The categorical trace $\\mathrm{tr}(\\mathrm{id}_A) = \\dim_q(A)$ is a different quantity ([the three Euler characteristics](#rem:three-euler-characteristics)); for $A = \\mathcal{O}_q(\\mathrm{SU}(2))$ its regularised value is $0$ ([Euler characteristic of the regular representation](#rem:euler-characteristic-of-the-regular-representation))." },
  ],
});
