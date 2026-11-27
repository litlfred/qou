import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:substrate-period-mass-resolvent",
  renamedFrom: ["alg:mass-identity"],
  title:
    "Archimedean Aether Period, Borromean Ratio, and Inhomogeneous Lepton-Resolvent Evaluation ($\\mathcal{L}_1$)",
  uses: [
    "def:mass-identity",
    "prop:mass-identity-unique",
    "thm:knot-mass-formula-unified",
    "def:three-calibration-discipline",
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "martelli2016",
    "codata2022",
  ],
  lean: {
    ref: "qou:QOU.Observations.InhomogeneousLeptonLoopResolvent.tauFigureEight_closed_form",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script:
      "computations/probes/w6_inhomogeneous_lepton_resolvent/w6_inhomogeneous_lepton_resolvent_probe.py",
    witness: [
      "computations/probes/w6_inhomogeneous_lepton_resolvent/w6-inhomogeneous-lepton-resolvent.witness.json",
      "computations/probes/w10_continuum_ecat_intranuc_em/w10-continuum-ecat-intranuc-em.witness.json",
      "computations/per-observable-100x-status.witness.json",
    ],
    status: "verified",
  },
  tags: [
    "mba",
    "substrate-period",
    "borromean-ratio",
    "lepton-resolvent",
    "calibration-discipline",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-24",
      body:
        "Renamed from `alg:mass-identity` (`mba-step09a-mass-identity`) under `qou-mba8` + `qou-nmjd` to eliminate the naming collision with Ch. 9 `def:mass-identity`, remove internal `CAL-1/2/3` codes and fit-tier `R_s5bb` from the title/algorithm, explicitly mark `/q^3` in `F_Bor` as an asserted model normalization (`#8964`), and wire `InhomogeneousLeptonLoopResolvent` (`#9216`) + intranucleon EM (`#9219`).",
    },
  ],
});
