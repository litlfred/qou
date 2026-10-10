import { definition } from "../../schema/builders";

export default definition({
  label: "def:braid-group",
  examples: ["ex:braid-group-su2"],
  lean: { ref: "qou:QOU.BraidGroup", validation: "not_checked" },
  title: "Braid group on three strands",
  tags: ["braid-group", "group-theory"],
  uses: [],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/braid-group-0.svg", blockIndex: 0, hash: "7617d6c04ba1" },
  ],

});
