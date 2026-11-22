# Large-A convention-D Markov trace of the v9 element — structure search (bean `qou-m7py`)

**Question.** Is there mathematical structure that lets us compute the
convention-D Markov trace of the v9 nuclear element exactly at A = 40
(⁴⁰Ar, ⁴⁰Ca) and A = 60 (⁶⁰Co)? The two-row tower method
(`computations/probes/markov_trace_two_row_tower_probe.py`, Rust port
`tools/hecke-engine/src/bin/tower_trace.rs`) costs about Catalan(A).

**Answer, in one paragraph.** No. None of the four candidate structures I
tested reduces the cost below exponential in A, and the q = 1 limit shows
why. The search turned up **one new exact method**: a planar tensor-network
contraction of the quantum trace. It costs about 2^A·A² rather than
Catalan(A)·A, it reproduces all 63 witness rows, and it extends the computed
range to A = 20. It does **not** reach A = 40: that would need a state of
2^40 (≈ 1.1·10¹²) high-precision numbers. The negative results below are
scope-(a), meaning "these constructions, as tested, do not give a cheap
route". No proved invariant rules out an exact polynomial algorithm.

All arithmetic is exact: mpmath at 70 dps for values at q₀, or integers
modulo the prime p = 536870909 at a random q for structure tests (ranks and
recurrences). There is no float arithmetic anywhere. Probe:
[`computations/probes/large_a_trace_structure_probe.py`](../../computations/probes/large_a_trace_structure_probe.py).

## 0. Setup, and three facts about the element used throughout

The element is
E = ∏_{k=1}^{A−1} ∏_{i=0}^{k−1} f(type_i, type_k; σ_i), multiplied on the
right in that order, with protons on strands 0..Z−1. The factors are:

- f(p,p) = σ
- f(n,n) = σ − h = σ⁻¹
- f(p,n) = σ − h/2

Here h = q − q⁻¹. The trace is the convention-D Markov trace with
z = q³/(q²+1).

**F1. The convention-D trace is the U_q(sl₂) quantum trace on (ℂ²)^{⊗A}.**

  tr(x) = Tr(K^{⊗A} ρ(x)) / [2]_q^A, with K = diag(q, q⁻¹) and
  ρ(σ_i) = Ř = [[q,0,0,0],[0,h,1,0],[0,1,0,0],[0,0,0,q]] on sites i, i+1.

By Schur–Weyl duality, (ℂ²)^{⊗A} = ⊕_k V_{A−2k} ⊗ S_{(A−k,k)} and
dim_q V_{A−2k} = [A−2k+1]_q, so this sum is exactly
Σ_k [A−2k+1]/[2]^A · χ_{(A−k,k)}. A check by hand at A = 2 gives
tr(σ) = q³/(q²+1) = z. The real check is that the network contraction built
on this formula reproduces the witness (§3).

**F2. The p–n factor is the average of the two crossings.**
σ − h/2 = (σ + σ⁻¹)/2. Its square is ([2]/2)²·1, so
s := (2σ − h)/[2] is an involution, s² = 1 (measured residual 1.8e-71).

**F3. At q = 1 every factor is the transposition s_i**, because h = 0. So
E|_{q=1} is a single permutation w_A that does not depend on Z, and

  tr(E)|_{q=1} = 2^{c(w_A) − A},

where c is the number of cycles. Under Schur–Weyl at q = 1, the trace of a
permutation on (ℂ²)^{⊗A} is 2^{cycles}. The permutation obeys the recursion
P_{n+1} = P_n[1:] + [n, P_n[0]]: each row takes the strand in slot 0 to the
top slot.

## 1. Idea 1 — twists Δ, Δ² and a Jones-type closure

**What it means.** If E were Δ^m·(local pieces), with Δ² central and acting
by a scalar on each irrep, the trace would collapse to a sum over k of
[A−2k+1]·f_{(A−k,k)}·(scalar).

**What was tested.** The q = 1 shadow w_A from F3, using
`staircase_perm` / `cycle_type` (probe lines 72–94) and `mode_q1`.

**Result.** w_A is neither the identity nor the longest element w₀, and its
cycle type changes erratically with A:

| A | cycle type of w_A | A | cycle type of w_A |
|---|---|---|---|
| 5 | [5] | 12 | [10, 2] |
| 7 | [3, 2, 1, 1] | 16 | [5, 5, 5, 1] |
| 8 | [4, 4] | 18 | [18] |
| 10 | [4, 2, 2, 1, 1] | 20 | [10, 10] |
| **40** | **[27, 9, 3, 1]** | **60** | **[55, 5]** |

Three consequences follow.

