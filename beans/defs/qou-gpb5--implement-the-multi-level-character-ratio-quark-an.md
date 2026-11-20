---
# qou-gpb5
title: 'Implement the multi-level character ratio: quark and nuclear-jet levels are unbuilt'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T06:49:42Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-10v9
---


Opened 2026-09-05. The **nucleon level is now implemented**
(`the_character_ratio_derivation_path_is_the_bond_model_probe`, 3/3); this bean
is the two levels that are not.

## What the specification says

`prf:confined-knot-binding`: "the character ratio measures the volume departure
from the free constituents. The total knot factor multiplies these strict,
empirically-independent character ratios **across all levels**." It names three:
**quark, nucleon, and nuclear jet**.

`hecke_core_legacy.knot_factor` concedes it does not run this: "the per-level
character ratio (nucleus/free-nucleon product) and confined-state accumulation
provide the categorical derivation path. **Currently using the product formula
for A<=4 and generic for A>=5.**"

## What implementing the nucleon level established

The character ratio `R = tr_M(nucleus)/tr_M(free constituents)` on the canonical
word, exact at 200 bits, **equals `exp(-L)` to the working floor**. So the
specified path and the bond model are the same object, and retiring the
knot-selection routes leaves no second unfitted channel in reserve.

| atom | R | B = -alpha log R | B_AME | error |
|---|---|---|---|---|
| 2H | 0.508229789377 | 2.8332 | 2.224566 | +27.36 % |
| 3H | 0.205135640449 | 6.6309 | 8.481796 | -21.82 % |
| 3He | 0.311386312073 | 4.8839 | 7.718041 | -36.72 % |
| 4He | 0.125684152895 | 8.6817 | 28.295662 | -69.32 % |

And the hardcoded factor is **not an approximation** to it: `1 - h^2 = 0.9563`
against a true ratio of `0.2051` / `0.3114`, and `(1-h^2)^2 = 0.9145` against
`0.1257` — off by 4.7x, 3.1x and 7.3x.

## Why the missing levels matter

Every character ratio is `< 1`, so multiplying in further levels drives `R`
**down** and `B = -alpha log R` **up**. The nucleon level alone leaves `4He` at
`-69 %`, i.e. short. So the missing levels move it in the right direction. That
is a direction and not a prediction, and nothing measured estimates their size —
this bean exists to find out, not to assume.

- [ ] Establish whether the quark level has a computable word at all. The
      substrate has quark-level structure (three strands per nucleon), so the
      "free constituents" at that level may be the three free quark strands and
      the "nucleus" the intra-nucleon word. If so it is the SAME engine with
      `include_inter=False` at one level down, and is cheap.
- [ ] Same question for the nuclear-jet level.
- [ ] If both are computable, multiply the three ratios and report. Do NOT tune
      anything: if the product overshoots or undershoots, that is the answer.
- [ ] If they are not computable, say so plainly and close. The specification
      would then name levels the framework cannot evaluate, which is itself the
      finding.

## Discipline

No fitting. This is the only unfitted binding route left after the 2026-09-05
ruling, and its value is precisely that it is unfitted — a number obtained by
computing beats a better number obtained by selecting. If the three-level
product misses, record the miss.

## Worked 2026-09-05 — the quark level HAS a word, but not a unique one

Owner: "It should be by definition almost. It goes through Gamma Gamma
production starting from photons to get to a quark."

### The word exists, and the corpus already derives it

`quark-antiquark-production-reduction` gives it step by step. Two coloured
photons `gamma = 1 + phi_0 sigma_0 + phi_1 sigma_1 + phi_01 sigma_0 sigma_1`
collide; their product in `H_3(q)` yields Hopf terms `L_+`, `L_-` from
cross-colour products; and

    NF(L_+ . e^-) = sigma_1 + h L_+ + h L_- + h^2 e^-

whose dominant output `sigma_1` is "the hadronic crossing that becomes the up
quark". Three independent productions give three quarks, "confined by the
Borromean braid `B_3`".

So per nucleon the quark-level word is the **intra word on generators
`(3k, 3k+1)`**, i.e. `H_3`, and the free constituents are the bare three
strands. That is exactly the owner's "by definition almost".

