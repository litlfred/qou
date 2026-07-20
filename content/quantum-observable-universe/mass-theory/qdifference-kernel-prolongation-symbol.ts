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
