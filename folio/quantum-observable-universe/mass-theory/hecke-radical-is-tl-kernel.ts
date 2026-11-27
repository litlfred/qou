import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:hecke-radical-is-tl-kernel",
  title:
    "The trace radical of the Hecke algebra is the Temperley--Lieb kernel, up to the " +
    "involution $\\sigma_i \\mapsto -\\sigma_i^{-1}$",
  tags: ["temperley-lieb", "radical", "convention-d", "trace-convention", "hecke"],
  lean: {
    ref: "qou:BraidKnotOctonion.TLKernelEquality.mem_tlKernelPulled_iff",
    validation: "not_checked",
  },
  uses: ["rem:hecke-radical-is-temperley-lieb"],
  cites: ["temperley-lieb1971", "jones1987", "jimbo1986"],
});
