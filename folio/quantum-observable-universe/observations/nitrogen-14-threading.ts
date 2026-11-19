import { example } from "../../schema/builders";

export default example({
  label: "ex:nitrogen-14-threading",
  title:
    "The ${}^{14}\\mathrm{N}$ maximal braid shortcut vs ${}^{14}\\mathrm{C}$ broken alternation",
  tags: [
    "nitrogen-14",
    "carbon-14",
    "braid-word",
    "threading",
    "alternation",
    "pauli-cost",
    "coulomb",
    "beta-decay",
  ],
  uses: ["thm:markov-trace-factorization"],
  computation: {
    engine: "mpmath",
    script: "computations/probes/h2_gg_electron/h2_gg_electron_probe.py",
    witness: "computations/probes/h2_gg_electron/h2-gg-electron.witness.json",
    status: "verified",
  },
});
