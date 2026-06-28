import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-threading-mass",
  lean: { ref: "qou:QOU.Information.photon_threading_mass", validation: "not_checked" },
  title: "Mass as photon threading cost",
  tags: [
    "mass",
    "photon",
    "groebner-shirshov",
    "hecke",
    "braid",
    "yekutieli",
    "speed-of-light",
  ],
  uses: ["def:mass-identity"],
});