### Two checks that make the level well-posed

- `tr_M(1) = 1` on every `H_n` (verified `n = 2, 3, 6, 9, 12`), so "free
  constituents = identity" needs no normalisation and `R_quark = tr_M(intra)`.
- The split union factors **exactly**: `tr_M(p on H_3) * tr_M(n on H_3)` equals
  `tr_M(p ⊔ n on H_6)` to the working floor (`0.629328402203 *
  0.475133517156 = 0.299015017185`). So free constituents compose correctly.

### The blocker: the intra ordering is not unique, and two live paths disagree

The same 22-letter multiset per nucleon pair appears in two orders:

    A) atom_braid_word_3A / atom_canonical_crossings : GROUPED     [0,0,0,0,0,0,0,1,1,1,1,...]
    B) atom_gen_chains / E.nucleon_word              : INTERLEAVED [0,1,0,1,0,1,0,0,1,0,0,...]

Generators 0 and 1 are **adjacent**, so they do not commute, and the traces
differ:

    atom    tr(intra) A      tr(intra) B      ratio
    2H      1.131716904322   0.299015017185   3.785
    3H      1.117846228978   0.142072056797   7.868
    3He     1.296675612245   0.188178642999   6.891
    4He     1.280783151529   0.089409980502   14.325

This is `qou-bygw`'s ordering ambiguity again, one level down, and it is worse:
it moves **every absolute trace in the corpus**, not just the all-pairs ones.

### What survives, and it is the important part

**The character RATIO is invariant under the intra ordering.** For `2H`,
`0.575172/1.131717 = 0.151968/0.299015 = 0.508230` exactly. The numerator and
denominator both move by the same factor, so `R_nucleon = tr(full)/tr(intra)`
does not. The bond model `L = -log R` is therefore safe; the individual levels
are not.

**But the multi-level product is not invariant.** It telescopes to
`R_quark * R_nucleon = tr_M(full)/1 = tr_M(full)`, which IS ordering-dependent.
So the three-level character ratio the specification calls for is not well
defined until the intra ordering is fixed.

### Correction to this bean's own earlier claim

It asserted "every character ratio is `< 1`, so the missing levels push `B` up".
Wrong on the numbers: `R_quark` is `0.6293` (proton) and `0.4751` (neutron) per
nucleon, but the multi-nucleon `tr(intra)` under ordering A exceeds 1
(`1.1317` at `2H`), so the direction depends on the ordering too. The
three-level `B` under ordering A: `2H +4.07 %`, `3H -27.32 %`, `3He -50.81 %`,
`4He -72.98 %` — i.e. worse than nucleon-level alone at `A >= 3`, not better.
The hand-waving direction argument was wrong and is withdrawn.

- [x] Establish whether the quark level has a computable word — **yes**, via
      gamma-gamma production, and it is the intra `H_3` word.
- [ ] **NEW BLOCKER, and it is prior to everything else:** fix the intra-word
      ordering. Two live production paths disagree by up to 14x on `tr(intra)`.
      Until that is settled no absolute trace in the corpus is well defined, and
      the multi-level product cannot be evaluated. Ratios are unaffected.
- [ ] The nuclear-jet level, untouched.

## BLOCKER CLEARED (2026-09-05), and the multi-level product is now MEASURED

The intra-ordering blocker is settled by `qou-hu1f`: the **interleaved**
`(σ₀σ₁⁻¹)³` *is* `β_Bor`, matched against the Lean closed form
`(4+h²−3h⁴−h⁶)/(h²+4)` to `5e-60`; the grouped `σ₀³σ₁⁻³` that
`atom_braid_word_3A` actually builds is `82 %` away. That is a measurement, not
an authoring call, and it agrees with the derivation this bean was opened on —
`quark-antiquark-production-reduction` says the three quarks are "confined by
the Borromean braid `B₃`", so the quark level's word is forced.

Probe: `the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py`
(9/9). Its grouped rebuild reproduces `atom_braid_word_3A`'s own trace to
`1e-60`, so every figure below is against production rather than a model of it.

### This bean's invariance claim is CORRECT, and now holds at every A

