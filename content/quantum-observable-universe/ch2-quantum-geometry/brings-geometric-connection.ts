import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:brings-geometric-connection",
  title: "Connection to the Brings surface",
  uses: ["def:q-harmonic-form", "ex:brings-surface"],
  tags: ["brings-surface", "pedagogy"],
});
