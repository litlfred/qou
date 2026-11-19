import { remark } from "../../schema/builders";

export default remark({
  label: "rem:cmb-functor-remark",
  title: "The CMB functor aggregates the boundary datum",
  interprets: "def:cmb-functor",
  tags: ["definition-commentary"],
  uses: [
    "def:cmb-functor",
  ],
});
