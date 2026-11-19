import { example } from "../../schema/builders";

export default example({
  label: "ex:grothendieck-group-of-a-qou-example",
  title: "The Grothendieck ring of $\\mathrm{Rep}(\\mathrm{SU}(2))$",
  interprets: "def:grothendieck-group-of-a-qou",
  uses: ["def:grothendieck-group-of-a-qou", "rem:grothendieck-group-of-a-qou-remark"],
  tags: ["grothendieck-group", "k-theory", "wedderburn", "quantum-dimension"],
  cites: ["bghl-2017"],
});
