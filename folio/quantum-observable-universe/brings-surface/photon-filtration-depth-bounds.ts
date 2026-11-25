import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:photon-filtration-depth-bounds",
  title: "Bounds on the photon stopping depth $L(n)$",
  lean: { ref: "qou:QOU.StandardModel.PhotonStoppingDepth.depth_lower_bound" },
  uses: ["def:photon"],
  cites: ["iwahori1964", "kassel2008"],
  tags: ["photon", "hecke-algebra", "filtration", "sliding-photon", "gamma-gamma"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-25",
      body: "Lean (sorry-free): `QOU.PhotonStoppingDepth.photon_pow_le`, `depth_lower_bound`, `filtration_le_photon_pow`, `sum_ceil_half`; `QOU.PhotonStoppingDepthThree` proves $L(3) = 2$ in the concrete model of $H_3(q)$. The Iwahori–Matsumoto facts about $H_n(q)$ for general $n$ (multiplicativity of the length filtration, $T_{w_0} \\notin C_{N-1}$, the reduced-word normal form) are standard and cited; the Lean files carry them as hypotheses because the corpus has a concrete model of $H_3(q)$ only. Measured: $L(4) = 4$, $L(5) = 6$, $L(6) = 9$ (`computations/probes/photon_jet_spectral/photon_stopping_depth_probe.py`). Audit: `docs/audits/2026-11-25-photon-jet-and-hearing-the-shape.md` §12.",
    },
  ],
});
