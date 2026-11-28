import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:ns-counterexample",
  lean: { ref: "qou:QOU.FluidDynamics.NSCounterexample" },
  title:
    "Conjectural anti-parallel vortex-collision singularity in the $q \\to 1^+$ limit",
  uses: [
    "conj:universality",
    "prop:acoustic-horizon-conditions",
  ],
  tags: [
    "counter-example",
    "navier-stokes",
    "blowup",
    "yekutieli",
    "homological",
    "vortex-collision",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation regression guard (`qou-x60n`): `2026-08-29-q-ns-conjecture-statement-strength-probe.lean` (`noSingularityAtT_refuted_by_strengthened`) verifies the left-neighbourhood quantifier on `NSCounterexample` excludes profiles regular as `t → T*⁻`.",
      see: "docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutability witness (`qou-x60n`, `qou-rq9n`): `2026-08-30-qns-carriers-are-refutable.lean` proves `¬ NSCounterexample (fun _ => 0)`.",
      see: "docs/audits/2026-08-30-qns-carriers-are-refutable.lean",
    },
  ],
});
