import { remark } from "../../schema/builders";

export default remark({
  label: "rem:unitary-stability",
  title: "Unitary stability of the observer drift",
  interprets: "cor:spectral-half-line",
  uses: ["cor:spectral-half-line", "thm:explicit-formula"],
  tags: ["stability", "unitarity", "observer-drift", "q-volume"],
});
