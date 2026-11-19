import { remark } from "../../schema/builders";

export default remark({
  label: "rem:skein-binding-lagrangian-remark",
  title: "Status of the strong and Coulomb terms of the binding Lagrangian",
  interprets: "def:skein-binding-lagrangian",
  uses: [
    "def:skein-binding-lagrangian",
    "prop:qou-canonical-action",
  ],
});
