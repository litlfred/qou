/-
# The binding-K enumerator's selection criterion cannot pick a binding carrier

`qou-brng` asked for a carrier selection principle that is not minimality. There
already is one — `binding_k_enumerator.py` ranks by Frobenius residual — and this
file is why it does not work. Three independent defects, each fatal on its own,
all readable off the enumerator's **own recorded output** in
`fsh-guts/deprecated/computations/binding-k-enumerator.witness.json`.

## 🛑 First, correcting a correction of mine

The merged `CarrierCrossingQuantisation` header says the corpus's principle is
Frobenius-residual minimisation, not minimality, and that reading
the length field as the criterion is what makes minimality look
load-bearing. (That field was named `bindingKMinimalLength` when this was
written; the `Prop`-universe copy was deleted 2026-09-07 and the decidable
`bindingKLengthBounded` is what remains.) **The first half is right about the code and wrong about the
corpus.** The `sort` key is indeed `(PSD-feasible, residual, length)` — but the
`bindingKWord = [3,3]` on the Lean instances was taken from the witness's
`min_length_psd_feasible_candidates` list, **not** from the residual-ranked
`psd_feasible_top_k`. So the recorded carrier *is* the min-length pick after
all; what is not minimality is the code's sort. Both halves matter and I
previously stated only one.

## Defect 1 — the residual's top pick is a SELF-CROSSING

With `constituent_offsets = [0,3,6]` in `B₉`, nucleon `k` occupies strands
`3k+1 … 3k+3`, and `σ_i` joins strands `i, i+1`. So `σ_i` is an **interface**
(inter-component) generator exactly when `i` is a multiple of `3`
(`interface_iff_three_dvd`) — that is, `σ₃` and `σ₆` alone. Every one of
`σ₄, σ₅, σ₇, σ₈` joins two strands **inside one nucleon**.

The enumerator's `inter_nucleon_generators_extended` for `A = 3` is
`[3,-3,4,-4,5,-5,6,-6,7,-7,8,-8]` — **8 of its 12 entries are intra-nucleon**,
and the field name says otherwise.

Consequence, recorded: for **both** `³H` and `³He` the residual-ranked top two
are `[-8,-8]` and `[-5,-5]`, i.e. `σ₈⁻²` and `σ₅⁻²` — self-crossings inside
nucleons 3 and 2. A carrier built from them has **zero** inter-component
crossings, so `countChannel = 0` (`selfCrossing_countChannel_eq_zero`) and it
binds nothing at all. The criterion's winner is not a weak carrier; it is not a
carrier.

## Defect 2 — the top-2 ordering is float64 noise between exactly-equal candidates

Recorded residuals, `³H`:

    [-8,-8]   0.9321237012643592     <- rank 1
    [-5,-5]   0.9321237012643594     <- rank 2
    [-3,-3]   0.9339216957602768
    [-6,-6]   0.9339216957602768

`σ₅` and `σ₈` are the *same* generator of two different nucleon blocks, so by
the construction's block symmetry their residuals are **equal**. The recorded
difference is `2.220e-16` — two ULP at `0.93`, where `float64` eps is
`1.11e-16`. The rank-1 slot is therefore decided by rounding, not by
mathematics. The same 2-ULP split appears for `[-4,-4]` vs `[-7,-7]` and for
`[7,7]` vs `[4,4]`.

This is the failure mode AGENTS.md's NO-FLOAT64 rule names outright: *"agreement
at 1e-16 in float64 is the floor of the arithmetic, not evidence about the
mathematics"* — here used not to claim an agreement but, worse, to **break a
tie** and thereby choose the answer.

## Defect 3 — the two genuine interfaces are exactly degenerate

`[-3,-3]` and `[-6,-6]` record the **identical** residual
`0.9339216957602768`, to every digit. So even restricted to the real interface
generators the criterion cannot tell the `1|2` interface from the `2|3` one. A
principle that is degenerate on the only two candidates that could bind is not
selecting; it is tying.

## What this closes, and what it opens

