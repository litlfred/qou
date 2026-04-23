import { definition } from "../../schema/builders";

export default definition({
  label: "def:quantum-temperature",
  title: "Quantum temperature",
  tags: [
    "temperature",
    "statistical-mechanics",
    "reeb-flow",
    "planck-time",
    "non-abelian-stokes",
    "surface-integral",
  ],
  lean: {
    decl: "QOU.Information.quantumTemperature",
    validation: "not_checked",
  },
  uses: [
    "def:planck-time",
    "def:quantum-planck-constant",
    "def:operational-entropy",
    "def:frobenius-pairing",
    "def:quantum-observable-universe",
    "def:yekutieli-triple",
    "def:q-energy",
    "rem:kashaev-volume-density",
  ],
});
