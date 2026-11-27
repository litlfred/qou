import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:critical-exponent",
  lean: { ref: "qou:QOU.FluidDynamics.CriticalExponent" },
  title: "Critical exponent of the enstrophy divergence at $q = 1$",
  uses: [
    "prop:q-ns-nonlinear-uniqueness",
    "conj:regularity-breakdown",
  ],
  tags: ["critical-exponent", "enstrophy", "phase-transition", "scaling"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation regression guard (`qou-x60n`): `2026-08-29-q-ns-conjecture-statement-strength-probe.lean` (`regularAtOne_refuted_by_strengthened`) verifies the punctured-neighbourhood quantifier on `CriticalExponent` excludes functions bounded near `q = 1⁺`.",
      see: "docs/audits/2026-08-29-q-ns-conjecture-statement-strength-probe.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-hjf4`): `2026-08-30-conditional-cone-binders-unused-probe.lean` exposed unused `[CriticalExponent]` binders and the `(3 * 4 : ℕ) = 12` placeholder in pre-repair `ConditionalCorollaries.lean`.",
      see: "docs/audits/2026-08-30-conditional-cone-binders-unused-probe.lean",
    },
    {
      kind: "note",
      date: "2026-11-24",
      body: "Formalisation refutability witness (`qou-x60n`, `qou-4670`): `2026-08-30-qns-carriers-are-refutable.lean` proves both refutation directions and satisfiability at `(q - 1)⁻¹` for the de-boxed `CriticalExponent` carrier.",
      see: "docs/audits/2026-08-30-qns-carriers-are-refutable.lean",
    },
  ],
});
