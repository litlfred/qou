---
# qou-tower
title: 'There is no tower: the production chain reduces every nucleus to the same 6 dims'
status: in-progress
pr: 8278
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
---

Asked to walk the generative production chain step by step, look past the
Gröbner normal form at the **full tower**, and check whether twist data changes
on magic isotopes. Probe:
[`gamma_chain_tower_magic_probe.py`](../computations/probes/gamma_chain_tower_magic_probe.py), 3/3.

**The first magic number is 2**; the first *doubly*-magic nucleus is ⁴He
(Z = N = 2), which on the N = Z line the producer walks is A = 4.

## THE FINDING: there is no tower

The atom braid nominally lives in `H_{3A}` — 3 strands per nucleon. But
`build_atom_nf_mp` applies the **H₃ Gröbner–Shirshov reduction after every
crossing**, so the state is a 6-vector at every step of every nucleus.
Measured:

| | NF dimension |
|---|---|
| all 33 stages of Z=N=4 | **6** |
| hydrogen (Z=1, N=0) | **6** |
| lead-208 (Z=82, N=126) | **6** |

**Hydrogen and Pb-208 occupy the same state space.** The `H_{3A}` structure is
destroyed as it is built, so "the full tower" does not exist in this code path —
the GS normal form *is* the whole object, not a projection of something larger.

**That one fact explains every negative on this arc.** Nothing in the
construction can distinguish one nucleon count from another except through
smooth growth, so no shell signal is expressible — not in δ²Φ, not in the LP
dual, not in the shell SDP. The searches were not unlucky; the degree of
freedom is absent.

## Twist / framing data does not change at magic

Replaying the chain and accumulating signed crossings (`d=0` is σ, `d=-h` is
σ⁻¹, `d=-h/2` a mixed interface that is not a pure crossing):

    writhe(Z) = 3Z        exactly  ->  writhe/A = 1.5 for EVERY nucleus
    mixed(Z)  = Z² + 4Z   exactly

Both smooth polynomials, no feature at 2, 8, 20, 28. The crossing schedule is
fixed per nucleon plus an O(A²) pair loop; it has no shell dependence to carry.

## The LP cannot be asked about T₃,₅ receptivity

Swept `n_target` over 0.25, 0.5, 1, 2, 3, 4, 6, 8, 12, 16, 20, 28, 50, 82, 126,
200, 500, 1000 — the active set is the singleton `{γ}` at **every** target. It
is not the target choice: the LP is structurally one-dimensional on this
6-channel basis, so "is the isotope receptive to a different knot such as
T₃,₅" is not a question this LP can express.

## 🛑 A candidate signal at ⁴He — RETRACTED, and it was mine

The final NF at Z=2 has σ₁, L₊, L₋ collapse to ~1e-3 while every neighbour is
O(1–30) — the state condensing onto the trivial channel exactly at the first
doubly-magic nucleus. I flagged it as promising. It does not survive its
control. With `R = ||nf_non-γ|| / |nf_γ|`:

- **R is strictly monotone increasing over even Z** — 0.489, 0.808, 1.143,
  1.404, … → 2.959 at Z=30 — and the odd branch descends to the same limit
  from above (2.997 at Z=29);
- so **Z=2 is the global minimum by being the smallest even Z**;
- magic Z rank **1st, 4th, 10th, 14th of 15** among even Z — spread across the
  whole range.

Parity split plus monotone convergence: the same artifact δ²Φ turned out to be.
And *"is the global minimum magic?"* returns **True** while being empty — 2 is
both the smallest even number and the first magic one, so any
monotone-in-even-Z quantity answers yes. Fifth instance of the input-presented-
as-output pattern today, second one mine.

## Where this says to look instead

The tower has to survive. A construction that reduces to H₃ at each step cannot
carry shell structure, so the question is whether the chain can be run **without
the per-step GS reduction** — keeping the H_{3A} state and reducing only at the
end (or not at all). That is a real compute problem (dim H_{3A} = (3A)!), but it
is the only place a shell degree of freedom could live in this construction.

Note this is not the same as the `qou-mgq3` finding that `gram.py` is hardwired
to H₃. That was about the LP's channel space; this is about the state itself
being collapsed during production, upstream of any LP.

## 🛑 CORRECTION — the tower is CHEAP at He-4, not infeasible. Mine.

The section above closes with *"a real compute problem (dim H_{3A} = (3A)!)"*.
**That is wrong, by ~3,400× at the nucleus that matters**, and it is the wrong
number in the pessimistic direction — it made a tractable experiment look
impossible.

`(3A)!` is the dimension of the **regular representation**. The state is not
carried that way. By Wedderburn `H_n(q) ≅ ⊕_λ M_{d_λ}`, and — as
`shell_closure_compute._extract_blocks` already exploits — the Hoefsmit
seminormal form has **gen 0 pure diagonal and gen 1 in 2×2 blocks**, so the
per-partition cost is `O(d_λ)`, not `O(d_λ²)`:

