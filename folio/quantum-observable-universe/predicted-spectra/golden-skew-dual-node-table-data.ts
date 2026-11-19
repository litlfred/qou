import { table } from "../../schema/builders";
export default table({
  label: "tbl:golden-skew-dual-node-table-data",
  title: "Golden-ratio bar-involution dual: sub- vs super-classical nodes",
  caption: "The two golden-ratio nodes under $q \\leftrightarrow q^{-1}$: sub-classical $q_{\\mathrm{gold}} = 1/\\varphi^2 \\approx 0.382$ and super-classical $q^*_{\\mathrm{gold}} = \\varphi^2 \\approx 2.618$, with distances from the aether $q_0 \\approx 1.110$.",
  uses: ["prop:golden-skew-dual-node"],
  tags: ["golden-ratio", "bar-involution", "dual-node"],
});
