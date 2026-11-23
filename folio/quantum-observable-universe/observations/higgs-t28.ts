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
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The identity is proved in [`QOU/StandardModel/ElectroweakBringSchwingerBridge.lean`](../lean/QOU/StandardModel/ElectroweakBringSchwingerBridge.lean). The 1-loop factor comparison: see [`electroweak_bring_schwinger_bridge_probe.py`](../../../computations/probes/electroweak_bring_schwinger_bridge_probe.py)." },
  ],
});
