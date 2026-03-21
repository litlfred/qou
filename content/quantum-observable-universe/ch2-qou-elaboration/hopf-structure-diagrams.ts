import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hopf-structure-diagrams",
  title: "Hopf-algebra structure: coassociativity",
  tags: ["hopf-algebra"],
  uses: [
    "rem:hopf-non-cocommutativity",
    "rem:self-dual-ses",
  ],
});
