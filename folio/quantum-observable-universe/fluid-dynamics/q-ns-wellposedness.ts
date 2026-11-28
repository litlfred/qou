import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-ns-wellposedness",
  lean: { ref: "qou:QOU.FluidDynamics.q_ns_wellposedness", validation: "not_checked" },
  title: "Global regularity of the $q$-deformed Navier--Stokes equation",
  uses: [
    "prop:kelvin-dispersion-derivation",
    // Introduced in the setup and carried into the statement: the modal
    // balance clause is stated over the Delta_q eigencomponents.
    "rem:q-laplacian-interpretation",
  ],
  tags: [
    "navier-stokes",
    "well-posedness",
    "regularity",
    "q-deformation",
    "global-existence",
    "categorical",
  ],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-27",
      body: "Owner ruling (Carl, card \"Weaken decay clause, keep Part A\"): property 3 used to assert per-mode decay $|\\hat v_k(t)| \\le |\\hat v_k(0)|e^{-\\nu_q[k]_q^2 t}$ for every solution. That is the modal law of the linear Stokes equation and forbids the triad transfer of the nonlinear flow. It now states the modal balance with a transfer term; per-mode decay holds for transfer-free flows only (`q_ns_spectral_decay_of_no_transfer`).",
      see: "docs/audits/2026-11-27-qns-part-a-enstrophy-order-parameter.md",
    },
  ],
});