| A | n=3A | partitions | max d_λ | **Σ d_λ (what you carry)** | Σ d_λ² = n! |
|---|---|---|---|---|---|
| 2 (deuteron) | 6 | 11 | 16 | **76** | 720 |
| 3 | 9 | 30 | 216 | **2,620** | 3.6e5 |
| **4 (⁴He)** | 12 | 77 | 7,700 | **140,152 ≈ 5.6 MB** | 4.8e8 |
| 5 | 15 | 176 | 292,864 | 10,349,536 ≈ 414 MB | 1.3e12 |
| 6 | 18 | 385 | 1.6e7 | 9.97e8 ≈ 40 GB | 6.4e15 |

**⁴He — the first doubly-magic nucleus, the exact object of interest — needs
about 5.6 MB at 50 dps.** A=5 is borderline at 414 MB; A=6 is out at 40 GB.

So the experiment is **reachable precisely up to the first doubly-magic
nucleus, and one step past it**. The question "does structural behaviour change
at the first magic number, with the tower intact" is computable now. It was
never a compute wall; my estimate was.

Note this also puts a measured number on where the tower genuinely ends: A=5
borderline, A=6 out. So even a full-tower walk cannot reach Z=8 (A=16), let
alone 20/28/50/82/126. The tower buys the **first** magic number, not the
ladder.

### It also collides with a corpus claim

`observations/k12-barrier-bypass.md` states that at `k ≥ 12` the partition
growth *"blocks the matrix-evaluation approach"*. The arithmetic above says
`k = 12` is 77 partitions and 140k numbers, and the existing producer already
does `k = 10` (42 partitions, max dim 768) in 37 s. A ~10–20× step is minutes,
not a barrier. Being tested directly by running `shell_closure_compute.py
--kmax 12`; if it completes, the k12-barrier framing needs re-scoping and the
homological bypass it motivates loses its stated justification.

## 🛑 The k=12 barrier IS real — my "minutes, not a barrier" was wrong

I predicted `--kmax 12` would finish in minutes. **It was OOM-killed**:
`anon-rss 12.6 GB` in a 16 GB container, dying silently after k=11 with no
traceback and no k=12 line. Measured timings up to the kill:

    k= 9:  30 partitions, max_dim=  216,    8.7s
    k=10:  42 partitions, max_dim=  768,   30.9s
    k=11:  56 partitions, max_dim= 2310,  129.4s
    k=12:  77 partitions, max_dim= 7700,  OOM-KILLED

### The cause is not what the corpus says either

`k12-barrier-bypass.md` attributes it to the **partition count** growing
combinatorially. 77 partitions is nothing. The real cause is that
`_extract_blocks` **materialises a dense d×d matrix per partition** (via
`seminormal_matrix`) and `shell_closure_compute` holds every partition's
structure simultaneously:

    structs[shape] = {0: _extract_blocks(shape,0), 1: _extract_blocks(shape,1)}

Summed over partitions that is `Σ d_λ² = n!`:

| k | Σd² = n! | per generator | both |
|---|---|---|---|
| 10 | 3,628,800 | 0.03 GB | 0.06 GB |
| 11 | 39,916,800 | 0.32 GB | 0.64 GB |
| **12** | **479,001,600** | **3.83 GB** | **7.66 GB** |

7.66 GB plus numpy temporaries gives the 12.6 GB observed. It matches.

### Two numbers I conflated, and the correction to my correction

- **state to carry once extracted**: `Σ d_λ` = 140,152 = **5.6 MB** — correct,
  and still correct;
- **what the current extractor transiently needs**: `Σ d_λ²` = `n!` = **3.8 GB
  per generator** — which is what actually runs.

My "5.6 MB, entirely tractable" was right about the *state* and wrong about the
*code path to it*. So the previous correction in this bean over-corrected: the
`(3A)!` figure I called wrong is exactly the right figure for
`_extract_blocks` as written. Both statements were half right, and the honest
version needs both numbers side by side.

### It is still fixable, and that is the actionable part

The barrier is an implementation artifact, not mathematics. Hoefsmit's form
gives matrix entries directly from **axial distances on standard Young
tableaux** — gen 0 is pure diagonal and gen 1 is 2×2 blocks plus diagonal, which
`_extract_blocks` *rediscovers by scanning a dense matrix it just built*. Built
directly from the SYT combinatorics the extraction is `O(Σ d_λ)` = 5.6 MB at
k=12, never allocating the dense matrix. That is also why the current code is
slow: the partner search is an `O(dim²)` Python double loop, 59M iterations per
partition at k=12.

So the k=12 barrier — and the homological bypass it motivates — rests on a
dense materialisation that the mathematics does not require. Re-scoping that
claim needs the direct-construction extractor written and measured first; until
then the correct statement is **"the barrier as stated is not what blocks this,
and what does block it is fixable"**, not "the bypass is unnecessary". Those are
different claims and only the first is measured.

