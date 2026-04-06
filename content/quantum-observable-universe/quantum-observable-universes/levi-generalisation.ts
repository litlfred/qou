import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:q-harmonic-form",
  label: "rem:levi-generalisation",
  title: "Generalisation beyond strict pseudoconvexity",
  tags: ["cr-geometry", "levi-form"],
  uses: [
    "def:q-harmonic-form",
    "rem:c-substrate-via-levi",
  ],
});
