import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:descent-involution",
  label: "rem:descent-involution-remark",
  title: "Idempotence of the descent involution",
  uses: ["def:descent-involution", "lem:descent", "prop:jet-prolongation"],
});