It asserted "the character RATIO is invariant under the intra ordering" from
`2H` alone. On the canonical chain it holds at `A = 2, 3, 4` to `~1e-60`:

    atom   R_nucleon (both orderings)   |diff|
    2H     0.508229789376739            1.2e-60
    3H     0.205135640448650            9.3e-61
    3He    0.311386312072596            6.2e-61
    4He    0.125684152895266            4.7e-61

and equals `∏ᵢ(z + dᵢ)` under **both**. The mechanism is connected-sum
multiplicativity, which is blind to letter order inside a summand. So `L`, the
three bond constants and every log-ratio binding number **cannot** move.

Caveat on scope: this is the CHAIN. The bean's earlier table was computed on the
all-pairs word, which is a different object and retired as ill-posed
(`qou-bygw`); its ratios are not invariant and are not re-tested.

### THE ANSWER — two-level character ratio, unfitted

`R_quark · R_nucleon` telescopes to `tr_M(W_atom)`, so `B = −α log tr_M(W_atom)`:

    atom   B interleaved (correct)   B grouped (live)   B_AME
    2H      7.8867  (+254.53 %)      2.3152  (+4.07 %)   2.224566
    3H     14.7996  ( +74.49 %)      6.1646 (−27.32 %)   8.481796
    3He    11.8760  ( +53.87 %)      3.7963 (−50.81 %)   7.718041
    4He    18.7888  ( −33.60 %)      7.6457 (−72.98 %)  28.295662

**It does not work.** It overshoots `2H` by `3.5×` and is worse than the grouped
word at every `A < 4`. Recorded as the answer, not repaired — the grouped
column's `+4.07 %` at `2H` is agreement produced by a word that is not `β_Bor`,
which is exactly what the 2026-09-05 no-fitting directive rates below an honest
miss. Nothing here was tuned.

### The direction argument this bean already withdrew stays withdrawn

Both `R_quark` values are `< 1` per nucleon under the correct ordering
(`0.299` at `2H` … `0.089` at `4He`), so the second level does push `B` **up** —
and that is precisely why it now overshoots at low `A`. "Up" was never the
useful question.

- [x] Quark level has a computable word — **yes**, and it is `β_Bor`.
- [x] Intra-ordering blocker — **cleared** (`qou-hu1f`, Lean-verified).
- [x] Multiply the ratios and report — **done, above. It misses.**
- [ ] The nuclear-jet level, still unbuilt. Two of the three levels the
      specification names are now computed; the third has no word, and if it
      turns out to have none, "the specification names a level the framework
      cannot evaluate" is the finding.

## THE NUCLEAR-JET LEVEL: ANSWERED (2026-09-05). All three levels are now accounted for.

Probe: `the_nuclear_jet_level_is_the_retired_all_pairs_object_probe.py`, 8/8.

### It HAS a word — and I nearly filed "it has none"

Grepping the corpus for "nuclear jet" returns exactly **one** sentence, the one
in `confined-knot-binding` that names the three levels. On that evidence the
finding this bean predicted — "the specification names a level the framework
cannot evaluate" — looked confirmed.

It is defined, in two blocks sitting **immediately after** `confined-knot-binding`
in the same section, under a name the phrase does not contain:

- `conj:jet-filtered-knot-factor` gives the **word**: `a(Z,N)` is the Jones
  polynomial of the *nuclear quotient braid*, which "tracks exclusively the
  `A(A-1)/2` inter-nucleon crossings, suppressing internal nucleon structure".
- `conj:jet-convergence-classical-limit` gives the **weights**:
  `W_λ = d_q(λ)²/[3]_q!`, exact at `k = 3`.

