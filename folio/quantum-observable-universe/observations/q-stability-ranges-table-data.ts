import { table } from "../../schema/builders";
export default table({
  label: "tbl:q-stability-ranges-table-data",
  title: "Intervals $[q_{\\min}, q_{\\max}]$ of constant predicted neutron number $n_{\\mathrm{pred}}(p)$ for light and medium elements",
  uses: ["rem:q-stability-ranges"],
  tags: ["extracted-table"],
});
