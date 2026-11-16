import { proposition } from "../../schema/builders";

/**
 * The QOU mass formula as a categorical descent decomposition:
 * descended (central) + transient (exceptional divisor)
 * components.
 *
 * History: renamed from `prop:mass-categorical-descent` on 2026-05-18
 * to align with the QOU six-term-mass-formula production framework
 * (the BW naming framed the same descent decomposition around the
 * empirical Bethe-Weizsäcker formula; the structural content is
 * mass-formula-agnostic and recovers BW as one phenomenology).
 */
export default proposition({
  label: "prop:mass-categorical-descent",
  title:
    "QOU mass formula as descent decomposition of the mass endomorphism",
  tags: [
    "mass",
    "mass-formula",
    "descent-decomposition",
    "exceptional-divisor",
    "casimir",
    "wedderburn",
    "quantum-dilogarithm",
  ],
  lean: { ref: "qou:QOU.ParticleInteractions.mass_categorical_descent",
    validation: "not_checked",
  },
  uses: ["thm:wedderburn-mass-formula"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement asserted, as facts, that the descended components are the volume, pairing and Wigner terms of the liquid-drop model and the transient components the surface, Coulomb, exchange and shell terms. The proof sketch supports neither; it only splits the mass into a central part and a remainder, which holds by definition. Those identifications are now marked conjectural, and the Wigner term is flagged as an empirical import. Wedderburn–Artin was stated over a general ring $R$; it needs a field where $H_n$ is split semisimple. Queued for the weak-proofs pass: demote to a conjecture, since the block's content beyond the definitional split is unproved.",
    },
    {
      kind: "status",
      date: "2026-08-14",
      body:
        "**Lean carrier: route-(b) channel structure landed — file sorry-free " +
        "(beans `qou-oq5r`/`qou-e2fi`, owner-selected full formalization).** " +
        "The flat `B = B_desc + B_trans` over free data fields was refutable " +
        "as written (its own refutation theorem) and had no honest conditional " +
        "fix. Now `MassDescentChannels` carries the Wedderburn channel " +
        "structure (finite channel type, per-channel contributions, decidable " +
        "centre predicate) and the additive identity is *derived* " +
        "(`descent_decomposition`: the splitting of a finite sum along the " +
        "centre predicate). Open physics, honestly confined to the absent " +
        "corpus instance: `Channel = {λ ⊢ n} + divisor sites`, " +
        "`contrib λ = m_e·y_λ χ^λ Δ_λ`, centrality = Casimir membership, and " +
        "the identification of `B_total` with the physical binding. " +
        "Verified lean-direct exit 0.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module `lean/QOU/ParticleInteractions/mass_categorical_descent.lean` " +
        "carries binding energies `B`, `B_desc`, `B_trans`, `B_BW` as physical quantities. " +
        "The `ℝ` is therefore forced by the statement itself rather than " +
        "chosen, so the block sits on the archimedean side of the §7c wall " +
        "by construction.",
    },
  ],

});
