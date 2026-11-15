import { remark } from "../../schema/builders";

export default remark({
  label: "rem:winding-parity-sign-transport",
  interprets: "prop:winding-lattice-norm-form",
  title:
    "Winding parity as a sign mechanism: what the golden order would buy, and why it is not yet a derivation",
  uses: [
    "prop:winding-lattice-norm-form",
    "prop:cusp-shape-bar-parity",
    "fundamental-knots-operator-basis",
  ],
  tags: [
    "winding-parity",
    "brings-surface",
    "golden-ratio",
    "bar-parity",
    "conjectural-transport",
    "anti-fit",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-07-27",
      body:
        "**Conjectural transport, 2 bits.** The parity→sign rule matches both anchors " +
        "parameter-free, but the $S$-channel/$\\mathrm{Im}\\,\\mathfrak{V}$ identification is " +
        "derived only on the disc-12 cusp torus; the Bring-side complex-volume computation " +
        "is not done. Magnitudes unexplained (observed ratio 4.08; best golden candidate " +
        "$\\varphi^3$ misses by 3.9%) and deliberately not pursued — dense cusp shapes " +
        "(Dang–Purcell) make magnitude-matching a fit trap. Probes: " +
        "`qbeta_cusp_lattice_geodesic_probe.py`, `qbeta_disc5_parity_probe.py`. " +
        "Bibliography entry for Dang–Purcell still to be added (arXiv lookup unavailable " +
        "in-session; publication metadata not verified, so no `\\cite` was fabricated).",
    },
  ],
});
