import { proof } from "../../schema/builders";

export default proof({
  label: "prf:reeb-beltrami-regular-flow",
  title: "Proof of the regular fibre-rotation flow on $\\mathrm{UT}(\\Sigma_4)$",
  uses: ["prop:reeb-beltrami-regular-flow"],
  authorNotes: [
    {
      kind: "status",
      body: "Lie-algebra computations proved in `QOU/FluidDynamics/BeltramiSteadyEuler.lean` (`QOU.FluidDynamics.BeltramiSteadyEuler`: `sl2_brackets`, `L3.toMat_br`, `L3.nab_torsion_free`, `L3.nab_metric`, `L3.V_killing`, `L3.X_not_killing`, `L3.nab_VV`, `L3.curl_V`, `L3.curl_curl_V`, `L3.ric_V`, `L3.ric_X`, `L3.rough_V`, `L3.weitzenbock_V`, `L3.deformation_V`), along with the flat Mathlib-derivative analogues `beltrami_eigen_ns` and `abc_ns_exact`. Standard left-invariant descent from PSL_2(R) to Gamma\\PSL_2(R) and the scalar ODE reduction in item 3 are analytical.",
    },
  ],
});
