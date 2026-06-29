import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bar-involution-c5-algebraic-identities",
  interprets: "def:bar-involution",
  title:
    "Bar-symmetric algebraic identities: half-step factorization of $h$, Hoefsmit-Quantum-2 ($b^2 = 1 - 1/[2]_q^2$), and the $c_5$ closed form",
  uses: [
    "def:bar-involution",
    "prop:c5-involution-leibniz-decomposition",
    "prop:silver-ratio-beta-decay-null",
  ],
  tags: [
    "bar-invariance",
    "c5",
    "hoefsmit-quantum-2",
    "skein",
    "wedderburn",
  ],
});
