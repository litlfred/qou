import { remark } from "../../schema/builders";

export default remark({
  label: "rem:jet-as-descent",
  title: "Jet prolongation as formal descent of information",
  tags: ["jet-bundle", "descent", "cosimplicial"],
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "prop:jet-prolongation",
    "def:descent-involution",
  ],
});
