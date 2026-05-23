import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:jet-prolongation",
  label: "rem:descent-one-dim",
  title: "Descent to one complex dimension",
  tags: ["archimedean-universe", "descent"],
  uses: [
    "prop:euler-char-stability",
    "rem:descent-reduction-zero",
  ],
});
