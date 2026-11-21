import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:pbw",
  title: "Poincaré--Birkhoff--Witt theorem over commutative rings",
  lean: { ref: "ugb:UGB.UnitalGroebner.pbw_corollary", validation: "not_checked" },
  tags: ["pbw", "universal-enveloping-algebra", "lie-algebra", "groebner-basis"],
  uses: [
    "thm:unital-groebner-decomposition",
    "thm:buchberger",
  ],
  cites: ["bokutchen2015pbw"],
  proofs: ["prf:pbw"],
});
