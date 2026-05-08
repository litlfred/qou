import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-bkm",
  lean: { ref: "qou:QOU.FluidDynamics.q_bkm_criterion", validation: "not_started" },
  title: "$q$-deformed Beale--Kato--Majda criterion",
  uses: ["prop:q-ns-nonlinear-uniqueness"],
  tags: ["BKM", "blowup-criterion", "vorticity", "regularity"],
});
