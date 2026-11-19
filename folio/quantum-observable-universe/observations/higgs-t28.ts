import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:higgs-t28",
  title:
    "The Higgs boson as $T(2,8)$: the link spanning three exceptional divisors",
  lean: {
    ref: "qou:QOU.HiggsT28.HiggsAsT28",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:fermion-boson-knot-link",
  ],
  authorNotes: [
    {
      kind: "note",
      body: "The 2-strand Plancherel trace identity and W/Z-anchor reconciliation (higgs_W_Z_anchor_reconciliation) are formalized in QOU/StandardModel/ElectroweakBringSchwingerBridge.lean; numerical 1-loop comparisons are evaluated in computations/probes/electroweak_bring_schwinger_bridge_probe.py.",
    },
  ],
  tags: [
    "tier:E",
    "higgs",
    "boson",
    "torus-link",
    "exceptional-divisor",
    "mass-mechanism",
    "scalar",
    "genus-3",
  ],
});
