import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-metric-contact-deformation",
  title:
    "$q$-deformation as a contact metric change (Miranda picture)",
  uses: [
    "conj:levi-degeneracy",
    "def:categorical-reeb-derivation",
    "def:frobenius-hopf-substrate",
    "def:ns-obstruction",
    "def:q-navier-stokes",
    "prop:core-levi-form",
    "rem:hyperbolic-overlap-saturation",
    "rem:madelung-fluid",
    "rem:q-ns-research-programme",
    "rem:reeb-contact-universal-computer",
    "rem:townsend-biot-savart-strain",
    "thm:q-ns-wellposedness",
  ],
  cites: ["cardona2021"],
  tags: [
    "q-deformation",
    "contact-geometry",
    "metric-change",
    "reeb",
    "miranda",
    "fluid-dynamics",
  ],
});
