import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:q-bkm",
  lean: { ref: "qou:QOU.FluidDynamics.q_bkm_criterion", validation: "not_checked" },
  title: "$q$-deformed Beale--Kato--Majda criterion",
  uses: ["prop:q-ns-nonlinear-uniqueness"],
  tags: ["BKM", "blowup-criterion", "vorticity", "regularity"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): All three are one shared object, `QOU.Information.SkeinObservationSystem` (regularity is `Regular` / `regular_of_len_nonincreasing`, the abstract shadow of this criterion)." },
  ],
});
