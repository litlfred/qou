import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hydrogen-shell-writhe",
  title:
    "Electron shell number equals writhe level of the trefoil embedding",
  tags: ["hydrogen", "shell", "writhe", "trefoil", "reidemeister", "orbital"],
  lean: { ref: "qou:QOU.BringsSurface.hydrogen_shell_writhe",
    validation: "not_checked",
  },
  uses: ["def:electron-knot"],
});
