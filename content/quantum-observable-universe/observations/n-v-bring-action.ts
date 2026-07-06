import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:n-v-bring-action",
  title: "S_5 action on H_n(q) at the electroweak slice",
  cites: ["bring1786", "klein1888"],
  uses: [
    "prop:brings-is-qou",
    "def:hyperelliptic-quintic",
    "conj:mass-endomorphism",
  ],
  defines: [],
  tags: ["tier:E", "n-v", "electroweak", "bring", "s5", "substrate-axiom"],
  lean: { ref: "qou:QOU.Observations.s5_acts_on_ew_slice" },
  authorNotes: [
    {
      kind: "status",
      body: "**Conjectural.**  This is a substrate axiom in the precise sense\nof [`AGENTS.md` §3b](../../../AGENTS.md#3b-conjectural-propagation):\nthe categorical $S_5$-action on $H_n(R, q)$ at the EW slice is\nasserted but not formally constructed.  It is the **first** of the\ntwo lemmas in the\n[N_v derivation](#conj:n-v-leading-order-derivation) chain;\ncombining it with\n[the EW-slice depth lemma](#conj:n-v-tower-depth-ninety) gives the\nleading-order closure $N_v = 120 \\cdot q_0^{90}$ (residual $-0.58\\%$\nvs CODATA Higgs VEV).",
    },
  ],
});