## k=12 RUNS — 403 s — and it reproduces a witness the corpus already had

With `extract_blocks_direct` swapped in for `_extract_blocks`, the level that
OOM-killed the dense path completes:

    k= 9:  30 parts,    8.1s
    k=10:  42 parts,   27.8s
    k=11:  56 parts,  103.4s     (dense: 129.4s)
    k=12:  77 parts,  403.0s     (dense: OOM-KILLED at 12.6 GB)

**Independent verification, stronger than the 186-pair check.** The K=12
δ²Φ values reproduce `computations/_deprecated/shell-closure.witness.json`
(`kmax: 12`) over all 26 overlapping Z. Max |diff| = **4.59e-05**, which is
exactly my log's 4-decimal print precision — the underlying values agree.

**So a k=12 result was already in the corpus.** `observations/k12-barrier-bypass.md`
states that at `k ≥ 12` the partition growth *"blocks the matrix-evaluation
approach from confirming saturation at {50, 82, 126}"* — and a committed
(deprecated) witness carries exactly that computation. The barrier claim is
contradicted from two directions now: by that witness, and by this 403 s run.

Careful scoping, unchanged: this says the barrier **as stated** is false, and
that the matrix-evaluation route reaches k=12. It does NOT establish that the
homological bypass is unnecessary — that needs the k ≥ 13 saturation results
the bypass was meant to supply, and the bypass may rest on other grounds.

## The parity artifact survives every level now reachable

    K=10:  parity exceptions NONE,  even-Z maxima [4, 12, 16],  none magic
    K=11:  parity exceptions NONE,  even-Z maxima [4, 12],      none magic
    K=12:  parity exceptions NONE,  even-Z maxima [4, 12],      none magic

So δ²Φ's parity structure is **not an artifact of the K=10 truncation**. It
persists at every level the new extractor opens up, and the local maxima stay
at 4 and 12 — neither magic. The `qou-pz4m` finding holds at K=11 and K=12.

## 🛑 Scoping the A=4 walk — THREE objects, and I had conflated two

Before building the tower walk I re-scoped it, having mis-estimated twice
already. There are three distinct objects and the "5.6 MB" figure belongs to
the first, not the one the walk needs:

| # | object | size at n=12 |
|---|---|---|
| 1 | **generator block structure** (what `hoefsmit_blocks_direct` builds) | `Σd_λ` = 140,152 → **measured 1.4 s, 92 MB** |
| 2 | **evolving algebra element** (the honest tower state) | `Σd²` = `n!` = **3.83 GB** |
| 3 | trace via matvecs (memory-cheap route) | 5.6 MB storage but ~**9.6e10** scalar ops |

Object 2 is what a tower walk actually carries. Each `σ_i` is 2×2-block
structured **in the seminormal basis**, but *different* generators have
*different* block structures, so a product of them is a general matrix — the
trick `nuclear_character_fast` uses works precisely because the H₃ code only
ever touches two generators. **So the A=4 walk is not 5.6 MB.** Object 3 keeps
the memory but costs ~1e11 scalar ops — out of reach in Python, plausible in
the Rust `hecke-engine`.

### But the first magic number is reachable *now*, at A=3

Magic-ness is a property of **Z or N separately**, so the first magic number
does not require the doubly-magic nucleus:

| A | n | `Σd²` = n! | size | nuclei |
|---|---|---|---|---|
| 2 | 6 | 720 | trivial | **²H** (Z=1,N=1) — neither magic |
| 3 | 9 | 362,880 | **2.9 MB** | **³He** (Z=2,N=1) **Z MAGIC** ; **³H** (Z=1,N=2) **N MAGIC** |
| 4 | 12 | 479,001,600 | 3.83 GB | **⁴He** — doubly magic; borderline in a 16 GB box |
| 5 | 15 | 1.3e12 | 10.5 TB | out |

So the **exact** magic-vs-non-magic contrast — ²H (neither) against ³He (Z=2)
and ³H (N=2) — costs **2.9 MB** and is fully tractable in Python today. That is
the experiment, and it does not need ⁴He.

⁴He at 3.83 GB is worth attempting afterwards (the container has ~12 GB
available), but it is the *second* step, not the gate.

### Correction to my own "next" from the previous entry

The previous entry said the A=4 walk was "affordable" on the strength of the
5.6 MB figure. That was object 1. The corrected plan is: do A ≤ 3 exactly,
which already contains the first magic number on both the Z and N axes, then
attempt A=4 separately.

## THE A=3 WALK RAN — and the tower shows nothing

[`tower_walk_h3a_magic_probe.py`](../computations/probes/tower_walk_h3a_magic_probe.py).
Real H₉ state: a full `d_λ × d_λ` matrix per partition `λ ⊢ 9`, **no per-step
GS reduction**, generators at their **true strand positions** per
`sigma_shell_characterization.shell_position` (nucleon `k` on strands
`3k+1..3k+3`, internal B₃ on generators `3k`/`3k+1`, interface at `3k−1`).
That last part is the collapse this walk removes — the H₃ code puts every
crossing on generators 0 and 1.

