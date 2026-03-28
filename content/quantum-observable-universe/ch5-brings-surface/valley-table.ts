import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:integer-stability",
  label: "rem:valley-table",
  title:
    "Representative stable isotopes: Coulomb ratio and Diophantine error",
  tags: [
    "valley-of-stability",
    "diophantine",
    "codata",
    "neutron-proton-ratio",
  ],
  uses: ["rem:diophantine-valley"],
});
