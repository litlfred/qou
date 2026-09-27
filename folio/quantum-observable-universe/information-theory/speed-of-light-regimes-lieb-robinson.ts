import { remark } from "../../schema/builders";

export default remark({
  label: "rem:speed-of-light-regimes-lieb-robinson",
  interprets: "def:information-speed-of-light",
  title: "Regime behaviour and Lieb--Robinson decay for $c_q$",
  tags: [
    "speed-of-light",
    "information-theory",
    "lieb-robinson",
    "causal-structure",
    "q-connection",
  ],
  uses: [
    "def:information-speed-of-light",
    "def:information-bandwidth",
    "ex:q-connection",
    "rem:light-cone-affine",
  ],
});
