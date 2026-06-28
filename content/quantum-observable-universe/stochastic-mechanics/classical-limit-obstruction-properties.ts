import { remark } from "../../schema/builders";

export default remark({
  label: "rem:classical-limit-obstruction-properties",
  interprets: "def:classical-limit-obstruction",
  title:
    "The Hochschild tower of the classical limit obstruction",
  uses: [
    "def:classical-limit-obstruction",
    "def:quantum-characteristic-classes",
  ],
  tags: [
    "obstruction",
    "classical-limit",
    "hochschild-cohomology",
    "deformation-theory",
    "q-to-1",
  ],
  cites: ["yekutieli2010"],
});
