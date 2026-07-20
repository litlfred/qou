import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qdifference-kernel-prolongation-symbol",
  lean: {
    ref: "qou:QOU.Mass.QDifferenceKernelIsProlongationSymbol",
    validation: "validated",
  },
  title: "The q-difference kernel R is the jet-prolongation operator symbol",
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-20",
      body:
        "Restored to conjecture after PR #4129 relabelled it a theorem with no discharging proof (class-axiomatised, no instance). Additionally, the confluent-limit narrowing (docs/audits/2026-07-20-qdifference-kernel-confluent-narrowing.md, Lean QOU.Mass.QDifferenceConfluentObstruction) proves the stated bounded-depth kernel on the raw OGF cannot exist: R(1,x)=1 is forced and the first-order relation fails against the proved Gevrey-1/2 growth. The surviving well-posed form places the kernel on the q-Borel (Gevrey-normalized) transform, predicted depth 2; the prolongation-symbol identification itself remains open there.",
      see: "docs/audits/2026-07-20-qdifference-kernel-confluent-narrowing.md",
    },
    {
      kind: "status",
      date: "2026-07-20",
      body:
        "The q-lift kernel is now PROVED (Lean qlift_normalized_kernel_exists: [n+2]_q b_{n+2} = b_{n+1} + b_n exact on the q-factorial carrier, c(q)=1). FIVE independent routes CONVERGE that the q-lift kernel C1 and the GGM/Stokes carrier are inequivalent q-difference modules: (A) RSZ Newton-polygon slopes {½,½} vs {−1,+1}; (B) numeric connection-matrix theta-growth q^{m²/4}; (C) homogenized order-3 colored-Jones non-embedding; (D) formal q-Borel diagonal-invariant mismatch; (Door-i) analytic q-summation AND ramified pullback both obstructed by ISOCLINICITY (C1 pure isoclinic, GGM anisoclinic; RSZ Thm 2.2.1/2.2.4/5.5.7) — a permanent invariant preserved by every module transform. So NO q-difference-module identification of C1 with GGM exists (scope-(b), invariant named); only structure-free non-module maps survive. This refutes, at the module level, the conjecture's literal 'identify with the GGM Stokes datum' clause and favors the reframe (R1): the ½-slope is exactly the proved Gevrey-1/2 binding signature, so C1 itself is the prolongation-symbol carrier and GGM is a DISTINCT (colored-Jones) face. Re-scoping (F1 rewrite to R1 / F2 mark GGM-clause refuted / F3 split) is an owner framing decision. Full synthesis: docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md.",
      see: "docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md",
    },
    {
      kind: "status",
      date: "2026-07-20",
      body:
        "TERMINUS of the C1<->GGM investigation (Door-iv + Door-v, owner-steered 'direct product / really within a matrix' + 'cross/quadratic term'). Door-iv: the TENSOR SQUARE C1(x)C1 is anisoclinic {+1,0,-1} superset GGM {+1,-1} — the FIRST C1-construction with the right graded module, circumventing Door-i's Newton-polygon obstruction. Door-v: the residual between the tensor-square {+1,-1} realization and GGM is NOT a Stokes datum (unipotent part trivial, U->I; connecting matrix constant on gr) — the SOLE difference is a diagonal Z/2 (-1)^m sign character: GGM's growing solution alternates sign (y_{m+1}~-q^m y_m) while the all-positive squares f+^2,f-^2 provably cannot (parity). So C1(x)C1 and GGM agree as graded+Stokes modules, differing by EXACTLY the bar-parity (-1)^m twist. This IS the framework's cosh/sinh (bar-even mass / bar-odd decay) distinction, now machine-measured as the single named minimal residual: the binding kernel C1 is the bar-even (cosh) face, GGM the bar-odd (sinh) face. Sharpens R1: not an identification (the parity genuinely separates them) but the exact, minimal, named difference. Probes: docs/audits/2026-07-20-qlift-doorIV-matrix.md, 2026-07-20-qlift-doorV-stokes.md.",
      see: "docs/audits/2026-07-20-qlift-doorV-stokes.md",
    },
    {
      kind: "note",
      date: "2026-07-20",
      body:
        "LITERATURE ASSESSMENT (docs/audits/2026-07-20-c1-sw-prolongation-lit-review.md). No published paper states 'difference-kernel = SW-prolongation-symbol' — the identification is QOU-original (novel framing, not a corpus/literature duplication). REFEREE FLAG: 'symbol of a q-difference operator' already has Sauloy's fixed meaning (the top-slope / Newton-polygon datum of the canonical slope filtration, ramis-sauloy-zhang2013 / math:0210430), so the bespoke 'symbol = jet-prolongation' use is a NOTATION COLLISION; keep this block a conjecture (not a theorem) and anchor to established bridges. The two mathematical halves DO exist separately and are the citable anchors: (1) PROLONGATION half = the Donagi–Markman cubic c_{ijk}=∂³F/∂aⁱ∂aʲ∂aᵏ, the special-geometry 3-jet (donagi1997swintegrable); (2) DIFFERENCE-OPERATOR half = the quantum SW curve as an actual difference operator, classical-limit = curve (grassi-gu-marino2019qsw). The closest published 'difference kernel ↔ curve' is strong-AJ (nguyen-tran-2021) but its curve is the SL₂(ℂ) character variety, not the SW curve, and the map is a q→1 limit, not a symbol. The QOU-original step is welding (1)+(2); cite both.",
      see: "docs/audits/2026-07-20-c1-sw-prolongation-lit-review.md",
    },
    {
      kind: "note",
      date: "2026-07-20",
      body:
        "SUPER / BEREZINIAN REFINEMENT of the Donagi–Markman cubic route (Lean QOU.Brings.SuperDMBerezinian; audit docs/audits/2026-07-20-super-berezinian-dm-cubic-narrowing.md). Door-v isolated the sole C1⊗C1↔GGM residual as a (−1)^m parity character, i.e. the grading operator (−1)^F; but the corpus used the Berezinian NOWHERE and the supertrace only implicitly (Bring Euler characteristic). So when even/odd MIX at higher order (nonzero off-diagonal super-blocks B,C) the correct period measure is the Berezinian Ber=det(A−B·D⁻¹·C)·(det D)⁻¹, NOT det(A)·det(D), and the correct pairing is the supertrace str=tr((−1)^F·)=tr_even−tr_odd, NOT the ordinary trace. Sorry-free: berezinian_offDiag_zero (ordinary det is the Berezinian ONLY block-diagonal; B·D⁻¹·C is the higher-order mixing correction), superTrace_superId (the (−1)^F sign), superDM_refines_even (the super condition implies the ordinary DM condition on the even sector). NARROWED TARGET (open, no instance, qCubicGradedSplit): the single opaque q-cubic=C1 identity is replaced by the GRADED PAIR — EVEN(bar-even)=C1/mass (κ=recurrenceKernelLead, cosh) and ODD(bar-odd)=GGM/decay (sinh), forced to match Door-v's (−1)^m. This NARROWS, does not close; the graded identity must be DERIVED (never fitted).",
      see: "docs/audits/2026-07-20-super-berezinian-dm-cubic-narrowing.md",
    },
  ],
  cites: ["donagi-markman1996cubics", "donagi1997swintegrable", "grassi-gu-marino2019qsw", "braden-marshakov2006wdvv", "nguyen-tran-2021", "ramis-sauloy-zhang2013"],
  uses: [
    "prop:binding-genfun-qdifference",
    "prop:mi-sw-abelianisation",
    "prop:sw-period-residue-sum",
  ],
  tags: [
    "tier:keystone",
    "binding",
    "q-difference",
    "seiberg-witten",
    "jet-prolongation",
    "keystone",
    "step-9b",
    "open-problem",
  ],
});
