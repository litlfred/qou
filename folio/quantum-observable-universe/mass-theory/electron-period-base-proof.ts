import { proof } from "../../schema/builders";

export default proof({
  label: "prf:electron-period-base",
  title: "Proof that the electron period is the n=0 base",
  uses: ["prop:electron-period-base", "prop:jet-sw-tau-decomposition"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): prefactor (`second_period_contains_me`, by `T.recurrence 0` and `base0`)." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): ([`QOU.Mass.electron_period_is_base`](#prop:electron-period-base), the structure\nprojection `base0`)." },
  ],
});
