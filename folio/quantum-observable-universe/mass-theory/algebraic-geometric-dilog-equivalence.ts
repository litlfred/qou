import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:algebraic-geometric-dilog-equivalence",
  title:
    "Algebraic-geometric dilogarithm equivalence: $\\Phi_n(x; q)$ poles map to ideal-tetrahedron cusps",
  lean: {
    ref: "qou:QOU.QPochhammer.algebraic_geometric_equivalence",
    validation: "not_checked",
  },
  uses: [
    "conj:dilogarithm-archimedean-limit",
    "conj:binding-qbeta-complex-volume",
    "prop:phi-b-unitary-bar-odd",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
    "neumann-zagier1985",
    "thurston1978",
    "zagier1986",
  ],
  tags: [
    "q-pochhammer",
    "dilogarithm",
    "bloch-wigner",
    "kashaev",
    "phi-q",
    "algebraic-geometric",
    "open-problem",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-21",
      body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner: fix issues): Three in-body citations of the later conjecture were replaced by a reference to the new opening conditional banner (the block already states it \"is stated conditionally on its open inputs\", one of which this conjecture supplies). Verbatim: note on n, \"the carrier of the bijection\\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy),\\ntable row 4)\"; dictionary, \"The bijection between the rows is the content of\\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).\"; conjectural standing, \"the matched-cusp volume identification supplied by\\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)).\". The banner title previously read \"**Conjecture (Algebraic-geometric dilogarithm equivalence).**\".",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): The sibling\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy))\nimposes the same requirement on its own shape assignment." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Those\ndistances ($0.40$ to $0.91$) are what bound the conjecture's canonical form, as\n[shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)\n§*Empirical scope* records." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean formalization follows the hypothesis-carrying conditional-class\npattern: the class `QOU.QPochhammer.AlgebraicGeometricEquivalence` carries\nthe open inputs — the matched shape parameter $z(x)$, the volume-conjecture\nsaddle asymptotic (a theorem for $4_1$ by Ohtsuki / Andersen–Hansen), and the\nmatched-cusp volume identification supplied by\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy)) —\nand the statement bundle `QOU.QPochhammer.algebraic_geometric_equivalence`\n*derives* both halves: item 1 (pole side) unconditionally, as the\ntheorem `denomPolyLocal_roots_explicit` (each $x = q^{-k}$ is a genuine root of\n$(x;q)_n$), and item 2 (Bloch–Wigner asymptotic) from the class fields.\nThe class asserts nothing provable-outright; no instance is fabricated. This\nmatches the conjectural-class pattern used for\n[Φ$_q$-tower JSJ bridge](#rem:phi-q-tower-jsj-bridge).\n\n**The shape parameter is a field, on the upper half plane.** Item 2 above\nstates the asymptotic at $D(z(x))$, with $z(x)$ the shape of the ideal\ntetrahedron; an earlier Lean revision typed the Bloch–Wigner function\n$D \\colon \\mathbb{R} \\to \\mathbb{R}$ and applied it to the state variable $x$\nitself, on the grounds that the matching map had been composed away. That\ndiverged from the statement above, and it was not a harmless simplification:\n$D$ is conjugation-antisymmetric, $D(\\bar z) = -D(z)$, so $D$ vanishes\nidentically on the reals and every volume the class could name was forced to\nzero — a *flat* tetrahedron, which is the negation of the conjecture rather\nthan a weak form of it. The map is now un-composed: `shape` is a class field\ntyped `UpperHalfPlane`, so a degenerate shape is not expressible, and $x$\nkeeps its own role as the $q$-Pochhammer state variable. The sibling\n([shared-denominator cusp holonomy](#conj:shared-denominator-cusp-holonomy))\nhad already made the same repair on its own shape assignment.\n\nThe Lean carrier is the hypothesis class\n`QOU.QBeta.PhiBSArgumentIdentification.SArgumentIdentification`,\nparametrized by the argument map itself: a bare existence claim\n($\\forall q_0\\, \\exists z$) would be near-vacuous by pointwise choice\nagainst the unbounded continuous phase, so the class carries the\nstructural map as a parameter and no instance is fabricated. Two\nconsequences are derived unconditionally from the class:\n\n$\\Phi_b$ readout is $1$ (Lean: `exists_zero_crossing`,\n   `exists_pure_bar_even`, which take the flip as an explicit hypothesis).\n\ntheorem: the near-$0$ piece (`integrableOn_kernel_Ioc_zero_one` — the\n$-2z/t^2$ subtraction cancels the pole, ...\n\n[1, \\infty)$) are discharged from Mathlib, not carried. The\n**definition-to-contour identity** — that the real-integral `phiB`\nequals the Faddeev contour integral — remains a numerical pin\n($8 \\times 10^{-29}$ against the validated contour evaluator) and is\nassumed nowhere in the Lean; its honest carrier is\n`QOU.MathlibExt.PhiBFibreExtension` (the constructed `phiB` extends to a\nfull Faddeev $\\Phi_b$; no instance).\n\nidentity; no statement here or in the Lean carriers above\nassumes it. The channel is carried explicitly as the class\n`SDeformedVolumeChannel` ($u(q_0)$ map + deformed volume + the identity\n$S = \\mathrm{Im}\\,\\mathfrak{V}(u(q_0))$), and the composition with the\nargument-identification map is derived, not assumed: `phase_eq_im_deformed_volume`,\n`phiB_eq_cs_phase`, and `exists_cs_vanishing` (the sign flip of $S$\nforces a substrate point with vanishing deformed Chern–Simons part)." },
  ],
});
