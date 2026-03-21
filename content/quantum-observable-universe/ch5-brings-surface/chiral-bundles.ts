import { remark } from "../../schema/builders";

export default remark({
  label: "rem:chiral-bundles",
  title: "Chiral space as spectral curve and spinor bundle",
  uses: [
    "prop:chiral-elliptic",
    "rem:lagrange-resolvents",
    "rem:holonomy-trefoil",
    "rem:t-duality-elliptic",
  ],
});
