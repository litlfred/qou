import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:borromean-two-photon-factorisation",
  title: "The Borromean element is a product of two photons",
  tags: ["photon", "hecke-algebra", "borromean", "gamma-gamma", "nucleon"],
  uses: ["def:photon"],
  lean: { ref: "qou:QOU.Photon.Borromean.HeckeThree.borromean_eq_two_photons", validation: "not_checked" },
});
