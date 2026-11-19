import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:hydrogen-shell-writhe",
  title:
    "Electron shell number equals writhe level of the trefoil embedding",
  tags: ["hydrogen", "shell", "writhe", "trefoil", "reidemeister", "orbital"],
  lean: { ref: "qou:QOU.BringsSurface.hydrogen_shell_writhe",
    validation: "not_checked",
  },
  uses: ["def:electron-knot"],
  authorNotes: [
    {
      kind: "note",
      body: "Archimedean specialisation over R (§7c).",
    },
  ],
});
