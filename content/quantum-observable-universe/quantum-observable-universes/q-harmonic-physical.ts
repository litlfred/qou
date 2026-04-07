import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:q-harmonic-physical",
  title: "Physical interpretation of q-harmonicity",
  tags: ["q-deformation", "harmonic-forms"],
  uses: [
    "rem:reeb-physical",
    "def:q-harmonic-form",
  ],
});
