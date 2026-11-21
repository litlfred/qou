import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:qstar-decay-sector-q0",
  title:
    "The $S = 0$ point $q^{*}$ is conditional on $c_3^{\\mathrm{even}} = -\\mathrm{Vol}(4_1)$, not an independent determination of $q_0$",
  uses: ["conj:im-q-physical-role", "rem:c3-s-imq-decay-projection"],
  tags: [
    "im-q",
    "decay-width",
    "q-beta",
    "c3-bar-odd",
    "substrate-anchor",
    "mu-p-tension",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The computation is recorded in [`qbeta_c3_imq_qstar_ladder_amplification_probe.py`](../../../computations/qbeta/qbeta_c3_imq_qstar_ladder_amplification_probe.py) (witness [`qbeta-c3-imq-qstar-ladder-amplification.witness.json`](../../../computations/qbeta/qbeta-c3-imq-qstar-ladder-amplification.witness.json))." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): The Lean is likewise untouched: `qstarRootStrictMonoInAnchor` and `qstarRootUniqueInAnchor` are stated about an abstract $\\Phi$ with a `StrictMonoOn` hypothesis and never mention $z$ or $\\alpha$" },
    {
      kind: "refined-framing",
      body: "An earlier version of this remark claimed q* was an independent third determination of q₀.",
    },
  ],
});
