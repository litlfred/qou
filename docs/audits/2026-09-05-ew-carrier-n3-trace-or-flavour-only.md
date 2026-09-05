# 2026-09-05 — Is the electroweak carrier the N=3 trace, or is N=3 flavour-only?

Bean `qou-yk03`. Both sides worked through, with what each implies, what is
derivable under it, and what it costs.

**Headline: the question is not a fork with two live branches.** One side is
blocked by four independent sorry-free proofs and the other is already the
corpus's position. What the analysis changes is *why* — and it surfaces a
sharper objection to the whole `(3,2,1)` Weinberg construction than the row cap,
which survives whichever side is taken.

## 0. The structural fact that reframes everything: N *is* the trace parameter

`N` is not a knob standing beside the Ocneanu parameter. It **is** it. The
Ocneanu/Markov trace on `H_n(q)` carries `a = q^{N−1}`:

| `a` | trace | role |
|---|---|---|
| `q` | Jones, `gl₂` | what the mass pipeline uses |
| `q²` | `gl₃` invariant | the eightfold way |

All the `N`-dependence sits in the weights, which are principal specialisations
`y_λ ∼ s_λ(1, q, …, q^{N−1})`, normalised by the Markov condition
`Σ_λ y_λ f^λ = 1` — i.e. `tr_M(1) = 1`. So "choose N" and "choose the trace" are
the same act, and the row cap is not an extra rule imposed on top: a λ with more
than `N` rows has a cell of content `−N`, contributing `[N + (−N)]_q = [0]_q = 0`
and killing the weight. **`RowCapObstruction.lean` arriving as arithmetic.**

## 1. The mass channel is locked at N = 2, and this is exact

Verified independently here, at the substrate `q₀`, against the corpus's own
`y_lambda_su_n`:

```
y_(2,1) / y_(3)  =  [2]·[N−1] / [N+2]        (balanced q-integers)

  N = 2 : 0.48930712047797097
  N = 3 : 0.774590881357880918
  N = 4 : 0.958124031288484858
```

Exact agreement with the closed form at all three. These are **different
rational functions of q**, not one function times a constant, so moving to
`N = 3` does not merely *add* the singlet channel — it **re-weights the
surviving channels against each other by 58 %**, on elements the mass pipeline
already evaluates.

> **Correction to my own first pass.** I initially read the mismatch against the
> probe's stated formula `q·[2][N−1]/[N+2]` as a discrepancy. It is not: that
> formula is written in the **asymmetric** convention `[m] = (1−q^m)/(1−q)`
> while the module computes with **balanced** integers, and the two differ by
> exactly the leading `q` — the factor `1/q = 0.90091828` I was seeing. Both
> statements are right in their own convention.

**Consequence:** an `N = 3` channel cannot be a re-parameterisation of the mass
trace. It has to be a *second, separate* trace. That is scope-(b), by exact
computation, and it is the good outcome for the eightfold programme rather than
the bad one — `HnMarkovTrace.lean` already types the Markov parameter as a free
class **field**, so two instances are typeable today.

## 2. Side A — the EW carrier IS the N = 3 trace

### What it buys

- The `λ = (3,2,1)` block becomes **occupied**: `y_(3,2,1) = 0.0103939752433`
  at `q₀`, against exactly `0` at `N = 2`. The row-cap objection in
  `sm-params-gauge-couplings.md` is **scoped to N = 2** and does not reach here.
- A genuine normalised Markov trace exists on the word. Measured, characters
  exact through the consumers' own Hoefsmit path:

  | N | `tr_M(β_EW Δ_I)` | occupied blocks |
  |---|---|---|
  | 2 | 4.83789085692050323822 | 4 / 11 |
  | **3** | **2.90062956640672874659** | 7 / 11 |
  | 4 | 2.19236562357645905376 | 9 / 11 |

- It is consistent with the eightfold chapter's own stated need for `N = 3`.

### What it costs, and this is the load-bearing half

**The N = 3 trace exists arithmetically; the N = 3 *carrier* does not.** The
weights `s_λ(1, q, q²)` are perfectly good numbers whatever exists. What makes
them *flavour SU(3)* is a three-dimensional fibre object, and the eightfold
chapter proves that object is **not available from a single fibre — four
independent times, all sorry-free**:

