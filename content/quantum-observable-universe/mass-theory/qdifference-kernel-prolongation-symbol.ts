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
  ],
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
