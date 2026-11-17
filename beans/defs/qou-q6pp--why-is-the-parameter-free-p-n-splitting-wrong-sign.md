---
# qou-q6pp
title: Why is the parameter-free p-n splitting wrong-signed? (and was my own test even valid)
status: in-progress
pr: 8265
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T06:06:25Z
updated_at: 2026-10-10T07:01:39Z
parent: qou-v2om
---

## RETRACTION — my own committed claim was invalid, in two independent ways

ec7546ac7a (merged to main in #5622) states: 'PARAMETER-FREE p-n splitting,
nothing fitted: predicted corr(n) - corr(p) = -0.62398 MeV, CODATA m_n - m_p =
+1.29333 MeV, err -148.2 %, WRONG SIGN', and concludes that this REFUTES
canonicalization-review.md §3.1's claim that alpha* absorbs the chirality term.

**That conclusion is withdrawn.** The test could not have shown it.

### Error 1 — compared a correction against a leading term

thm:wedderburn-mass-formula is

    m(Z,N) = Z*m_p + N*m_n + Z*m_e + alpha*( Phi_1 - 2[3]_q*Phi_2 + h_A^2*Phi_3 )

so (m_n - m_p) is a LEADING term the formula CONSUMES AS INPUT, while
alpha*(Phi..) is the correction on top of it. The formula never predicts the p-n
splitting. I compared the difference of correction terms against the very
quantity the formula takes as given and called it a prediction.

### Error 2 — fed nucleon-internal chains into an atomic formula

    _PROTON_G0, _PROTON_G1 = nucleon_gen_chains(['u','u','d'])

Quark-level chains INSIDE one nucleon. The formula's M_i are drawn from the
ATOMIC braid A in H_{A+Z}(q). atom_gen_chains(Z, N) — in the same module,
which is how obvious this should have been — builds the right object, including
inter-nucleon and electron crossings.

Independent check that error 2 alone was fatal: with the nucleon chains the
correction for the proton is +0.1165 MeV against a hydrogen binding energy of
-1.36e-5 MeV. 8569x too large and the wrong sign, for a quantity that is
supposed to BE the binding.

## The correct test, and it is still a negative

alpha_gen_chains(Z,N), so alpha*(Phi..) should equal -B_AME:

    atom   Z,N     alpha*(Phi..)      -B_AME        ratio
    H-1   (1,0)      -7.39963621    -0.0000136     5e5 too large
    D     (1,1)      -3.22133812    -2.224566      1.4481  right sign, 45% high
    T     (1,2)      +1.51922867    -8.481798     -0.1791  WRONG SIGN
    3He   (2,1)      +4.67222883    -7.718043     -0.6054  WRONG SIGN
    4He   (2,2)      +6.42417246   -28.295674     -0.2270  WRONG SIGN

The correction becomes MORE POSITIVE as A grows while binding becomes more
negative — anti-correlated. And H-1, which has no nuclear binding at all, gets
-7.4 MeV where 13.6 eV is the whole answer.

So there IS a real sign problem. It is in the binding correction for A >= 3, not
in a p-n splitting the formula never claimed.

## What survives from ec7546ac7a

- The Phi_1/Phi_2/Phi_3 IMPLEMENTATION. Verified analytically; that verification
  is pure algebra and is independent of which chains are fed.
- Phi_3 = w*ln q with integer w, and Phi_2 = 2*ln(1 + h^2/4) being p/n-identical.
  Both are algebra about the chain words, and both hold for the chains named.
- alpha = m_e*8G is a DIFFERENT OBJECT from alpha*, sharing a glyph.
- **The alpha* EXCISION survives.** It rested on alpha* being a FIT (scale
  normalised on CODATA M_p, root-found on CODATA M_n, neither a CAL-1/2/3
  input). That ground is untouched by this retraction.

## What does NOT survive

The refutation of canonicalization-review.md §3.1. Whether alpha* was absorbing
the chirality term is **once again open** — my measurement did not test it.
Both docs and the commit message assert the refutation and must be corrected.


## Repair note

Two phrases in this bean were eaten by shell command substitution when it was
written: backticked (m_n - m_p) and atom_gen_chains(Z, N) were executed rather
than quoted, leaving two sentences without their subjects. Restored above.

Second time this session — the same trap also mangled a phrase in qou-l1gv.
Write bean bodies through a heredoc or a file, never as a shell argument
containing backticks.

## The defect is localised to Phi_1 — measured

Per-term decomposition with the correct atomic chains (alpha = m_e*8G):

    atom     a*Phi_1   a*(-2[3]Phi_2)   a*h^2 Phi_3     total    -B_AME
    H-1     -6.97252        -0.49542        +0.06830   -7.39964   -0.0000
    D       -2.08525        -1.23855        +0.10246   -3.22134   -2.2246
    T       +3.39845        -1.98168        +0.10246   +1.51923   -8.4818
    4He     +9.19178        -2.97252        +0.20491   +6.42417  -28.2957

1. PHI_1 IS THE WHOLE PROBLEM. It alone flips sign with A (-6.97 -> +9.19) and
   it dominates every row. Phi_1/L (L = total chain length) runs
   -0.155, -0.023, +0.025, +0.045, +0.047 for H-1/D/T/3He/4He: it is NOT
   extensive, crosses zero between D and T, and saturates near +0.047. A binding
   term must be monotone negative and grow with A. Phi_1 does the opposite.

2. PHI_2 IS WELL-BEHAVED: -0.495, -1.239, -1.982, -2.973 — monotone negative,
   roughly linear in A. Shaped like a binding term.

3. PHI_3 IS TINY AND INTEGER-QUANTISED. In units of h^2*ln q the weight w is
   EXACTLY 4, 6, 6, 12, 12 for H-1, D, T, 3He, 4He — i.e. w = 6Z once N >= 1,
   with the bare proton at 4.

## The defensible version of what I wrongly claimed

My retracted commit argued chirality cannot be what alpha* was absorbing, via an
invalid test. There IS a valid magnitude argument for the same conclusion, and
it needs no splitting test: Phi_3 contributes 0.07-0.20 MeV against deficits of
5-35 MeV. It is 1-3 % of the total and cannot close a gap two orders of
magnitude larger. That constrains MAGNITUDE only — scope-(a). It does not
exclude chirality from the formula, and it says nothing about what alpha*
absorbed in the 2-term frame, which remains open.

## Assumption that needs checking before anyone builds on this

alpha = m_e*8G is taken from cor:commutative-chirality-vanishes, which states it
for the COMMUTATIVE (q -> 1) reduction. I assumed the same alpha multiplies the
bracket in the full non-commutative formula. thm:wedderburn-mass-formula writes
"alpha" without redefining it, so this is the natural reading — but it is a
reading, not a verified identification, and every magnitude above scales
linearly with it. The SIGN results (Phi_1 flipping, Phi_2 monotone) are
alpha-independent and survive regardless.

## The Phi_1 localisation is NOT established either — same error, one level down

atom_gen_chains(Z, N) returns EXACTLY TWO chains (g0, g1), for generators sigma_0
and sigma_1, for every (Z, N). It accumulates every nucleon's crossings into
those two. Read the body: the returns are unconditional.

thm:wedderburn-mass-formula sums over the generators i of the atomic braid
A in H_{A+Z}(q). That algebra has A+Z-1 generators:

    H-1  (A=1, Z=1)  H_2  -> 1 generator      atom_gen_chains gives 2
    D    (A=2, Z=1)  H_3  -> 2 generators                          2
    T    (A=3, Z=1)  H_4  -> 3 generators                          2
    4He  (A=4, Z=2)  H_6  -> 5 generators                          2

So my Phi_1 is a sum of exactly TWO logs regardless of A, while the chains
inside them grow. That is trivially non-extensive — and "Phi_1 is not extensive"
was precisely the defect I reported. The finding may be an artifact of the input,
not a property of the formula.

Worse, it is the SAME MISTAKE AS THE RETRACTION, one level down. atom_gen_chains
is documented as feeding atom_V_full for "the mass-tower formula" — it is built
for the TOWER construction, not for the Phi formula. I substituted a helper from
a neighbouring construction because it had a plausible name and the right
arity-ish shape, exactly as I earlier substituted nucleon chains into an atomic
formula.

## What this leaves standing

- The RETRACTION stands. It rests on the formula's own algebra (m_n - m_p is an
  input) and on nucleon_gen_chains being quark-level. Neither depends on how
  M_i is built.
