import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:local-infinitesimal-field",
  title:
    "Substrate parameter as a local infinitesimal field $\\varepsilon(x)$",
  tags: [
    "surreal-numbers",
    "substrate-parameter",
    "local-field",
    "infinitesimal",
    "points-and-topology",
    "sheaf",
    "open-problem",
  ],
  uses: [
    "def:substrate-parameter",
    "rem:valuation-ring-finite-surreals",
    "def:standard-part-functor",
    "conj:hahn-substrate",
  ],
  cites: [
    "conway1976",
    "ehrlich2012",
    "berarducci-mantova2018",
  ],
});