**A=3 is exhaustive**, which is why it is the right control: `Z ∈ {0,1,2,3}`
is *all four* configurations, so the contrast is at fixed algebra, fixed
partitions and fixed strand count with only nucleon composition varying.

    Z=3,N=0      neither   top-share 0.0907  participation 18.895  argmax (6,3)
    ³He Z=2,N=1  Z MAGIC   top-share 0.0802  participation 20.256  argmax (3,3,1,1,1)
    ³H  Z=1,N=2  N MAGIC   top-share 0.0961  participation 20.591  argmax (3,3,1,1,1)
    Z=0,N=3      neither   top-share 0.0968  participation 19.819  argmax (3,3,1,1,1)

**No separation.** Top-block share interleaves — the magic ³He is the *lowest*
and the magic ³H sits between the two non-magic configurations. The argmax
partition does not separate either: non-magic `Z=0,N=3` sits on the same
`(3,3,1,1,1)` as both magic configurations, and only `Z=3,N=0` (non-magic)
differs. Rank is full in every block for every configuration.

### The one quantity that split, and why it is NOT reported as a signal

Participation ratio splits cleanly — magic `{20.256, 20.591}` against
non-magic `{18.895, 19.819}`, `min(magic) > max(non-magic)`. Checked before
believing it: with **2 versus 2** there are 6 label orderings and 2 of them are
clean splits, so **P = 1/3 under the null**. A one-in-three coincidence is not
evidence, and A=3 is *exhausted* — there are no further configurations to add,
so it cannot be tested further at this A. Reporting it as a find would have
been a sixth instance of the input-presented-as-output / inadequate-control
pattern this arc has now hit five times.

### What is left

**⁴He (A=4) is the only doubly-magic case in reach and is UNTESTED.** Object 2
(`Σd²` = 12! = **3.83 GB**) is borderline in a 16 GB container, and the same
container OOM-killed the k=12 dense run at 12.6 GB. Needs a memory guard, and
it is the *only* remaining place in this construction where "doubly" magic
could matter.

Beyond that, §2's structural finding narrows where to look at all: the collapse
is in `build_atom_nf_mp`, **upstream of every LP and SDP**, so any shell degree
of freedom has to enter *before or outside* the GS reduction. It cannot be
recovered downstream of it.

### Precision, stated not hidden

The block values inherit **float64** from `level_k_binding`'s `q0`/`qi`/`HA`,
which this probe does not re-implement. The question here is structural —
whether the distribution over partitions differs qualitatively — and the
compared quantities differ at O(0.1), ~15 orders above the float64 floor. **No
agreement at any digit count is claimed.** Per AGENTS.md §PROBES ARE NOT
EXEMPT: this is a stated limitation on an *inherited* input, not a float64
computation introduced here, and the conclusion is a negative that float64
cannot manufacture.

## 🛑 CLOSED: the tower shows nothing at ANY level it can reach

[`tower_walk_magic_replication_probe.py`](../computations/probes/tower_walk_magic_replication_probe.py)
(renamed from `tower_walk_a4_doubly_magic_probe`). All three reachable levels,
**exhaustively** — every `Z` in `0..A`, so there is no unmeasured configuration
to appeal to:

    A=2  Z=2,N=0 MAGIC    top-share 0.1996  participation  7.624  argmax (6,)
         Z=1,N=1 neither  top-share 0.1960  participation  7.801  argmax (3,3)
         Z=0,N=2 MAGIC    top-share 0.1909  participation  7.560  argmax (2,2,2)

    A=3  Z=3,N=0 neither  top-share 0.0907  participation 18.895  argmax (6,3)
         Z=2,N=1 MAGIC    top-share 0.0802  participation 20.256  argmax (3,3,1,1,1)
         Z=1,N=2 MAGIC    top-share 0.0961  participation 20.590  argmax (3,3,1,1,1)
         Z=0,N=3 neither  top-share 0.0968  participation 19.819  argmax (3,3,1,1,1)

    A=4  Z=4,N=0 neither  top-share 0.0530  participation 42.169  argmax (9,3)
         Z=3,N=1 neither  top-share 0.0436  participation 44.400  argmax (5,4,1,1,1)
         Z=2,N=2 DOUBLY   top-share 0.0504  participation 45.487  argmax (5,4,1,1,1)
         Z=1,N=3 neither  top-share 0.0481  participation 44.826  argmax (5,4,1,1,1)
         Z=0,N=4 neither  top-share 0.0567  participation 43.818  argmax (3,3,3,1,1,1)

### A=2 is what settled it, and I had skipped it

The entry above treats **A=4** as the decisive test because it is the only
**doubly**-magic case. That framing was wrong in a way that cost a session:
magic-ness is a property of `Z` **or** `N`, so **A=2 already carries magic
numbers** — `Z=2,N=0` and `Z=0,N=2` are singly magic, the deuteron is neither
— and A=2 is *eleven partitions of dimension ≤ 16*, i.e. seconds. It was
skipped only because the probe was written around "doubly magic", and its
`dm`-empty guard returned early on it.