| route | statement | Lean |
|---|---|---|
| row cap | `C(N,3) = 0 ⟺ N < 3` | `RowCapObstruction.lean` |
| Sym² gate | a passing `W` is a sum of *distinct even-dimensional* irreps, so `dim W` is even; 3 is odd | `Sym2GateMultiplicity.lean` |
| volume form | `Λ²V ≅ 1` forces `N = 2` | `SU2EmergenceRankForced` |
| fibre functors | 3-dimensional fibre functors **exist** \[bichon2003] and don't help: they are monoidal, so preserve Clebsch–Gordan, and the required spin-0 summand is absent from `V^{⊗3}` by parity | `FibreFunctorDimensionNotCategorical.lean` |

The fourth is the one that closes the obvious escape. And the property any
construction must exhibit is itself proved: **non-self-duality**
(`SelfDualSectorConfinement.lean`) — a 3-dimensional object passing the gate
must contain a complex-type irrep, and every `SU(2)` irrep is self-dual.

So Side A does not import a solved N = 3. **It imports the eightfold chapter's
single largest open problem**, which that chapter states gates *every* flavour
statement it makes.

### And even granting N = 3, two further gates stay shut

1. **Flavour vs colour is not separable by any object-level gate.**
   `FlavourColourDiscriminator.no_object_gate_separates` is scope-(b) with the
   invariant named: the colour triple (the `ℂ³` of
   `Im(𝕆) = ℝ ⊕ ℂ³`) and the flavour triple (Dynkin `(1,0)`) have equal
   dimension, equal Frobenius–Schur type and equal triality, so **no** gate
   reading only object data tells them apart. A discriminator must read the
   Young-symmetry *channel* — which is open item 7.
2. **Hypercharge is open, and it is the actual θ_W blocker.** The writhe→`I₃`
   map is derived; the writhe→`Y` map is **falsified** (p and n share `Y = +1`
   with different writhes). `sm-params-gauge-couplings.md` says θ_W *"mixes
   exactly the two U(1)'s the framework has not yet separated."* The twist
   battery that appeared to filter candidates is proved **vacuous**
   (`TwistBatteryVacuity.lean`: the spectrum battery is exactly `T = 3Q`, an
   identity, not a test; the `ℤ₆` condition never sees the assignment).

**This second gate is independent of N.** Whatever N you pick, θ_W needs a
second crossing invariant that does not exist yet.

## 3. Side B — N = 3 is flavour-only

### What it buys

- Consistent with every proof above, and with the appendix's existing ruling.
- Respects the mass-channel lock-in without needing a new object.
- Nothing to build.

### What it costs

- The `(3,2,1)` Weinberg construction is outside the carrier **permanently**,
  not pending a fix. `cot θ_W ≈ 1.8208` is then not a result awaiting
  justification; it is arithmetic on an unoccupied block.
- θ_W is left with one named candidate, the Milnor triple linking `μ̄₁₂₃`,
  which supplies the writhe-independent second crossing invariant and separates
  the two U(1)'s — and which is gated on the open flavour `SU(3)` sector for its
  relative coupling normalisation.

## 4. What the eightfold way implies for the choice

Three things, and the third is the one that decides it.

1. **The eightfold's N = 3 is `SU(3)_f` — flavour.** Its own ledger marks
   `dim V = N = 3` **open**: *"framework supplies dim V = 2; no q raises the row
   cap. The obstruction is proved; the construction is missing."*
2. **The octonionic route supplies a colour `SU(3)_c` candidate that the gate
   does not exclude** — and *not excluded* is carefully distinguished there from
   *passes*, the singlet count being a cited input rather than a formalised one.
   Whether it yields flavour is untested.
3. **The electroweak group is `SU(2) × U(1)`, not `SU(3)`.** Putting the EW
   sector on an `N = 3` trace asserts that its carrier is a `gl₃` object. That
   is a strong claim and nothing in the corpus argues for it. The apparent pull
   comes from the partition label `(3,2,1)` reading like the Standard Model's
   3-2-1 — but `(3,2,1)` is selected here for a *structural* reason with no
   gauge-group content: **it is the unique self-conjugate partition of 6** (11
   partitions, exactly one self-conjugate, verified). Reading the parts as gauge
   factors would be numerology, and it is worth saying so explicitly because the
   coincidence is seductive.

