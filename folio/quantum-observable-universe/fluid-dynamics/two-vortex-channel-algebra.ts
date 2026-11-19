import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-vortex-channel-algebra",
  title: "Channel algebra of the two-vortex interaction",
  tags: ["vortex", "channel", "hecke", "spectral", "hopf"],
  lean: { ref: "qou:QOU.FluidDynamics.TwoVortexChannelAlgebra.channel_algebra",
    validation: "not_checked",
  },
  uses: [
    "prop:r-matrix-braiding-structure",
  ],
  examples: ["rem:two-vortex-scattering-channels"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-05",
      body:
        "Detangler forward-ref resolution (foxn, audit " +
        "`docs/audits/2026-07-05-detangler-watcher-swarm2.md`). The Hopf-channel " +
        "reference `def:van-der-waals-hopf-channel` (information-theory, a later " +
        "chapter) was removed from `uses[]`: this proposition is proved " +
        "*abstractly* over a generic commutative ring $R$ from the self-contained " +
        "axioms (1)-(4), so the reader is not asked to rely on the Hopf-channel " +
        "definition to follow the argument — it names the *intended model* only. " +
        "The motivational pointer is retained as the prose cross-reference " +
        "`[Hopf channel](#def:van-der-waals-hopf-channel)`, so discoverability is " +
        "preserved; only the spurious logical-dependency edge (which the " +
        "forward-ref classifier scored as `L-dependency`) is dropped. The " +
        "van-der-Waals/Hopf definition genuinely belongs in its information-theory " +
        "home chapter (subject-matched), and the true logical flow runs the other " +
        "way: that definition consumes this channel algebra, not vice versa.",
    },
    {
      kind: "status",
      body: "Lean sibling over generic CommRing (`QOU.FluidDynamics.TwoVortexChannelAlgebra`): `channel_algebra` and standalone field lemma `eigenvalue_ratio`.",
    },
  ],
});
