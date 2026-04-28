import { definition } from "../../schema/builders";

export default definition({
  label: "def:covalent-bond-types",
  title: "Covalent bond (shared Hopf links)",
  tags: [
    "covalent-bond",
    "hopf-link",
    "shared-sub-link",
    "single-bond",
    "double-bond",
    "triple-bond",
    "electron",
    "molecular",
  ],
  lean: { ref: "qou:QOU.Organic.CovalentBond",
    validation: "not_checked",
  },
  uses: ["prop:metallic-character-knot"],
});
