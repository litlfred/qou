import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:delta-lambda-closure",
  title: "Per-partition Springer/Donaldson–Thomas weight $\\Delta_\\lambda = (-1)^{n(\\lambda)}\\dim V_\\lambda$ and extensive separation",
  cites: ["shoji2019", "springer1976"],
  uses: [
    "prop:delta-lambda-dt-index-unification",
    "rem:term6-binding-density",
    "prop:wedderburn-trace-identity",
    "alg:per-isotope-binding",
  ],
  tags: [
    "mba",
    "sidecar",
    "delta-lambda",
    "donaldson-thomas",
    "extensive-separation",
  ],
});
