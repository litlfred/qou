import { remark } from "../../schema/builders";

export default remark({
  label: "rem:phi-b-bar-parity-interpretation",
  title: "Bar-parity decomposition: sinh/cosh interpretation and the c_k ladder",
  interprets: "prop:phi-b-bar-parity-decomposition",
  tags: ["bar-involution", "sinh-cosh", "complex-volume", "qbeta", "ck-ladder"],
  uses: [
    "prop:phi-b-bar-parity-decomposition",
    "conj:binding-qbeta-complex-volume",
  ],
});
