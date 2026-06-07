import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:bigbang-heatdeath",
  title:
    "Big Bang and heat-death functors as evaluations at named surreal endpoints",
  lean: { ref: "qou:QOU.AppendixSurreals.BigbangHeatdeath", validation: "stub" },
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
});
