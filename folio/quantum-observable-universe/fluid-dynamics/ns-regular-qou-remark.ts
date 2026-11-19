import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:ns-regular-qou",
  label: "rem:ns-regular-qou-remark",
  title: "NS-regularity, the Euler characteristic and the Navier--Stokes bridge",
  uses: ["def:ns-regular-qou", "thm:ns-singularity-descartes", "def:q-navier-stokes"],
});
