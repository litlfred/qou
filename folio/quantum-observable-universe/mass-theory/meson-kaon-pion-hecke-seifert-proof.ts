import { proof } from "../../schema/builders";

export default proof({
  label: "prf:meson-kaon-pion-hecke-seifert",
  title: "Proof of meson kaon pion hecke seifert",
  uses: ["prop:meson-kaon-pion-hecke-seifert"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): the four rows are `chi_21_odd`, `seifert_ratio_T25_T23`, `meson_squaring_exponent` (proved by `rfl`), `mesonMassRatio` (a `def`); stated over `[Field R]`, avoiding `CharZero`, verified with `lake env lean`.",
    },
    {
      kind: "note",
      date: "2026-08-08",
      body: "Moved out of the published prose (one-voice sweep): the base-ring note used to add \"(so it stays inside the sandbox cache cone)\" after \"This avoids `CharZero` entirely\". That is the build rationale \u2014 stating the char \u2260 2,3,5 hypotheses explicitly instead of importing `CharZero` keeps the Lean file inside the sandbox's Mathlib cache \u2014 and it belongs here rather than in the paper.",
    },
  ],
});
