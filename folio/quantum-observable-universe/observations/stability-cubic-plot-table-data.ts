import { table } from "../../schema/builders";
export default table({
  label: "tbl:stability-cubic-plot-table-data",
  title: "Predicted and observed neutron numbers along the stability cubic $t^3 = p(2 + c t^2)$ at $q = q_0$",
  uses: ["rem:stability-cubic-plot"],
  tags: ["extracted-table"],
});
