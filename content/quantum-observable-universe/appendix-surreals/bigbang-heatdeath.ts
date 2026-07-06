import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bigbang-heatdeath",
  title:
    "Big Bang and heat-death functors as evaluations at named surreal endpoints",
  lean: { ref: "qou:QOU.AppendixSurreals.BigBangHeatDeath", validation: "stub" },
  tags: [
    "tier:P",
    "surreal-numbers",
    "big-bang",
    "heat-death",
    "cosmology",
    "functor-limit",
    "named-infinity",
    "open-problem",
    "speculative",
  ],
  uses: ["conj:classical-limit-stpart"],
  cites: ["conway1976"],
  authorNotes: [
    {
      kind: "caveat",
      body: "**Highly speculative** and outside the appendix's main thrust. It is included to record an evident application of named-surreal calculus (Big Bang $\\sim 1 + \\varepsilon^\\omega$; heat death $\\sim \\omega$) without claiming any of the physics-of-cosmology details. The QOU paper does not commit to any particular cosmological reading, and this conjecture should not be read as such.\n\nThe mathematical content — that the QOU functors evaluate at named infinite/infinitesimal surreals — is correct (rational expressions in $q$ make sense at any non-pole element of $\\mathbf{No}$). The interpretive content — that these are *the* Big Bang and heat death — is metaphor, pending a separate discussion of cosmological time in QOU.",
    },
  ],
});
