import { example } from "../../schema/builders";

export default example({
  interprets: "thm:qu-to-qou",
  label: "ex:archimedean-yekutieli",
  title: "Bring's surface and $q$-flatness obstructions",
  tags: ["archimedean-universe", "yekutieli", "brings-surface", "motivic-galois"],
  uses: [
    "rem:mass-geometric-drag",
    "rem:chirality-trefoil",
    "rem:kummer-tower",
    "prop:ns-kummer-specialisation",
  ],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-17",
      body:
        "**PARTLY RESOLVED 2026-11-17.** The `chi(A) = -6` is now `chi_eu(M_0) = -6`, the integer of the Kummer obstructions under the unit-tangent-bundle hypothesis stated in `prop:ns-kummer-specialisation`; no trace of `A` enters. **Still OPEN:** the reading of the six branch points as three pairs under `S_3 < S_5`, and of three lepton generations as cyclotomic Galois orbits on them. Bean `qou-qhcr` records that the six Weierstrass points in Bring's curve are the fixed points of one transposition, not an `S_3` orbit structure, so the three-pairs reading has no derivation in the corpus. PR #8365.",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"the perpetual non-vanishing $\\kappa_n \\neq 0$ implies\"",
    },
    {
      kind: "refined-framing",
      date: "2026-11-15",
      body:
        "Re-scoped 2026-11-15 (owner decision, PR #7747, bean qou-lx8f): the previous text read: \"The non-vanishing obstruction classes $\\kappa_n$ obstruct smooth lifting at every level, creating\"",
    },
  ],
});
