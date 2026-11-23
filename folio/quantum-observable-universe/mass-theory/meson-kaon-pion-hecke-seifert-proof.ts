import { proof } from "../../schema/builders";

export default proof({
  label: "prf:meson-kaon-pion-hecke-seifert",
  title: "Proof of meson kaon pion hecke seifert",
  uses: ["prop:meson-kaon-pion-hecke-seifert"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ## Computational witness\n\n[`meson-kaon-pion-derivation.witness.json`](../../../computations/meson-kaon-pion-derivation.witness.json)\nverifies the formula at $50$-digit precision, confirms the algebraic\nidentity $q^5 - q^{-5} = h \\cdot [5]_q$, and validates the Seifert\nratio $V_S(T(2,5))/V_S(T(2,3)) = 9/5$ exactly.\n\n## Lean structure — what is proved vs. the remaining gap\n\nThe Lean sibling separates the **two algebraic identities** (proved)\nfrom the **physical / empirical content** of the mass-ratio\nclaim (not a Lean theorem). This makes precise what remains \"to be\nproved\" downstream.\n\n| Lean declaration | content | status |\n|---|---|---|\n| `chi_21_odd` | $\\chi^{(2,1)}(\\sigma_1^n)=q^n+(-q^{-1})^n=q^n-q^{-n}$ for odd $n$ | **proved** |\n| `seifert_ratio_T25_T23` | $V_S(T(2,5))/V_S(T(2,3))=9/5$ | **proved** (needs char $\\neq 2,3,5$) |\n| `meson_squaring_exponent` | the exponent record $n_q=2$ | **proved** (`rfl`) |\n| `mesonMassRatio` | the assembled formula $\\chi^{(2,1)}(\\sigma_1^5)\\cdot(9/5)^2$ | **definition** |\n\n**The gap (NOT Lean-proved, and intentionally so):**\n\n1. **The exponent $n_q=2$** has a *physical rationale* (two-quark\n   composite) and is *not contradicted* by the power scan ($290$ ppm at\n   $n_q=2$ vs $4.4\\times 10^5$ ppm at $n_q=1$). It is **not derived** from\n   the substrate, and the scan does not supply the missing derivation —\n   see the caveat in the proof body. The `meson_squaring_exponent` lemma\n   only records the value; it does not select it.\n2. **The canonical exact match to the PDG ratio** ($\\approx 290$ ppm) is a\n   *witnessed near-match*, not a Lean equality — the witness JSON is the\n   evidence, the Lean file proves only the two underlying identities.\n\n**Base-ring note.** The Lean sibling is stated over a generic\n`[Field R]` (no archimedean `$\\mathbb{R}$` dependence). `chi_21_odd` is\nunconditional; `seifert_ratio_T25_T23` carries explicit `$2,3,5\\neq 0$`\nhypotheses — the invertibility the rational identity genuinely needs,\nvacuous in any characteristic-0 specialisation. This avoids `CharZero`\nentirely and is verified (`lake env lean`)." },
    {
      kind: "note",
      date: "2026-08-08",
      body: "Moved out of the published prose (one-voice sweep): the base-ring note used to add \"(so it stays inside the sandbox cache cone)\" after \"This avoids `CharZero` entirely\". That is the build rationale \u2014 stating the char \u2260 2,3,5 hypotheses explicitly instead of importing `CharZero` keeps the Lean file inside the sandbox's Mathlib cache \u2014 and it belongs here rather than in the paper.",
    },
  ],
});
