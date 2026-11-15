import { remark } from "../../schema/builders";

export default remark({
  interprets: "rem:bsd-surreal-bound",
  label: "rem:adelic-tate-bsd-reduction",
  title:
    "Adelic Fourier transform gives the BSD leading-coefficient prefactor as a local-squeeze check",
  uses: [
    "rem:bsd-surreal-bound",
    "rem:adelic-tate-squeeze",
  ],
  tags: [
    "adeles",
    "tate-thesis",
    "bsd",
    "fourier-transform",
    "millennium-problem",
    "surreal",
    "local-global",
  ],
});
