import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:confinement-sdp",
  title:
    "Confinement as semidefinite program with matrix Frobenius positivity",
  lean: { ref: "qou:QOU.ParticleInteractions.confinement_sdp",
    validation: "not_checked",
  },
  uses: ["prop:confinement-lp"],
  tags: [
    "semidefinite-programming",
    "confinement",
    "psd-cone",
    "matrix-frobenius",
    "cross-channel-coupling",
    "multi-operator-binding",
    "sdp-duality",
    "spectral-gap",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-24",
      body: "Formalisation audit (`qou-x60n`, `qou-z9ws`): `2026-08-30-context-classes-hand-adjudicated.lean` shows `HasBindingMultiplicity` (`ElectronShell.lean`) carries unconstrained data (`mu := fun _ => 2`), making `NobleGasMultiOperator` jointly vacuous.",
      see: "docs/audits/2026-08-30-context-classes-hand-adjudicated.lean",
    },
  ],
});
