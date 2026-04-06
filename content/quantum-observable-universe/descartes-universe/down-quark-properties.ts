import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:down-quark",
  label: "rem:down-quark-properties",
  title: "Down quark: mass splitting and isolation",
  tags: ["quark", "down", "crossing", "borromean", "confinement", "mass-splitting"],
  uses: ["def:down-quark", "def:up-quark", "def:borromean-baryon", "rem:skein-crossing-asymmetry"],
});
