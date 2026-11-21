# Sidecar re-triage: lifting-and-descent chapter (2026-11-21)

Umbrella issue #8766. There were 13 stale items, plus 3 statements whose only verdict was an unhashed heuristic pass. After the writes the census shows every Lean-backed statement (22) and every proof (21) in this chapter fresh.

## Re-stamped (wording only, earlier verdict kept)

These were all fail before and stay fail:

- jet-prolongation, brane-boundary-structure, jet-prolongation-C, euler-char-stability (statements);
- descent-lemma, yekutieli-lifting, cosimplicial-crossed-groupoid, brane-boundary-structure, euler-char-stability, qu-to-qou (proofs).

The edits were voice changes, removed Lean names, and removed "Descartes chirality" phrases. The known false items are unchanged: dim J¹(A) = dim A in euler-char-stability, and Riemann–Hurwitz for χ > 0 in qu-to-qou.

## Full reviews

- **quantum-characteristic-classes-exists-proof: pass.** It was rewritten as the standard Čech obstruction for lifting an object along a B-gerbe, landing in H², which now matches the statement. Minor: the transition morphisms ξ_{αβ} are used before they are introduced.
- **quantum-characteristic-classes-unique-proof: pass.** Different choices change the cocycle by a coboundary. This is brief but correct.
- **ordering-jet-compatibility (statement): fail, major.** There is real progress: the axioms became sorry-free theorems on a word model (bean qou-6qbv). But the md still claims three things the Lean does not show:
  - The ordering on the actual Hecke basis is preserved by the actual jet map. The Lean takes "ℓ_n is a monotone relabelling" as a hypothesis.
  - Item 2 holds for all algebra elements c, d. That is false at c = 0; it holds for monomials.
  - Leading monomials exist in the direct limit.

  lean.ref still names only degLex_wellFounded.

## First real reviews (previously unhashed heuristic passes)

- **quantum-characteristic-classes-exists: fail, major.** The Lean is `Nonempty` with the trivial witness ⟨0, ℤ, 0⟩, so nothing about gerbes or H² is encoded. The file says so honestly.
- **quantum-characteristic-classes-unique: fail, major.** The Lean proves only structure extensionality, not that the cocycles are cohomologous. The file says so honestly.
- **p3-blowup-yekutieli: fail, major.**
  - lean.ref points at the class, not the theorem.
  - The theorem is `not_forall` applied to the definitional input field.
  - The obstruction is typed ℕ → ℕ.
  - The Sobolev-level claim n* = ⌊s*⌋+1 is neither encoded nor argued.

## Ruling check

No block in this chapter uses the photon form, the electron strand or the two-term trace.
