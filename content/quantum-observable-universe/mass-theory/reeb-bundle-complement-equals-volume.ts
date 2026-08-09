import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:reeb-bundle-complement-equals-volume",
  lean: {
    ref: "qou:QOU.BraidsKnots.ReebBundleComplementEqualsVolume",
    validation: "not_checked",
  },
  title:
    "Reeb-bundle complement is the JSJ-graded volume sum (Reeb-bundle face of mass-volume)",
  tags: [
    "knot-complement",
    "hyperbolic-volume",
    "jsj-decomposition",
    "reeb-bundle",
    "mass-volume",
    "markov-trace",
  ],
  foreshadows: ["conj:mass-volume-factorization"],
  uses: [
    "prop:six-canonical-knot-operators",
    "conj:mass-volume-factorization",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`MassVolumeFactorization` types `markov_trace` and " +
        "`jsj_volume_sum` over `ℝ`. The geometric side is a JSJ-graded " +
        "*hyperbolic volume* — a transcendental quantity with no " +
        "generic-ring form — so the bridge identity is necessarily stated " +
        "post-wall. The conditional-class packaging (§3b-cond) is " +
        "orthogonal to the base-ring question.",
    },
  ],
});
