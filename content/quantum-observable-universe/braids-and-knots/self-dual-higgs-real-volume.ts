import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:self-dual-higgs-real-volume",
  title:
    "The self-dual Higgs ($4_1$) has a real complex volume ($\\mathrm{CS}=0$)",
  cites: [
    "nguyen-tran-2021",
    "koelink-stokman-2003",
    "kashaev1997",
    "murakami-murakami2001",
  ],
  lean: {
    ref: "qou:QOU.Knot.SelfDuality.higgs_complex_volume_real",
  },
  tags: [
    "figure-eight",
    "higgs",
    "amphichiral",
    "self-duality",
    "complex-volume",
    "chern-simons",
    "aj-conjecture",
    "askey-wilson",
    "keystone",
  ],
});
