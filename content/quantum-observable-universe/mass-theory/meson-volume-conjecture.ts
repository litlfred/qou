import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:meson-volume-conjecture",
  title:
    "Meson mass ratio from dual hyperbolic volume",
  uses: [
    "def:categorical-meson",
    "prop:borromean-markov-trace-closed-form",
  ],
  cites: [
    "kashaev1997",
    "murakami-murakami2001",
  ],
  tags: [
    "meson",
    "kaon",
    "pion",
    "hyperbolic-volume",
    "highest-lowest-weight-duality",
    "mass-ratio",
  ],
});
