import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:pawlowski-leitner-basis",
  label: "rem:pawlowski-leitner-basis-construction",
  title: "PBW derivation of the Pawlowski--Leitner basis",
  uses: ["unital-groebner-bases:cor:pbw"],
  tags: ["basis", "intertwiner", "pbw", "groebner-shirshov"],
});
