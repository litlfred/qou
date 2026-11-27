import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-shell-braid-capacity-remark",
  title: "Shell filling order",
  interprets: "def:electron-shell-braid-capacity",
  tags: ["definition-commentary"],
  uses: [
    "def:electron-shell-braid-capacity",
  ],
});
