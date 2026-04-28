import { remark } from "../../schema/builders";

export default remark({
  label: "rem:algebraic-core-survives",
  title: "The algebraic core of QOU lifts to any real-closed field",
  tags: [
    "surreal-numbers",
    "algebraic",
    "field-polymorphism",
    "hecke-algebra",
    "hoefsmit",
    "jones-polynomial",
  ],
  interprets: "def:quantum-observable-universe",
  uses: ["prop:hoefsmit-scattering-pipeline"],
  cites: ["conway1976", "gonshor1986"],
});
