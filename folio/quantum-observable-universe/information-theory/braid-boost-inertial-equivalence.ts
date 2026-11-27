import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:braid-boost-inertial-equivalence",
  title: "Braid-boost inertial equivalence",
  tags: ["mass-energy", "legendre-transform", "inertial-mass", "conditional-class"],
  lean: {
    ref: "qou:QOU.Core.CategoricalHamiltonianLegendre.BraidBoostInertialEquivalence",
    validation: "not_checked",
  },
  uses: ["def:categorical-hamiltonian", "def:mass-identity", "def:information-speed-of-light", "def:categorical-dirac-operator", "def:contact-affine-chart"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body:
        "Filed as a conjecture by owner ruling (2026-11-25): `prop:mass-energy` is contingent on it. " +
        "The Lean class takes the inertial mass as a free function, so it constrains nothing until the inertial mass " +
        "has a definition independent of $\\mathfrak{m}$ (bean `qou-2k68`). Route 1, inertial mass = the Reeb-clock kinetic " +
        "coefficient $2\\hbar_q^2\\,\\tau(\\iota_\\xi\\nabla^2)$, is excluded: exact test in $H_2(q)$, $H_3(q)$ on nine braids " +
        "(`computations/probes/braid_boost_inertial_clock/`). Route 2 (owner, 2026-11-25: use the affine causality cone): the boosts and the worldline form are derived from the cone (`QOU.Core.AffineCausalityCone`, `worldlineLagrangian_eq_sqrt_coneForm`); the identification of the boost coefficient $m$ with $\\mathfrak{m}(\\beta)$ is open. Covariance of a traced Dirac square is rigid in $q$ (`QOU.Core.BoostCovarianceRigidity`): a $q$-independent datum, such as the substrate Dirac operator, can satisfy it at only one $q$, so a proof needs a braid-attached Dirac datum with $A/C = -1/(q-1)^2$ for every $q$.",
    },
  ],
});
