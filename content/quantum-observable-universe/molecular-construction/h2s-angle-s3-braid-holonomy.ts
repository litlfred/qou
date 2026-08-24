import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:h2s-angle-s3-braid-holonomy",
  title: "H₂S bond-angle residual $=$ chiral $S^3$ braid holonomy",
  lean: {
    ref: "qou:QOU.Molecular.H2SAngleS3HolonomyConjecture",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "failed",
    // STAYS "failed" — correct terminal state, like binding-qbeta-complex-volume
    // and for a related reason. Two of the three cited witnesses are green; the
    // third is red and should be.
    //
    // The red assertion offered a bracket as the parity evidence:
    // h·z³ (1.49°) < 2.1° < h·z² (2.99°). Those two numbers are CONVENTION C.
    // The producer has computed z in convention D since the 2026-08-09
    // excision, where the same expressions are 2.755° and 4.496° — and the
    // observed 2.1° is BELOW the whole window, not inside it. Measured:
    //
    //     C (excised):    1.491° < 2.1° < 2.986°   bracketed
    //     D (canonical):  2.755° < 2.1° < 4.496°   NOT bracketed
    //
    // Two separate defects, and only one is about arithmetic:
    //
    // 1. THE PREMISE FAILS UNDER D, which is the serious one. "h·z^k is odd in
    //    h" is a bar-PARITY statement, so it needs z bar-even — otherwise z
    //    contributes its own parity and the product has none. Exactly:
    //    z_C(1/q)/z_C(q) = 1 (bar-even), z_D(1/q)/z_D(q) = q⁻⁴ (not). Under the
    //    canonical convention h·z^k has no clean bar-parity at all, so the
    //    classification the identification rests on is UNAVAILABLE rather than
    //    merely unfavourable. The producer's own comment called z "the
    //    bar-symmetric Markov param" — a convention-C fact left attached to a
    //    convention-D value.
    //
    // 2. THE BRACKET WAS WEAK EVIDENCE EVEN UNDER C. [h·z³, h·z²] spans 1.495°
    //    about a 2.1° target — 71% of the value. Any residual in [1.49°, 2.99°]
    //    passes it. Per AGENTS.md §"Defined residual ≠ derived decomposition"
    //    item 2, a window that wide gets reported with its width, not presented
    //    as confirmation; "right parity, right scale" does no work if nearly
    //    any scale would have fit. The witness now records both widths.
    //
    // SCOPE. (b) structural, invariant cited: the bar-parity argument for h·z^k
    // does not exist under D, because z_D is exactly not bar-even. (a) scope-
    // limited: this bracket does not contain 2.1° under D. NEITHER excludes the
    // +2.1° being chiral by some other route, and neither touches the H₂O-clean
    // / H₂S-residual dichotomy itself, which is a structural reading. What is
    // retracted is the quantitative argument offered for it.
    //
    // Noted, not fixed: the producer binds via set_content_block to
    // prop:symmetric-block-domain-weight, a different block from the one citing
    // it here.,
    script:
      "computations/h2s_chirality_residue_s3_holonomy.py",
    witness: [
      "computations/h2s-chirality-residue-s3-holonomy.witness.json",
      "computations/h2s-chiral-residue-bar-antisymmetric.witness.json",
      "computations/h2s-bring-residual-mixing.witness.json",
    ],
  },
  uses: [
    "prop:symmetric-block-domain-weight",
    "prop:chirality-residue-mass-term",
    "def:bar-involution",
    "prop:bring-trefoil-cinquefoil-channel",
  ],
  tags: [
    "H2S",
    "bond-angle",
    "chirality",
    "S3-holonomy",
    "Chern-Simons",
    "bar-anti-symmetric",
    "q-Dirac-kernel",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "What is **established** (not conjectural):\n\n- The chiral channel is exactly the $c_\\lambda=0$ block $V_{(2,1)}$\n  ([`prop:chirality-residue-mass-term`](#prop:chirality-residue-mass-term):\n  $c_\\lambda(3)=+3$, $c_\\lambda(2,1)=0$, $c_\\lambda(1,1,1)=-3$).\n- The residue is the braid holonomy around the singular fibre — the q-deformed\n  Chern–Simons holonomy of a Wilson loop in $S^3$\n  ([`rem:residue-as-braid-holonomy`](#rem:residue-as-braid-holonomy)).\n- The split is the bar-involution ([`def:bar-involution`](#def:bar-involution)):\n  the clean second-row angles are the bar-symmetric backbone, the H$_2$S residual\n  the bar-anti-symmetric ($P_{\\mathrm{skew}}$) part. **Parity is established**:\n  the residual is odd in $h$ (scale $h z^2 \\approx 3^\\circ$, $h z^3 \\approx\n  1.5^\\circ$, observed $2.1^\\circ$ between).\n\nThe **conjectural content** is the identification itself — that the\nmolecular-angle opening $\\Delta\\theta_{\\mathrm{H_2S}}$ *is* this S$^3$ holonomy\nphase, and that the monodromy/Reshetikhin–Turaev evaluation at $\\zeta_\\ell$\nreturns the observed $\\approx 2.1^\\circ$.\n\n> **Caveat (the exact form is open).** Three a-priori distinct involutions are\n> in play and must not be conflated: the **palindromic reversal** (which fixes\n> the orbital $\\ell = \\tfrac12$ defect, so $s$ self-dual / $p$ chiral), the\n> **bar-involution** $\\sigma_i \\mapsto \\sigma_i^{-1}$ (the $P_{\\mathrm{avg}}$ /\n> $P_{\\mathrm{skew}}$ even–odd split), and the **longest-element** $w \\mapsto\n> w_0 w$ (the self-duality of `palindromicity-orbital-type`). The naive\n> $P_{\\mathrm{skew}}$ of the length-3 chiral word on $V_{(2,1)}$ in fact\n> *vanishes*, so $\\Delta\\theta$ is **not** the leading bar-skew matrix part;\n> the parity argument ($\\Delta\\theta$ odd in $h$, bracketed by $hz^2/hz^3$) is\n> observational. Pinning the exact form requires the monodromy phase at\n> $\\zeta_\\ell$ with the correct involution — this is the open content.",
    },
  ],
});
