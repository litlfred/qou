import { proof } from "../../schema/builders";

export default proof({
  label: "prf:reeb-beltrami-regular-flow",
  title: "Proof of the regular fibre-rotation flow on $\\mathrm{UT}(\\Sigma_4)$",
  uses: ["prop:reeb-beltrami-regular-flow"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Formal verification.** The Lie-algebra computations are proved in Lean, sorry-free, in `QOU/FluidDynamics/BeltramiSteadyEuler.lean`, namespace `QOU.FluidDynamics.BeltramiSteadyEuler`:\n\n- `sl2_brackets` and `L3.toMat_br` for the brackets, checked as $2 \\times 2$ matrix commutators;\n- `L3.nab_torsion_free` and `L3.nab_metric`, which identify the Koszul connection used with the Levi-Civita connection on left-invariant fields;\n- `L3.V_killing`, with the non-vacuity check `L3.X_not_killing`;\n- `L3.nab_VV`, `L3.curl_V`, `L3.curl_curl_V`, `L3.ric_V`, `L3.ric_X`, `L3.rough_V` and `L3.weitzenbock_V`;\n- `L3.deformation_V`, the identity $(\\Delta_H - 2\\,\\mathrm{Ric})\\,V = 0$.\n\nThe same file proves the flat analogue end to end with Mathlib derivatives: a Beltrami eigenfield yields an exact Navier--Stokes solution, and the ABC field gives the solution $e^{-\\nu t} u_{\\mathrm{ABC}}$ on the three-torus.\n\nTwo standard steps are not formalised: the descent of left-invariant data and the identification of the manifold operators on left-invariant fields." },
  ],
});
