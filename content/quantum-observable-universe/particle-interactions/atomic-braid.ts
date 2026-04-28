import { definition } from "../../schema/builders";

/**
 * Atomic braid definition: electrons in the nuclear braid.
 */
export default definition({
  label: "def:atomic-braid",
  title: "Atomic braid $H_{A+Z}(q)$",
  lean: { ref: "qou:QOU.AtomicBraid.NeutralAtom",
    validation: "not_checked",
  },
  uses: ["def:transfer-matrix-operator", "def:derived-atom"],
});