- The alpha* EXCISION stands. Independent ground entirely.
- Phi_3 = w*ln q with INTEGER w survives as algebra ABOUT THE CHAINS GIVEN
  (4, 6, 6, 12, 12) — but whether those are the formula's chains is exactly
  what is now in doubt.
- The per-term decomposition, the "Phi_1 flips sign", the "Phi_2 well-behaved",
  and the chirality magnitude bound are ALL CONDITIONAL on the input being
  right, and it probably is not. Do not cite them.

## What is actually needed

A verified constructor for the formula's M_i: for generator i, the 2x2 transfer
matrix from chaining the crossing matrices of all strands j > i, over the atomic
braid in H_{A+Z}(q), giving A+Z-1 of them. I did not find one and did not write
one. Until that exists, no number computed from Phi_1/Phi_2/Phi_3 on atomic
braids should be trusted, including mine.

STOPPING HERE rather than building further on an unverified input. Three
inference layers in this session rested on a substituted object; two are already
retracted.

## Read the rest of the spec — the formula states its own domain, and I had not

wedderburn-mass-formula.md continues past the part I was working from:

  "For n >= 4, the Hecke algebra has additional irreducible representations
   (one per partition of n), producing ADDITIONAL INVARIANTS NOT CAPTURED BY
   THE 2x2 TRANSFER MATRIX. ... The mass functional uses the three extremal
   invariants as the LEADING-ORDER formula; the full partition sum gives the
   exact Markov trace."

