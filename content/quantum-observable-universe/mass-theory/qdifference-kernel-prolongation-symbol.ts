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
        "The q-lift kernel is now PROVED (Lean qlift_normalized_kernel_exists: [n+2]_q b_{n+2} = b_{n+1} + b_n exact on the q-factorial carrier, c(q)=1). Four independent routes (RSZ Newton-polygon slopes {½,½} vs GGM {−1,+1}; numeric connection-matrix theta-growth q^{m²/4}; formal q-Borel diagonal-invariant mismatch; homogenized order-3 colored-Jones non-embedding) CONVERGE: the q-lift kernel and the GGM/Stokes carrier are inequivalent q-difference modules under every meromorphic gauge and every formal q-Borel weight — a scope-(b) distinction with the invariant named (slopes, RSZ Thm 2.2.1/2.2.4). So the conjecture's ALGEBRAIC-gauge identification is excluded; any identification is necessarily an analytic/ramified summation functor (Door-i, in progress). Note the reframe (Door-ii): the ½-slope is exactly the proved Gevrey-1/2 binding signature, so a live reading is that the q-lift kernel IS the prolongation-symbol carrier and GGM is a distinct (colored-Jones) face. Full synthesis: docs/audits/2026-07-20-qlift-gauge-gap-synthesis.md.",
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
