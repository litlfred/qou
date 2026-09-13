# Re-embedding the binding word on 3A strands: the obstruction is the coupling graph, not the embedding

**Bean:** `qou-w6x3` — option 2 of `qou-hxz4` / PR #7173.
**Probe:** [`computations/probes/binding_word_3A_reembedding_probe.py`](../../computations/probes/binding_word_3A_reembedding_probe.py) (18/18, 47 s).
**Lean:** [`QOU/Hecke/ContiguousCouplingGraph.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/ContiguousCouplingGraph.lean) (7 declarations, sorry-free).
**Witness:** `computations/probes/binding-word-3A-reembedding.witness.json`.

Precision: `mpmath.mpf` throughout at 70 dps; `q₀` from `Q_50_DIGIT_STR`, the
proton pin, taken as a decimal string. No float64, no `statistics`, no `math`.
The layout searches are exact integer combinatorics.

## The question

PR #7160 proved that a **level-local** word — one whose letters group into
consecutive blocks with pairwise disjoint generator sets — has a dimension-free
seminormal character,

    χ^λ(T_β) = Σ_{T ∈ SYT(λ)} Π_j ⟨T | F_j | T⟩ ,

and shipped `computations/chi_path_sum_seminormal.py`. That took ⁵Li to 2.5 s
over 176 partitions and ⁶Li to 8.5 s over 385.

PR #7173 (`qou-hxz4`) measured that the words
`hecke_core_legacy.unified_iterative_correction` hands its Rust kernel are
**not** level-local for any atom or any partition size `k`, and that no
trace-preserving reordering repairs that. It diagnosed the cause as the
**fixed-`H_k` embedding**: `_step_chain_generic` cycles the generator index
`g mod (k−1)`, so every letter of every step touches every generator.

Its **option 2** was to re-embed on **3A strands** — the layout
`mass_at_3A_proper.atom_braid_word_3A` uses, where nucleon `k` owns strands
`3k, 3k+1, 3k+2` and its intra-nucleon crossings are the single generators
`σ_{3k}`, `σ_{3k+1}`. This is that measurement.

## Verdict

**The 3A re-embedding does not restore level-locality for `A ≥ 3`, and the
reason is not the one #7173 named.** The obstruction is the **coupling graph**,
which the change of embedding does not touch.

`A = 2` is the sole exception and it works completely — and there the character
**moves**, so option 2 is a re-derivation exactly as the owner was told.

## 1. The two coupling structures (measured, not read off docstrings)

Instrumenting `_step_chain_generic` directly: for each step `i` it appends one
inter-nucleon letter **per previous nucleon** (`for ti in prev_types`). Summed
over steps that is `0 + 1 + … + (A−1) = C(A,2)` — **the complete graph `K_A`**.
`atom_braid_word_3A` emits its bond only between consecutive nucleons, at
generator `3k+2` — `A−1` bonds, **the path `P_A`**.

| A | binding inter letters | C(A,2) | mass inter letters | A−1 |
|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 1 |
| 3 | 3 | 3 | 2 | 2 |
| 4 | 6 | 6 | 3 | 3 |
| 5 | 10 | 10 | 4 | 4 |
| 6 | 15 | 15 | 5 | 5 |

The mass word's segmentation, via the shipped `segments_of`, is `2A−1` segments
with **largest generator set 2** — the dimension-free structure #7160 exploits.
The fixed-`H_k` binding word is a **single** segment, re-confirming #7173
against this branch's code.

## 2. What a linear 3A layout can supply

A single-generator coupling between nucleons `i` and `j` needs an adjacent
strand pair with one strand in each. Exhaustively:

| A | n = 3A | C(A,2) | adjacencies 3A−1 | contiguous graph always P_A | K_A contiguous | K_A any layout |
|---|---|---|---|---|---|---|
| 2 | 6 | 1 | 5 | yes | **yes** | yes |
| 3 | 9 | 3 | 8 | yes | no | yes |
| 4 | 12 | 6 | 11 | yes | no | yes |
| 5 | 15 | 10 | 14 | yes | no | yes |
| 6 | 18 | 15 | 17 | yes | no | yes |
| 7 | 21 | 21 | 20 | yes | no | **no** |

Two separate exclusions:

* **Contiguity ⇒ path.** Over every contiguous layout (all `A!` block orderings,
  `A = 2…7`) the coupling graph is exactly `P_A`. `K_A` is reachable **iff
  `A ≤ 2`**. Proved for general `A` in
  `ContiguousCouplingGraph.complete_coupling_forces_A_le_two`.
* **Layout-free counting.** A linear arrangement of `3A` strands has only
  `3A−1` adjacent pairs, so `K_A` is impossible once `C(A,2) > 3A−1` — that is,
  from **`A = 7`, which is ⁷Li**. Proved as
  `pair_count_exceeds_adjacency_budget`; the exhaustive DFS agrees, finding
  witnesses at `A = 2…6` and none at `A = 7`.

### The escape costs exactly what it buys

Dropping contiguity does make `K_A` reachable for `3 ≤ A ≤ 6` — but the
intra-nucleon crossings are single generators *only* under contiguity.
Exhaustively over every `K_A`-realising layout:

| A | layouts realising K_A | max contiguous nucleon triples |
|---|---|---|
| 3 | 234 | 2 of 3 |
| 4 | 5 736 | **0 of 4** |
| 5 | 64 986 | **0 of 5** |

From ⁴He up, **not one nucleon** of a `K_A`-realising layout keeps its three
strands together, so every intra-nucleon crossing would need conjugating too.
`A = 3` is a lone partial case.

## 3. The conjugated-bond route, and what it costs

A non-adjacent pair can be coupled by conjugating a boundary crossing —
walk nucleon `i`'s top strand up with `T_w = σ_{3i+2}⋯σ_{3j−2}`, cross at
`σ_{3j−1}`, walk back. Built explicitly and segmented:

| A | n | L | segments | segment sizes | largest | of | order-free floor | mass word |
|---|---|---|---|---|---|---|---|---|
| 2 | 6 | 23 | 5 | 1,1,1,1,1 | 1 | 5 | — | 3 segs, max 2 |
| 3 | 9 | 42 | 3 | 1,1,6 | 6 | 8 | 4 | 5 segs, max 2 |
| 4 | 12 | 74 | 3 | 1,1,9 | 9 | 11 | 7 | 7 segs, max 2 |
| 5 | 15 | 125 | 3 | 1,1,12 | 12 | 14 | 10 | 9 segs, max 2 |
| 6 | 18 | 201 | 3 | 1,1,15 | 15 | 17 | 13 | 11 segs, max 2 |

Only nucleon 0's two generators survive as their own segments; everything else
merges into one segment of `3A−3` of the `3A−1` generators — all but two,
growing linearly in `A` against the mass word's constant 2. The
**order-free floor is `3A−5`**: the conjugating walk *brackets* its crossing, so
generators `[2, 3A−4]` share a segment wherever the remaining letters are
placed. The measured `3A−3` is specific to this emission order; the floor is
not.

**Measured price at `A = 3`** — same algebra `H_9`, same 30 partitions of 9:

    level-local mass word (max segment 2):      0.349 s
    conjugated binding word (max segment 6):   41.311 s      118× slower

The path sum has degenerated into the dense seminormal trace the route existed
to avoid.

**The ratio is wall-clock and varies between runs — do not quote it as a
constant.** Two runs of the same probe on the same tree gave `0.349 s / 41.311 s`
(118×) and `0.335 s / 41.685 s` (124×). Every *mathematical* assertion in the
witness is byte-identical between them; only the timings and the provenance
stamps move. The load-bearing figure is the **segment size** — `3A−3` of `3A−1`
generators against a constant 2, which is exact combinatorics and does not
vary — and the two-orders-of-magnitude gap it produces. "Roughly 120×" is the
honest phrasing.

## 4. `A = 2` works — and the value moves

At `A = 2` the binding coupling `C(2,2) = 1` **is** the chain `A−1 = 1`, so the
deuteron word re-embeds with no conjugation at all. It is level-local with
**every segment holding one generator** — finer than the mass word's, because
the binding producer's intra chain is *grouped* (seven letters on `3k`, then
four on `3k+1`) where `atom_braid_word_3A`'s is *alternating*. The path sum runs
**7.8× faster** than on the fixed-`H_k` word.

Both words then live in the **same `H_6`**, carry the **same 23 letters** with
the same `(c, d)` offsets, and differ **only** in which generator each letter is
assigned to. That isolates the embedding exactly. `χ^λ` for every `λ ⊢ 6`:

| λ | dim | χ fixed-`H_k` | χ 3A | relative |
|---|---|---|---|---|
| [6] | 1 | 1.55987019956 | 1.55987019956 | 3.5e-71 |
| [5,1] | 5 | −0.827205187582 | **+3.21631734224** | 1.257 |
| [4,2] | 9 | −0.723775461914 | +1.67439526203 | 1.432 |
| [4,1,1] | 10 | +1.12315502702 | −0.469805886378 | 1.418 |
| [3,3] | 5 | +0.607391469465 | +4.24940202292 | 0.857 |
| [3,2,1] | 16 | −0.0198841499897 | −1.97227244615 | 0.990 |
| [3,1,1,1] | 10 | −0.701358255758 | −0.490125652323 | 0.301 |
| [2,2,2] | 5 | +0.721835313965 | −3.49729440651 | 1.206 |
| [2,2,1,1] | 9 | −0.616562022823 | −0.819654948504 | 0.248 |
| [2,1,1,1,1] | 5 | +0.963194639863 | +2.15525533745 | 0.553 |
| [1⁶] | 1 | −0.676876683433 | −0.676876683433 | 1.3e-71 |

**Nine of eleven move, several change sign.** Cross-checked against an
independent dense Young-seminormal matrix product (built from
`hecke_core_legacy._build_ysn_matrices`, a different implementation) at
`< 1e-45` relative on both words, every partition.

The two one-dimensional irreps are **blind** to the embedding: `ρ(σ_i) = q` for
`λ = (6)` and `−q⁻¹` for `λ = (1⁶)` independent of `i`, so
`χ = Π_pos (q + d_pos)` and `Π_pos (−q⁻¹ + d_pos)` exactly. The whole move sits
in `dim ≥ 2`.

### A latent trap in the corpus — at ONE of two sites, not both

There are two nearby claims in `hecke_core_legacy.py` and they are **not** the
same claim. An earlier draft of this document quoted them as one sentence from
`_step_chain_22`'s docstring; that was wrong, and the difference is the whole
point.

**`hecke_core_legacy.py:1040–1042`** — the comment before the seminormal matrix
code — is the false one, and it is now corrected in place:

> *"The character χ_λ(σ_k) is independent of k (class function), so any
> embedding of crossings into σ_1, σ_2, … yields the same trace."*

The premise is true: all `σ_k` are conjugate. The conclusion does **not**
follow, because `χ` is a class function on the *group*, not a function of the
multiset of letters — `σ_1 σ_2` and `σ_1 σ_3` are not conjugate. The `A = 2`
table above is how false: 9 of 11 partitions move, by `O(1)` relative amounts,
with sign changes. Read at face value the sentence says a re-embedding is free;
it is a re-derivation.

**`hecke_core_legacy.py:1004`** — `_step_chain_22`'s docstring — makes only the
narrow claim, and that one is **TRUE**:

> *"(2,2) characters are independent of which σ_j we use because
> χ_{(2,2)}(σ_j) = h for all j."*

Measured: in `λ = (2,2)` at `n = 4`, `ρ(σ_1)` and `ρ(σ_3)` are the **same
matrix**, both `diag(q, −q⁻¹)` — because 1,2 share a row and 3,4 share a row in
one tableau, and share a column in the other. So `σ_1 ↔ σ_3` substitutes inside
**any** word without changing `χ^{(2,2)}`. The conclusion stands; the *reason*
given is weaker than the fact, since equal characters of single generators would
not suffice for a word. That distinction is exactly what the sentence two
paragraphs up gets wrong.

**One thing this audit does not claim.** An attempt to exhibit a direct
counterexample to the general claim inside `H_4` — `χ^{(3,1)}(σ_1σ_2)` against
`χ^{(3,1)}(σ_3σ_2)` — is **not** one: those two are equal by the `w₀`
conjugation `σ_i ↦ σ_{n−i}`, which `qou-hxz4` had already recorded as a genuine
trace identity, and the residual difference observed was ~1e-70, i.e. the floor
of the arithmetic and not a mathematical fact. The refutation rests on the
`A = 2` `H_6` measurement alone, where the moves are `O(1)`.

## 5. Scope classification

Per AGENTS.md §"Before declaring refuted / ruled out / dead end":

* **scope-(b), structural exclusion** — that a contiguous 3A layout admits the
  path `P_A` and nothing more, and that `K_A` needs `C(A,2) > A−1` couplings for
  `A ≥ 3`. Invariant cited: the interval lemma of `LayoutConflict.lean`,
  extended to non-adjacent blocks and to general `A` in
  `ContiguousCouplingGraph.lean` (sorry-free; `#print axioms` shows exactly
  `[propext, Classical.choice, Quot.sound]`).
