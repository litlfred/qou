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

## 3. Part A — the vacuity, verified mechanically

[`computations/probes/nastokes_orbit_symmetric_readout_probe.py`](../../computations/probes/nastokes_orbit_symmetric_readout_probe.py)
→ `nastokes-orbit-symmetric-readout.witness.json`. 17/17 assertions pass, 162 s.

The `S_Z × S_N` action is enumerated (not asserted) and its orbit on the ordering
string measured:

| atom | `Z,N` | `\|S_Z × S_N\|` | orbit of the ordering **string** | cross-species orderings | distinct words |
|---|---|---|---|---|---|
| D | 1,1 | 1 | **1** | 2 | 2 |
| T | 1,2 | 2 | **1** | 3 | 3 |
| ³He | 2,1 | 2 | **1** | 3 | 3 |
| ⁴He | 2,2 | 4 | **1** | 6 | 6 |

The forced group has order up to 4 and its orbit of ordering strings is a **single
point** in every case, exactly as Lemma 1 requires. Meanwhile every cross-species
ordering gives a genuinely **different word**.

---

## 4. Part B — the decisive measurement

`tr_M` is computed from the canonical Frobenius pairing
`tr_M(β) = Σ_{λ⊢n} y_λ(q₀) χ^λ(β)`, with `y_λ` from the live closed form
[`schur_principal_mpmath.y_lambda_at_q0_mpmath`](../../computations/schur_principal_mpmath.py)
at the **experimental proton anchor** (never the muon-built cache), and `χ^λ` the
trace of the corpus seminormal/Hoefsmit representation.

**Certification, run before use** (this is what makes the result citable):

| check | D (n=6) | T (n=9) | ³He (n=9) |
|---|---|---|---|
| rep: braid + Hecke + far-commutation | 2.3e-15 | 8.4e-15 | 8.4e-15 |
| `tr_M(1) = 1` (normalisation `Σ y_λ f^λ`) | 1.000000000000000 | 1.000000000000000 | 1.000000000000000 |
| **M1** cyclic `tr_M(AB) = tr_M(BA)` on the real atom word | 1.4e-16 | 2.7e-16 | 4.0e-16 |
| **M2** stabilisation ratio `tr_M(βσ_{n-1})/tr_M(β)` | `z = 0.499320334184` | same `z` | same `z` |
| M2 spread of `z` over several `β ∈ H_{n-1}` | 5.6e-16 | 4.5e-16 | 2.2e-16 |

M1 alone would hold for *any* character weights; the **constant M2 ratio** is what
certifies `y_λ` as genuine **Jones–Markov** weights.

### 4.1 Result

| atom | ordering | interface multiset | `tr_M` | rel. to canonical |
|---|---|---|---|---|
| **D** | `pn` ← canonical | `{pn:1}` | 3.883571411978e-01 | 0 |
| | `np` | `{pn:1}` | 3.883571411978e-01 | **+1.4e-16** |
| **T** | `pnn` ← canonical | `{pn:1, nn:1}` | 1.040710573547e-01 | 0 |
| | `nnp` | `{pn:1, nn:1}` | 1.040710573547e-01 | **0.0e+00** |
| | `npn` | `{pn:2}` | 1.415755179229e-01 | **+3.604e-01** |
| **³He** | `ppn` ← canonical | `{pp:1, pn:1}` | 2.065784335107e-01 | 0 |
| | `npp` | `{pp:1, pn:1}` | 2.065784335107e-01 | **−1.3e-16** |
| | `pnp` | `{pn:2}` | 1.633620457246e-01 | **−2.092e-01** |

**The corpus's own canonical scalar observable is cross-species
ordering-dependent — by 36.0 % on tritium and 26.5 % on ³He**, three times the
13 % that #4849 treated as disqualifying for the transverse pairing.

### 4.2 The structure of the dependence, and two controls

**`tr_M` tracks the interface multiset exactly.** Orderings sharing an interface
multiset give *bit-identical* traces (`0.0e+00` / `1e-16`); orderings with
different multisets differ at `O(10⁻¹)`. Verified as an assertion for all three
atoms (`trM_tracks_interface_multiset_*`). So the ordering dependence is not
noise with a pattern — it is precisely the dependence on **how many `pn`
interfaces the arrangement has**.

**Null control (D).** Deuterium's two orderings `pn`/`np` share the single
interface multiset `{pn:1}`, so the trace *must* be invariant there. Re-run
entirely in **mpmath at 40 dps**: `|tr_M(np) − tr_M(pn)| / |tr_M(pn)| = 1.48e-41`.
The machinery does **not** manufacture spurious ordering differences.

