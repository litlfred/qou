import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-navier-stokes",
  label: "rem:q-navier-stokes-remark",
  title: "Dissipation, induced viscosity and incompressibility",
  uses: ["def:q-navier-stokes", "rem:madelung-fluid", "def:substrate-parameter", "def:quantum-observable-universe"],
});
