import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:binding-manybody-eq-jet-filtration",
  title:
    "Binding many-body series equals the jet-order filtration: $B(K)=\\sum_n m_e\\,a_D^{(n)}$",
  lean: {
    ref: "qou:QOU.Mass.BindingManyBodyJetFiltration",
    validation: "validated",
  },
  uses: [
    "lem:bond-order-eq-jet-degree",
    "prop:sw-period-residue-sum",
    "prop:mi-sw-abelianisation",
    "prop:magic-A-binding-formula",
  ],
  tags: [
    "binding",
    "many-body",
    "jet-order-filtration",
    "seiberg-witten",
    "q-difference",
    "step-9b",
    "open-problem",
  ],
});
