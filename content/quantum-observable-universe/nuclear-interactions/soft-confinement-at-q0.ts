import { remark } from "../../schema/builders";

export default remark({
  label: "rem:soft-confinement-at-q0",
  title:
    "Soft confinement level $\\ell_*(q_0)$ from Plancherel decay",
  interprets: "rem:frobenius-packing-density",
  tags: [
    "confinement",
    "plancherel",
    "root-of-unity",
    "fusion-category",
    "truncation",
    "substrate-parameter",
  ],
  uses: ["rem:frobenius-packing-density"],
});
