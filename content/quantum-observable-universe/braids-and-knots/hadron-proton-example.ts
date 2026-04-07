import { example } from "../../schema/builders";

export default example({
  label: "ex:hadron-proton",
  title: "The proton as a Borromean hadron",
  interprets: "def:hadron",
  uses: ["def:hadron", "def:borromean-baryon", "ex:crossing-energy-trefoil"],
  tags: ["hadron", "proton", "borromean", "example"],
});
