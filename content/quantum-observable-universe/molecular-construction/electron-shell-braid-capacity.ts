import { definition } from "../../schema/builders";

/**
 * Electron shell structure as braid bonding capacity.
 */
export default definition({
  label: "def:electron-shell-braid-capacity",
  title: "Electron shell as braid bonding capacity",
  lean: { ref: "qou:QOU.Molecular.ElectronShellCapacity",
    validation: "not_checked",
  },
  uses: ["def:atomic-braid"],
  tags: [
    "electron-shell",
    "bonding-capacity",
    "valence",
    "trefoil",
  ],
});
