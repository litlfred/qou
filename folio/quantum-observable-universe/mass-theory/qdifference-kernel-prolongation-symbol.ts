import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:qdifference-kernel-prolongation-symbol",
  lean: {
    ref: "qou:QOU.Mass.QDifferenceKernelIsProlongationSymbol",
    validation: "validated",
  },
  title:
    "The q-difference kernel R is the jet-prolongation symbol, carried by the binding q-lift module",
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
      kind: "status",
      date: "2026-08-08",
      body:
        "**F2 recorded: the GGM-identification clause is REFUTED at module " +
        "level** (bean qou-kyst; owner said proceed on the F1/F2/F3 re-scoping). " +
        "Of the three options left open on 2026-07-20 — F1 rewrite the whole " +
        "conjecture to R1, F2 mark the GGM clause refuted, F3 split the block — " +
        "F2 is the one already carried by evidence in this corpus, so it is the " +
        "one taken; F1 and F3 remain available and are NOT foreclosed by this " +
        "note. The refutation is now machine-checked rather than asserted: " +
        "`QOU.Mass.ThetaSlopeArithmetic.newtonSlopes_c1_ne_ggm` derives the two " +
        "Newton-polygon slope multisets from the operators' coefficient " +
        "valuations — C1 `{1/2,1/2}` pure isoclinic, GGM eq-49 `{-1,+1}` — and " +
        "proves they differ, so `pullback_cannot_reach_ggm` no longer rests on " +
        "hand-entered constants. By RSZ Thm 2.2.1(i) the polygon is a module " +
        "invariant and by Thm 2.2.4 the slope multiset is preserved by every " +
        "gauge, so NO q-difference-module identification of C1 with GGM exists. " +
        "The conjecture's surviving content is the reframe (R1): C1 itself is " +
        "the prolongation-symbol carrier and GGM is a distinct colored-Jones " +
        "face, differing by exactly the bar-parity (-1)^m twist (Door-iv/v). " +
        "That surviving clause is what the class " +
        "`QDifferenceKernelIsProlongationSymbol` should be instantiated " +
        "against; it still has no instance, which remains the honest open " +
        "state. What is NOT settled by this note and needs the owner: whether " +
        "the block's title and statement should be rewritten to R1 (F1) or the " +
        "block split (F3). Recorded so the refuted clause is not re-litigated " +
        "and not silently carried as open.",
      see: "docs/audits/2026-07-20-qlift-routeA-rsz-invariants.md",
    },
    {
      kind: "status",
      date: "2026-08-08",
      body:
        "**F3 taken (owner-confirmed): this block is now the R1 half of a " +
        "split.** The statement's `equivalently, the monodromy/Stokes data of " +
        "the prolonged SW connection` clause has been REMOVED — that is the " +
        "clause `newtonSlopes_c1_ne_ggm` refutes at module level, and keeping " +
        "it as an equivalence asserted something the corpus has disproved. What " +
        "remains is the well-posed R1 claim: R is the jet-prolongation symbol " +
        "and its carrier is the pure-isoclinic slope-1/2 module C1 " +
        "(`qlift_normalized_kernel_exists`). Consequences (1) and (2) and the " +
        "keystone role are untouched — neither ever used the GGM clause, and " +
        "`conj:schwinger-measure-computational-time`, the only block that " +
        "`uses[]` this one, depends on the prolongation-symbol claim alone. The " +
        "label is unchanged so no dependency edge moves.\n\n" +
        "The C1<->GGM relationship is NOT dropped: it moves to " +
        "`conj:c1-ggm-bar-parity-faces`, where the Door-iv/v terminus can be " +
        "stated as its own falsifiable claim (C1(x)C1 and GGM agree as graded + " +
        "Stokes modules, differing by exactly the diagonal Z/2 (-1)^m " +
        "bar-parity character) instead of surviving as prose. F1 would have " +
        "demoted that measured residual to a remark; F3 keeps it as content. " +
        "Still open and unchanged: the class " +
        "`QDifferenceKernelIsProlongationSymbol` has no instance.",
      see: "docs/audits/2026-07-20-qlift-doorV-stokes.md",
    },
  ],
  cites: ["pugliese2023", "garoufalidis-wheeler-modular"],
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
