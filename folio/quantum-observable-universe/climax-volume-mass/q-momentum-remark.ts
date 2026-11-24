import { remark } from "../../schema/builders";

export default remark({
  label: "rem:q-momentum-remark",
  title: "Writhe equality, trace form and canonicity of the q-momentum",
  interprets: "def:q-momentum",
  uses: [
    "def:q-momentum",
    "rem:markov-moves-brane-tower",
  ],
});
