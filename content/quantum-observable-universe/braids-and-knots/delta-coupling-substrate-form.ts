import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:delta-coupling-substrate-form",
  lean: {
    ref: "qou:QOU.MagicShell.DeltaCouplingSubstrateForm",
    validation: "not_checked",
  },
  title: "Magic-shell stabilization energy: closed form from substrate primitives",
  tags: ["magic-shell", "binding-energy", "boltzmann", "thermodynamic", "delta-coupling"],
  uses: [
    "conj:magic-shell-stabilization",
    "prop:hecke-log-decomposition",
    "rem:beta-decay-energy-scale",
    "prop:boltzmann-constant",
  ],
});
