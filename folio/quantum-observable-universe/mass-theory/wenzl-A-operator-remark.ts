import { remark } from "../../schema/builders";

export default remark({
  label: "rem:wenzl-A-operator-remark",
  title: "Role and extraction of the Wenzl A-operator",
  interprets: "def:wenzl-A-operator",
  uses: [
    "def:wenzl-A-operator",
    "prop:lr-coefficient-hecke",
  ],
});
