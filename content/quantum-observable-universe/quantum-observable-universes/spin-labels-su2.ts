import { example } from "../../schema/builders";

export default example({
  interprets: "prop:spin-labels",
  label: "ex:spin-labels-su2",
  title: "Spin decomposition of $\\mathrm{Rep}(\\mathrm{SU}(2))$",
  lean: { ref: "qou:QOU.Examples.su2SpinLabels", validation: "not_checked" },
  uses: ["prop:spin-labels", "ex:qou-su2"],
  tags: ["su2", "spin"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/spin-labels-su2-0.svg", blockIndex: 0, hash: "0720fbda8f1d" },
  ],

});
