import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-as-noncomm-fourier",
  title:
    "The Wedderburn--Artin mass sum is the inverse non-commutative Fourier transform on $H_n(q)$",
  lean: {
    ref: "qou:QOU.WedderburnFourier.peter_weyl_decomposition",
    validation: "not_checked",
  },
  uses: [
    "thm:wedderburn-mass-formula",
    "thm:jones-markov-trace",
    "thm:markov-trace-product",
    "prop:wedderburn-weight-canonical",
  ],
  cites: ["jones1987", "kassel1995", "fulton1997"],
  tags: [
    "wedderburn-artin",
    "peter-weyl",
    "non-commutative-fourier",
    "hecke-algebra",
    "plancherel",
  ],
});