**The participation ratio reverses sign between levels.** It is the one
quantity that split cleanly at A=3 (magic `{20.256, 20.590}` above non-magic
`{18.895, 19.819}`), and this bean carried it as "the one thing that
separated". At A=2 the magic configurations are the **two lowest** (7.624 and
7.560, against the deuteron's 7.801). A quantity that is high for magic at one
level and low at the next is measuring **the level**, not the magic number.
The A=3 split was the P = 1/3 coincidence it was labelled as, and A=2 is the
direct demonstration rather than an argument from the null.

The other two criteria fail outright:

- **rank** — every block is full rank in every configuration at every level;
- **argmax** — ⁴He's `(5,4,1,1,1)` is shared with **three** non-magic A=4
  configurations. The criterion is also *vacuous* at every level, for three
  different reasons the probe now names: A=2 has one non-magic configuration
  (a singleton "agrees with itself"), A=3's non-magic argmaxes disagree with
  each other, A=4 has one magic configuration.

### And A=4 is the end of the road

`Σ_λ d_λ²` = 12! is **not** the binding constraint — partitions are
independent under the braid action, so peak memory is `max_λ d_λ²` = 7700² =
474 MB (measured RSS **0.64 GB**), and the `O(d³)` dense matmul becomes
`O(d²)` column ops in the Hoefsmit basis (verified against the dense route,
max relative disagreement **6.34e-16**). But at A=5, `max_λ d_λ²` =
292,864² = **686 GB**. So A=4 is the last reachable level and ⁴He the only
doubly-magic nucleus this construction can ever test.

### Three defects in my own instrument, all caught before the verdict

1. **The vacuity guard was itself vacuous.** It asked whether the non-magic
   configurations agree with each other — and at A=2 there is only one, which
   agrees with itself trivially, so A=2 reported a spurious qualitative
   separation. Now requires ≥2 members in *both* groups *and* internal
   consistency in both, and prints why when it cannot decide.
2. **Two assertions asserted the answer** (`expected="False"` on the verdict).
   A test that passes exactly when the result is the one wanted. Removed; the
   assertions now record the *control* and the verdict is payload data.
3. **39 raw float64 fields** would have entered the witness. Aggregation moved
   to mpmath (`mp.fsum`, `mpf`) and serialized through `_precision.fmt`. The
   per-partition `|tr|` inputs remain float64 — inherited from
   `level_k_binding`, stated, not stringified. The headline is a negative plus
   a **sign reversal of ~0.24 in a quantity of size ~7.7**; float64 cannot
   manufacture either.

### Where a shell degree of freedom could still be

Not downstream. The collapse is in `build_atom_nf_mp`, **upstream of every LP
and SDP**, and removing it does not produce a signal. So a shell DOF would
have to enter the construction *before or outside* the Gröbner–Shirshov
reduction — it cannot be recovered from the tower, because the tower has now
been carried intact and has none.

## 🛑 RETRACTED IN SCOPE (2026-08-30, owner correction). The claim "the H_{3A}
structure is destroyed as it is built" is WRONG, and the corpus says so in
three places this probe did not reach:

  * `trace-locality-gs-reconciliation.md` -- "The GS algorithm DIGESTS global
    entanglement into local coefficients; after digestion, the Markov trace
    factorises locally over the normal form." Digested, not destroyed.
  * `bond-order-eq-jet-degree-proof.md` -- adding a nucleon "rais[es] the
    Groebner-Shirshov normal-form length by a fixed increment", placing the
    n-nucleon cluster sub-word at JET VERTICAL DEGREE n.
  * `prop:gb-spectral-sequence` (E_2 collapse) + `prop:jet-prefix-gb-filtration`
    -- the associated graded gr_n IS the n-nucleon cluster contribution.

So the NF is 6 LAURENT POLYNOMIALS IN q graded by GS filtration length, and
the surviving grading is exactly the many-body decomposition. "Hydrogen and
Pb-208 occupy the same state space" is true of the DIMENSION and false of the
CONTENT. Reading `len(nf) == 6` and concluding "no shell degree of freedom is
expressible" was reading the wrong object.

WHAT THIS PROBE ACTUALLY MEASURED, and it stands as that: numeric magnitudes
at the single point q = q_0. Evaluating at q_0 collapses the whole filtration
into one float per basis element, so a negative here is a negative about
magnitudes at a point -- NOT about the graded structure, which this probe
never looked at. Scope (a), and narrower than it was written.