One more grep spelling and I would have published the wrong finding. Recording
that because it is the same blind-spelling failure `qou-5pgl` warns about, and
the search that found it was structural (read the section's block list) rather
than lexical.

### Obstruction 1 — the word is the retired all-pairs object

`A(A-1)/2` crossings is a **multiset**; a link needs a **word**, and
non-adjacent pairs need bands that do not commute with what they span.
Enumerated on the quotient braid itself (`A` strands, not the `3A`-strand word),
over every pair ordering and both resolutions of the averaged `pn` letter:

    3H    A=3    12 orderings  ->   4 distinct Jones polynomials
    3He   A=3    12 orderings  ->   4 distinct
    4He   A=4  1440 orderings  ->  30 distinct

So `a(Z,N) = J_β̄(q)` is **not a function of `(Z,N)`**. This is `qou-bygw`
exactly, arriving as the *definition* of the third level.

### Obstruction 2 — the weights are a different family from the other two levels

Quark and nucleon are Markov traces: `y_λ`, convention D, `≤ 2` rows only. The
jet blocks specify `w̃_λ = d_q(λ)²/[n]_q!` over **all** partitions. On `H_3`:

    λ           y_λ (D)                w̃_λ
    (3)         0.505404226503931      0.163383228056257
    (2,1)       0.247297886748035      0.660673773661173
    (1,1,1)     0                      0.163383228056257

`Σ dim·y = 1` exactly; `Σ w̃ = 0.98744`. The `(1,1,1)` row is structural —
convention D is the `sl₂` point of the Ocneanu family, so `y_λ = 0` beyond two
rows, while `w̃` is a ratio of positive quantum integers. **The jet measure
charges a block the Markov trace annihilates.**

Corroborated by the corpus, not just by me: `prop:wedderburn-weight-canonical`
tabulates `y^D(q₀) = 0.24729789` against `w̃(q₀) = 0.66067377` at `(2,1)` — the
same two numbers — and states they are distinct families on every stratum.

### And they disagree qualitatively about the pn bond

    tr_M(σ + d_pn) under y   = 0.508229789376738963   (= z + d_pn)
    the same letter under w̃  = 0.000071511999728866   — 7107x smaller

`w̃` weights the two `H_2` blocks equally and `d_pn` is their midpoint up to `δ`,
so the `pn` letter is `w̃`'s **near-null vector**: `w̃·(h + 2d_pn) = w̃·h·δ/2`.
The `pn` bond is the one the binding arc turns on, and the two families do not
agree on whether it is `0.51` or `0.00007`.

### Where the level IS evaluable, it contributes 1

At `A = 2`, `A(A-1)/2 = A-1 = 1`: one crossing on two strands, no ordering to
choose. Its closure is the **unknot**, `J = 1`, for every bond type and both
averaged resolutions. So the jet level multiplies the deuteron's knot factor by
exactly `1`.

- [x] The nuclear-jet level. **It has a word; the three-level product is not
      evaluable as specified.** Two independent obstructions, either sufficient.

### What this closes, and what it does not

`prf:confined-knot-binding`'s multi-level product is closed as a *derivation*:
it cannot be evaluated as written. Combined with the earlier result that the
two-level product misses badly (`2H +254.53 %`, `4He −33.60 %`), the
character-ratio route does not produce binding.

Not retracted: both jet blocks are **Conjectures**, and a conjecture may be
reformulated on a well-posed word in a stated convention. This bean now says
precisely what such a reformulation must supply — a rule fixing the word rather
than its crossing content, and one trace family across all three levels. Caveats
added to `conj:jet-filtered-knot-factor` and `prop:confined-knot-binding`.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-05 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-11-15 — γγ-built nucleon (PR #7741, `h2_gg_atom/`, `h2_gg_electron/`; owner decision C)

On three strands every γγ word is a power of V = σ₀σ₁⁻¹, so a γγ-built nucleon is V^m. Pre-registered and measured: only V³ and V⁶ pass reading 3 at every level (m = 3…7); proton and neutron are then the same word, so there is no flavour on three strands. With a γγ electron (V³ or V⁶) H₂ passes every level and the only passing bond is V³. Every γγ word has χ_(1³) = 1 (#7896). Scope (a). Bearing on this bean: every-level reading 3 (closing strands from the top) is now implemented in h2_one_rule_probe.level_chars; it is a positivity test per level, not the character ratio R this bean asks for.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8345, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-05: "merge: intra-word ordering — beta_Bor confinement core, the invariance proved in Lean, and the 5.045e-4 residual retract"). The work may be partly or fully done. Read the bean before you close it.
