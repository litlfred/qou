import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:descent-fixed-point",
  title: "Fixed-point mechanism: ascent and descent",
  tags: ["descent", "ascent", "fixed-point", "involution"],
  uses: [
    "prop:jet-prolongation",
    "lem:descent",
    "def:descent-involution",
    "def:brane-boundary",
    "prop:descent-eigenspaces",
    "rem:algebraic-filter",
    "rem:descent-reduction",
    "rem:descent-reduction-zero",
  ],
});
