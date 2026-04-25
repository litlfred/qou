import { definition } from "../../schema/builders";

export default definition({
  label: "def:so3-generators",
  lean: { ref: "qou:QOU.So3Generators", validation: "not_checked" },
  title: "$\\mathrm{SO}(3)$ generators",
  tags: ["so3", "rotation-group"],
  uses: ["def:su2-generators"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/so3-generators-0.svg", blockIndex: 0, hash: "a75c2979e568" },
  ],

});
