# The orbit principle does not force a symmetrization — and the ordering disqualifier is void

**Date:** 2026-08-09 · **Bean:** `qou-prjo` (deuteron Δ_λ magnitude) — stays **OPEN**
**Branch:** `claude/nastokes-orbit-symmetric-readout-2026-08-09`
**Predecessors:** [#4849](https://github.com/litlfred/qou/pull/4849) (multi-generator
super-pairwise, ordering-dependent), [#4848](https://github.com/litlfred/qou/pull/4848)
(single-generator scope-(b)), [#4818](https://github.com/litlfred/qou/pull/4818)
(pairwise cap), [#4798](https://github.com/litlfred/qou/pull/4798) (the discretization),
[#4619](https://github.com/litlfred/qou/pull/4619) (`tr[A,B] = 0`).

---

## 0. The question, and the answer

#4849 named two blockers for reviving the transverse route. This audit runs
**principle (i)**: *is a nucleon-symmetric readout forced by the corpus's own
treatment of an atom, and if the readout is symmetrized accordingly, does the
super-pairwise content survive or cancel?*

**Answer, in four lines.**

1. The corpus orbit identity `tr_M(β) = tr_M(rep)` is an identity over
   **`S_Z × S_N` only** (protons among protons, neutrons among neutrons), and its
   own proof (Lemma 1) establishes it by showing such a permutation **leaves the
   braid word literally unchanged**. It is therefore **vacuous as a symmetrization
   of the ordering**: the orbit of words is a single point.
2. So orbit-symmetry over the group the corpus actually invokes **is forced —
   and is the identity map.** Symmetrizing the transverse readout over it changes
   nothing. `R₃` **survives**, trivially and by derivation rather than by choice.
3. The permutations #4849 varied — `pnn`/`npn`/`nnp` — are **cross-species**.
   They are **not** in `S_Z × S_N`, no corpus identity covers them, and no physical
   principle demands invariance under them: a proton and a neutron are
   distinguishable, so exchanging one for the other is not an exchange symmetry.
   The corpus's construction is *explicitly* not invariant under them — it changes
   the interface multiset.
4. **Decisively: the corpus's own scalar observable `tr_M` is itself
   cross-species-ordering-dependent** (§3, measured). #4849's disqualifier —
   *"a nuclear observable cannot be a function of the braid word"* — therefore
   applies verbatim to the canonical mass/binding trace. It does not single out the
   transverse pairing, and as a reason to reject the transverse pairing **it is
   void**.

**Net effect on the bean.** Blocker (i) is **dissolved, not solved**: there is no
symmetrization to impose, so there is nothing left to fix on that axis — but
nothing is thereby determined either. Blocker (ii) (which germ observer pair, plus
the representation gauge of #4849 §2.3, a **16.4×** spread) is **untouched and
still binding**. The transverse route remains blocked, on one blocker instead of
two. `free_parameters = 0`; no AME quantity and no `g₂` appears in this audit's
compute; nothing is wired; bean stays **OPEN**.

A separate finding falls out (§6): the corpus's *canonical* cross-species ordering
`p…pn…n` is a **choice**, the orbit identity does **not** license it, and the
canonical trace depends on it. That is an open item in the canonical chain, filed
as its own bean — not a transverse-route matter.

---

## 1. Phase 0 — corpus grep: what `atom_orbit_reduction` actually guarantees

Per AGENTS.md §"Before declaring open math". Searched `computations/`, `content/`,
`docs/audits/`, `docs/coordination/` for `atom_orbit_reduction`,
`orbit_representative`, `interface-minimal`, identical-particle symmetrization,
and every consumer of the orbit identity.

| Corpus object | What it says | Group |
|---|---|---|
| [`computations/atom_orbit_reduction.py`](../../computations/atom_orbit_reduction.py) | `tr_M(β_{Z,N}) = tr_M(rep)`, **no `\|orbit\|` multiplier**; `orbit_size = Z!·N!` is *audit metadata* | `S_Z × S_N` |
| [`docs/audits/2026-05-30-orbit-trace-identity-proof.md`](2026-05-30-orbit-trace-identity-proof.md) **Lemma 1** | a same-species `σ` **(a)** fixes the ordering string `p…pn…n` and **(b)** preserves every adjacency type ⇒ *"the word is unchanged under `σ`"* | `S_Z × S_N` |
| same, **Lemma 2** | Markov axiom M1: `tr_M` is conjugation-invariant; a *block* relabelling is conjugation by a strand-permutation braid | `S_Z × S_N` |
| [`QOU/Hecke/IdenticalParticleSymmetrization.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/IdenticalParticleSymmetrization.lean) | Schur–Weyl: `p₁^Z = Σ_{λ⊢Z} f^λ s_λ`; an identical-nucleon state occupies **one** `S_Z` sector | `S_Z` (and `S_N`) |
| [`computations/symmetrized_binding_probe.py`](../../computations/symmetrized_binding_probe.py) | the corpus's one *explicit* symmetrization operator: `tr_atom_sym = \|G\|⁻¹ Σ_{σ ∈ S_Z×S_N} tr_M(W_atom·σ)` | `S_Z × S_N` |

**Every** symmetry statement in the corpus is over `S_Z × S_N`. **No corpus object
asserts invariance under a cross-species reordering**, and none was found by any of
the four grep paths.

### 1.1 The identity is vacuous *as an ordering symmetry* — by its own proof

This is the point that decides the question, and it is visible in the proof rather
than in the headline. Lemma 1 does not show that a nontrivial reordering leaves the
*trace* invariant. It shows the reordering leaves the **word** invariant:

> *"A permutation `σ ∈ S_Z × S_N` **(a)** fixes the ordering string — protons stay in
> positions `0..Z-1`, neutrons in `Z..A-1`, so `p…pn…n` is unchanged; … Hence the
> word is unchanged under `σ`."*

The `S_Z × S_N` orbit of the canonical word is a **single word**. So the identity
`tr_M(β) = tr_M(rep)` is not evidence that the corpus's observable is invariant
under a nontrivial relabelling of the nucleon ordering — it is the statement that
the ordering never changed. (Lemma 2 adds a genuine invariance, conjugation by the
block-permutation braid; that is an invariance of the *trace functional*, and it
too is same-species.)

The module docstring is candid that other orderings are **different words**:

> *"the canonical `p…pn…n` ordering is **interface-minimal** (exactly one pn
> crossing; every other ordering of the same multiset has ≥ 1 and generically
> more)"*

Interface-minimality is a comparison **across** the `S_A` orderings — i.e. across
words the identity says nothing about. `interface_multiset('pnn') = {pn:1, nn:1}`
but `interface_multiset('npn') = {pn:2}`: the words genuinely differ, and the
corpus knows it.

### 1.2 Negative Phase-0 findings

Recorded so a later agent does not re-search: there is **no** corpus block deriving
the canonical cross-species ordering from a principle (interface-minimality is
stated as a cost/convenience property, not as a physical selection rule); **no**
block asserting `tr_M` is invariant under `S_A`; and **no** prior probe measuring
`tr_M` across cross-species orderings. `symmetrized_binding_probe.py` is the only
explicit symmetrization operator in the corpus and it is `S_Z × S_N`.

---

## 2. The crux — FORCED or CHOSEN, decided

The task's crux question admits a sharper answer than either branch it anticipated,
because the group matters more than the act:

| Group | Is symmetrization forced? | What it does to the word | Effect on a readout |
|---|---|---|---|
| **`S_Z × S_N`** (same-species) | **YES — forced.** Identical nucleons are indistinguishable; the corpus formalizes it twice (Schur–Weyl sector projection; the orbit identity). | **Nothing.** Lemma 1: the word is unchanged. | **Identity map.** Every readout — scalar or operator, `tr_M` or `Ω` or `R₃` — is already `S_Z × S_N`-symmetric. |
| **`S_A` / cross-species** (`pnn ↔ npn`) | **NO — and not merely "convenient": it is not a symmetry at all.** A proton and a neutron are distinguishable particles; there is no exchange symmetry between them, and no corpus object claims one. | Changes the interface multiset ⇒ a **different word**. | Would change every readout — **including the corpus's own `tr_M`** (§3). |

**Therefore:**

- **Symmetrization is forced, and it is vacuous.** The derived orbit-symmetric
  readout on the atom *is* the readout on the canonical word. This is a derivation,
  not a convenience: it follows from Lemma 1, which is the corpus's own proof.
- **The symmetrization #4849 implicitly demanded — over `S_A` — is not derivable**,
  because the invariance it would enforce is not a property the corpus's own
  observables have. Imposing it would be a *new* assumption, and one that
  contradicts the canonical construction.

Committed **before** any measurement, per the anti-fit discipline: the derived
symmetrization is the `S_Z × S_N` one, it is the identity, and the answer to
"survive or cancel" is therefore **survive** — fixed by derivation, with no freedom
to shop. §4 reports the `S_A` average anyway, as a labelled counterfactual, because
it is informative whichever way it comes out and because reporting it costs nothing
now that the derived answer is already committed.

---

## 3. The decisive measurement — the corpus's own `tr_M` is cross-species ordering-dependent

*(filled in below)*

---

## 4. The counterfactual `S_A` average

*(filled in below)*

---

## 5. Scope classification

*(filled in below)*

---

## 6. Fallout: the canonical ordering is an unlicensed choice

*(filled in below)*