So the three-Phi formula is explicitly LEADING-ORDER, exact only while the three
extremal blocks (sym, std, alt) exhaust the partitions. With n = A + Z strands:

    atom   n   p(n)  extremal  missing   measured ratio
    H-1    2     2      3       over-specified   5e5 off
    D      3     3      3       0  EXACT         1.448  right sign
    T      4     5      3       2                -0.179 WRONG SIGN
    3He    5     7      3       4                -0.605 WRONG SIGN
    4He    6    11      3       8                -0.227 WRONG SIGN

n = 3 is the UNIQUE n where the three extremal invariants are all of them, and D
is the ONLY atom whose sign is right. The breakdown starts exactly at the n >= 4
boundary the source names. That is a much better explanation of my measurements
than "Phi_1 is defective".

CAVEAT, and it is not small: my M_i inputs are still unverified (two chains where
the formula wants A+Z-1). So this correspondence is SUGGESTIVE, not established
— two candidate explanations for the same numbers, and I cannot separate them
until the constructor exists. Recording it because it reframes what the
constructor is for: not to fix a defect, but to test the formula inside and
outside its stated domain.

## Retiring my own flag

The previous entry flagged "alpha = m_e*8G is stated for the COMMUTATIVE limit;
I assume it carries to the full formula". It does — the formula's own coefficient
list gives alpha = m_e x 8G citing prop:binding-scale-catalan, alongside
[3]_q = (q^3 - q^-3)/(q - q^-1) and h_A = q - q^-1, and states "All quantities
are derived from q_0 and m_e. The formula has zero fitted parameters." Flag
retired. Also confirms [3]_q = q^2 + 1 + q^-2 as implemented, since
(q - q^-1)(q^2 + 1 + q^-2) = q^3 - q^-3.

## Bearing on the alpha* question

canonicalization-review.md §3.1 holds that alpha* absorbs the CHIRALITY term.
The source says what is missing at n >= 4 is the NON-EXTREMAL PARTITION
INVARIANTS. Those are different objects — chirality is the alt block, which is
one of the three the formula already has. So the spec itself points at the
partition sum rather than chirality as the deficit, which is independent support
for the conclusion I reached by an invalid route and retracted. Still not proof:
the retraction stands, and this is the source's framing, not a measurement.

## TERMINUS — this converges on a documented open problem, not a defect

