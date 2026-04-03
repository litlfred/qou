import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:observation",
  label: "rem:observation-archimedean",
  title: "Archimedean realisation of observation",
  tags: ["observation", "archimedean"],
  uses: [
    "def:observation",
    "ex:c-quantum-observable-universe",
  ],
});
