import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:brunnian-binding-channel",
  title:
    "The binding multiplier is the unsigned coordination count, not a Gauss linking number: forced by Brunnian topology and bar-parity",
  lean: {
    ref: "qou:QOU.Mass.BrunnianBindingChannel.brunnian_energy_is_count_channel",
    validation: "not_checked",
  },
  uses: ["def:crossing-energy"],
  cites: ["kassel1995"],
  tags: [
    "binding",
    "coordination-number",
    "brunnian",
    "linking-number",
    "crossing-energy",
    "bar-parity",
    "many-body",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): which is exactly what `QOU.Mass.ClosureNormalisationDefect` makes precise (`freeEnergy_closureNorm_additive_iff`: additivity holds iff $\\delta = 1$, excluded for $q > 1$)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): (the complete graph is excluded there, `QOU.Mass.CoordinationSaturation`)." },
    {
      kind: "note",
      body: "An earlier version of this paragraph conflated connected-sum multiplicativity of the Jones polynomial with the disjoint-union loop value.",
    },
    {
      kind: "status",
      date: "2026-08-30",
      body:
        "**Proved (Lean, sorry-free).** `QOU.Mass.BrunnianBindingChannel` (lean-direct exit 0; axioms `propext`/`Classical.choice`/`Quot.sound`). Resolves the *type question* of bean `qou-brng` — the binding multiplier is an unsigned coordination count, complementary in bar-parity to the bar-even mass self-trace. Still open: the exact `n₊+n₋ → z=A−1` coefficient beyond the minimal-bond model, and the Hamiltonian-level claim that rest mass **is** the closed self-trace and binding **is** the open mutual pairing. Audit: [docs/audits/2026-08-30-brunnian-binding-channel.md](../../../docs/audits/2026-08-30-brunnian-binding-channel.md).",
    },
  ],
});
