import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-threading-mass",
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
  uses: [
    "thm:mass-energy-equivalence",
    "thm:groebner-shirshov-energy",
    "def:mass-identity",
    "def:crossing-energy",
  ],
  cites: [
    "yekutieli2015",
    "reshetikhin1991",
  ],
});