Followed the spec's own pointer: "the full partition sum gives the exact Markov
trace". That sum is implemented — binding_K_direct.py:

    Binding(K) = m_e * sum_lambda y_lambda(q) * chi^lambda(beta_K) * Delta_lambda(K)

It runs, and emits NO binding prediction for any atom. Every row is
status = delta_lambda_value_present, carrying |tr_M| and B_codata and nothing
else. Its own comment says why:

  "Proved per-partition VALUE present; binding NOT computable from it alone
   (needs y_lambda*chi^lambda + the open extensive magnitude term). Emit the raw
   Sigma Delta_lambda as a labelled DIAGNOSTIC only — never a binding prediction
   (anti-laundering)."

That is the Delta_lambda many-body MAGNITUDE — AGENTS.md's Track A blocker. The
per-partition value is proved (signed Springer dimension, sorry-free, PR #4580);
the extensive term is open, and six ansaetze have already failed on the deuteron.

## So the chain closes

  1. "wrong-sign parameter-free p-n splitting"
       -> my test was invalid: correction vs a leading term the formula CONSUMES,
          and quark-level chains in an atomic formula.            RETRACTED
  2. -> "Phi_1 is not extensive"
       -> my input was invalid: two chains where the formula wants A+Z-1.
                                                                  RETRACTED
  3. -> the formula is EXPLICITLY leading-order, exact only where the three
        extremal blocks exhaust the partitions, i.e. n = 3 alone. D (n=3) is the
        only atom whose sign is right.
  4. -> the exact route is the Delta_lambda partition sum,
  5. -> which deliberately emits nothing, because the many-body magnitude is a
        known open problem.

CONCLUSION. The wrong sign at A >= 3 is NOT a defect to fix. It is a
leading-order formula evaluated outside its stated domain, and the exact
replacement is blocked on the documented Delta_lambda magnitude gap. Nothing
here is new mathematics; what is new is the route in, and two of my own claims
retracted along the way.

DO NOT build the M_i constructor as a research project. It would only re-measure
a leading-order formula whose limits the source already states. If it is built
at all, build it as a TEST: D (n = 3) should come out exact, not 45 % high. That
is a falsifiable check on the implementation, not a path to the binding.

AND DO NOT propose a seventh Delta_lambda ansatz. AGENTS.md names that
explicitly, and arriving here by a fresh route is not a licence to retry it.


### 2026-09-06 — CROSS-REFERENCE from `qou-jgg0`. Not a claim on this bean; status left `todo`.

Flagging one input dependency, because it is invisible from inside this bean and
it changes which explanation survives. **I am not taking this bean and have not
touched the p-n sign question.**

`qou-jgg0` measured that **three** strand counts are live for the atomic braid
with no block saying which is canonical: `A+Z` (7 content blocks, incl.
`def:atomic-braid`), `3A` (26 blocks, incl. the notation register), `3A+Z`
(1 block, `mass-endomorphism/atomic-mass-gb-nf.md:3`, which asserts
`𝓑_K ∈ B_{3A+Z}` while citing the `A+Z` definition). `H_A` is a fourth cell but
appears only as an explicit "Default-coarse" approximation.

This bean computes `n = A+Z` throughout — correctly, since
`thm:wedderburn-mass-formula` says `H_{A+Z}(q)`. But the entry above rests on a
coincidence that is **reading-dependent**. `p(3) = 3` is the only partition count
equal to the extremal count, so "which atom has `n = 3`" decides it:

| reading | atom at `n = 3` | its verdict in this bean | coincidence |
|---|---|---|---|
| `A+Z` | **D** | RIGHT sign (1.448) | **holds** |
| `3A` | **H-1** | over-specified, 5e5 off | **inverts** |
| `3A+Z` | *(none)* | — | **evaporates** |

Under `3A` the uniquely-exact `n` lands on this bean's *worst* data point rather
than its best; under `3A+Z` no neutral atom reaches `n = 3` at all (`3A+Z = 3`
needs `Z = 0`). The three readings also differ at **every** atom in the sample.

**Your argument is not refuted** — under the reading you use, which your source
theorem states, it stands. What is added is that its force is contingent on a
corpus question that is currently open, so the "SUGGESTIVE, not established"
caveat already recorded above has a second, independent reason to hold.

Measured: `computations/probes/q6pp_unique_n_is_reading_dependent_probe.py`,
10/10, exit 0, exact integers, no witness. Check 2 reproduces this bean's own
`n` column at 5 of 5 atoms before departing from it. Naming decision framed for
the author on PR #6821.

## 2026-09-08 — THE SANCTIONED TEST IS RUN. D is not exact: right sign, 2.79× too large

This bean's terminus asks for exactly one thing and forbids the rest:

> *"DO NOT build the M_i constructor as a research project. … If it is built at
> all, build it as a TEST: D (n = 3) should come out exact, not 45 % high."*

**It is run. D is not exact.** Under the corrected reading it is *worse* than
the 45 % this bean recorded, and in the same direction.

| | value |
|---|---|
| `α(Φ₁ − 2[3]_q Φ₂ + h²Φ₃)` at D | **−6.213929627 MeV** |
| `−B_AME(D)` | −2.224566 MeV |
| residual | **−179.33 %** — right sign, magnitude 2.79× too large |

Anchor-robust: the producer's recorded `q = 1.10998` gives −6.213945612 MeV,
−179.333 %. Probe
`computations/probes/deuterium_is_the_untested_exact_point_probe.py`, **7/7**,
convention D, all-pairs, mpmath 50 dps, no witness, no fitted parameter.

### First: three things in this bean are SUPERSEDED, and the next agent should not redo them

This bean says *"A verified constructor for the formula's M_i … I did not find
one and did not write one."* **One exists**, and the arc went two rounds
further:

1. **`computations/wedderburn_Mi_constructor_test.py`** was built and merged —
   under an **adjacent-suffix** reading of *"chaining the crossing matrices of
   all strands j > i"*.
2. That reading is **RETRACTED** (`b2701f33c`, 2026-08-29). The prose is
   ALL-PAIRS: for strand `i`, cross with every `j > i`. Four variants of the
   misreading were tested and the plain reading never was. Its residuals
   (54 %–2653 %) are the record of a refuted reading and are not evidence about
   the formula.
3. Under the correct reading (`computations/phi_allpairs_reconstruction.py`),
   **Φ₂ and Φ₃ are re-derived exactly**: `Φ₃ = w ln q` with
   `w = −2Z − N(N−1)` on **19/19** non-hydrogen rows including Ar (the row that
   refuted the previous candidate), and `Φ₂ = Z·N·ln(1+h²/4)` on 19/19 to
   5.0e-6, entirely publication precision.
4. **Φ₁ is a convention-C artifact** (`phi1_convention_d_probe.py`): 0 of 5
   carried values are reachable under convention D, each lying 27–42 % **below**
   D's minimum. So the published mass table is C-derived and must be recomputed
   under D — an owner decision, not taken.

Point 4 **converges with this bean's own retracted finding from the opposite
direction.** This bean concluded *"PHI_1 IS THE WHOLE PROBLEM"* and then
withdrew it as input-dependent. The sibling arc reaches the same object by
measurement: Φ₁ is the only one of the three that uses the Markov parameter `z`,
hence the only convention-dependent one, and its carried values are unreachable
under the canonical convention. Two independent routes, same term.

### The gap that was actually left, and why it is D

Every one of those results runs over **elemental rows Z = 1…20** — and their
"H" row is `(Z=1, N=0)`, i.e. protium. `phi1_convention_d_probe` covers He, Li,
Be, B, C. **Deuterium `(Z=1, N=1)` appears in none of them.** So the one atom at
which the formula claims exactness had never been evaluated under the correct
reading. That is what this probe fills, and it is a TEST, not a research route:
it proposes no closure, fits nothing, and adds no ansatz.

`n = 3` is confirmed structurally: both ground-state orderings (`epn`, `nep`)
have exactly 3 strands `= A+Z`, and `p(3) = 3` is the unique partition count
equal to the extremal count.

### A caveat this probe RETIRES rather than inherits

`phi_allpairs_reconstruction` documents the H row as an **exception** to the Φ₃
closed form (recorded `w = 10` against the all-pairs `−2`), attributed to the
`pe` crossing. D is also `Z = 1`, so the exception plausibly extends to it.
**Measured: it does not.** At D both closed forms reproduce the direct
all-pairs computation to **4e-50 / 2e-51** — i.e. exactly, at the full working
precision. The Z=1 exception is specific to `N = 0`.

### Two defects in my own probe, caught before the numbers were reported

1. **A float64-seeded anchor.** The first run used
   `qou_substrate.constants.Q`, which is solved by `_solve_q_proton_f64`, and
   every comparison capped at **3.44e-15** — float64 resolution presented by a
   50-dps script. Re-seeded from `Q_50_DIGIT_STR`, the same comparisons return
   **4e-50**. AGENTS.md forbids reporting a float64 agreement as exact; this is
   what that looks like when it nearly happens.
2. **Φ₃'s sign convention, and it inverted a conclusion.** `Σ log|alt/sym|`
   gives the opposite sign to the closed form's `w < 0` (He: `w = −6`). With the
   wrong convention, check 3 read *"the closed forms do NOT extend to D"* — the
   caveat above, asserted backwards. The correct convention is `Σ log|sym/alt|`.
   Φ₃ enters the formula **signed**, so this also moved the headline
   (−176.26 % → −179.33 %).

### Scope — (a), not (b)

**This does not refute `thm:wedderburn-mass-formula`.** It measures one
construction, at one atom, under one convention, against one experimental
number. It constrains magnitude, not ingredients. What it does establish is the
falsifiable check this bean asked for and answers it in the negative: at the
single point where the formula's own stated domain says it is exact, and where
the strand count and both auxiliary invariants are independently confirmed
correct, the correction overshoots the deuteron binding by **2.79×**.

**Do NOT read this as licence for a seventh Δ_λ ansatz.** AGENTS.md names that
explicitly and arriving here by a fresh route is not a licence to retry it.

**Status stays open.** The subject — why the parameter-free construction misses
— is unresolved mathematics, and §13a forbids closing on a recorded measurement.

## 2026-09-08 — CORRECTION to my own merged PR #7162: no exactness claim exists

**#7162's title and body are wrong on the framing, and the number in them is
right.** That PR is titled *"the one point the mass formula claims exactness
at"*. **The corpus makes no such claim, at n = 3 or at any n.** I took it from
this bean's own terminus — *"D (n = 3) should come out exact, not 45 % high"* —
and carried it into a title and a body without resolving it against the blocks.
That is the AGENTS.md §"Grep the claim SHAPE, not only the topic" failure: I
grepped the topic and never checked what proposition was actually asserted.

**What the blocks say, with line numbers** (`folio/quantum-observable-universe/mass-theory/`):

| file:line | text |
|---|---|
| `wedderburn-mass-formula.md:55` | "the three extremal invariants as the **leading-order** formula" |
| `wedderburn-mass-formula.md:56` | "the **full partition sum** gives the exact Markov trace" |
| `wedderburn-mass-formula-proof.md:66` | "Chaining within a single crossing algebra is the defining **Level-0** transfer-matrix reduction" |
| `wedderburn-mass-formula-proof.md:105` | "This is the claimed completeness **at the 2×2 transfer level**" |

So "exact" attaches to the **partition sum**, a different object from the three
`Φ`; and the completeness claim is scoped to invariants **of the `M_i`**.
Neither block carries an `n ≤ 3` clause of any kind — the only order clause in
either is `n ≥ 4` (checked mechanically, check 6).

**Why n = 3 does not rescue the construction, and this is the substantive
half.** `p(3) = 3`, so the three extremal blocks *do* exhaust the partitions of
3 — that part of #7162 stands. It does not follow that the `M_i` carry the
`H_3` data, **because the `M_i` do not live in `H_3`.** Step 2 of the proof
builds them as the regular representation of the **commutative** two-dimensional
crossing algebra `R[σ] = R[x]/((x−q)(x+q⁻¹))`, and chains the crossings of
*different strand pairs* inside that one algebra. In `H_3(q)`, `σ₁` and `σ₂` do
not commute. **The Level-0 reduction discards that at every `n ≥ 3`, deuterium
included.**

The trap is a dimension coincidence: `dim(standard block of H_3) = n−1 = 2 =
dim R[σ]`, which makes the correspondence table's row *"Φ₁ | standard (dim
n−1)"* read as if `M_i` were the standard-block image. Step 2 shows its two
eigenvalues are the **sym and alt characters** — verified here to `2.7e-51` on
all four D chains — so the standard block never enters as a 2-dimensional
representation at all.

