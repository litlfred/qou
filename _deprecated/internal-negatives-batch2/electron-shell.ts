import { definition } from "../../schema/builders";

export default definition({
  label: "def:electron-shell",
  title: "Electron shell as cabled strands with SDP-selected binding",
  lean: { ref: "qou:QOU.BraidKnot.ElectronShell",
    validation: "not_checked",
  },
  tags: [
    "electron",
    "shell",
    "cable",
    "sdp-binding",
    "multi-operator",
    "hunds-rule",
    "magic-numbers",
  ],
});
