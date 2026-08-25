import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:kashaev-surreal",
  title:
    "Kashaev volume conjecture as a surreal standard-part identity",
  lean: { ref: "qou:QOU.AppendixSurreals.KashaevSurreal", validation: "stub" },
  tags: [
    "tier:famous",
    "surreal-numbers",
    "kashaev",
    "volume-conjecture",
    "hyperbolic-volume",
    "standard-part",
    "open-problem",
    "reformulation",
  ],
  uses: [
    "rem:kashaev-volume-density",
    "conj:kashaev-volume-conjecture",
    "def:surreal-blowup-calculus",
    "def:ecalle-borel-resummation",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "berarducci-mantova2018",
    "ecalle1981",
    "garoufalidis-zagier-2024",
    "garoufalidis-gu-marino2021",
    "fantini-rella2024",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-13",
      body:
        "**Figure-eight instance discharged (conditional on the transfer " +
        "equivalence only).** For $K = 4_1$ the classical Kashaev limit is " +
        "the Murakami–Murakami theorem, so the surreal standard-part " +
        "identity holds with $=$ for $4_1$; Garoufalidis–Zagier quantum " +
        "modularity supplies the exact all-orders cocycle refinement and " +
        "Garoufalidis–Gu–Mariño the integer Stokes data. General knots " +
        "remain open. See the 2026-07-13 alien-calculus ↔ surreal " +
        "integration review audit.",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body:
        "Lean sibling: archimedean specialisation over $\\mathbb{R}$ " +
        "(AGENTS.md §7c). Here the $\\mathbb{R}$ is not the surreal ordering " +
        "— it is the standard-part map, and the conjecture is *about* that " +
        "map, so it cannot be moved. `KashaevSurreal.st_volume_eq_asymptotic` " +
        "asserts $\\mathrm{st}\\big(2\\pi\\,\\log|J(\\zeta_\\omega,\\omega)| / " +
        "\\omega\\big) = \\mathrm{Vol}(S^3 \\setminus K)$, and both sides are " +
        "**real numbers**: `standardPart : K → ℝ` on the left, " +
        "`HyperbolicVolume : Knot → ℝ` on the right. The $2\\pi$ is " +
        "`SurrealField.ofReal Real.pi`, and `surrealLog` is not a surreal " +
        "primitive at all — the file defines it as " +
        "`ofReal (Real.log (standardPart x))`, i.e. it routes through " +
        "$\\mathbb{R}$ by construction. An equation between two reals, " +
        "obtained by taking standard parts, has no `CommRing` restatement.\n\n" +
        "Worth separating from the ordering, since the two are easy to " +
        "conflate: the surreal order is intrinsic and would *not* by itself " +
        "trip §7c, but `SurrealField` is declared as " +
        "`Field K, LinearOrder K, IsStrictOrderedRing K` **plus a " +
        "distinguished ring embedding `ofReal : ℝ →+* K`**, so " +
        "$\\mathbb{R}$ is part of the ambient vocabulary of the whole " +
        "appendix rather than something this conjecture introduces. Per " +
        "AGENTS.md §7ab the surreal layer is Language-tier bookkeeping over " +
        "the archimedean statement, not a replacement for it — which is " +
        "exactly what the standard-part form records.",
      see: "content/quantum-observable-universe/lean/QOU/AppendixSurreals/Conjectures.lean",
    },
  ],
});
