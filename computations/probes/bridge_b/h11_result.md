# H11: where the photon word lives in the folded picture (2026-11-21)

Question (owner card, "Derive it from the corpus"): does the photon/nucleon word live in the ambient H_n(q) or in Lusztig's folded bulk at q²?

Criteria fixed before the toy computation below: (1) the answer must come from a corpus statement, an owner ruling, or the held Lusztig text, never from which D value is nicer; (2) if the corpus leaves it open, say so.

## 1. The home is fixed by the corpus: the ambient, at q

- `conj:type-b-folding-cpt` folds "the canonical atomic-braid Hecke algebra H_n(q)". The photon (owner ruling) and the nucleon word are elements of that algebra.
- Owner ruling 2026-11-21 (`docs/coordination/owner-rulings.md`): "in the six-strand folding of the nucleon word, the mirror strands are traced over". So the word is written in the ambient six-strand H_6(q), doubled onto mirror strands.

So the photon and nucleon words live in the **ambient, at q**. No corpus statement places them in the folded algebra. Corpus searched: `type-b-folding-cpt.md` and its 20 citing files, the 2026-11-15 helicity and confinement audits, owner-rulings, grep for ι-fixed / stable matter / fixed points of the folded crystal. `corpus-search.ts` returned nothing (light platform not mounted).

## 2. What remains open: which trace takes them down to the type-B algebra

Lusztig §16.1–16.7 reaches the folded algebra from the ambient by the ι-twisted Grothendieck group K♯: classes of ι-equivariant objects, with ι-swapped (traceless) pairs set to zero (16.1(b)). That is a **twisted** trace. The owner-ruled reading (H9, "summed") is a **plain** trace over the mirror strands. They differ.

Toy check, one doubled letter σ⊗σ on V⊗V, σ with eigenvalues {q, −q⁻¹} (`h11_swap_trace_toy.py`, exact):

| trace | spectrum seen | Hecke-quadratic? |
|---|---|---|
| plain over both copies (H9 ruled "summed") | {q², −1, −1, q⁻²} | no (H9b's cubic) |
| naive swap-twisted, tr(P·(A⊗A)) = tr(A²) | {q², q⁻²} | no |
| Lusztig 16.7(b) folded bulk letter | {q², −q⁻²} | yes |

The naive swap trace removes the cross eigenvalue −1, as the traceless relation predicts, but gets the sign of the q⁻² line wrong (it matches Lusztig only at even powers). Lusztig's sign comes from the normalised equivariant structure φ_x (16.4) on graded Soergel bimodules. A plain matrix model of strands does not reproduce it. So **reading B (bulk q², wall q, D(q₀) = 0.94911520554914481986) is the K♯-level descent of the ambient word, not a strand-level trace of it.**

## Verdict

- **Home: derived.** The word lives in the ambient H_n(q) at q (conjecture wording + owner ruling).
- **Descent: open, and in tension with a ruling.** The ruled "summed" trace is not Lusztig's; Lusztig's twisted trace has no strand-level model in the corpus, and the naive one gets a sign wrong.
- No D value is adopted. D is a trace ratio, not a mass.