1. E is not a power of the full twist. Δ^{2m} specialises to the identity at
   q = 1, and w_A ≠ 1 for every A ≥ 2.
2. E is not conjugate to Δ^{±1}. That would force w_A to be conjugate to w₀,
   whose cycle type is 2^{⌊A/2⌋}1^{A mod 2}.
3. The all-proton word ∏_k σ₀⋯σ_{k−1} is not the half twist. It is not even
   a reduced word: at A = 3 it is σ₀²σ₁, with permutation s₁. Its closure is
   T(2,4) at A = 4. At A = 7 it is a 4-component link with Euler
   characteristic −14, which no torus link has, because (p−1)(q−1) = 15 has
   no solution with gcd(p,q) = 4.

So the closure is not a torus link or twist family, and the slot-labelled
p–n factors (§4) give it no topological meaning anyway.

**Scope (a).** The construction "E = twist × local" is excluded by the q = 1
cycle-type invariant for the forms listed above (powers of Δ², and conjugates
of Δ^{±1}). I did not exclude a more elaborate twisted-torus decomposition.

## 2. Idea 2 — expand the p–n factors and use the block structure

**What it means.** Protons come first, so

  E = S_Z · M · ∏_{k=Z+1}^{A−1} (M · N_k),

where:

- S_Z = ∏_{k<Z} σ₀⋯σ_{k−1} is the all-proton staircase.
- M = g(σ₀)⋯g(σ_{Z−1}), with g = (σ+σ⁻¹)/2 by F2, and **M is the same
  element in every neutron row**.
- N_k = σ_Z⁻¹⋯σ_{k−1}⁻¹.

**What was tested.**

- Does the p–n block admit braid isotopy? The involutions s_i do not satisfy
  the braid relation: max |s₀s₁s₀ − s₁s₀s₁| = 0.0119 on (ℂ²)^{⊗3}, at q₀,
  70 dps.
- Expanding g into ±1 crossings writes tr(E) as an average of
  2^{pn} = 2^{ZN} braid-closure Jones invariants. That is 2^{400} terms for
  ⁴⁰Ca and 2^{891} for ⁶⁰Co.

**Result.** The decomposition is exact and is what the probe's `gate_list`
builds (probe line 61). It does not shorten anything. The mixed block is not
a braid, so it cannot be isotoped. The neutron rows N_k interleave with M
along the slot-Z worldline, so splitting the network into a proton region
and a neutron region cuts about 2N legs.

**Scope (a).** "Block factorisation + p–n expansion", alone, gives no
sub-exponential route.

## 3. Idea 3 — spin chain, MPO bond dimension, and the network contraction

**What it means.** By F1, tr(E)·[2]^A is the partition function of a
six-vertex-type network: one 4-leg tensor a·1 + b·Ř per gate, legs along
site worldlines, and the closure carrying K. A product of low-bond-dimension
MPOs, or a network with a narrow cut, would give polynomial or mild
exponential cost.

**Tested, part 1: operator-Schmidt rank of ρ(E)** across every site cut. This
is an exact rank mod p at a random q (`mode_osr`, probe lines 342–381). I
compared it with the **same network carrying random gate coefficients**,
which are equally U_q(sl₂)-symmetric:

| A | OSR per cut — v9 element, Z = A/2 | random coefficients |
|---|---|---|
| 8 | 4, 16, 64, 16, 16, 4, 4 | identical |
| 9 | 4, 16, 64, 64, 16, 16, 4, 4 | identical |
| 10 | 4, 16, 64, 64, 64, 16, 16, 4, 4 | identical |
| 11 | 4, 16, 64, 256, 64, 64, 16, 16, 4, 4 | identical |

- The maximum OSR grows like 4^{⌊(A+1)/3⌋}. That is the generic value for
  this circuit geometry: the v9 coefficients carry **no rank deficiency**
  beyond what the network shape forces.
- Only the all-p and all-n words (Z = 0 or A) dip, at one cut (40 vs 64 at
  A = 9, 160 vs 256 at A = 11). That dip is still exponential.
- An MPO with bond 4^{A/3} costs at least 4^{2A/3} to trace. That is worse
  than part 2.

**Tested, part 2: planar contraction.** I contracted the closed network in a
greedy minimum-cut order (`network`, `greedy_order`, `contract`; probe
lines 97–265).

- Validated **63/63** witness rows (A ≤ 16), worst |diff| = 4.8e-61. The
  witness is serialised to 60 digits, so this is agreement to its last digit
  (`mode_validate`, probe line 278).
- Independent cross-check at A = 17 (¹⁷O) against the Rust two-row tower
  (`hecke-tower-trace --chain 8:9`): all 43 printed digits agree.
  Rust: 2.000745044986577487327981918471747416521e-4.
