import { remark } from "../../schema/builders";

export default remark({
  interprets: "thm:frobenius-antipode-unifies-chirality-and-tower",
  label: "rem:frobenius-antipode-unifies-chirality-and-tower-interpretation",
  title: "Geometric reading of $G/3$ as the Borromean volume over $|S_4|$",
  uses: [
    "thm:frobenius-antipode-unifies-chirality-and-tower",
    "def:algebraic-quantum-volume",
    "rem:kashaev-volume-density",
  ],
});
