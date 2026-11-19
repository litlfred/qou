import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-bkm",
  lean: { ref: "qou:QOU.FluidDynamics.q_bkm_criterion", validation: "not_checked" },
  title: "$q$-deformed Beale--Kato--Majda criterion",
  uses: ["prop:q-ns-nonlinear-uniqueness"],
  tags: ["BKM", "blowup-criterion", "vorticity", "regularity"],
  authorNotes: [
    {
      kind: "note",
      body: "Abstract filtration shadow in `QOU.Information.SkeinObservationSystem`: `Regular` and `regular_of_len_nonincreasing`.",
    },
  ],
});