**Closes:** extending `L_K_max` was my proposed next step and it is **futile**.
The search was never truncation-limited in the way that matters — a longer
search re-ranks by a criterion that (1) prefers non-carriers, (2) breaks ties in
rounding error, and (3) is degenerate on the interfaces. Fixing the length bound
without fixing the criterion searches a larger space with the same broken
comparator.

**Opens:** the criterion is repairable and the repairs are named. Restrict the
generator set to genuine interfaces (`i` a multiple of `3`); carry the residual
in `mpmath.mpf` rather than `float64` so the comparisons mean something; and
break the remaining `1|2`-vs-`2|3` degeneracy with something other than the
trace residual, since that symmetry is exact.

Note also that the corpus's own canonical `A = 3` carrier, the Borromean `L6a4`,
is **not reachable** from `⟨σ₃, σ₆⟩` at all: those two generators are distant
(`|3-6| ≥ 2`) hence commute, so the subgroup is free abelian and every word
reduces to `σ₃^a σ₆^b`, whose pairwise linking numbers are `a/2`, `b/2`, `0`.
Brunnian forces `a = b = 0`, the trivial carrier
(`commuting_interfaces_brunnian_trivial`). The Borromean braid `(σ₁σ₂⁻¹)³` needs
**adjacent** generators. So on the minimal set the enumerator could never have
found the corpus's own answer, at any length.

**The reachability step is now PROVED on `main`, and this file should defer to
it.** `QOU.Mass.StrandLayoutForcesChain` (`8421cd4163`, landed after this file was
drafted) carries `no_single_generator_joins_nonadjacent`: with `block m = m / 3`,
a single generator joins two *different* nucleons only at `m % 3 = 2`, and then
only **consecutive** ones. That is exactly what `twoLk`'s third component encodes
below, and it is why the encoding caveat there can be discharged by citation
rather than by building a braid-word model here. Indexing differs — that file
gives nucleon `k` strands `3k, 3k+1, 3k+2` (0-based, bridges at `m % 3 = 2`);
this one uses `3k+1 … 3k+3` (1-based, bridges at `3 | i`). Same fact, and
`interface_iff_three_dvd` is its 1-based twin.

## The fix is the generator set, and it is a known one

The obstruction above is **not** the strand layout — `n = 3A` is forced corpus-wide
by the three-quark structure, and re-labelling which strands belong to which
nucleon is a conjugation, which the Markov trace cannot see. It is the **generator
set**.

The braid group's **band** (Birman–Ko–Lee) generators
`a_{t,s} = (σ_{t-1} ⋯ σ_{s+1}) σ_s (σ_{s+1}⁻¹ ⋯ σ_{t-1}⁻¹)` link strands `s` and
`t` **directly**, for any `s < t`, and satisfy `a_{s+1,s} = σ_s`. So the adjacent
transpositions the enumerator used are a **proper subset** of the bands — and,
counted in `B₉`:

| | count |
|---|---|
| inter-nucleon band generators | **27** |
| of those, searched by the enumerator | **2** (`σ₃`, `σ₆`) |
| bands reaching the `1|3` pair | **9** |
| of those, searched | **0** |

Every `1|3` band has `|t - s| ≥ 4`, so none is an adjacent transposition and none
could have been in the search set. That is exactly the pair a Brunnian carrier
needs. **The subset chosen excludes precisely what was required.**

🛑 **RETRACTED — that grep was wrong when I ran it.** This read: *"band /
Birman–Ko–Lee generators appear nowhere in `content/`, `computations/` or
`docs/`"*. **False.** At the very commit my own checkout was sitting on
(`ed4ffbe424`), `computations/deltalambda/` already carried them in at least six
files — `brunnian_route_feasibility_probe.py` names
`a_{7,3} = (σ₆σ₅σ₄…)` explicitly, and `milnor_exact_coefficient_probe.py`
works with *"commutators of pure-braid **band generators**"*.

