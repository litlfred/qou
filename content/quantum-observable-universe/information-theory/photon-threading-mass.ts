import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean sibling's claim is " +
        "`E_H = |q - q⁻¹| * (Finset.range n_steps).sum (fun i => c_w_abs i)` — " +
        "an **absolute value**, which needs an ordering on the base ring, " +
        "together with the `PhotonThreadingContext` fields `m_H` (a hadron " +
        "mass) and `E_H` (a crossing energy). Both the `abs` and the " +
        "physical-observable reading put this on the archimedean side: `|·|` " +
        "has no generic-`CommRing` counterpart, and a mass in MeV is `ℝ` by " +
        "meaning (§7c). The `c_w_abs` coefficients are likewise magnitudes. " +
        "Not a gratuitous specialisation.",
    },
  ],
  label: "prop:photon-threading-mass",
  lean: { ref: "qou:QOU.Information.photon_threading_mass", validation: "not_checked" },
  title: "Mass as photon threading cost",
  tags: [
    "mass",
    "photon",
    "groebner-shirshov",
    "hecke",
    "braid",
    "yekutieli",
    "speed-of-light",
  ],
  uses: ["def:mass-identity"],
});
