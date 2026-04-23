import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:mass-volume-factorization",
  title:
    "Mass-volume factorization of the categorical mass endomorphism",
  tags: [
    "mass-endomorphism",
    "hyperbolic-volume",
    "density",
    "frobenius-packing",
    "jsj-decomposition",
    "categorical-action",
  ],
  lean: {
    decl: "QOU.ParticleInteractions.MassVolumeFactorization",
    validation: "not_checked",
  },
  uses: [
    "rem:kashaev-volume-density",
    "prop:thurston-volume-additivity",
    "prop:tower-binding-energy",
    "def:atomic-braid",
  ],
  cites: ["thurston1978", "murakami2001"],
});
