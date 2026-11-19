import { remark } from "../../schema/builders";

export default remark({
  label: "rem:electron-knot-remark",
  title: "Electron and up quark share a knot type",
  interprets: "def:electron-knot",
  tags: ["electron", "trefoil"],
  uses: [
    "def:electron-knot",
    "def:up-quark",
  ],
});
