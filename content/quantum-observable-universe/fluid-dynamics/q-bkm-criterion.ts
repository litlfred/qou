import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-bkm",
  lean: {
    decl: "QOU.FluidDynamics.q_bkm",
    validation: "not_checked",
  },
  title: "$q$-deformed Beale--Kato--Majda criterion",
  uses: [
    "thm:q-ns-wellposedness",
    "prop:q-ns-nonlinear-uniqueness",
    "prop:q-spectral-sobolev",
    "def:q-navier-stokes",
  ],
  tags: ["BKM", "blowup-criterion", "vorticity", "regularity"],
});
