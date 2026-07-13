import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:im-q-physical-role",
  label: "rem:ohtsuki-tower-bar-parity",
  title:
    "Bar-parity of the Ohtsuki tower at the imaginary substrate: even rungs are $\\mathrm{Re}\\,\\mathfrak{V}$ (mass), odd rungs are $\\mathrm{Im}\\,\\mathfrak{V}$ (the bar-odd $S$)",
  uses: ["conj:im-q-physical-role", "rem:c3-s-imq-decay-projection"],
  tags: [
    "im-q",
    "ohtsuki-tower",
    "complex-volume",
    "bar-parity",
    "c3-bar-odd",
    "q-beta",
    "candidate-iii",
  ],
});
