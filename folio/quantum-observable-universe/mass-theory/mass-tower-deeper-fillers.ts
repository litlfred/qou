import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Prose restated without Lean vocabulary (voice drain, epic `qou-d4kh`). The previous text called the five items \"Mathlib extensions\" consolidated \"into a single synthesis class\"; the five are the fields (A)–(E) of that class, named in the note below.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c), now confined to one of the five fillers. Parts " +
        "(A)–(D) are substrate-side: (A) `HeightSixPartition` is over " +
        "$\\mathbb{N}$, (B) `IsDemazureSubCrystal` and (D) " +
        "`HasBlochGroupQuotient` quantify over a generic carrier, and (C) " +
        "`KLClassicalLimit` was de-specialised in this pass from `ℝ → ℝ` to " +
        "a generic `[CommRing R]` — the Kazhdan–Lusztig $q = 1$ " +
        "specialisation $H_n(R,q) \\to \\mathbb{Z}[S_n]$ is a ground-ring " +
        "homomorphism, so typing it over $\\mathbb{R}$ had mislabelled a " +
        "pre-archimedean operation as archimedean.\n\n" +
        "What forces the residual $\\mathbb{R}$ is (E) alone: " +
        "`Cl_2_PentagonIdentity.pentagon_holds_modulo_2pi` quantifies over " +
        "`α β γ : ℝ` because `Cl_2` is the *real* Clausen function " +
        "$\\mathrm{Cl}_2(\\theta) = \\sum_{k\\ge1}\\sin(k\\theta)/k^2$ " +
        "(`QOU.Archimedean.ClausenFunctionMathlibFiller`), i.e. the " +
        "Bloch–Wigner dilogarithm restricted to the unit circle. A Fourier " +
        "sine series has no statement over a generic `CommRing`: the " +
        "five-term functional equation is an identity of real-analytic " +
        "functions, and the \"modulo $2\\pi$\" qualifier is itself " +
        "archimedean. The same applies to " +
        "`Cl_2_zero_consistent_with_pentagon`, which evaluates `Cl_2` at $0$.",
      see: "folio/quantum-observable-universe/mass-theory/mass-tower-deeper-fillers.lean",
    },
  ],
  label: "rem:mass-tower-deeper-fillers",
  title:
    "Deeper conditional-class fillers: Term-7 enumeration, Demazure sub-crystals, KL classical limit, BlochGroup carrier, Cl_2 pentagon",
  interprets: "prop:crystal-basis-resolves-mass-tower-open-problems",
  uses: [
    "prop:type-b-folded-crystal-combinatorics",
    "rem:bloch-wigner-mathlib-filler",
  ],
  cites: [
    "borel1974",
    "bloch2000",
    "suslin1991",
    "kashiwara1991",
    "khovanovlauda2009",
    "zagier1986",
  ],
  tags: [
    "mathlib-filler",
    "deeper-scaffolding",
    "height-6-partition",
    "demazure-sub-crystal",
    "kazhdan-lusztig",
    "bloch-group",
    "pentagon-identity",
    "lean-infrastructure",
  ],
});
