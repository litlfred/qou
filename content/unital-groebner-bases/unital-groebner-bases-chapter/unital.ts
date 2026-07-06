import { definition } from "../../schema/builders";

export default definition({
  label: "def:unital",
  title: "Unital subset",
  lean: { ref: "ugb:UGB.UnitalGroebner.UnitalGroebnerBasis",
    validation: "not_checked",
  },
  tags: ["groebner-basis", "unital"],
  uses: ["def:groebner-basis", "def:leading-term-data"],
  cites: ["leitnerpawloski2004"],
});