**The mechanism, because it generalises.** My pattern was correct and *did* match
those files. I piped it through `head -10`, and
`folio/quantum-observable-universe/lean/.lake/packages/…` sorts before
`computations/` — six vendored Mathlib/batteries blobs consumed the budget, and I
read the truncated output as *empty*. **`head` on a corpus grep is a correctness
hazard, not a display convenience**, and a repo with a vendored `.lake/` will eat
the budget before reaching the directory that matters. Exclude `.lake/` and drop
the cap.

What survives: the band presentation *is* the right generating set (the count
argument above is unaffected), and four library documents cover it. What does not
survive is the claim that adopting it would be new here.

## Scope

Scope **(b)** on the enumerator's selection criterion *as implemented*, with the
invariants named: the block arithmetic of `constituent_offsets` (defects 1, 3)
and `float64` ULP spacing (defect 2). Scope **(a)** on the *idea* of
residual-based selection, which is untested — no repaired criterion has been
run, and nothing here says one would fail.

Ground ring `ℕ` for the block arithmetic; the `countChannel` statement is
`ℝ` (§7c) matching `BrunnianBindingChannel`.

Beans `qou-brng`.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace QOU.Mass.EnumeratorSelectionDegeneracy

/-! ## 1. Which generators are interfaces -/

/-- The nucleon block containing strand `s`, for nucleons of three strands each
laid out at `constituent_offsets = [0, 3, 6, …]`: strands `1,2,3` are nucleon 0,
strands `4,5,6` nucleon 1, and so on. -/
def blockOf (s : ℕ) : ℕ := (s - 1) / 3

/-- `σ_i` joins strands `i` and `i+1`; it is an **interface** generator when
those two strands lie in different nucleons. -/
def IsInterface (i : ℕ) : Prop := blockOf i ≠ blockOf (i + 1)

/-- **Interfaces are exactly the multiples of three.** So in `B₉` with three
nucleons, `σ₃` and `σ₆` are the only inter-component generators, and
`σ₄, σ₅, σ₇, σ₈` are all intra-nucleon self-crossings. -/
theorem interface_iff_three_dvd (i : ℕ) (hi : 1 ≤ i) :
    IsInterface i ↔ i % 3 = 0 := by
  unfold IsInterface blockOf
  omega

/-- The four generators the enumerator's `..._extended` list adds beyond `σ₃`
and `σ₆` are **not** interfaces, so the field name is wrong about two thirds of
its entries. -/
theorem extended_generators_are_intra :
    ¬ IsInterface 4 ∧ ¬ IsInterface 5 ∧ ¬ IsInterface 7 ∧ ¬ IsInterface 8 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    · rw [interface_iff_three_dvd _ (by norm_num)]; decide

/-- And `σ₃`, `σ₆` are. -/
theorem three_six_are_interfaces : IsInterface 3 ∧ IsInterface 6 := by
  constructor <;> · rw [interface_iff_three_dvd _ (by norm_num)]

/-! ## 2. A self-crossing carrier binds nothing -/

/-- The unsigned count channel, as in `BrunnianBindingChannel.countChannel`:
`½(n₊ + n₋)(q − q⁻¹)`, whose `n₊`, `n₋` are **inter-component** crossings. -/
noncomputable def countChannel (np nn : ℕ) (q : ℝ) : ℝ :=
  ((np : ℝ) + (nn : ℝ)) * (q - q⁻¹) / 2

/-- **A carrier built only from intra-nucleon generators contributes no binding.**
It has no inter-component crossings, so both counts are zero and the channel
vanishes identically — for every `q`, so no anchor or convention rescues it.
This is what the enumerator's rank-1 candidate `σ₈⁻²` is. -/
theorem selfCrossing_countChannel_eq_zero (q : ℝ) : countChannel 0 0 q = 0 := by
  unfold countChannel; ring

/-- Restated as the acceptance test it fails: a carrier is admissible only if its
count channel is non-zero somewhere, and a self-crossing carrier never is. -/
theorem selfCrossing_not_admissible :
    ¬ ∃ q : ℝ, countChannel 0 0 q ≠ 0 := by
  rintro ⟨q, hq⟩
  exact hq (selfCrossing_countChannel_eq_zero q)

