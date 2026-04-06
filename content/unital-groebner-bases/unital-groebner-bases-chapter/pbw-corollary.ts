import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:pbw",
  title: "Poincaré--Birkhoff--Witt theorem over commutative rings",
  tags: ["pbw", "universal-enveloping-algebra", "lie-algebra", "groebner-basis"],
  uses: [
    "thm:unital-groebner-decomposition",
    "thm:buchberger",
  ],
  proofs: ["prf:pbw"],
});
