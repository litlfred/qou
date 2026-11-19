import { remark } from "../../schema/builders";

export default remark({
  label: "rem:atomic-valence-open-sites-remark",
  title: "Valences of H, C, N, O and lone-pair assignment",
  interprets: "def:atomic-valence-open-sites",
  tags: ["definition-commentary"],
  uses: [
    "def:atomic-valence-open-sites",
  ],
});