- The largest cut is **A legs** for every A tested from 10 to 60
  (`mode_cutwidth`). This is the best of 13² × 7 linear sweep directions and
  about 60 greedy seeds; the linear sweeps gave A+2. Spin conservation
  across a closed planar cut lowers the state count from 2^A to at most
  C(A, A/2).

**Cost.** Measured wall time in pure-Python mpmath at 70 dps:

| A | wall time |
|---|---|
| 16 | ≈ 4 s |
| 17 | 30 s |
| 18 | 52 s |
| 19 | ≈ 143 s |
| 20 | ≈ 245 s |

| | network: state 2^A (≤ C(A, A/2) with S_z) | two-row tower: Catalan(A) |
|---|---|---|
| A = 20 | 1.0·10⁶ (1.8·10⁵) | 6.6·10⁹ |
| A = 40 | 1.1·10¹² (1.4·10¹¹) | 2.6·10²¹ |
| A = 60 | 1.2·10¹⁸ (1.2·10¹⁷) | 1.6·10³³ |

At A = 40 the state alone is 1.4·10¹¹–1.1·10¹² MPFR numbers, about 5–35 TB
at 70 dps, with about 780 gate sweeps over it. **Infeasible.** A Rust/MPFR
port of the network would plausibly reach A ≈ 26–28 (2^28 numbers ≈ 9 GB).
That is an estimate, not a measurement.

**Lower bound for this route.** The network contains a square-lattice
triangle with about A²/2 nodes. Its pathwidth is Ω(A), so no contraction
order beats 2^{Θ(A)}. The constant may sit between about A/3 and A; I found
nothing below A.

**Scope (a).** Neither MPO compression nor planar contraction is
polynomial. Planar contraction is the cheapest exact method found, and it
is exponential.

## 4. Idea 4 — Baxterisation, Yang–Baxter, commuting transfer matrices

**What it means.** Each factor is α − e_i with e = q − σ, so each factor is a
Baxterised Ř at some spectral parameter:

| factor | spectral point (Ř(x) = xσ − x⁻¹σ⁻¹) |
|---|---|
| pp | braid limit, x → ∞ |
| nn | other braid limit, x → 0 |
| pn | x = i, the point where Ř² ∝ 1 |

If the parameter at each crossing were θ_a − θ_b for the two *physical*
strands meeting there, the Yang–Baxter equation would let us rearrange E
into commuting transfer matrices (algebraic Bethe ansatz).

**What was tested.**

- Who crosses whom. In row k, read left to right, the strand in slot 0
  travels to slot k, and σ_i crosses it with the occupant of slot i+1. The
  weight is chosen by the **slot** labels (type_i, type_k), not by the
  physical strands. Slot 0's occupant changes every row
  (P_{n+1} = P_n[1:] + [n, P_n[0]]).
- The three values the weights take: two protons, a proton and a neutron,
  and two neutrons would each need θ_a − θ_b to be +∞, iπ/2 and −∞ for the
  same pair-type. No finite inhomogeneities do that.
- The braid relation fails for the pn involution (§2).

**Result.** E is not an integrable (difference-form) network, so there is no
commuting-transfer-matrix factorisation to exploit. The sweep identity
Ř₀₁Ř₁₂⋯ = (cyclic shift)·R_{a,k}⋯R_{a,1} does rewrite each row as a
monodromy of the travelling strand. The shifts compose to the erratic w_A,
though, and that destroys the commuting structure.

**Scope (a).** Baxterisation, as the element is defined, gives no
integrable reduction.

## 5. A further test — recurrences in A at fixed Z

I tested the sequence a_A = [2]^A·tr(E) mod p at a random q
(`mode_recur`, probe lines 409–440) for Z = 0, 1, 2 (A = 2..21) and Z = 8
(A = 9..21). Two searches:

- Berlekamp–Massey linear complexity came out 10, 10, 10 and 7 for 20, 20,
  19 and 13 terms. That is the maximal, generic value, so there is **no
  constant-coefficient linear recurrence of order ≤ 9** (≤ 6 for Z = 8).
- A q-holonomic search Σ_{j≤d} Σ_{e≤δ} c_{je} q^{eA} a_{A+j} = 0, for
  (d, δ) = (1,3), (2,2), (2,3), (3,1), gave nullity 0 in every case, so no
  recurrence of those orders.

There is a structural reason to expect this. By F3,
a_A|_{q=1} = 2^{c(w_A)}, and c(w_A) jumps erratically (1, 4, 2, 1, 5, 2, 4,
1, 2 cycles at A = 6, 7, 8, 9, 10, 12, 16, 18, 20; 4 at A = 40; 2 at A = 60). A q-holonomic
recurrence whose specialisation at q = 1 does not degenerate would make
2^{c(w_A)} P-recursive. I have not proved that this is impossible, so this
is evidence, not a theorem.

