import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:electroweak-higgs-torus-link-triplet",
  title:
    "$(W^\\pm, Z, H) \\leftrightarrow (T(2,4), T(2,6), T(2,8))$ — non-Bring even-twist 2-component torus-link triplet",
  uses: [
    "prop:force-carrier-bring-uniqueness",
    "prop:torus-knot-genus-four-unique",
    "def:hecke-normal-form",
    "rem:hecke-algebra-from-braiding",
  ],
  computation: {
    engine: "python",
    script: "folio-assistant/computations/ew_higgs_sdp_probe.py",
    witness: "folio-assistant/computations/ew-higgs-sdp-probe.witness.json",
    status: "verified",
  },
  tags: [
    "electroweak",
    "higgs",
    "torus-link",
    "non-bring",
    "psd-feasibility",
    "weak-sector",
    "force-carrier",
    "open-problem",
  ],
});
