import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-q-piece-remark",
  title: "Properties and motivic interpretation of the Φ_q-pieces",
  interprets: "def:phi-q-piece",
  uses: [
    "def:phi-q-piece",
    "def:quantum-bloch-group",
  ],
});
