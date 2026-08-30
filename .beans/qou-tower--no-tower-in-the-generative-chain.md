---
# qou-tower
title: 'There is no tower: the production chain reduces every nucleus to the same 6 dims'
status: in-progress
type: task
priority: high
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-08-30T16:10:00Z
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
