import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:mass-side-kernel-formalize-first-gates",
  title:
    "Mass-side $\\S 4$ formalize-first gates as parametric Lean classes — `MassSideKernel` bundles anchor-stability, q=1 shadow (open gap), and direction sanity for any `linking_weight` candidate $w(q)$; mirrors the $Q_\\beta$ `BarEvenKernel` typeclass",
  lean: {
    ref: "qou:QOU.Mass.MassSideKernelFormalize.MassSideKernel",
    validation: "not_checked",
  },
  uses: [
    "prop:q-beta-bar-even-kernel-invariant",
    "prop:q-beta-bar-even-kernel-typeclass",
    "prop:q-beta-radius-of-convergence-gate",
    "prop:q-beta-q-eq-one-shadow-gate",
    "prop:q-beta-direction-sanity-gate",
  ],
  cites: ["jones1987", "wenzl1988", "habiro2004"],
  tags: [
    "mass-theory",
    "linking-weight",
    "structural",
    "formalize-first",
    "parametric-typeclass",
    "kernel-invariant",
    "no-fit",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-06-06",
      body: [
        "Authoring archaeology (moved out of prose per CLAUDE.md §4d, \"Author notes vs. scholarly prose\").",
        "",
        "**Typeclass pattern.** The Lean typeclass mirrors the decay-side `BarEvenKernel` pattern introduced in PR #1893; the sympy companion `mass_theory_formalize_first_invariants_probe.py` (PR #1896, Track 3) runs the 4×3 verdict matrix on Family A / via-Jones / Bring color-tube candidates.",
        "",
        "**Direction-sanity form.** The additive direction-sanity form follows the decay-side `q-beta-direction-sanity-gate.lean` precedent from PR #1890.",
        "",
        "**Bar-even structural identity.** The §4(b) bar-even invariant is the CommRing R lemma from PR #1875.",
        "",
        "**§4(c) anchor candidate.** A `Σ f^λ / 4 = 5/2` value for the §4(c) anchor was surfaced by PR #1899's mass-side q=1 anchor hunt; the parametric class admits this via `MassQOneShadowGateClass w (some (5/2))` but does not assert it as the canonical anchor.",
      ].join("\n"),
    },
  ],
});
