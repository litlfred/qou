import { remark } from "../../schema/builders";

export default remark({
  label: "rem:descent-one-dim",
  title: "Descent to one complex dimension",
  tags: ["descartes-universe", "descent"],
  uses: [
    "prop:jet-prolongation",
    "prop:euler-char-stability",
    "rem:descent-reduction-zero",
  ],
});
