import { table } from "../../schema/builders";
export default table({
  label: "tbl:curvature-rank-gb-stratification-table-data",
  title: "Stratification of the Gröbner--Shirshov filtration $J^r(q)/J^{r+1}(q)$ by curvature rank $\\ell$",
  uses: ["prop:curvature-rank-gb-stratification"],
  tags: ["extracted-table"],
});
