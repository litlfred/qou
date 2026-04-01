import { example } from "../../schema/builders";

export default example({
  interprets: "def:recursive-brane-tower",
  label: "ex:brane-tower-levels",
  title: "Archimedean realisation of the brane tower",
  tags: ["archimedean", "brane-tower"],
  uses: [
    "def:recursive-brane-tower",
    "cor:jet-prolongation-C",
  ],
});
