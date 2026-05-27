import { conjecture } from "../../schema/builders";

export default proposition({
  label: "prop:bigbang-heatdeath",
  title:
    "Big Bang and heat-death functors as evaluations at named surreal endpoints",
  lean: { ref: "qou:QOU.AppendixSurreals.BigbangHeatdeath", validation: "stub" },
  tags: [
    "surreal-numbers",
    "big-bang",
    "heat-death",
    "cosmology",
    "functor-limit",
    "named-infinity",
    "open-problem",
    "speculative",
  ],
  uses: ["prop:classical-limit-stpart"],
  cites: ["conway1976"],
});