**Noise floor.** float64 vs mpmath max relative difference `3.7e-15`; T's measured
`3.604e-01` is `9.7e+13 ×` that floor. Real, not arithmetic.

### 4.3 What this does to #4849 §5.1

#4849 wrote: *"A many-body binding term must be invariant under relabelling the
nucleons; the corpus's own scalar observable is (`tr_M(β) = tr_M(rep)` exactly)."*

The second clause is a **misreading of the identity's group**. Under the
permutations the identity actually ranges over, `tr_M` is invariant because the
word never moves (§1.1). Under the permutations #4849 varied, `tr_M` is **not**
invariant — it swings 36 %. The premise fails, so the disqualifier fails with it:
whatever the 13 % ordering spread of the transverse pairing means, it cannot mean
that the pairing is disqualified *relative to* the canonical trace, which is worse
on the same measure.

---

## 5. Part C — survive or cancel

**Derived answer: survive.** The symmetrization forced by the corpus's own
principle is the identity map (§2, §3), so the orbit-symmetric readout on the atom
*is* `‖R‖` on the canonical word — unchanged and nonzero. Nothing was chosen.

**Counterfactual.** The `S_A` operator average `⟨R⟩ = |orderings|⁻¹ Σ_o R(word_o)`
— well defined because the top-level Möbius residual sums over **all** subsets and
is therefore independent of which nucleon carries which label — is reported for
**all three** of #4849's germ readings, `λ = (10,1,1)`, dim 55:

| atom | germ reading | `‖R‖` canonical | mean `‖R‖` | `‖⟨R⟩‖` | `‖⟨R⟩‖`/mean |
|---|---|---|---|---|---|
| T (`R₃`) | `(0,1)` | 8.294e3 | 8.424e3 | 8.304e3 | **0.9858** |
| T | `(3,4)` | 6.510e3 | 6.615e3 | 6.587e3 | **0.9957** |
| T | band-local | 7.113e2 | 7.376e2 | 7.375e2 | **0.9998** |
| ⁴He (`R₄`) | `(0,1)` | 2.863e3 | 3.303e3 | 3.219e3 | **0.9746** |
| ⁴He | `(3,4)` | 1.069e4 | 9.574e3 | 9.434e3 | **0.9854** |
| ⁴He | band-local | 1.49e-11 | 1.71e-11 | 1.69e-11 | — |

**The `S_A` average does not cancel either** — it retains 97–99.98 % of the mean
norm. So the answer is *survive* on both readings: the derived one (trivially) and
the counterfactual one (measured). The last row reproduces #4849 §4.2's finding
that the four-body cluster level is empty for the band-local curvature — a
cross-check, not a survival failure, and asserted separately.

> **This is not evidence for the route.** Survival was fixed by derivation before
> any arithmetic; the counterfactual merely fails to overturn it. Neither number
> is a magnitude, and neither is compared to anything.

---

## 6. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end".

**scope-(b) — for the vacuity claim only.** *Symmetrizing an atomic-word readout
over `S_Z × S_N` is the identity map.* **Cited invariant:** the word is a function
of the species string, and a species-preserving relabelling fixes that string —
Lean-proved sorry-free (`wordOf_of_speciesPreserving`), with the symmetrization
corollary `sum_symmetrize_eq_nsmul` proved for an arbitrary readout into an
arbitrary `AddCommMonoid`. This is a proved structural fact about the corpus
construction, not a failed search, which is what licenses (b).

**scope-(a) — everything else.**

- **(a⁺)** The super-pairwise residual **survives** the derived symmetrization, and
  also survives the non-derived `S_A` counterfactual. Blocker (i) is **dissolved**.
