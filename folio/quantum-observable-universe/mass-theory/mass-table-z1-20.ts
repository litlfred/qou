import { remark } from "../../schema/builders";

/**
 * Mass comparison table Z = 1-20.
 */
export default remark({
  label: "rem:mass-table-z1-20",
  title: "Predicted vs observed masses, $Z = 1$--$20$",
  interprets: "thm:wedderburn-mass-formula",
  uses: ["rem:kashaev-volume-density"],
  authorNotes: [
    {
      kind: "note",
      body: "Computational provenance: computations/wedderburn_mass_table_z1_20.py (witness wedderburn-mass-table-z1-20); replaces legacy third coefficient 0.0499 and convention C.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/wedderburn_mass_table_z1_20.py",
    witness: [
      "computations/wedderburn-mass-table-z1-20.witness.json",
      "computations/wedderburn-mass-table-convention-d.witness.json",
      "computations/binding-block-multiplicative.witness.json",
    ],
    status: "verified",
  },
});
