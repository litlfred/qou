import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:q-plancherel-asymptotic-skeleton",
  title:
    "Asymptotic skeleton of the q-Plancherel measure $\\tilde w_\\lambda$ — convergence on a continuous Young-diagram space",
  lean: {
    ref: "qou:QOU.Observations.QPlancherelAsymptoticSkeleton",
    validation: "not_checked",
  },
  cites: [
    "vershik-kerov1977",
    "biane1998",
    "feray2010",
  ],
  tags: [
    "causal-fermion-systems",
    "plancherel",
    "asymptotic-plancherel",
    "kerov-vershik",
    "wedderburn-weight",
    "thoma-simplex",
    "partly-established",
  ],
  uses: ["prop:wedderburn-weight-canonical", "prop:algebraic-gns-embedding"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "The Lean module " +
        "`lean/QOU/Observations/QPlancherelAsymptoticSkeleton.lean` uses " +
        "`Real.sqrt`. These are real-analytic constructs with no " +
        "generic-`CommRing` counterpart, so the `ℝ` specialisation is " +
        "forced by the statement itself rather than chosen. The block " +
        "therefore sits on the archimedean side of the §7c wall by " +
        "construction.",
    },
  ],
});
