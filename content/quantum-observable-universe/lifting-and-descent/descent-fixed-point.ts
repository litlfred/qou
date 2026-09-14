import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:descent-fixed-point",
  title: "Fixed-point mechanism: ascent and descent",
  tags: ["descent", "ascent", "fixed-point", "involution"],
  uses: [
    "def:brane-boundary",
    "prop:descent-eigenspaces",
    "rem:descent-reduction",
    "rem:descent-reduction-two",
    "rem:descent-reduction-three",
  ],
});
