import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:motivic-galois-character",
  label: "rem:motivic-galois-character-remark",
  title: "The motivic Galois character and the obstruction classes",
  uses: ["def:motivic-galois-character", "def:quantum-characteristic-classes", "rem:hochschild-kummer-connection", "thm:motivic-perpetual-obstruction", "def:motivic-substrate"],
});
