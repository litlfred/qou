import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-as-noncomm-fourier",
  title:
    "The Wedderburn--Artin mass sum is the inverse non-commutative Fourier transform on $H_n(q)$",
  lean: {
    ref: "qou:QOU.WedderburnFourier.peter_weyl_decomposition",
    validation: "not_checked",
  },
  cites: ["jones1987", "kassel1995", "fulton1997"],
  tags: [
    "wedderburn-artin",
    "peter-weyl",
    "non-commutative-fourier",
    "hecke-algebra",
    "plancherel",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-07",
      body:
        "**§7c base-ring note (archimedean specialisation).** " +
        "`NonCommFourierData` types the trace `tr`, the characters `chi`, the " +
        "quantum dimensions `dim` and the Plancherel weights `weight` over " +
        "`ℝ`. The decomposition divides by `dim lam` (guarded by " +
        "`dim_ne_zero`), so the ground object must at minimum be a field; `ℝ` " +
        "is the evaluation target because the Plancherel measure and the " +
        "Markov trace are read as *numerical* weights feeding the mass sum. " +
        "The purely algebraic Wedderburn–Artin content this file re-labels " +
        "lives upstream in `QOU.WedderburnMass`.",
    },
  ],
});
