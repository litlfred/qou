import { definition } from "../../schema/builders";

export default definition({
  label: "def:neutrino-knot",
  title: "Neutrino",
  tags: ["neutrino", "unknot", "lepton", "fermion", "vacuum-drag"],
  lean: { ref: "qou:QOU.Archimedean.Neutrino",
    validation: "not_checked",
  },
  uses: ["prop:torus-knot-generators"],
});