**Scope (a).** No low-order recurrence exists in the orders searched.
Extrapolating from A ≤ 20 to A = 40 is therefore not available as an exact
method. It would in any case be a fit under §NO FITTING.

## 6. New values beyond the witness (network contraction, mpmath 70 dps)

Written to
[`computations/probes/large-a-trace-network-extension.witness.json`](../../computations/probes/large-a-trace-network-extension.witness.json)
by `mode_extend`. This uses the same element and the same `tr_markov_d`
normalisation (÷ 2^pn) as the two-row tower witness. ¹⁷O is cross-checked
against Rust (§3).

**Cross-check against the two-row tower, added 2026-11-15.** Seven rows also
have a Rust two-row tower value in `markov-trace-two-row-tower-rust.witness.json`
(#7800): ¹⁷F, ¹⁸F, ¹⁹F, ¹⁷Ne, ¹⁸Ne, ¹⁹Ne and ²⁰Ne. All seven are **identical
in all 60 serialised digits** (|difference| = 0 when both strings are read at
80 dps). ¹⁹F and ²⁰Ne have a third method as well, the column-wise tower of
#7775. ¹⁸O–²⁰O, ²⁰F and ²¹Ne have only the network computation behind them so
far; a tower run for ²¹Ne is in progress.

²¹Ne was added on 2026-11-15 by the same producer
(`extend --chains 10:11:11`). Its wall time is not comparable with the other
rows, because it shared four cores with another job.

| isotope | Z | N | A | tr_markov_d (first 40 digits) | wall (s) |
|---|---|---|---|---|---|
| 17o | 8 | 9 | 17 | 0.000200074504498657748732798191847174741652 | 30.3 |
| 18o | 8 | 10 | 18 | -0.00001195900550309935666728067987191151368 | 51.8 |
| 19o | 8 | 11 | 19 | 0.000003406112675646868204829036532247952018 | 142.9 |
| 20o | 8 | 12 | 20 | -0.00000046404113297844828585493379198662040 | 246.1 |
| 17f | 9 | 8 | 17 | 0.000705752846265963739828094742515246835711 | 30.0 |
| 18f | 9 | 9 | 18 | -0.00000838339050971060125873300434438127364 | 53.6 |
| 19f | 9 | 10 | 19 | 0.000044557113274236630339840890429261085757 | 143.1 |
| 20f | 9 | 11 | 20 | -0.00000231971119312230690847396776964833757 | 242.1 |
| 17ne | 10 | 7 | 17 | 0.003373541527612597305899816434015970378693 | 30.1 |
| 18ne | 10 | 8 | 18 | 0.000067152681484991843799942083531522172793 | 52.4 |
| 19ne | 10 | 9 | 19 | 0.000148746379488971517025899906709594433874 | 154.5 |
| 20ne | 10 | 10 | 20 | -0.00001121972109603442494693384247311459215 | 254.4 |
| 21ne | 10 | 11 | 21 | -0.00000111369018222330944886508394912425428 | 426.6 |

Wall times are single-threaded pure-Python mpmath (no gmpy backend); they grow by about 2× per strand, as a 2^A state predicts. The rows printed here are the first digits of the 60-digit serialised values.

## 7. Summary of costs for the target nuclei

| method | A = 40 | A = 60 | status |
|---|---|---|---|
| two-row tower (Python dense / Rust DFS) | ~Catalan(40)·40 ≈ 10²³ | ~10³⁵ | infeasible |
| planar network (this probe) | state 2^40 (≥ C(40,20) = 1.4·10¹¹), × 780 gates | 2^60, × 1770 gates | infeasible; reaches A ≈ 20 in Python, an estimated ≈ 26–28 in Rust |
| twist / closure reduction | excluded for Δ^m and conjugates of Δ^{±1} (F3 invariant) | same | no route |
| MPO compression | bond ≈ 4^{⌊(A+1)/3⌋} = 4^{13} ≈ 6.7·10⁷ | 4^{20} | worse than the network |
| integrable / commuting transfer matrices | weights are not difference-form | same | no route |
| recurrence in A | none at the orders searched; q = 1 shadow erratic | same | no route (and would be a fit) |

**Open, and recorded as such.** No polynomial algorithm is known, and none
is excluded. Evaluating the Jones polynomial is #P-hard at generic q in
general, but this is one specific family, and that general result does not
decide it. What would change the picture is a closed form for E's two-row
characters, i.e. a structure that diagonalises it in the Gelfand–Tsetlin
basis. None was found.
