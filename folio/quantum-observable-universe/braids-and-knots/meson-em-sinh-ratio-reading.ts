import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:meson-em-sinh-closed-form",
  label: "rem:meson-em-sinh-ratio-reading",
  title: "The meson mass ratio and its electromagnetic factor",
  tags: ["meson","alpha-em","empirical-comparison","interpretation"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Moved out of the statement of `prop:meson-em-sinh-closed-form` on owner ruling (2026-11-15): physical and empirical readings are kept out of proposition statements and recorded as interpreting remarks. The text is unchanged.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/meson_em_sinh_closed_form.py",
    witness: "computations/meson-em-sinh-closed-form.witness.json",
    status: "verified",
  },
});
