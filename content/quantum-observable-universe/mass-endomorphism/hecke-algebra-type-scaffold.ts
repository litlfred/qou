import { remark } from "../../schema/builders";

export default remark({
  label: "rem:hecke-algebra-type-scaffold",
  interprets: "rem:braid-group-n-strand",
  title:
    "Iwahori-Hecke algebra $H_n(R, q)$ type scaffold: `HeckeGen n`, `HeckeWord n`, plus `HeckeRelations n q` (quadratic + far-commute + braid cubic via explicit-residual) and `HeckeWedderburn n q` (Plancherel completeness)",
  uses: [
    "rem:braid-group-n-strand",
    "rem:h3-hecke-idempotents",
    "prop:hoefsmit-V21-cos-symmetrization",
  ],
  cites: [
    "kassel1995",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "lean-infrastructure",
    "hecke-algebra-type",
    "wedderburn",
    "scaffolding",
    "open-rd-item-2",
  ],
});
