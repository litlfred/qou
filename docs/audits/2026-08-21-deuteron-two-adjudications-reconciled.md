# Deuteron: reconciling the two adjudications of 2026-08-21

**Date:** 2026-08-21 · **Branch:** `claude/deuteron-frame-reconciliation-2026-08-21`
**Reconciles:** [`2026-08-21-deuteron-w3-knot-identity-adjudicated.md`](2026-08-21-deuteron-w3-knot-identity-adjudicated.md) (**A**, commit `f264ebbabf`)
and [`2026-08-21-deuteron-knot-assignment-adjudication.md`](2026-08-21-deuteron-knot-assignment-adjudication.md) (**B**, PRs #5350 / #5363).
**Tier:** audit-only. No witness written, no producer re-run, nothing wired.
**Arithmetic:** exact integers throughout (permutation cycle counts). No float entered any conclusion.

## 0. BLUF

**A and B are compatible as *measurements* and incompatible as *verdicts*, and the
incompatibility is localised to exactly one step — A's identification of the
deuteron's `T_w` word.**

1. **A's rule is right.** "The canonical knot is the braid-closure of the `T_w`
   word, not the volume-match" is the registry's own `principled-derivation`
   tier, quoted correctly.
2. **A's words are not the deuteron's.** A applies that rule to `σ₁³` and to
   `σ₃²`. Measured against the content layer: **`σ₁³` is the *electron's* word**
   — the registry's own `principled-derivation` example — and **`σ₁²`/`σ₃²` is
   the *gluon* and the *binding link*, named as such in the same registry
   paragraph. Neither is the deuteron atom's `T_w`.
3. **B's word is the deuteron's `T_w`.** It is what the mass/trace chain
   consumes, from two independent producers.
4. **The crux — A's rule applied to B's word does not fail, it redirects.**
   It returns **a 3-component link**, which excludes *all three* of A's
   candidates, including the two A endorsed. So A's tie-breaker, applied
   faithfully, refutes A's own conclusion.
5. **New, and the reason this is a reconciliation rather than a stalemate:**
   the corpus's *only* principled selector — the R5-full canonical-knot SDP —
   returns a deuteron winner that **also closes to a 3-component link**, as do
   **all 8** of its top-`k` candidates and **all 8** of its PSD-feasible top-`k`.
   The independent-arity agreement between the `H₆` mass word and the `B₃` SDP
   winner is the one measured bridge between the frames.
6. **Verdict.** B's `UNDETERMINED` stands and is *sharpened*: the question is
   not "which of these three", it is "which 3-component link", and the SDP
   already returns a candidate. A's `6₂` elimination survives fully and is the
   part both adjudications agree on. A's `Vol(deuteron) = 0` conclusion does
   **not** survive.

---

## 1. Four frames, and which object each names

The corpus does not have three assignments to one object; it has four frames.
B established this. What is added here is the **`T_w` word each frame actually
supplies** and its **measured arity**.

| # | frame | strands | the deuteron's word | closure | what the object *is* |
|---|---|--:|---|--:|---|
| 1 | **constituent / mass chain** | `H₆` (`3A`) | 23 letters, `p · I_pn · n` | **3 comp** | the object `tr_M`, `χ_λ`, `Δ_λ` consume |
| 2 | **atom knot / SDP** | `B₃` (`n₀ = 3`) | `[1,2,2,2,2,2,2,−1]` (R5-full winner) | **3 comp** | `knot_name` slot of the registry |
| 3 | **coordination / binding** | nucleon-level | `σ₃²` ≅ `σ₁²` (Hopf `L_H`) | **2 comp** | `binding_link_name` — the inter-nucleon *operator* |
| 4 | **channel** | `B₂` | `σ₁³` (trefoil) | **1 comp** | see §3 — **not the deuteron in the content layer** |

A ruled between frame 4 (its "Δ_λ frame") and frame 3 (its "coordination
frame"), and eliminated the historical `6₂` which lives in frame 2. **Frame 1 —
the frame the mass chain runs in — is absent from A entirely.**

---

## 2. Frame 1 measured: the two producers, and what they actually emit

Both producers were reconstructed from source and evaluated with integer
arithmetic only. `_proton_body` / `_neutron_body`
([`sublemma_2_1_h9_tritium_verify.py:61,76`](../../computations/sublemma_2_1_h9_tritium_verify.py))
through `hecke_word_to_braid_word`
([`atom_braid_words.py:44`](../../computations/atom_braid_words.py)):

```
P = [1, -2, 1, -2, 1, -2, 1, 1,  2, 1, 1]     (11 letters)
N = [1, -2, 1, -2, 1, -2, 1, 1, -2, 1, 1]     (11 letters)
D = P · [3] · shift(N, 3)                      (23 letters, H_6)
```

| producer | `|gen|` multiset | closure on 6 strands | cycles |
|---|---|--:|---|
| [`delta_lambda_jsj_phase3.load_atom_braids()["D"]`](../../computations/delta_lambda_jsj_phase3.py) **as coded** | `{1:11, 2:4, 3:1, 4:7}` | **3** | `(1)(2345)(6)` |
| same, sign-corrected (bean `qou-yaqm`) | `{1:7, 2:4, 3:1, 4:7, 5:4}` | **3** | `(1)(234)(56)` |
| [`mass_at_3A_proper.atom_braid_word_3A(1,1)`](../../computations/mass_at_3A_proper.py) (run directly) | `{0:7, 1:4, 2:1, 3:7, 4:4}` 0-indexed | **3** | `(12)(345)(6)` |

**Correction to a natural reading of B §1D/§2.** The two producers are **not the
same braid word**. They emit the **same letter multiset** but in a **different
order** — `atom_braid_word_3A` groups per generator
(`σ₀⁷ σ₁⁴ σ₂ σ₃⁷ σ₄⁴`), `load_atom_braids` interleaves
(`σ₀σ₁σ₀σ₁…`). They therefore induce **different permutations**
(`(12)(345)(6)` vs `(1)(234)(56)`) that happen to have the **same cycle count**.
B's arity conclusion is unaffected; the "one word" reading is not exact.

**All 32 resolutions of the 5 non-braid letters give component count `[3]`** —
re-measured here, confirming B §2, and now covered by the sorry-free Lean
`QOU.BraidsAndKnots.wordPerm_eq_of_indices_eq` / `closureComponents_ne_of_perm_ne`
landed on `main` at `01a4dd3bb6`.

### 2a. Frame 1 does **not** descend to frame 3 — measured

Whether the coordination frame is a *quotient* of the constituent frame is
decidable, and the answer is no:

> The closure permutation of the deuteron mass word **does not preserve the
> `{1,2,3} ⊔ {4,5,6}` nucleon partition.** Its middle component —
> `(2,3,4)` sign-corrected, `(2,3,4,5)` as-coded — **visits both nucleons**.

So the single interface letter `σ₃` links one strand of the proton to one strand
of the neutron; it is not a crossing of two *cables*, and there is no
strand-collapse under which frame 1 pushes forward to a nucleon-level braid.
**Frames 1 and 3 are not related by a map.** They are separate models sharing an
intent. (This is also why frame 3's `σ₃²` — two crossings — cannot be recovered
from the mass word's single `m_pn = 1` interface letter; B §1A Note 2 records
the 1-vs-3 crossing ambiguity, and this is a third value.)

---

## 3. A's frame 4 is the electron's word — the finding neither adjudication has

A's candidate (a) is *"Δ_λ / octahedral frame: `σ₁³` closes to the trefoil"*.
B scoped this to *"the **pn channel** word, not the atom"*, citing one probe.
The content layer is stronger and unanimous — **`σ₁³` is the electron**:

| site | says |
|---|---|
| [`recursive-atom-knot-atlas-registry.md:11`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md) | `principled-derivation` example: **electron** `σ₁³ → 3₁` |
| [`recursive-atom-knot-atlas-registry.md:49`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md) | *"Used for: the **electron** (e⁻), and as the nucleon binding factor in `H₃`"* |
| [`recursive-atom-knot-atlas-registry.md:234`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md) | table row: Trefoil `3₁` \| `σ₁³` \| **electron** |
| [`fundamental-knots-operator-basis.md:6`](../../content/quantum-observable-universe/braids-and-knots/fundamental-knots-operator-basis.md) | electron `e⁻` \| trefoil \| `σ₁³` |
| [`confined-particle-examples.md:8`](../../content/quantum-observable-universe/knots-particles-confinement/confined-particle-examples.md) | *"`electron`: ℓ = 1, n₀ = 2, `[K]_M = [σ₁³]`"* |
| [`atom-knot-mass-derivation-table3-data.md:6`](../../content/quantum-observable-universe/mass-theory/atom-knot-mass-derivation-table3-data.md) | electron \| `σ₁³ = T_{2,3}` |
| [`lepton-bring-surface-h3-3channel.md:17`](../../content/quantum-observable-universe/mass-theory/lepton-bring-surface-h3-3channel.md) | *"the electron `σ₁³`"* |

Against that, "the deuteron's word is `σ₁³`" appears **only** in one directory —
eight sibling probes under `computations/deltalambda/` — every one of which
traces the claim to **"#4158"**. Corpus-grepped: all twelve in-tree references to
`#4158` are about the **Magnus / bar-parity `g₂`** route
(`octahedral_barsplit_convergence_probe.py:10,63-65`,
`deuteron_r_is_binding_residual_probe.py:7,123,142`,
`deuteron_binding_frame_independent_probe.py:161`). **None of them identifies a
knot.** So `deuteron_octahedral_gluing_probe.py:7` — *"The deuteron braid word is
`σ₁³` (#4158)"* — cites a PR for a claim its other citations never make, and the
assertion then propagated across the directory by copy.

**Scope-(a).** This does not show the trefoil is *not* the deuteron's; it shows
the corpus contains **no derivation** that it is, and contains seven blocks
asserting the same word belongs to a different particle. Registry:49's third
role — *"the nucleon binding factor in `H₃`"* — makes `σ₁³` a **three-role
symbol**, which is the AGENTS.md §"attributes do not transfer across overloaded
symbols" failure mode.

**Consequence for A.** Both of A's principled readings supply an object the
registry assigns to something else: `σ₁³` → electron (frame 4), `σ₁²` → gluon
and binding link (frame 3). A's tie-breaker is correct and is applied to the
wrong inputs, twice.

---

## 4. The crux — A's rule applied to B's word

A's tie-breaker, verbatim: *"the canonical rule is braid-closure of the `T_w`
word, not volume-match."* B's finding: the mass chain's `T_w` word closes to a
3-component link.

**Applying A's rule to the `T_w` word the mass chain actually uses:**

| A's candidate | components | verdict under A's own rule |
|---|--:|---|
| trefoil `T(2,3)` (A's (a), endorsed) | 1 | **excluded** |
| Hopf `L2a1` (A's (b), endorsed) | 2 | **excluded** |
| census `6₂` (A's (c), rejected) | 1 | **excluded** — same ground, plus §5 |
| *the actual closure* | **3** | the rule's answer |

**Scope-(b) structural exclusion**, on the elementary fact that a braid
closure's component count is the orbit count of the induced permutation, hence
a function of the crossing *indices* alone. The **resolution-independence** of
that count is Lean-proved sorry-free —
`QOU.BraidsAndKnots.wordPerm_eq_of_indices_eq` → `closureComponents_resolve`
(`main` `01a4dd3bb6`, `lean`-direct exit 0, no `sorryAx`). So the exclusion
holds for every resolution of the 5 non-braid letters and every crossing
convention; it is not a numerical near-miss. **See §5e — the Lean carries the
resolution-independence, not the link-level exclusion, and an earlier draft of
this section cited it for both.**

### 4a. Both readings of "the `T_w` word" give 3 — the argument does not turn on which

A's tie-breaker cites **two** sources for its rule: the registry's
`principled-derivation` tier (which is about braid words in `H_{n₀}(q₀)`) and
`r5_full_canonical_knot_solver.py` / `prop:atom-knot-mass-derivation` (which
selects `T_w` by the joint PSD-feasibility + binding SDP, in `B₃`). Those are
two different objects, so "the `T_w` word" admits two readings. **Both give the
same arity:**

| reading of "the `T_w` word" | the word | strands | components |
|---|---|--:|--:|
| the mass chain's Hecke word (`H₆`) | 23 letters | 6 | **3** |
| the SDP-selected `T_w` (`B₃`) | `[1,2,2,2,2,2,2,−1]` | 3 | **3** |

So the exclusion in the table above does not depend on resolving which `T_w` A
meant. Under either reading, A's rule returns a 3-component link and excludes
all three of A's candidates. This is what makes the disagreement resolvable
rather than a standoff between two defensible frames.

**So A's tie-breaker does not survive as an argument for `Vol = 0`.** It survives
as a *rule*, and the rule's own output is "a 3-component link" — an answer A did
not consider and B reached from the other side.

---

## 5. What survives — and the one thing both adjudications agree on

### 5a. `6₂` is eliminated. Verified, on three independent grounds.

This is the part of A that is fully sound, and B reaches the same place by a
different route. Re-verified here from the sources:

1. **Tier.** [`recursive-atom-knot-atlas-registry.md:13,73`](../../content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas-registry.md):
   `²H = 6₂` is `manual-historical-volume-match`, defined as *"the GB-NF
   derivation in `H_{n₀}(q₀)` has **not been computed yet**."* Not a derivation
   by the registry's own definition.
2. **SDP-infeasible.** [`r5-full-canonical-knot-solver.witness.json`](../../computations/r5-full-canonical-knot-solver.witness.json)
   `per_atom_results[0].historical_cross_check`, read directly:
   `psd_feasible: false`, `alpha_gap: 0.890510299676959`,
   `rank_in_full_search: 1075`, `rel_residual: 0.735`,
   `winner_matches_historical_class: false`. A's figures are exact.
3. **AME-inverted, self-declared in production source.**
   [`mass_table_ppb.py:19-21`](../../computations/mass_table_ppb.py): *"that IS a
   form of AME-driven fitting (we picked the knot whose volume is closest to
   `B_AME/ρ`)"*; [`2026-05-24-rule14-atom-knot-census.md`](2026-05-24-rule14-atom-knot-census.md)
   §1: *"**This is empirical fitting**"*, §2: *"no canonical `(Z,N) ↦ K_census`
   functor … the census assignments are scaffolding."*

Ground 3 is B's; grounds 1 and 2 are A's. They are independent and all three
hold. **`6₂` is out.** Add the arity ground from §4 and it is out four ways.

### 5b. New: the SDP and the mass chain agree on arity

Not in A, not in B. Read directly from the R5-full witness and evaluated by
exact cycle count:

| | word | strands | components |
|---|---|--:|--:|
| **deuteron SDP winner** | `[1,2,2,2,2,2,2,−1]` | 3 | **3** |
| all 8 `top_k_candidates` | — | 3 | **3** (all) |
| all 8 `psd_feasible_subset.top_k` | — | 3 | **3** (all) |
| historical `6₂` | `[1,−2,1,1,1,−2]` | 3 | 1 · `psd_feasible: false` |
| **deuteron mass word (`H₆`)** | 23 letters | 6 | **3** |
| ³He SDP winner | `[1,1,1,1,1,1,2,2]` | 3 | **3** |
| ³He historical `L6a4` | `[−1,2,−1,2,−1,2]` | 3 | **3** · `psd_feasible: true` |

Two things follow.

- **The arity agreement is not forced.** Over all `2⁸ = 256` index sequences of
  length 8 in `B₃` (signs are irrelevant to the count), **86 give 3 components
  and 170 give 1** — exactly `43/128 ≈ 33.6 %`. So "all 8 top-`k` are
  3-component" is a real feature of the selected set, not an artifact of the
  word length. (Stated as a base rate, not a significance test — the top-`k` are
  ranked by a cost that is itself word-dependent, so they are not independent
  draws.)
- **³He is the corroborating case.** It is the one atom whose historical
  assignment is PSD-feasible, and it is also the one whose historical assignment
  matches the SDP winner's arity. The deuteron's `6₂` fails both together.

This is the measured bridge between frames 1 and 2: **no map is exhibited, but
the two frames' arities agree, and they agree on a value that a third of the
search space would have given by chance.**

### 5c. Disposition of each claim

| claim | source | status |
|---|---|---|
| canonical rule = braid-closure of `T_w`, not volume-match | A | **survives** — and is the right rule |
| `6₂` is non-canonical | A + B | **survives**, four independent grounds |
| `6₂` is SDP-infeasible, `α_gap` 0.89 | A | **verified exact** |
| `6₂` is AME-inverted | B | **verified**, self-declared in production source |
| mass word closes to 3 components, all 32 resolutions | B | **verified exact**; Lean-proved on `main` |
| all three candidates arity-excluded | B | **survives** (scope-(b), invariant cited) |
| `Vol(deuteron) = 0` is canonical | A | **does not survive** — both supporting words are other objects (§3) |
| deuteron's word is `σ₁³` | A, via 8 `deltalambda` probes | **unsupported** — cites #4158, which is about `g₂`; content layer says electron (§3) |
| frames 1 and 3 related by nucleon collapse | implicit in A | **refuted** (§2a, measured) |
| verdict `UNDETERMINED` | B | **survives, sharpened** — the class is 3-component links, and the SDP returns one |

### 5e. Scoping the Lean citation — and correcting my own over-reach

**Self-correction.** §4 above, this branch's PR body, and the coordination
comments I posted on #5389 and #5363 all cite
`closureComponents_ne_of_perm_ne` as the invariant that **excludes** `6₂`,
the trefoil and Hopf as the mass word's closure. Read against the actual Lean
([`ClosureComponentsSignInvariant.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ClosureComponentsSignInvariant.lean)),
**that citation is one step wider than the theorem.** Per AGENTS.md
§"Grep the claim SHAPE, not only the topic" — resolve the symbol, read the
type — the file's contents are:

```lean
noncomputable def closureComponents (π : Perm (Fin n)) : ℕ :=
  Nat.card (MulAction.orbitRel.Quotient (Subgroup.zpowers π) (Fin n))

theorem closureComponents_ne_of_perm_ne {π π' : Perm (Fin n)}
    (h : closureComponents π ≠ closureComponents π') : π ≠ π'
```

Three things follow, and they should be kept apart:

1. **What is proved.** `closureComponents` is the **orbit count of a
   permutation**. `wordPerm_eq_of_indices_eq` → `wordPerm_resolve` →
   `closureComponents_resolve` prove that this count is **independent of every
   crossing sign and every resolution**. That is real content and it is the
   half the "all 32 resolutions" claim needs. Nothing in the file mentions a
   link.
2. **What `closureComponents_ne_of_perm_ne` actually concludes** is `π ≠ π'` —
   **distinct permutations**, not distinct *links*. It is the contrapositive of
   a congruence and carries no topology. It is therefore **not** the exclusion
   step; it is the bookkeeping around it.
3. **The step that does the excluding is not in the Lean.** "The closure of a
   braid has as many components as the induced permutation has orbits" is
   stated in the file's **docstring prose** (*"the strands `Fin n` fall into
   components exactly as they fall into orbits of `⟨π⟩`, since the closure
   joins strand `i` to strand `π i`"*) and is a modelling bridge, not a
   theorem. It is elementary, standard (Birman), and I do not doubt it — but it
   is asserted, not formalised.

**Does the verdict move? No.** The bridge is a textbook fact about braid
closures, so the arity exclusion of §4 stands on ordinary mathematics. What
changes is only the **strength of the citation**: the correct form is

> **scope-(b), on the elementary fact that a braid closure's component count is
> the orbit count of the induced permutation — with the *resolution-independence*
> of that count Lean-proved sorry-free** (`closureComponents_resolve`,
> `wordPerm_eq_of_indices_eq`).

not "Lean-proved that `6₂` is excluded". The Lean prunes the *convention*
degree of freedom, which is exactly what a formalize-first prune should do and
is why the 32-resolution enumeration was replaceable; it does not by itself
carry the link-level exclusion. B §3 Ground 1 states this correctly on its own
terms (*"that invariant is elementary and convention-free"*) — the over-reach
is mine, introduced in §4 of this document, and is corrected here rather than
silently edited away.

**Verification performed** (CI is `workflow_dispatch`-only; this is the agent
gate). `lean`-direct against the restored Mathlib olean tree, no `lake build`:

```
lean ClosureComponentsSignInvariant.lean        -> exit 0, no diagnostics
#print axioms wordPerm_eq_of_indices_eq          -> [propext, Quot.sound]
#print axioms wordPerm_resolve                   -> [propext, Quot.sound]
#print axioms closureComponents_resolve          -> [propext, Classical.choice, Quot.sound]
#print axioms closureComponents_ne_of_perm_ne    -> [propext, Classical.choice, Quot.sound]
#print axioms braidClosureComponents_resolve     -> [propext, Classical.choice, Quot.sound]
```

No `sorryAx`. Mathlib olean count `6990` before and `6990` after — the restored
tree was not evicted.

### 5d. What is *not* disturbed

A's Lean citation `QOU.MassTheory.deuteron_volume_leg_eq_zero`
(`BlochVolumeLegFlatVanishing`, sorry-free) is a theorem about **real shapes**,
not about the trefoil, and B §4(b) already records that it holds for every
tetrahedron count. It is true regardless of which link the deuteron is; only its
*physical labelling* moves. Likewise the `σ₁³` Lean cone
(`TrefoilColoringBarEven`, `PinchedOctahedronDegenerate`,
`RogersDilogInflection`, `TransverseSurfaceCurvature`,
`GermRootVectorGaugeFixing`) states facts **about `σ₁³`** that are true whoever
`σ₁³` belongs to. Nothing proved is retracted here.

---

## 6. Answering the four questions put to this reconciliation

1. **Genuinely different words, or is one wrong?** Genuinely different *frames*,
   and A's word is misattributed. Frame 1's word (B's) is the mass chain's
   `T_w`, verified from two producers. Frame 4's `σ₁³` (A's) is the electron's
   word in seven content-layer sites and has no derivation as the deuteron's.
2. **If both frames are legitimate, name the map — or record that none exists.**
   Frames 1 and 3 (**mass chain ↔ coordination**): **no map exists**, measured —
   the closure permutation does not preserve the nucleon partition (§2a).
   Frames 1 and 2 (**mass chain ↔ atom-knot SDP**): **no map is exhibited**, but
   their arities agree at 3 against a `43/128` base rate (§5b). Frame 4 is not
   the deuteron in any of them.
3. **Does A's tie-breaker survive B's finding?** The **rule** survives; the
   **conclusion** does not. Applied to B's word it returns a 3-component link,
   excluding both of A's endorsed candidates (§4).
4. **What survives regardless?** The `6₂` elimination — verified on three
   independent grounds plus arity (§5a). It is the one thing both adjudications
   agree on, and it is sound.

---

## 7. Next steps (not executed here)

The two adjudications converge on B §5 item 3, which is now the only live
direction: **search the 3-component slice.** The R5-full SDP already returns
3-component candidates from `B₃`, so the cheapest next step is not a census
search — it is to ask whether the SDP winner `[1,2,2,2,2,2,2,−1]` and the `H₆`
mass word are related by anything beyond arity (Markov trace, HOMFLY, Wedderburn
content). That is a comparison between two objects the corpus already has.

**Explicitly not a determining experiment**, restating B: any procedure that
ranks candidates by agreement with `B_AME`. That is how `6₂` got here.

## 8. Reproduction

Exact integer arithmetic only; component counts are cycle counts of the induced
permutation. `atom_braid_word_3A(1,1)` was run directly from the tree; the R5-full
figures are read from the committed witness. No witness was written or
regenerated, no producer re-run. Script:
[`computations/probes/deuteron_frame_arity_reconciliation.py`](../../computations/probes/deuteron_frame_arity_reconciliation.py).

## 9. Beans

- `qou-e5jf` (B) and `qou-985x` (A) — both are about this question; §5c is the
  merged disposition.
- **New:** the `σ₁³` three-role symbol collision (electron / deuteron / nucleon
  binding factor in `H₃`) and the unsupported `#4158` citation across eight
  `deltalambda` probes.
- **New:** frames 1 and 2 agree on arity — the comparison in §7.
