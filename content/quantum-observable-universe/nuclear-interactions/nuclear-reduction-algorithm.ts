import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:nuclear-groebner-reduction",
  label: "rem:nuclear-reduction-algorithm",
  title: "Nuclear braid reduction algorithm",
  tags: [
    "algorithm",
    "groebner-shirshov",
    "hecke-algebra",
    "normal-form",
    "leitner-pawloski",
  ],
  uses: ["prop:inductive-gb-reduction"],
  cites: [
    "leitnerpawloski2004",
  ],
});