THE OBJECT TO MEASURE INSTEAD is the symbolic NF over Q(q, sqrt q) --
`hecke_core_symbolic.build_atom_nf_sym(Z, N)` -- and its q-degree /
filtration shape. The corpus already ships the data model:
`gb-filtration-jet-order.witness.json` carries per word a
`filtration_certificate` (grade -> {perm, canonical_word, coefficient_in_q}),
a `filtration_shape` (grade -> multiplicity), and a `jet_log` recording
`filtration_before -> filtration_after` per reduction step. Measured, the
order rises with interactions: electron sigma_1^3 gives q^2 - 1 + q^-2, the
proton body (sigma_1 sigma_2^-1)^3 gives
-q^5 + 4q^3 - 7q + 7/q - 4/q^3 + q^-5. And at A=1 the symbolic NF already
separates p from n by q-degree (max 11 / ops 169 vs max 10 / ops 103) -- a
distinction the numeric NF at q_0 cannot express at all.

ALSO RETRACTED: "A=4 is the end of the road; A=5 needs 686 GB". That is
max_lambda d_lambda^2, the cost of storing a general OPERATOR in the largest
irrep -- a property of the representation chosen here, not of the
construction. The corpus algorithm for this object is O(N * dim H_n(q)),
LINEAR in the Hecke dimension (`mba-step08-jet-prefix`, Complexity), and the
symbolic NF is 6 coefficients for ANY nucleus at ANY A: the state does not
grow with A, only the polynomial degree does.

Tracked in bean `qou-tower` (REOPENED).

## 🛑 THE GRADING CARRIES NO MAGIC SIGNAL EITHER — and that closes the arc

Follows the owner correction that reopened this bean. The retraction was
right: the GS reduction *digests* entanglement into the coefficients rather
than destroying it, and the q-degree is the surviving grading. So the grading
was measured directly —
[`symbolic_nf_q_degree_magic_probe.py`](../computations/probes/symbolic_nf_q_degree_magic_probe.py),
exact over `ℚ`, never evaluating at any numerical `q`.

**Gate first:** 18/18 exact coefficient checks against the corpus's own
`hecke_core_symbolic.build_atom_nf_sym`, 5303 s, *all coefficients agree
exactly*. The numbers below are reportable because of that, not despite it.

**Result: `interleaved` at every level, every observable.**

    A = 2 .. 20   (reaches Z = 2, 8 and 20 — three magic numbers)
    max_degree / degree_span / n_terms / support_size
        interleaved at EVERY level
    ANY graded observable replicating across levels:  False
    levels where degree_span separates magic cleanly:  0 / 19

**Both directions of the correction are now confirmed.** The order structure
**is** real — it survives the reduction, and it separates the proton from the
neutron, which is kernel-checked as
`QOU.BraidKnot.LaurentWalk.proton_ne_neutron_degrees` and is a distinction the
numeric NF at `q₀` cannot express at all. It simply carries no *magic* signal.

### The artifact that would have faked a positive is PARITY — sixth instance

I first hypothesised `degree_span` was monotone in `Z` at fixed `A`. **Wrong**
— only 6 of 19 levels are monotone. What is actually there is an even/odd
zigzag concentrated at low `Z`. At `A = 20`:

    Z     4    3    2    1    0
    span  562  596  458  560  420      odd Z sit ABOVE their even neighbours

Local minima favour **even** `Z` on **13 of 17** levels. Every magic number is
even, so *"magic Z has low degree span"* would have been measuring parity, not
shell structure — the same artifact that killed the δ²Φ result, the ⁴He NF
collapse and the A=3 participation split. The per-level control reported
`interleaved` and refused it.

### Where this leaves the search

Three independent places have now been measured with exhaustive fixed-A
controls and all are negative: the **numeric NF at q₀** (6-vector, every
nucleus), the **full H_{3A} tower** (A = 2,3,4 exhaustively), and the
**q-degree grading** (A = 2..20, reaching Z = 2, 8, 20). A shell degree of
freedom is not in the state, not in the tower, and not in the grading. It
would have to enter the *construction* — before or outside the GS reduction —
rather than be recovered from any of them.

## 🛑 A seventh control failure, caught by a sibling before it cost anything

