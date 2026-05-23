import { definition } from "../../schema/builders";

export default definition({
  label: "def:unit-particle-state",
  title: "The unit particle state $\\mathrm{Li}_q(z)$",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.UnitParticleState",
    validation: "not_checked",
  },
  uses: ["def:local-cohomology-group"],
  tags: ["unit-particle", "q-polylogarithm", "generator", "local-cohomology"],
});
