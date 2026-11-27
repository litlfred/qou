import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spin-involution-isospin",
  title: "Isospin from the spin grading",
  interprets: "def:spin-involution",
  tags: ["spin", "isospin"],
  uses: [
    "def:spin-involution",
  ],
});
