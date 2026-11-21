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
    "omega-grade",
    "asymptotics",
  ],
  uses: [
    "rem:kashaev-volume-density",
    "conj:kashaev-volume-conjecture",
    "def:surreal-blowup-calculus",
    "def:ecalle-borel-resummation",
    "prop:one-loop-prefactor-provenance",
  ],
  computation: {
    engine: "python",
    script: "computations/qbeta/kashaev_remainder_omega_grade_probe.py",
    witness: [
      "computations/qbeta/kashaev-remainder-omega-grade.witness.json",
    ],
    status: "verified",
  },
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
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): \"provenance and the Lean axiomatisation live in that block\"; \"Lean `c_pow_four_eq_third`\"; step 5: \"Use `QOU.AppendixSurreals.gonshorIn` and `omegaSurreal` to express the surreal evaluations.\"; **Required infrastructure**:\n- Coloured Jones polynomial in Lean (does not exist in mathlib).\n- Berarducci–Mantova exponential/logarithm on $\\mathbf{No}$\n (partial in mathlib).\n- Hyperbolic-volume formalisation (does not exist in mathlib). ; \"provable in Lean (transfer principle)\"." },
    {
      kind: "note",
      date: "2026-09-13",
      body:
        "**The \u03c9-grade section's input is the corpus, not a citation.** " +
        "The probe backing that section " +
        "(`kashaev_remainder_omega_grade_probe.py`, merged as " +
        "`f6f17fa092`) and its witness `description` both attribute the " +
        "sub-leading asymptotic " +
        "$\\langle 4_1\\rangle_N = (N^{3/2}/3^{1/4})e^{NV/2\\pi}(1+O(1/N))$ " +
        "to *\"the cited Ohtsuki / Andersen\u2013Hansen expansion\"*, and " +
        "state that it is not re-derived here. That framing is weaker than " +
        "the truth and was written without checking: " +
        "[`prop:one-loop-prefactor-provenance`](../mass-theory/one-loop-prefactor-provenance.md) " +
        "**derives** both $3^{-1/4}$ and the power $3/2$ from the " +
        "one-variable saddle at $\\theta^\\ast = 5\\pi/6$ " +
        "(Lean `c_pow_four_eq_third`), and records that the $4_1$ " +
        "calibration the $c_\\sigma$ arc once rested on is thereby retired. " +
        "The `.md` section here is written against that proposition. Two " +
        "things do NOT change: the $O(1/N^2)$ tail is **measured** (check 1 " +
        "of the probe), not derived \u2014 the proposition states a leading " +
        "asymptotic and leaves the step from its two machine-checked " +
        "analytic inputs to the saddle hypotheses assumed; and the scope " +
        "stays (a), an asymptotic statement about $4_1$ alone.",
      see: "folio/quantum-observable-universe/mass-theory/one-loop-prefactor-provenance.md",
    },
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
      see: "folio/quantum-observable-universe/lean/QOU/AppendixSurreals/Conjectures.lean",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): (see\n [analytic obstructions](#rem:analytic-obstructions))" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Read\n   through [$\\mathrm{st}$ as median resummation](#rem:st-is-median-resummation),\n   the cocycle supplies precisely the real-single-valued function\n   whose surreal evaluation $\\mathrm{st}$ selects: the\n   quantum-modular functional equation is the inequality-free form of\n   the asymptotic statement." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ; it\nis unrelated to the alien derivative $\\Delta_\\omega$ of\n[Écalle--Borel resummation](#def:ecalle-borel-resummation) and to the\nper-partition binding weight $\\Delta_\\lambda$, both of which carry the\ncapital" },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): — see [algebraic core survives](#rem:algebraic-core-survives)" },
  ],
});
