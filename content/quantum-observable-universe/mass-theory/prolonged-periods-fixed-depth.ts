import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:prolonged-periods-fixed-depth",
  lean: {
    ref: "qou:QOU.Mass.prolongation_fixed_depth_recurrence",
    validation: "validated",
  },
  title: "A fixed-depth recurrence for the prolonged periods exists (Cayley–Hamilton)",
  uses: ["prop:mi-sw-abelianisation"],
  proofs: ["prf:prolonged-periods-fixed-depth"],
});
