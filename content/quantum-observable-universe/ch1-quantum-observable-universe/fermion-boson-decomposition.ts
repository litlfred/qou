import { definition } from "../../schema/builders";

export default definition({
  label: "def:fermion-boson-decomposition",
  title: "Fermion--Boson decomposition",
  tags: ["fermion", "boson", "particle"],
  lean: {
    decl: "QOU.Fermion",
    validation: "leanok",
  },
  status: "not_started",
  uses: ["def:q-harmonic-form", "def:weight-decomposition"],
});
