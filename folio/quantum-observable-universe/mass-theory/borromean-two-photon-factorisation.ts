import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-two-photon-factorisation",
  title: "The Borromean braid is a product of two commuting photons in $H_3(q)$",
  lean: {
    ref: "qou:QOU.Mass.BorromeanPhotonFactorisation.borromean_eq_photon_product",
  },
  uses: ["prop:borromean-markov-trace-closed-form"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["borromean", "hecke-algebra", "photon", "gamma-gamma", "nucleon-element"],
});
