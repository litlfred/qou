import { definition } from "../../schema/builders";

export default definition({
  label: "def:electron-shell",
  title: "Electron shell as cabled strands with SDP-selected binding",
  lean: {
    decl: "QOU.BraidKnot.ElectronShell",
    validation: "not_checked",
  },
  uses: [
    "def:confined-particle",
    "prop:confinement-sdp",
    "def:hecke-normal-form",
  ],
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
