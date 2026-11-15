import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-navier-stokes-archimedean",
  title: "Archimedean realisation of the $q$-Navier--Stokes system under the fibre functor",
  interprets: "def:q-navier-stokes",
  tags: ["navier-stokes", "q-deformation", "archimedean", "fluid-dynamics"],
  uses: [
    "def:q-navier-stokes",
    "prop:categorical-archimedean-bridge",
    "ex:c-quantum-observable-universe",
  ],
});
