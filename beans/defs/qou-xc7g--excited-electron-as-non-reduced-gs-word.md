---
# qou-xc7g
title: 'Excited electron as a non-reduced GS word? Two corpus excitation constructions disagree'
status: todo
type: task
priority: normal
created_at: 2026-11-21T00:00:00Z
updated_at: 2026-11-21T00:00:00Z
---

Owner question (2026-11-21): "Can we see this in the grobner bases calculations that an excited electron is a non-reduced?" Measured in PR #8727 (branch claude/photon-excitation-gs-reduction-2026-11-21, audit docs/audits/2026-11-21-photon-excitation-gs-reduction.md).

- Stabilisation reading (transfer-matrix-operator-properties.md, sigma_i -> sigma_i sigma_n): the excited word stays reduced. Bruhat length +1 per curl; tr_D x z_D per curl (x z_D(q^-1) for a negative curl).
- Same-strand reading (hydrogen-orbitals.md, writhe 3->5->7, n=(w-1)/2): sigma^(2n+1) is non-reduced, but so is the ground state sigma^3. The level shows only in the q-degree of the NF coefficient (2n). On two strands sigma^5 is T(2,5), not a trefoil.
- Proved in H2 (QOU/Excitation/WritheIndexCharacterH2.lean, sorry-free): chi(NF(w)) = q^writhe(w). Rewrite count is not invariant (#8682).

Open: (1) which construction the corpus means (owner); (2) general-n Lean for chi = q^writhe and for length additivity under stabilisation; (3) neither construction alone gives a 1/n^2 ladder (scope a). Do not close while (1) is undecided.

## 2026-11-21 coordinator note
Owner: the electron is σ₀σ₁σ₀, whose closure is the Hopf link (ruled 2026-11-21; trefoil σ₀³ is the backup). Under that ruling, the strand-adding construction is the consistent one: the excited word is reduced, its closure stays the Hopf link, and the level is word length. The writhe +2 reading belongs only to the trefoil backup. Audit §4a (#8732). Bean stays open: general-n Lean for χ = q^writhe and the +1 length per strand.