**What the −179.33 % therefore is.** The first measurement of the **Level-0
commutative-reduction error at the smallest atom carrying two distinct braid
generators**. That is a *stronger* result than the one merged, because it is
attributable to a named approximation rather than being an unexplained failure
of a promise nobody made. The number is unchanged (re-derived here from the
merged probe's own functions: `−179.332222 %` against the recorded `−179.332 %`).

**Scope (a), not (b).** It constrains the size of one named approximation at one
atom under one convention. It excludes no ingredient, and it does not refute
`thm:wedderburn-mass-formula` — which claims leading-order, and is measured
here doing exactly that.

**Verification:** `computations/probes/level0_reduction_is_not_an_exactness_claim_probe.py`,
**12/12**, exit 0.
Checks 1–2 verify Step 2's homomorphism and the commutativity being discarded;
check 3 builds the `H_3` regular representation on the `T_w` basis and
self-verifies it (Hecke relation on both generators, braid relation) before
reporting `max |[σ₁,σ₂]| = 1.0`; checks 4–5 verify Step 2's eigenvalues and
readouts at D; check 6 asserts the four quoted sentences are present; check 7
reproduces the merged residual. mpmath 50 dps throughout, anchored on
`Q_50_DIGIT_STR`.

**Still open, and this bean stays open (§13a).** The mathematics is untouched:
nothing here derives the missing non-commutative contribution, and the
`Φ₁`-is-a-convention-C-artifact finding from the sibling arc is unaffected. What
changed is that the D residual now has a mechanism attached to it.

## 2026-09-11 — my merged remark is (a)-CONDITIONAL on qou-jgg0 and does not say so

`rem:level-zero-discards-braid-noncommutativity` (PR #7171, merged `20671dcc1`)
states *"Deuterium is the unique atom with `n = A + Z = 3`."* That is true under
`def:atomic-braid`'s strand count and **false under the production one**.

Bean `qou-jgg0` established (2026-09-05) that the corpus carries **two different
objects sharing the name "atomic braid" and the symbol `𝒜`** — `H_{A+Z}(q)` in
`def:atomic-braid`, `H_{3A}(q)` in production — and reserves the choice between
them to the author. Measured now:

| reading | D's strand count | unique atom with `p(n) = 3` |
|---|---|---|
| `A + Z` | 3 | **deuterium** |
| `3A` | 6 (`p(6) = 11`) | **hydrogen-1** |

So the two readings name **different atoms** as the unique point where the three
extremal blocks exhaust the partitions. Exact: `p` is strictly increasing, so
`p(n)=3` iff `n=3`; then `2Z+N=3` with `Z≥1` gives `(1,1)` and `3(Z+N)=3` gives
`(1,0)`.

**This does not invalidate the Level-0 finding.** The mechanism — Step 2 chains
crossings of different strand pairs inside the commutative `R[σ]`, while
`σ₁σ₂ ≠ σ₂σ₁` — holds at every `n ≥ 3` under either reading, and the `−179.33 %`
was computed from the mass formula's own construction. What is (a)-conditional is
the *uniqueness* claim and the identification of D as the separating point.

**Not fixed here, deliberately.** Adding a scope sentence to the remark is close
to picking (a), which is `qou-jgg0`'s author decision. Raised to the owner rather
than edited.

**Verification:** `computations/probes/strand_count_reading_is_load_bearing_probe.py`,
15/15, exit 0. Check 6 asserts mechanically that the merged remark makes the claim
and mentions neither `3A` nor `qou-jgg0`.

**Bean stays open** (rule 13a).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M9 (qou-jgg0) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.
