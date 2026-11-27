import { proof } from "../../schema/builders";

export default proof({
  label: "prf:q-zero-complex-extension",
  title: "Proof of q zero complex extension",
  uses: ["prop:q-zero-complex-extension"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): the QOU formalisation enforces the same generic typing. The relevant Lean files\n([`hq-bi-filtration.lean`](hq-bi-filtration.lean),\n[`explicit-central-idempotent.lean`](../mass-endomorphism/explicit-central-idempotent.lean),\n[`categorical-q-lie-bracket.lean`](../quantum-observable-universes/categorical-q-lie-bracket.lean),\n[`bar-involution.lean`](../braids-and-knots/bar-involution.lean)) all carry\n`{R : Type*} [CommRing R]` (or stronger) and `{q : R}` without an\nordering predicate." },
  ],
});