A parallel session (#6304, `claude/nf-q-degree-2026-08-30`) built the same
Laurent walk independently and caught a confound in an observation I made
while the scan was still running.

**What I claimed:** *"the degree span is non-monotone in A — it peaks at A=5
(94) and then falls (86, 76, 72 at A=6,7,8) … whether that has anything to do
with shell structure is exactly what the exhaustive scan is for."*

**What is true:** those four numbers are the **Z = 0 column** and nothing else.
Verified against my own witness after the fact:

    my Z=0 column:  A=4→76  A=5→94  A=6→86  A=7→76  A=8→72
    max over Z:     22, 48, 76, 106, 138, 172, 208, 246
    second diffs:    2,  2,  2,  2,  2,  2      exactly quadratic, lead coeff 1

So the span is **strictly increasing and quadratic in A**; the "falling" series
is pure-neutron matter. Holding `Z = 0` while varying `A` varies the
**composition** at the same time as the mass number — the classic
one-variable-at-its-boundary confound, and the same family as the six already
recorded here.

It cost nothing because it never reached a durable artifact — the shipped
analysis is fixed-A throughout, and the probe docstring, the Lean and the PR
body all describe that. But it was on its way to being the *motivating signal*
for a scan explicitly hunting Z=8 and Z=20, which is exactly how a fitted
reading gets born.

**The sibling also confirmed the real finding from the other side.** They
flagged `Z=1 → Z=2` at A=8 (164 → 158) as *"the axis a shell signal would live
on"* and correctly declined to call one dip a pattern. It is a pattern, and it
is parity: counting local minima in Z at fixed A over A = 8..20 gives **24 at
even Z and 0 at odd Z**. Their dip is its first member. Every magic number is
even, so a shell reading of that axis fits parity.

And the two implementations agree **exactly at A=8 across all nine
configurations** (72, 164, 158, 200, 210, 228, 238, 244, 246), not just at
A=1 — two sessions, two independent programs, one answer.

**Technique note worth keeping:** their gate compares the two builds *in
lockstep after every factor* rather than comparing final vectors. Mine
compares at the end, which is weaker precisely here — cancellation is what the
Z=0 line is made of, so a transcription error can be masked by a later
cancellation. Adopt lockstep if this walk is rebuilt.

---

## The grading identification is FALSE, and two of my own claims about it were wrong

The open question after the jet-shape probe was whether the GS word-length
filtration I measured (Coxeter length of the H₃ normal form, values 0..3) is
the bond-product / Mayer grading the corpus proves things about (values
0..|s|, |s| = C(A,2) bonds). Measured on the canonical builder, with a control
that the sweep IS the canonical builder:

**No — and not for the reason I gave.** Two retractions first:

1. I wrote that `QOU.Mass.BodyOrderJetGrading.body_eq_graded` is "an assumed
   hypothesis field … the premise is assumed rather than established". It is a
   field of that structure, but it is **discharged** for the bond-product
   model by `body_eq_graded_of_bond_product`
   (`QOU/Knot/BodyOrderExpansion.lean:138`, proof `esymm_eq_compl_sum s d hn`,
   sorry-free). Nothing is left assumed there.
2. I wrote that the two models "index in opposite directions". They do not.
   `prod_bonds_graded` **defines** `gradedTerm n` as the coefficient at bond
   grade `|s| − n`; `esymm_eq_compl_sum` is precisely the complement bijection
   that absorbs the reversal. There was never a direction mismatch.

What actually blocks the identification is measured, not assumed:

- **Cardinality.** Bond-product grading: `C(A,2)+1` values — 7 at A=4, 191 at
  A=20. GS word-length grading: **4**, at every A. No bijection exists.
- **The ceiling is reached, not stipulated.** Starting from the empty word the
  support grows `{0} → {0,1} → {0,1,2} → {0,1,2,3}` over the first three
  crossings and then **never grows again**, at any bond count.
- **The folding is lossy on bond count.** At Z=2, N=2 the seven bond counts
  m = 0..6 give only **6** distinct normalised shapes (m=5 ≡ m=3). Over the
  222 configurations (Z, N ≤ 4; every m ≤ C(A,2)) there are **115 collisions**
  and only **107** distinct shapes. The H₃ normal form does not determine even
  the *number* of inter-nucleon bonds.

**Third retraction, mine, same session.** A scratch sweep that appended extra
mixed bonds *past* C(A,2) gave 13 distinct shapes for 13 bond counts, and I
was about to report "bond count is recoverable from the H₃ shape". On the
canonical construction it is the opposite. The toy laid every bond as
`MINUS_H_HALF` at the end of the word; the canonical builder interleaves
type-dependent bonds (pp→`ZERO_D`, nn→`MINUS_H`, pn→`MINUS_H_HALF`) after each
nucleon block. Monotone appending gives monotone term growth, hence spurious
injectivity. **Control: keep-all reproduces `build_atom_nf_lau` exactly on all
24 configurations** — added to the probe as an assertion so a lookalike
construction cannot pass again.

**Collision offsets are even** (m=5≡3, m=6≡4, m=8≡4, m=10≡4). Parity, an
eighth time on this arc.

**Consequence.** The ceiling fact stands and is unconditional, but it does not
license a body-order reading — the identification it would need is false, not
merely unproved. It is also *stronger* than the identification would have
been: the ceiling is not "191 grades folded faithfully into 4", it is lossy
folding. Any surviving many-body information lives in the **weights** on four
grades, never in the grade index. This probe does not exclude that.

PR #6333.


---

## 🛑 SCOPE CORRECTION (2026-09-04, bean qou-hu1f) — "the production chain" is too wide, and the substance survives it

This bean's title and §2 say `build_atom_nf_mp` collapses **"the production
chain"**. Measured, it has **seven consumers**: five probes, plus
`all_nuclides_sdp_admissibility_mp.py` (a producer with a committed witness) and
`qbeta_level_k_binding_operator_probe`. It is **not** the canonical mass path --
that is `canonical_mass.py`, per the mass-formula guardrail in AGENTS.md.

**The correction does not rescue the tower**, because the canonical path is H_3
too, by a **different mechanism**. `binding_canonical.py` calls its own current
path `tower_binding_full (H_3 tower)` (:37), builds from "the H_3 building
blocks tr_M^3(p), tr_M^3(n)" (:324), and bridges "tau_p, tau_n via the Wenzl
bridge at H_3" (:341), while carrying `n = 3 * (Z + N)` (:528) as the nominal
strand count.

Two routes to H_3, and they must not be conflated:

- **NF route** (`build_atom_nf_mp`) -- a growing word is REDUCED to 6 dimensions
  after every crossing. The tower is built and destroyed. **This bean measures
  this one.**
- **Canonical route** (`binding_canonical`) -- per-nucleon H_3 traces are
  COMPOSED. The tower is never built, so there is no reduction to point at and
  this bean's argument does not reach it.

### The central claim reproduces, at a case this bean never tested

Re-run directly against `compound_shift_nf.build_atom_nf_mp` (a bean is not a
primary source, including this one):

    hydrogen A=1    nominal n= 3 strands  -> NF has 6 components
    4He      A=4    nominal n=12 strands  -> NF has 6 components
    16O      A=16   nominal n=48 strands  -> NF has 6 components

**16O** -- a nominal `H_48` object carried as six numbers -- is sharper than the
Pb-208 row already here, because it was run rather than reasoned.

### And it collides with an owner ruling this bean predates

The owner ruled **2026-09-03** that derivations must be carried on the **full
tower** (both senses: all `n`, all orders in `q`).
`2026-09-03-sm-26-term-status.md` §10 applies that ruling to the **SM** surface
only -- it never mentions mass or binding. Meanwhile `build_atom_nf_mp` appears
in **zero** files under `docs/` or `content/`, so this finding had no durable
home to be found from. Written up in
`docs/audits/2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md`.

### The measurable step this bean stopped one move short of

The full-tower walk here measured **distributional** quantities -- top-block
share, participation ratio, argmax partition -- against magic numbers. It never
compared **a binding energy**. So this is open and reachable:

> does the A <= 4 full-tower walk reproduce the canonical H_3 binding numbers?

Yes => H_3 is a faithful order-zero rendering and the ruling is satisfied in
substance. No => the two routes disagree, and that gap is a bigger finding than
the magic-number negative this bean closed on. Tracked as `qou-hu1f`.


---

## 🛑 CORRECTION (same day) — I was wrong about the canonical route, and it was the important half

The entry above says `binding_canonical` is H_3 too and that on the canonical
route "the tower is never built". **False.** Its DEFAULT path
(`use_transfer=True`) is the fine-Bratteli transfer matrix and sums the Frobenius
pairing over EVERY partition of `3A`. Measured, not read:

| nucleus | `n = 3A` | `n_partitions` | `p(3A)` |
|---|---|---|---|
| 2H  | 6  | **11** | 11 |
| 3He | 9  | **30** | 30 |
| 4He | 12 | **77** | 77 |

Exact at every level. **The canonical binding path is full-tower in `n`** and
already satisfies that half of the 2026-09-03 ruling.

**The trap, because it is reusable.** I cited `binding_canonical.py:37`, `:324`
("the H_3 building blocks tr_M^3(p), tr_M^3(n)") and `:341` (Wenzl bridge at
H_3). Those lines exist — but **:324 and :341 are inside the
`use_closed_form=True` branch**, a non-default alternative kept for one caller
family. Three grep hits naming H_3, and I inferred the default from them without
checking which branch they sat in. **A grep hit inside a branch that does not run
is not evidence about the path that does.**

### What survives, and it is sharper than what I claimed

- `build_atom_nf_mp` really does collapse to 6 components at every A — measured
  here at hydrogen, 4He and **16O** (nominal `H_48` carried as six numbers).
- The 2026-09-03 ruling has still been applied to **neither** route in any doc.
- But the two routes are **different objects**: canonical = full tower in `n`;
  NF = no tower at all. So the live question is not "does the mass surface
  honour the ruling" — it is **do the two routes agree**, and any probe that
  reasons from `build_atom_nf_mp` to a claim about *the framework's* binding is
  reasoning about the wrong object.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-04 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.

## Progress Update (PR #8278 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/IsospinChannelReachabilityAndB3ChainSign.lean`, `QOU/MassTheory/PeeledMarkovDefectAndHigherInterleaving.lean`, `QOU/MassTheory/GradedLogPairCancellationAndH3TowerCollapse.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/isospin_b3chain_markov_defect_logjet_h3tower_probe.py` and 2-commit stamped witness `computations/probes/isospin-b3chain-markov-defect-logjet-h3tower-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8278](https://github.com/litlfred/qou/pull/8278) (`ready: b3288da132ea8d0d185d184a5e18432c89e4858e`).
