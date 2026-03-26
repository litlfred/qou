import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spin-half-representation",
  title: "The spin-$\\tfrac{1}{2}$ representation $V_{1/2}$",
  uses: [
    "thm:su2-emergence",
    "prop:spin-labels",
    "rem:simple-objects-V",
  ],
  tags: ["spin", "representation", "su2", "fundamental-object"],
});
