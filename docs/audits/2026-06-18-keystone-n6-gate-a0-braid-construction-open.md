# A0 (formalize-first): the n=6 tower gate is blocked on an undefined braid construction

**Date:** 2026-06-18
**Branch:** `claude/keystone-tower-n6-gate-2026-06-18`
**Status:** formalize-first gating result — a PRUNE, not a refutation. Nothing wired.

## The gating question

The decisive keystone test (§4a of
[`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md))
recomputes the y-frozen single-x over-determination residual of the bar-odd
`χ_λ(𝓑_n − 𝓑_p)` tower at **n = 6, 9, 12**; a monotone shrink → 0 would identify
the bar-odd sector with the Hahn–Exton q-Bessel contraction object (baseline at
n=3 is 6.8%, #2453). Per the formalize-first discipline (CLAUDE.md), before any
n=6 compute: **is the level-6 object even defined?**

## Verdict: NO canonical level-6 proton/neutron braid exists

A corpus sweep (content/, computations/ incl. `_deprecated/`, docs/, Lean) finds:

- **`𝓑_p` (uud), `𝓑_n` (udd) are defined only at H₃** — the typed-`B₃` braids of
  `chi-per-irrep-cyclotomic-closed-forms.md` (`𝓑_p = 6σ+3σ⁻¹+2 avg`, `𝓑_n =
  5σ+4σ⁻¹+2 avg`). Their per-block character differences are Lean-proved at H₃
  only. There is **no** `𝓑_p^{(6)}` / `𝓑_n^{(6)}`, and no proved `χ_λ(𝓑_n − 𝓑_p)`
  for λ⊢6.

- **Higher-strand braids in the corpus are different physical objects.** The
  atomic-braid assembly `atom_braid_word_3A(Z, N)` (`mass_at_3A_proper.py`) builds
  an H_{3A} braid for a *multi-nucleon* atom — A nucleons × 3 quark strands, with
  intra-nucleon + inter-nucleon (pp/nn/pn) crossings. The deuteron (H₆), tritium
  (H₉), ⁴He (H₁₂) braids are **quark-level composites of several nucleons**, not a
  single nucleon lifted to more strands. There is no `𝓑_n − 𝓑_p` analogue at A≥2.

## The framework's "brane tower" is not a strand/crossing tower of the character

Two distinct constructions in the corpus carry the name "brane tower"; **neither**
is a strand/crossing tower of `χ_λ(𝓑_n − 𝓑_p)`:

1. **Categorical jet-prolongation tower** (`recursive-brane-tower.lean`):
   `A_0 = A`, `A_{n+1} = J^1(A_n)` (1-jet prolongation of the Frobenius–Hopf
   object); level n = jet level, a categorical embedding, **not** a strand count.

2. **z-Habiro mass/binding tower** (`brane-tower-z-habiro.md`):
   `Φ_mass^trans(β) = Σ_{i=1}^N Φ_q(\hat V_i)` — a sum of quantum-dilogarithm
   values over the N *per-generator algebraic volumes*, completed cyclotomically
   in z. Its level is the cyclotomic projection level `n_⋆`, **not** a sinh-order
   or strand count. `n_⋆` is the **open part**, and **all six probed forms are
   refuted** (scalar uniform-k; `ℓ·n₀+k`; per-eigenvalue operator-valued;
   multiplicity / Type-B crystal; pair-knot product-volume; pair-knot
   Markov-trace+SDP — see `2026-06-17-refuted-ansatz-lemmas.md`,
   `brane-tower-z-habiro.lean::nStar_all_probed_forms_refuted`). The algebraic
   Cauchy-limit half (`ZHabiroCauchy`) is open.

The §4a audit's dictionary row maps "brane-tower level sum `Σ_ℓ w_ℓ sinh(ℓη)`" to
the Jacobi–Anger q-Bessel expansion (orders 2m+1, weights `2 J_{2m+1}(x)`). That
is an *analytic* identification of a sinh-order series; it does **not** supply a
construction of the underlying braid sequence at higher strand count, and it is
**not** demonstrated to be the same object as either tower above. Whether the
bar-odd q-Bessel tower (Q_β character sector) and the z-Habiro Φ_q tower
(mass/binding) are two faces of one construction is itself **an open structural
question**, not an established identity.

## Why the n=6 scan is pruned (formalize-first)

The higher sinh orders {7, 9, …} the q-Bessel test needs come from higher **Laurent
degree** of `χ_λ(𝓑)(q)`, i.e. **more crossings**, not merely more strands. The
candidate level-6 constructions each fail to canonically supply that:

- **Markov stabilization** `𝓑_p ↦ 𝓑_p · σ_n^{±}` (insert strands): the added
  strands carry no new flavour/crossing structure, so the character at λ⊢6 is
  fixed by branching `λ⊢6 → μ⊢3` of the H₃ values — it reshuffles the same
  {1,3,5} data rather than generating independent higher orders. (A bounded
  follow-up could make this a proved prune.)
- **Higher-A atomic assembly** does add crossings and degree, but it is a
  *different physical object* (a nucleus, not `𝓑_n − 𝓑_p`), with no canonical
  neutron-minus-proton difference at A≥2.
- **Jet-prolongation lift** of `χ_λ(𝓑)` along `A_n → A_{n+1}` is **unformalized**
  (no proof the character is compatible with the jet maps).

Inventing a level-6 braid to feed the scan would be exactly the ungrounded ansatz
the three-calibration / formalize-first discipline forbids — and would re-enter
the same refuted-ansatz space the z-Habiro `n_⋆` probes already exhausted. So the
honest result is: **the n=6 gate is blocked on a missing, first-principles tower-
object construction; n=3 (6.8%) is the furthest the gate advances until that
construction exists.**

## What this redirects toward

The gate's blocker is *the same shape* as the open z-Habiro brane-tower problem —
"which structural level/sequence does the substrate canonically select?" — for
which six fitted forms are already refuted. Productive directions are therefore
**not** a seventh fitted level-6 braid, but:

1. **The structural question** whether the §4a bar-odd q-Bessel tower (Q_β) and
   the z-Habiro Φ_q tower (mass/binding) are the same construction — if so, the
   q-Bessel contiguity (`QBesselContiguityRecurrence.lean`) and the z-Habiro
   Cauchy-limit (`ZHabiroCauchy`) constrain each other, and the open
   `analytic ↔ algebraic` identification (the `c_n` localised-Euler family,
   `z-habiro-increment-probe`) is the shared keystone.
2. **Path B** (this branch's other tranche): derive the uud/udd typed-crossing
   model from the substrate. A substrate derivation of the *crossing* structure is
   what would canonically dictate how the braid (hence its Laurent degree, hence
   the sinh-order tower) extends — closing A0 from first principles rather than by
   stabilization ansatz.

## Discipline

Formalize-first PRUNE (the structural fact that no canonical level-6 braid exists
narrows the search before running it); three-calibration (no seventh fitted
level-6 ansatz); TIERED; nothing wired; c_3/Q_β stay cal-anchored.
