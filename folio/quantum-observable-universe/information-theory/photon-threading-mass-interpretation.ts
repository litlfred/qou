import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:photon-threading-mass",
  label: "rem:photon-threading-mass-interpretation",
  title:
    "The three computations agree, the physical threading picture, and gauge invariance",
  uses: [
    "prop:photon-threading-mass",
    "ex:mass-identity-su2",
    "def:mass-energy",
    "thm:groebner-shirshov-energy",
    "ex:photon-wavefront",
  ],
  cites: ["yekutieli2015", "reshetikhin1991"],
});
