import { proposition } from "../../schema/builders";

/**
 * Schur–Weyl duality: eightfold-way multiplets as H₃(q) partners.
 *
 * The 10/8/1 dimensions (decuplet/octet/singlet) are the SU(N=3)
 * irrep dimensions that appear as Schur–Weyl partners of H₃(q)
 * in V^⊗3. The Hecke block dimensions (1,2,1) are the
 * multiplicities: 3³ = 10·1 + 8·2 + 1·1 = 27.
 *
 * CRITICAL: This derivation requires N=3 (why V is 3-dimensional).
 * In QOU's single-fibre tower, V is 2-dimensional (Descartes
 * condition χ = -6), so N=3 cannot come from one fibre. The N=3
 * must arise from a multi-fibre/groupoid structure — this is the
 * open problem (T3b).
 */
export default proposition({
  label: "prop:schur-weyl-eightfold",
  title: "Eightfold-way multiplets via quantum Schur--Weyl duality",
  // Immediate neighbours only. rem:hecke-algebra-from-braiding was also
  // listed here, but prop:a2-from-three-strands already uses it, so the
  // direct edge was transitively redundant (uses-editorial-hygiene warn).
  uses: [
    "prop:a2-from-three-strands",
  ],
  // Lean backs the OBSTRUCTION half of this block, not the affirmative half.
  // RowCapObstruction proves sorry-free that the alternating channel (1³)
  // vanishes iff N < 3, that the decuplet dimension forces N = 3, and the
  // channel arithmetic at N = 2 (8 = 4+4+0) and N = 3 (27 = 10+16+1).
  // What it does NOT formalise is quantum Schur-Weyl duality itself, nor any
  // construction supplying N = 3 -- that remains the chapter's principal open
  // problem (bean qou-8pl3).
  // The ref now names a DECLARATION, not the module. `weyl_dim_alt_eq_zero_iff`
  // is the row-cap obstruction the module is named for: the alternating
  // channel (1³) has dimension zero iff N < 3.
  lean: { ref: "qou:QOU.Eightfold.RowCapObstruction.weyl_dim_alt_eq_zero_iff" },
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **The obstruction, and what is machine-checked about it.**\nThe following are verified in\n`QOU/Eightfold/RowCapObstruction.lean`:\n\n- `weyl_dim_alt_eq_zero_iff` --- the alternating channel\n  $\\dim V_{(1^3)} = \\binom{N}{3}$ vanishes *if and only if* $N < 3$.\n  This is the obstruction in one line.\n- `decuplet_forces_three` --- if the symmetric channel has\n  dimension $10$ then $N = 3$.  The implication runs from the decuplet\n  dimension to the flavour dimension, in that direction.\n- `singlet_forces_three` --- a one-dimensional alternating\n  channel likewise pins $N = 3$.\n- `schur_weyl_cube_split_two_three` --- the channel\n  arithmetic closes at both values ($8 = 4 + 4 + 0$ at $N = 2$;\n  $27 = 10 + 16 + 1$ at $N = 3$), so the $N = 2$ deficit sits precisely in the\n  vanishing alternating channel and not in some unaccounted-for piece.\n\n**What that Lean does not establish.**\nThe same caveat applies here as to\n`WeylInvarianceQDeformation.lean` above, and it is load-bearing in this one\nplace because $N = 3$ is the chapter's central open problem.  What is\nmachine-checked is the *arithmetic* of the row cap on the channel\ndimensions: the file *defines* $\\dim V_{(1^3)}^{\\mathfrak{gl}_N}$ to be\n$\\binom{N}{3}$ and then reasons about $\\binom{N}{3}$, with every proof a\n`Nat.choose` identity, a `decide`, or an `omega`.  That the hook-content\nformula gives $\\dim V_{(1^3)} = \\binom{N}{3}$, and that the Schur--Weyl row\ncap is $\\ell(\\lambda) \\leq N$, are standard and cited --- carried by the\ndefinition names and docstrings, not proved.  The file's own docstring\nconcedes the boundary, noting that Worpitzky's identity is not formalised\nhere.  So the tier is *standard mathematics, with a\nmachine-checked arithmetic instance* --- not *proved* in the sense the other\nLean-backed rows of this chapter use.\n\n**The $N = 2$ half of the duality is machine-checked.**\n`QOU/SchurWeyl/JimboActionKernel.lean` builds the Jimbo action of $H_n(q)$ on\n$V^{\\otimes n}$ with $\\dim V = 2$ and proves over an ordered field\nat generic $q$: the induced trace is the Markov trace with\n$z = q^3/(q^2+1)$; the kernel of the action is\nexactly the trace radical, i.e. the blocks with three or more rows\n; and the image has dimension the Catalan\nnumber. Surjectivity onto the\n$\\mathcal{U}_q(\\mathfrak{sl}_2)$ commutant is not claimed, and no $N \\geq 3$\naction is formalised, so the $N = 3$ statement above remains cited.\n\n`decuplet_forces_three` and `singlet_forces_three` run from an\n*observed* channel dimension to $N = 3$; what the framework requires is\n$N = 3$ *supplied* by a construction.  That is the affirmative half, and it\nremains open.\n\nrepresentation-theoretic content is machine-checked in\n`QOU/Eightfold/Sym2GateFSTrichotomy.lean`: at dimension three,\n\nis the cited input, not a\nformalised one, so the octonionic route is *not excluded* rather than\n*machine-checked to pass*." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): ([Proposition](#prop:color-su3-from-g2))" },
  ],
});
