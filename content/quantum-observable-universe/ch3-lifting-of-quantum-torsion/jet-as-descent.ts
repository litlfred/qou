import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:cosimplicial-crossed-groupoid",
  label: "rem:jet-as-descent",
  title: "Jet prolongation as formal descent of information",
  tags: ["jet-bundle", "descent", "cosimplicial"],
  uses: [
    "prop:cosimplicial-crossed-groupoid",
    "def:descent-involution",
  ],
});
