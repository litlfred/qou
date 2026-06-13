import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:n-v-tower-depth-ninety",
  title: "Brane-tower depth from m_e to v equals 90",
  cites: [],
  uses: ["conj:mass-endomorphism"],
  defines: [],
  tags: ["tier:E", "n-v", "electroweak", "tower-depth", "substrate-axiom"],
  lean: { ref: "qou:QOU.Observations.tower_depth_m_e_to_v_is_ninety" },
  authorNotes: [
    {
      kind: "status",
      body: "**Conjectural.**  This is the **second** of the two substrate\naxioms in the\n[N_v derivation](#conj:n-v-leading-order-derivation) chain.\nCombined with [the Bring action lemma](#conj:n-v-bring-action) it\ngives the leading-order closure $N_v = 120 \\cdot q_0^{90}$\n(residual $-0.58\\%$ vs CODATA Higgs VEV).",
    },
  ],
});
