import { remark } from "../../schema/builders";

export default remark({
  label: "rem:covalent-bond-shared-trefoil-remark",
  title: "Each shared electron contributes two attractive crossings",
  interprets: "def:covalent-bond-shared-trefoil",
  tags: ["definition-commentary"],
  uses: [
    "def:covalent-bond-shared-trefoil",
  ],
});