* **scope-(b)** — that **no** layout whatever realises `K_A` for `A ≥ 7`: the
  counting bound `C(A,2) ≤ 3A−1`, proved for every `A`, plus the exhaustive
  check at `A = 7`.
* **scope-(a), scope-limited negative** — that the conjugated-bond escape
  destroys the dimension-free property. One explicit conjugation is built and
  measured. Its generator support is forced by the cut lemma (if `σ_g` is never
  used, no strand starting at position `≤ g` ever crosses one starting at
  `≥ g+1`), but no claim is made that *every* realisation of a non-adjacent
  coupling segments the same way.

## 6. Consumers, if the re-embedding were ever adopted

`binding_energy` (`hecke_core_legacy.py:2987`) is the entry point. Non-probe
consumers: `computations/canonical_mass_table_extended.py`, and the
`qou-mass` researcher facade (`qou-mass/src/qou_mass/api.py`,
`prediction.py`, `__init__.py`). Four `computations/deltalambda/` probes read it
as well. `unified_iterative_correction` itself has nine importers, of which
`computations/audits/lp_accumulator_kernel_gate.py` is a gate.

Adopting the 3A embedding would move every one of those numbers, and would also
require redefining the fixed partition table on `λ ⊢ 3A` rather than `λ ⊢ k`
(`k ≤ 11`) — `qou-hxz4` already flags the `C_λ` / Pass-2 gate as needing
re-definition.

**Nothing here is enacted.** Nothing is wired, no recorded number moves, and no
route is adopted: the `A = 2` character comparison is reported, not acted on,
because choosing an embedding by the number it produces is selection against the
target (AGENTS.md §"NO FITTING, EXCEPT CAL-1/2/3").

## 7. What this leaves open

The deuteron is the one atom where option 2 is available and it is also the one
`qou-hxz4` records as costing 942 s kernel-live. Whether a level-local `H_6`
deuteron word is the *right* object — as opposed to merely a faster one — is not
a question this measurement can answer, and picking it because it is faster
would be the same defect one level down. That is an owner call and is left in
the bean.
