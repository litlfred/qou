import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:ugb-pbw",
  title: "Poincaré–Birkhoff–Witt theorem over a commutative ring",
  lean: { ref: "ugb:UGB.BuchbergerPBW.ugb_pbw_corollary", validation: "not_checked" },
  tags: ["groebner-basis", "lie-algebra", "pbw", "main-result"],
  uses: [
    "thm:ugb-main",
    "thm:ugb-buchberger",
  ],
  cites: ["bokutchen2015pbw"],
});