That self-conjugacy has two real consequences, both already in the corpus:
`κ_(3,2,1) = 0`, so the Molien weight's `q^{−κ}` factor is exactly 1 on this
block; and the block is **bar-odd** — `T_(3,2,1)(q^{-1}) = −T_(3,2,1)(q)` — so it
contributes only to the bar-odd impurity and never to the bar-even coefficient.

## 5. What is derivable under each side

| | Side A (EW on N = 3) | Side B (flavour-only) |
|---|---|---|
| `tr_M(β_EW Δ_I)` at N = 3 | **already computed**: 2.9006 | n/a |
| a `cot θ_W` from it | needs the hypercharge invariant — **open either way** | same, via `μ̄₁₂₃` |
| the N = 3 fibre object | **open**, four proofs it is not single-fibre; needed for interpretation, not for arithmetic | not needed |
| flavour/colour separation | **open**, and no object-gate can do it | untouched |
| the external flavour test | Gavrilik (TG) — already audited: **"FITTING, NOT DERIVATION. Do not wire."** | same |

**The one thing genuinely derivable today under either side** is the negative:
that the `(3,2,1)` construction's `cot θ_W` is not reachable from the carrier at
`N = 2`, and that at `N = 3` it would still need an invariant nobody has.

## 6. The objection that survives both sides

Independent of N, and stronger than the row cap because it does not depend on
which trace you pick: **the `1.8208` figure was obtained by a proximity search.**
Its residual factor was selected as the closest of **74 enumerated candidates**,
the best missing the required `1.02239` by `1.3 × 10⁻³`, and its own witness
records the ansatz as *neither supported at 10⁻³ nor falsified at 10⁻²*.

The appendix already states the figure **"must not be cited as a framework
accuracy result."** Moving the construction to `N = 3` would not touch this. A
redo that re-runs the same 74-candidate search on re-weighted numbers has gained
nothing — it is the fit signature the anti-fit discipline exists to catch,
reproduced one trace over.

## 7. Recommendation

**Side B, and it is not close.** Not because Side A is refuted — it is not; the
`N = 3` trace is well-defined and the row-cap objection genuinely does not reach
it — but because Side A's *only* new content is an arithmetic value whose
interpretation depends on an object with four independent proofs of
non-existence in the single-fibre setting, while its target observable is gated
on hypercharge either way.

Concretely:

1. **Do not move the EW sector to N = 3.** It would import the eightfold's
   largest open problem to gain a number that still cannot be read.
2. **Keep the N = 3 trace as a flavour object**, where the eightfold chapter
   already wants it, and where the missing construction is already tracked.
3. **The tractable EW lever is `μ̄₁₂₃`**, as the appendix says — it is what
   separates the two U(1)'s, which is θ_W's actual problem. It is gated on
   `SU(3)`, so it is not free either, but it is gated on a sector the framework
   is already working, rather than on a new one.
4. **`qou-yk03` should be re-scoped, not worked as posed.** The question "is the
   EW carrier the N = 3 trace" is answerable now: no, on present evidence. The
   question worth keeping is the *flavour* one it was standing in for — build
   the non-self-dual three-dimensional object, which the eightfold chapter has
   already reduced to a single checkable property.

**Marked as judgement, not finding:** items 1–3 follow from the measurements
above; item 4 is a call about where effort goes, and the author may reasonably
want the N = 3 EW number on the record anyway, in which case it already is
(§2, and `probes/beta_ew_n3_second_trace_probe.py`).

## What would change this

A single result: **a three-dimensional non-self-dual object in the multi-fibre
groupoid whose `Sym²` is irreducible.** That would convert `N = 3` from a
well-defined trace with no carrier into a carrier — and it would do so for
flavour first, with the EW reading still needing a separate argument that the
electroweak group is `gl₃`-carried, which nothing currently supplies.
