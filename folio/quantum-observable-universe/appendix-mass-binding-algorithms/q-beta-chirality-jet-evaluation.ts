import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:q-beta-chirality-jet-evaluation",
  renamedFrom: [
    "alg:jet-prefix-transport",
    "alg:q-beta-truncation",
    "alg:ck-truncation-ladder",
  ],
  title:
    "Two-Term Lagrangian Chirality Trace and Tiered $\\mathfrak{Q}_\\beta$ Jet Evaluation ($\\mathcal{L}_1\\text{--}\\mathcal{L}_2$)",
  uses: [
    "prop:q-beta-categorical-precision-ladder",
    "conj:jet-prefix-gb-filtration",
    "def:three-calibration-discipline",
  ],
  cites: [
    "codata2022",
    "ame2020",
  ],
  lean: {
    ref: "qou:QOU.QBeta.decayLadder_zC_threeRow_ne_zero",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/qbeta_chirality_and_compton_polarizability/qbeta_chirality_and_compton_probe.py",
    witness: [
      "computations/probes/qbeta_chirality_and_compton_polarizability/qbeta-chirality-and-compton.witness.json",
      "computations/q-beta-predicted.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "mba",
    "q-beta",
    "chirality",
    "jet-truncation",
    "precision-ladder",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Consolidates `mba-step08-jet-prefix`, `mba-step11-q-beta-truncation`, and `mba-sidecar-ck-truncation-ladder` under `qou-mba8` + `qou-nmjd`, removing internal `CAL-1/2/3` and `Convention C/D` prose labels per owner `one-voice` ruling while preserving `QOU.QBeta.decayLadder_zC_threeRow_ne_zero` in `lean.ref` and the strict `c_k` epistemic tiering.",
    },
  ],
});
