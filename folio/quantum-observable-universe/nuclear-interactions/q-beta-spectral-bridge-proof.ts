import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-beta-spectral-bridge",
  title: "Proof of q beta spectral bridge",
  uses: ["prop:q-beta-spectral-bridge", "prop:beta-decay-transfer-matrix"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-11-17",
      body: "Owner ruling (card D): state the one-site reading. With L_i = R_i = I the conversion telescopes T_nn -> T_mix -> T_pp, so V_pp/V_nn = 1 + zh exactly and the h^2 coefficient is -z^2/2 (sympy, z free). The two-independent-sites reading gives -z^2/4 and first-order term (z/4 - 1/2)h; at q0 the ratio is 0.9238 vs 0.9517 for the one-site reading. The corpus does not construct L_i, R_i for the free neutron, so the one-site reading is a stated model choice. Form A is the retired z = 1 cell.",
    },
  ],
});