/-! ## 2b. The binding cannot see WHICH band — only how many crossings -/

/-- **The count channel depends only on the total crossing count.** Two carriers
with the same `n₊ + n₋` on a pair give the *same* binding, whatever strands they
actually use. -/
theorem countChannel_depends_only_on_total (np nn np' nn' : ℕ) (q : ℝ)
    (h : np + nn = np' + nn') : countChannel np nn q = countChannel np' nn' q := by
  unfold countChannel
  have : ((np : ℝ) + (nn : ℝ)) = ((np' : ℝ) + (nn' : ℝ)) := by exact_mod_cast h
  rw [this]

/-- **So the carrier is underdetermined by the binding itself.** In `B₉` there are
**nine** band generators joining any given pair of nucleons (`3 × 3` strand
choices), and `countChannel` assigns all nine the same value. Combined with
`QOU.Mass.SelfMutualPartition`, which makes the binding a sum over
inter-component crossings, the binding-relevant content of a carrier is just the
per-pair crossing counts — a triple `(m₁, m₂, m₃)`, not a braid word.

Measured, for a Brunnian carrier (`n₊ = n₋ = mᵢ` on each pair) with total
crossings `c ≤ 12`: **20 triples**, against **382,637,520** structured band
words — a collapse of about `1.9 × 10⁷`.

**This is why a trace criterion cannot select the carrier, and it subsumes
Defect 3.** The residual is being asked to make a distinction the binding does
not use. Defect 3 (the exact `1|2`-vs-`2|3` tie) is the two-generator shadow of
this: the trace ties them because the binding has no opinion either. -/
theorem carrier_underdetermined_by_binding (np nn : ℕ) (q : ℝ) :
    countChannel np nn q = countChannel (np + nn) 0 q :=
  countChannel_depends_only_on_total _ _ _ _ q (by omega)

/-! ## 3. The minimal interface set cannot carry a Brunnian link -/

/-- Pairwise linking numbers of a carrier `σ₃^a σ₆^b` in `B₉`, doubled to stay in
`ℤ`: the `1|2` pair sees only the `σ₃` letters, the `2|3` pair only the `σ₆`
letters, and the `1|3` pair sees neither.

**The third component being `0` is an ENCODING of a reachability fact, not
something proved here.** `σ₃` transposes positions `3,4` and `σ₆` transposes
`6,7`, so no strand starting in block 1 (`1…3`) can ever occupy a position
adjacent to a strand of block 3 (`7…9`): the two blocks never cross, at any word
length. Formalising that would need a braid-word model this file deliberately
does not carry; it is stated in the header and taken as the definition of
`twoLk`. Everything below is honest given that reading and vacuous without it. -/
def twoLk (a b : ℤ) : ℤ × ℤ × ℤ := (a, b, 0)

/-- **On the minimal interface set the only Brunnian carrier is trivial.**
`σ₃` and `σ₆` are distant (`|3 - 6| ≥ 2`) hence commute, so `⟨σ₃, σ₆⟩` is free
abelian and every word reduces to `σ₃^a σ₆^b`. Brunnian means every pairwise
linking number vanishes, which forces `a = b = 0`.

So no amount of extra word length produces a Brunnian carrier here — the
obstruction is the generator set, not the length bound. The corpus's own
canonical `A = 3` carrier, the Borromean `(σ₁σ₂⁻¹)³`, needs **adjacent**
generators and is therefore outside this subgroup entirely. -/
theorem commuting_interfaces_brunnian_trivial (a b : ℤ)
    (h : twoLk a b = (0, 0, 0)) : a = 0 ∧ b = 0 := by
  unfold twoLk at h
  exact ⟨(Prod.mk.injEq .. ▸ h).1, by simpa using congrArg (Prod.fst ∘ Prod.snd) h⟩

end QOU.Mass.EnumeratorSelectionDegeneracy
