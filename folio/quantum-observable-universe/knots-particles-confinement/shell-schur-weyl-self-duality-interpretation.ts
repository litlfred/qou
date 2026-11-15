import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:shell-schur-weyl-self-duality",
  label: "rem:shell-schur-weyl-self-duality-interpretation",
  title: "Physical interpretation: shell closures as charge-conjugate-invariant braids",
  tags: ["shell-closure", "magic-numbers", "charge-conjugation", "parity", "schur-weyl"],
  uses: [
    "prop:shell-schur-weyl-self-duality",
    "prop:skein-crossing-asymmetry",
  ],
});
