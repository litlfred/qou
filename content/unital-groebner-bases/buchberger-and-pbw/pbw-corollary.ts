import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:ugb-pbw",
  title: "Poincaré–Birkhoff–Witt theorem over a commutative ring",
  tags: ["groebner-basis", "lie-algebra", "pbw", "main-result"],
  uses: [
    "thm:ugb-main",
    "thm:ugb-buchberger",
    "def:unital-groebner-basis",
  ],
});