- **(a⁻)** Nothing is thereby **determined**. Blocker (ii) — *which* two germ
  observers (a **16.4×** spread, #4849 §4.4) plus the unpinned representation gauge
  of the connection-like germ (#4849 §2.3) — is **untouched and still binding**. The
  transverse route is **still blocked**; it is blocked on one principle instead of
  two.

**What is NOT claimed:**

- **Not** that the transverse pairing is the missing many-body term. This audit
  removes an objection; it supplies no magnitude, no sign, no `Δ_λ`.
- **Not** that #4849 is wrong on its measurements. Its numbers reproduce here. What
  fails is §5.1's *inference* from them, because the cited identity was read as
  covering a group it does not cover.
- **Not** that cross-species ordering dependence is *harmless*. It is a real defect
  — see §7 — but it is a defect of the **canonical chain**, shared by `tr_M`, and
  therefore not a discriminator against the transverse pairing.

---

## 7. Fallout — the canonical ordering is an unlicensed choice (separate item)

Not a transverse-route matter, and recorded here only because §4 measures it:

1. The corpus's canonical word fixes the cross-species arrangement to `p…pn…n`.
2. The orbit identity **does not license** that choice: it covers `S_Z × S_N`, under
   which the arrangement never varies.
3. The stated reason — *interface-minimality* — is presented in
   `atom_orbit_reduction.py` as a **cost** property ("the cheapest (canonical) one is
   always valid"), justified by an identity that only holds *within* the orbit. It
   is not derived from a physical selection rule.
4. And §4 measures that the canonical trace **depends** on the choice: 36.0 % on T,
   26.5 % on ³He, tracking the `pn`-interface count exactly.

So a canonical mass/binding number for any `A ≥ 3` isotope with both species
inherits an undetermined `O(10 %)` factor from an arrangement convention. Either a
principle selects the arrangement (interface-minimality promoted to a derived rule,
with an argument), or the observable must be built to not depend on it. Filed as
its own bean; **not** addressed here and **not** a reason to distrust §§3–5, whose
statements are all *relative* comparisons within one convention.

---

## 8. Lean

[`QOU/MassTheory/NucleonOrderingSymmetry.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/NucleonOrderingSymmetry.lean)
— `scripts/lean-verify.sh` **exit 0, zero warnings**; `#print axioms` on **all 8**
declarations gives at most `[propext, Quot.sound]`. No `sorryAx`, no `axiom`, no
`native_decide`, no `: True`, no tautological conclusion. Purely combinatorial —
**no ring at all**, hence trivially §7c-clean (no `ℝ`, no ordering, no `Real.*`).

| Declaration | Statement |
|---|---|
| `iface`, `ifaces`, `wordOf` | the corpus `_interface_type` / `interface_multiset` / `atom_braid_word_ordered` shape, over a generic letter type `L` |
| **`wordOf_of_speciesPreserving`** | `(∀ k, s (σ k) = s k) → wordOf (s ∘ σ) = wordOf s` — Lemma 1(a): the word is *literally equal*, not merely equal-in-trace |
| **`sum_symmetrize_eq_nsmul`** | `∑_{σ ∈ G} f (wordOf (s ∘ σ)) = G.card • f (wordOf s)` for **any** readout `f : List L → M` into any `AddCommMonoid` — symmetrization over the forced group is the identity, for scalar *and* operator readouts alike |
| `ifaces_pnn_ne_ifaces_npn` | `pnn ↦ [pn, nn]` but `npn ↦ [pn, pn]` |
| `count_link_pn` | the word's count of the `pn` letter equals the interface list's `pn` count |
| **`wordOf_pnn_ne_wordOf_npn`** | hence the two words **differ**: cross-species reordering is not a symmetry of the construction |

> **`sorry-free ≠ derived`.** The Lean proves the combinatorics of the word map.
> It derives no magnitude, no `Δ_λ`, no binding energy, and it is **not** evidence
> that the transverse route closes anything. `wordOf_pnn_ne_wordOf_npn` carries the
> distinctness of the interface letters as **hypotheses** (true of the corpus
> letters, but hypotheses here, not corpus facts imported into Lean) — cite it as
> the conditional it is.

---

## 9. Discipline record

- **The symmetrization was derived and committed *before* the compute** (§2, first
  commit on the branch, ahead of the probe commit). Exactly one symmetrization was
  ever adopted; the `S_A` average is reported as a labelled counterfactual and
  selects nothing. No symmetrization was tried and discarded — the forbidden
  seventh-ansatz failure mode.
- `free_parameters = 0`. **No AME quantity and no `g₂` appears anywhere in this
  audit's compute** — not even as a post-hoc comparison, because no value is
  claimed.
- `q₀` = **experimental proton anchor** (`qou_substrate.constants`, owner directive
  2026-08-07); `y_λ` from the live `y_lambda_at_q0_mpmath` closed form, **never** the
  muon-built cache; layer-pure, no straddling. The pin is recorded in the witness
  and is **material** (the `A ≥ 3` germ is `q`-dependent, #4849 §5.2).
- Arithmetic: float64 sweep, mpmath 40-dps re-run of Part B at `n = 6` as the null
  control; the measured effect exceeds the float64 floor by `9.7e13 ×`.
- Run cost: 162 s, single process. No long-compute logging discipline needed.
- Lean sorry-free, `#print axioms` clean on all 8 declarations.
- Bean `qou-prjo` stays **OPEN**. This dissolves one blocker; it closes no
  magnitude.
