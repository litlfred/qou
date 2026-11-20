import { proof } from "../../schema/builders";

export default proof({
  label: "prf:toffoli-lp-stability",
  title: "Proof of toffoli lp stability",
  uses: ["prop:toffoli-lp-stability"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Witness:** `toffoli-lp-stability.witness.json` evaluates $P_{7,7}(q)$, $\\Phi(q)$, and the Gram spectrum $\\{\\lambda_i(\\mathrm{G}(q))\\}$ on the grid $q \\in \\{0.30, 0.35, q_\\star, 0.45, 0.60, 0.80, 0.95, 1.00, 1.05, q_0, 1.25, 1.50, 2.00, 3.00\\}$. Those three confirmations — $P_{7,7}(q_\\star) = 0$, a q-AND zero between $q = 0.45$ and $q = 0.60$, and both amplitudes strictly positive at $q_0$ — belong to the pre-2026-08-30 convention-$C$ producer and are **not** properties of the derived family: the convention-$D$ diagonal has no positive zero, the only off-diagonal zero is at $q = 1$, and $P_{7,6}(q_0) < 0$. The witness has not been regenerated; per item 3 of the proposition the producer needs its Gram trace rule and precision fixed before it can be re-run, so the file on disk should be read as a record of the excised frame." },
    {
      kind: "refined-framing",
      body: "This proof used to close with \"all amplitudes of the correct sign\", and located the sign reversal at q_Φ ≈ 0.466 with the claim that the gate fails CCNOT semantics on (q_Φ, 1). Both were withdrawn along with Φ.",
    },
  ],
});
