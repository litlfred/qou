import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-ir-zero-mode-bring",
  title:
    "Photon IR zero-mode on Bring's surface: $\\delta(1/\\alpha_{EM})_{\\mathrm{IR}} = b_1/\\mathrm{Area} = 2g/(4\\pi(g-1))$",
  lean: {
    ref: "qou:QOU.Archimedean.PhotonIRZeroMode.photonZeroModeShift_eq",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    status: "verified",
    script: "folio-assistant/computations/photon_ir_zero_mode_bring.py",
    witness: [
      "folio-assistant/computations/photon-ir-zero-mode-bring.witness.json",
    ],
  },
  uses: [
    "prop:em-coupling-bring-zero-mode",
    "prop:force-carrier-bring-uniqueness",
    "prop:jet-sw-tau-decomposition",
    "prop:alpha-em-habiro-bar-involution",
  ],
  tags: [
    "alpha-em",
    "bring-surface",
    "hodge",
    "gauss-bonnet",
    "photon-zero-mode",
    "harmonic-forms",
    "from-lagrangian",
  ],
  authorNotes: [
    {
      kind: "status",
      body: "The topological/geometric core — Betti number $b_1=2g$, Gauss–Bonnet area, the ratio $2g/(4\\pi(g-1))$, and the strict surface-over-naive dominance — is **proven sorry-free** in Lean (`QOU.Archimedean.PhotonIRZeroMode`). The single cited input is the standard heat-kernel identity (zero-mode contribution $= b_1/\\operatorname{Vol}$). The upstream archimedean uniqueness — that $\\tau_{\\mathrm{arch}}$ lands the substrate state-sum on this Hodge datum ([`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness)) — remains the named conditional input. This proposition resolves the **mechanism** (which manifold, which operator) that [`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode) left open, replacing the failed $M\\times S^1$ guess with the surface harmonic zero-mode. Witness: [`photon_ir_zero_mode_bring.py`](../../folio-assistant/computations/photon_ir_zero_mode_bring.py).",
    },
  ],
});
