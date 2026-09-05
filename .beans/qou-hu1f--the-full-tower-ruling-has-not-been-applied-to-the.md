---
# qou-hu1f
title: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the whole object
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:54:56Z
updated_at: 2026-09-05T08:01:57Z
---

Audit: [`2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md`](../docs/audits/2026-09-04-full-tower-ruling-vs-the-h3-mass-surface.md)

## The gap

The owner ruled on 2026-09-03 that derivations must be carried on the **full
tower** (both senses: all `n`, all orders in `q`).
[`2026-09-03-sm-26-term-status.md` §10] applies that ruling to the
**standard-model** surface only. It says nothing about mass, binding, or the
nuclear chain -- and that is the surface where bean `qou-tower` has already
measured that **there is no tower**.

Worse, the collapse finding has no durable home: `build_atom_nf_mp` appears in
**zero** files under `docs/` or `content/`. One bean, five probes.

## Re-measured here (a bean is not a primary source)

Direct against `compound_shift_nf.build_atom_nf_mp`:

| nucleus | nominal strands `n = 3A` | NF components |
|---|---|---|
| hydrogen A=1 | 3 | **6** |
| 4He A=4 | 12 | **6** |
| **16O A=16** | **48** | **6** |

16O is a case `qou-tower` never tested and is the sharpest instance.

## Scope correction to qou-tower, which does NOT rescue the tower

`qou-tower` says "the production chain". Measured, `build_atom_nf_mp` has seven
consumers: five probes plus `all_nuclides_sdp_admissibility_mp.py` and
`qbeta_level_k_binding_operator_probe`. It is **not** the canonical mass path.

But `binding_canonical.py` is H_3 too, by a **different mechanism** -- it calls
its own path `tower_binding_full (H_3 tower)` (:37), builds from "the H_3
building blocks tr_M^3(p), tr_M^3(n)" (:324), and bridges at H_3 (:341). So:

- **NF route** -- the tower is built and destroyed (reduced to 6 per crossing);
- **canonical route** -- the tower is never built (per-nucleon H_3 traces are
  composed).

Do not conflate them; `qou-tower`'s argument covers only the first.

## The measurable next step, which nobody has run

`qou-tower`'s full-tower walk measured **distributional** quantities (top-block
share, participation ratio, argmax partition) against magic numbers. It never
compared **a binding energy**. So the obvious question is open:

> Does the A <= 4 full-tower walk reproduce the canonical H_3 binding numbers?

If yes, H_3 is a faithful order-zero rendering and the ruling is satisfied in
substance. If no, the two routes disagree and that gap is the finding. Either
answer is worth having, and A <= 4 is reachable (A=5 needs `max_d^2` = 686 GB).


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


## The agreement test: RAN, and it is NOT yet interpretable — the two routes trace DIFFERENT WORDS

Compared the NF route's Markov trace (`Σ_i nf[i]·TR_M[i]`, with
`TR_M = [1, z, z, z², z², h·z²+z]` from `compound_shift_nf.tr_m_weights_mp`)
against the canonical `tr_M_atom` (`Σ_{λ⊢3A} y_λ χ^λ`, all `p(3A)` partitions).
mpmath end to end at 50 dps, proton pin both sides:

| nucleus | A | NF trace (6-dim) | canonical tr_M_atom | rel diff |
|---|---|---|---|---|
| 1H  | 1 | 1.14633769063500507 | 1.14575969245730087 | **5.0e-4** |
| 2H  | 2 | 0.404361815683575801 | 0.575172243917771871 | 0.297 |
| 3He | 3 | 0.687073324770033545 | 0.40376703685142817 | 0.702 |
| 3H  | 3 | 0.853070865421924793 | 0.229310102104556507 | 2.72 |
| 4He | 4 | 1.58467953221993593 | 0.160974145442407382 | **8.84** |

**🛑 Do NOT read this as "the H_3 reduction is unfaithful".** Checked before
believing it, and the comparison is not apples-to-apples: `tr_m_atom_zn`'s
docstring says **"Canonical color-weighted p-n convention"**, and
`compound_shift_nf.py` contains **zero** references to `m_pp` / `m_pn` / `m_nn`
or colour at all. The two routes therefore build different words, and colour
weighting enters exactly on the **interfaces**, which exist only for `A >= 2`
and grow as `O(A²)` — which is also the shape of the divergence. So the growth
with A is consistent with the convention difference alone and is not evidence
about the tower.

This is the same trap `qou-82mc` records against itself ("I nearly compared the
corpus mu3/mu4 signs against Ursell b3/b4 as if they were the same family").

### The one convention-independent number, and it is the interesting one

**At A=1 there are no interfaces**, so colour weighting cannot apply and both
sides trace the same 3-strand word in the same algebra — `n = 3`, so `H_{3A}` IS
`H_3` and the "collapse" is not a collapse. They should agree to the arithmetic,
~1e-50. They differ by **5.0e-4**, about 46 orders above the floor.

That residual is small, real, and unexplained. It is the cheap, well-posed
question this comparison actually produced, and it is worth more than the big
numbers beside it.

### What the test needs before it can answer the original question

Run the NF route with the canonical colour convention (or the canonical with
colour off, `m_pp=m_pn=m_nn` neutralised in whatever sense makes the words
identical), so that the only difference left is the H_3 reduction. Until then
the A>=2 rows measure the convention, not the tower.


## The A=1 residual is STRUCTURAL — not the q pin, and it sits on a documented corpus invariant

Forced both routes onto the identical `q = q_at(55)` (proton,
`1.109978582751380807591669`):

    NF trace                    1.1463376906350050736
    canonical (default q)       1.1457596924573008697   rel 5.045e-4
    canonical (forced same q)   1.1457596924573008697   rel 5.045e-4
    canonical default vs forced-q                       rel 1.33e-49

**The pin is not the cause** — forcing it moves the canonical value by 1.33e-49,
i.e. nothing, and the gap is unchanged to every printed digit. At A=1 there are
no interfaces (so colour cannot apply), `n = 3` (so `H_{3A}` IS `H_3` and there
is no collapse), and `q` is identical. Same word, same algebra, same anchor,
**5.045e-4 apart**.

### It is the corpus's own bug-detector, currently failing

[`2026-05-19-trm5-markov-bug.md`](../docs/audits/2026-05-19-trm5-markov-bug.md)
found a bug by running EXACTLY this comparison: *"the y_λ values ... did NOT
satisfy `tr_M(b_i) = Σ_λ y_λ·χ_λ(b_i)` for the NF basis element
`e_- = σ_0·σ_1·σ_0`. Least-squares residual ~0.12 instead of 0."* The fix was
`TR_M[5]`: `z³` -> `h·z² + z`.

So this identity is a **known, load-bearing consistency invariant** between the
NF Markov trace and the Frobenius pairing, and it was worth a bug fix once.

**`TR_M[5]` is NOT the current culprit — checked.** That audit's arithmetic is
convention-C (`z = 0.4993`, giving 0.5514). Re-derived in convention D:
`h·z² + z = 0.20907·0.375387 + 0.612688 = 0.691173`, and `tr_m_weights_mp`
returns `0.69116648`. The weight is internally consistent with its own
derivation, in the live convention.

### The decisive next test, named precisely

Run that audit's own **per-basis-element** check under convention D: for each of
the six NF basis elements `b_i`, compare `TR_M[i]` against `Σ_λ y_λ χ_λ(b_i)`.
Whichever element carries the 5.045e-4 localises it to the `TR_M` weights, the
`y_λ`, or the reduced-block `χ`. A whole-word residual cannot separate those
three; a per-element one can.

Scope, stated: this says the invariant fails at 5.045e-4 on the A=1 atom word.
It does NOT say which side is wrong, and it is not yet a defect report against
either.


## ANSWERED (2026-09-05): the residual is the WORD ORDER — none of the three suspects

The "decisive next test" named above ran. Probe:
[`nf_vs_canonical_word_order_probe.py`](../computations/probes/nf_vs_canonical_word_order_probe.py),
4/4, mpmath end to end at 60 dps, proton pin `q_at(55)`, no float64.

**The identity is intact, and that is the first result.** Under convention D,
`TR_M[i] == Σ_λ y_λ χ^λ(b_i)` holds on **all six** NF basis elements to
**8.3e-61** — the arithmetic floor. The invariant that caught the 2026-05-19
`TR_M[5]` bug is healthy. So the residual is not in the `TR_M` weights, not in
the `y_λ`, and not in the reduced-block characters. All three are exonerated
by the one measurement that was supposed to convict one of them.

**Second: `hm_mp` is correct too.** Fed the *canonical* word, it reproduces the
canonical Frobenius pairing to **1.1e-60**. So the NF machinery evaluates the
pairing correctly for whatever word it is handed.

### The consequence is forced, not conjectural

Both sides are linear, and `TR_M[i] = Σ_λ y_λ χ^λ(b_i)` exactly. Therefore the
NF route's `Σ_i nf[i]·TR_M[i]` **is** the Frobenius pairing evaluated on the
element `Σ_i nf[i]·b_i`. Two exact evaluations of one linear functional that
disagree by 5.045e-4 cannot be looking at the same algebra element.

They are not. Same 11-letter multiset — 6 `σ₀`, 1 averaged on gen 0, 3 `σ₁⁻¹`,
1 averaged on gen 1 — in **different order**, and `H₃` is non-commutative:

    canonical (grouped by generator):  s0 s0 s0 s0 A0 s0 s0 S1 S1 S1 A1
    NF route  (interleaved):           s0 S1 s0 S1 s0 S1 s0 A0 A1 s0 s0

(`s` = σ, `S` = σ⁻¹, `A` = averaged `σ − (h/2)·1`; digit = generator.)

### Both orderings are deliberate and each cites a source

- `pyhecke.atom.build_atom_nf` — which `build_atom_nf_mp` says it mirrors —
  comments its loop **"B₃ confinement (3 interleaved σ₀, σ₁⁻¹)"**.
- `mass_at_3A_proper.atom_braid_word_3A` says it **"Matches the chain-walk
  convention of `hecke_core.atom_per_generator_volumes`"**.

Two conventions, two sources, one disagreement. Neither is a typo, and this is
why the earlier framing ("at A=1 both sides trace the same 3-strand word in the
same algebra") was the wrong assumption rather than the safe one.

### Why the order is not cosmetic

`(σ₀σ₁⁻¹)³` is the standard braid word for the **Borromean rings**, and it is
exactly the interleaved route's intra-nucleon core. The grouped word contains
no such subword. The framework's mass law is built on the Borromean braid
(`F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`), so *which* word the binding surface traces
is a question about the physics, not about formatting.

### A caution the numbers make concrete

The two words are wildly different elements of `H₃` — NF coefficient vectors
`[0.594, 1.309, −0.174, 0, −0.383, 0]` against
`[1.019, 0.087, −0.092, −0.070, 0.016, 0.218]`, the first carrying two exact
zeros — yet their Markov traces agree to four digits. **Trace proximity is not
evidence that two routes built the same object.** That is the same class as the
`qou-82mc` trap this bean already cites, one level down.

### Two of my own hypotheses were refuted en route, and both are worth recording

1. **"The residual is convention C vs D in the Markov parameter."** The
   corpus's own `tr_q_plancherel_symbolic` docstring states the Markov property
   as `z = 1/[2]_{q^{1/2}}` — convention **C** — while `TR_M` is built from
   `z_D`. Measured instead: the SU(2) Frobenius pairing at `n = 2` gives
   `Σ_λ y_λ χ^λ(σ) = 0.6126880371464652…`, which is `z_D = q³/(q²+1)` to the
   precision of `q` itself. **The two routes agree on the Markov parameter**;
   that docstring line is stale, and C-vs-D does not explain anything here.
2. **My hand-transcription of the NF ordering was wrong.** Read off the source
   it reproduced neither the NF route (45 % off) nor even its own letter
   multiset. Every claim above is **by construction** — words pushed through
   the real `hm_mp` and the real `atom_braid_word_3A` — not by reading either
   file. A source-reading of a word ordering is not evidence about the word.

### Scope, and what is now open

Scope-(a): this localises the **A=1** residual and establishes that the two
routes trace different words. It does **NOT** say which word is correct.

That is the live question, and it is an authoring decision rather than a
measurement: the mass law names the Borromean braid, one route builds it and
the other does not. Whoever settles it should also decide whether the A≥2 rows
in the table above are worth re-running — they were attributed to the colour
convention, and the colour convention is real, but the ordering difference
measured here is present at every `A` and was not accounted for.

**Precision note:** the earlier entry's `q0 = 1.1099785827513808` is the
float64-solved `q_parameter.Q` (~16 digits). Downstream agreements floor at
~1e-16 for that reason alone; use `q_at(55)` when the question is whether an
identity is exact.


### SETTLED, and it is a measurement rather than an authoring call

The paragraph above left "which word is correct" as a judgement for the owner.
It is not — it is checkable against Lean, and the check is decisive.

The mass law's Borromean factor has a **Lean-proved closed form**
(`BorromeanMarkovTrace.lean`, consumed by
`m_p_substrate_identity_50dps.trM_borromean`), independent of both word
builders:

    |tr_M(β_Bor, q)| = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

Evaluated at the proton pin and compared against both candidate intra-nucleon
confinement words:

| word | `|tr_M|` | vs the Lean closed form |
|---|---|---|
| `(σ₀σ₁⁻¹)³` **interleaved** | 0.9985621638367872659512131 | **7.0e-61** |
| `σ₀³σ₁⁻³` **grouped** | 0.1800645395355010983036299 | **0.82** |

So the **interleaved** ordering *is* `β_Bor` — the Borromean braid the
framework's own mass law names — verified against Lean to the arithmetic
floor. The grouped ordering is a different object, 82 % away.

`atom_braid_word_3A` — the canonical route feeding `tr_m_atom_zn` →
`binding_canonical` → the binding surface — uses the **grouped** one.

**Scope, stated tightly, because the temptation here is to over-read it.**
This does **NOT** show that any binding number is wrong. Binding is not the
mass identity; whether `binding_canonical` needs `β_Bor` at all is a separate
question this probe does not answer, and the closed form reaches the mass law
without passing through either word builder. What is established is narrower
and still worth acting on: **two production constructions of "the nucleon's
intra-nucleon braid" disagree, and exactly one of them is the Borromean object
the framework elsewhere treats as canonical.**

The next measurement, named precisely: does anything downstream of
`atom_braid_word_3A` depend on its intra-nucleon block *being* `β_Bor`? If yes,
the grouped ordering is a defect with a computed blast radius. If no, the two
are simply different objects with different jobs and the only fix owed is a
docstring on each saying so.

## 2026-09-05 — ANSWERED, and my own framing above is RETRACTED

**Probe:** `computations/probes/atom_intra_block_is_not_a_braid_probe.py`, 5/5, exit 0, mpmath at 60 dps, no float64, emits no witness.

### What I got wrong

The section above asks *"does anything downstream of `atom_braid_word_3A` depend on its intra-nucleon block **being** β_Bor?"* and offers exactly two candidates — interleaved `(σ₀σ₁⁻¹)³` and grouped `σ₀³σ₁⁻³` — asserting that **"`atom_braid_word_3A` … uses the grouped one"** at 0.82 from the Lean closed form.

**That is false. The production block is neither.** Measured (proton, `include_inter=False`):

| | letters | of which non-braid | `|tr_M|` | rel vs Lean `(4+h²−3h⁴−h⁶)/(h²+4)` |
|---|---|---|---|---|
| **REAL production block** | **11** | **2 averaged** | 1.145759692457300869689082 | **0.147409** |
| interleaved `(σ₀σ₁⁻¹)³` = β_Bor | 6 | 0 | 0.9985621638367872659512131 | 9.06872e-72 |
| grouped `σ₀³σ₁⁻³` | 6 | 0 | 0.1800645395355010983036299 | 0.819676 |

So the corrected numbers are **11 letters, 2 averaged, 14.7 %** — not 6 letters and 82 %.

### Why the question was malformed

Two of the block's eleven letters are **averaged**: `σ − (h/2)·1 = (σ + σ⁻¹)/2`, which is **provably outside the image of ρ : B_n → H_n(q)**. The block is therefore **not a braid at all**, so it is not β_Bor and *cannot be* — not "is a different braid", but "is not a braid". The dichotomy the question was built on does not exist.

**And this is documented in the producer's own docstring**, which I did not read before writing the claim. `mass_at_3A_proper.atom_braid_word_3A` opens with **"⚠ NAME IS A MISNOMER — this does NOT return a braid word"**, states "the returned object lies in `H_n(q)` and is **NOT** in the image of `rho`", and gives the exact count: `2A + 1` averaged letters, two per nucleon from its two `ud` pairs plus one per interface. Measured `navg = 2` for one nucleon — the docstring's own arithmetic.

This is the same defect recorded **one day earlier, by me, in the commit message of the probe that established it**: *a source-reading of a word ordering is not evidence about the word.* I wrote that lesson down and then re-committed the error in the next paragraph of the same bean, because I read the construction instead of instrumenting the object.

### The answer to the question as asked

**Nothing downstream can depend on it, because the two routes are DISJOINT.** The mass law reaches β_Bor through the Lean-proved closed form and never through the word builder:

    canonical_mass → m_p_substrate_identity_50dps.F_Bor
                   → _h4_substrate.trM_borromean_closed(q) = (4+h²−3h⁴−h⁶)/(h²+4)

All three of those files contain **zero** occurrences of `atom_braid_word_3A` (asserted by check 4, by reading them). The word builder feeds the *other* route — `tr_m_atom_zn` → `binding_canonical`, and `derived_masses`' `M(𝔥) = ρ·[|tr_M(T_w)| + tower(T_w) + tr_M(C_dim_q)]` with `T_w = atom_braid_word_3A(Z,N)`.

So the disposition the bean named for the no-dependency branch is the right one: **the two are different objects with different jobs**, and what is owed is a docstring — except that `atom_braid_word_3A` already carries it, and it was the *bean* that needed correcting, not the code.

### What this does NOT establish

Not that the 14.7 % gap is acceptable, and not that the binding route *should* consume a non-braid object. Both are live and untouched here. Note in particular that the averaging is exactly what makes the object non-topological: by the producer's own docstring `tr_M` of it is a weighted sum of `2^(2A+1)` link invariants (32 for ²H), so **no volume, crossing number or genus may be read off it** — and all 32 branch closures for ²H were measured non-hyperbolic, `Vol = 0`.

### Contamination — where the wrong figures went

The "grouped / 0.82 / two competing braid words" framing is in: this bean (above, now corrected here); the body of **PR #6712**, merged to `main` as `58ab6f8563`; and my chat report of that PR. It did **not** reach any audit doc, content block, Lean file or witness — the probe committed in #6712 (`nf_vs_canonical_word_order_probe.py`) measures word-ORDER sensitivity and its five checks are unaffected; it never claims the production block is a braid.

## Reconciling the two sections above (2026-09-05, at rebase)

Both sections landed the same day from different sessions and they **agree on
every number**; the clash is one of naming, and the retraction is right about it.

The retraction's `|tr_M| = 1.145759692457300869689082` for the real production
block is *exactly* the `R_quark grouped` proton figure the blast-radius section
below measures (`1.1457596924573008697`). Same object, same engine, same value.

**What the retraction correctly kills:** the phrase "`atom_braid_word_3A` uses
the grouped one", where "the grouped one" meant the six-letter `σ₀³σ₁⁻³` at
`|tr_M| = 0.18`. The production block is **eleven** letters, two of them
averaged, so it is not a braid at all and cannot be `β_Bor` or any other braid.
`0.82` was never the production block's distance from the closed form; `0.147`
is.

**What survives, and is a different claim:** the six confinement letters *inside*
that eleven-letter block were laid down in the grouped arrangement — three `σ₀`
first, three `σ₁⁻¹` seven letters later — rather than alternating. The two
arrangements give production blocks differing by `3.785×` to `14.325×`, measured
against `atom_braid_word_3A` itself (probe §2 rebuilds both and reproduces the
production trace to `1e-60` under each). That is a real difference in a real
object, and it is what the owner ruled on.

**So the correct statement of the fix is narrower than "emits `β_Bor`":** the
confinement *core* is now ordered as `(σ₀σ₁⁻¹)³`. The block around it still
carries two averaged letters and is still not a braid — the producer's own
"⚠ NAME IS A MISNOMER" docstring stands unchanged and unchallenged. Anywhere the
2026-09-05 ordering work said the function "emits `β_Bor`", read "has a
`β_Bor`-ordered confinement core"; the code docstrings have been corrected to
say so.

## The named next measurement: RAN (2026-09-05). The blast radius is a clean split.

The previous section asked: *"does anything downstream of `atom_braid_word_3A`
depend on its intra-nucleon block being `β_Bor`?"* Measured in
`the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe.py` (9/9),
whose grouped rebuild reproduces `atom_braid_word_3A`'s own trace to `1e-60`.

**Answer: log-ratio routes are provably immune; difference routes scale by a
computable factor.**

### Immune — and it is a theorem-shaped reason, not a coincidence

On the chain, `R_nucleon = tr_M(W_atom)/tr_M(W_free)` is identical under the two
orderings to `~1e-60` at `A = 2, 3, 4`, and equals `∏ᵢ(z + dᵢ)` under both.
Connected-sum multiplicativity does not see letter order inside a summand, so
the interface factors survive any reordering of the intra block. `L`, the three
bond constants, `rem:bond-log-ratio-is-a-free-energy` and the whole binding arc
computed as a log-ratio **cannot move**.

### Moves — by exactly `R_quark`

    atom   R_quark grouped   R_quark interleaved   factor
    2H     1.131716904322    0.299015017185         3.785
    3H     1.117846228978    0.142072056797         7.868
    3He    1.296675612245    0.188178642999         6.891
    4He    1.280783151529    0.089409980502        14.325

`binding_canonical` computes `B = Q_β·(tr_M(W_free) − tr_M(W_atom))` — a
**difference**. Both terms carry the same intra factor, so
`Δtr = R_quark·(1 − ∏(z+d))` and that route is *exactly proportional* to
`R_quark`: it would fall by the factors above. Verified numerically, same column.

### A third thing the measurement turned up, unprompted

`rem:canonical-trace-factorises-over-chain` states the per-generator form
`tr_M(∏ᵢ pᵢ(σᵢ)) = ∏ᵢ[w₊pᵢ(q) + w₋pᵢ(−1/q)]`. **That form assumes the grouped
ordering** — it needs each generator's letters contiguous. Grouped factorises to
`~3e-59`; interleaved fails by `2.8×` (`A=2`) to `13.3×` (`A=4`).

The arc's **conclusion** is unaffected: it rests on connected sum, which
survives (measured above). Only the stated identity is ordering-specific. A
caveat section has been added to the block saying so. `QOU.Mass.ChainTraceFactor`
proves the factor algebra and never claims an intra ordering, so the Lean is
untouched.

### What is NOT decided here

Whether `atom_braid_word_3A` should be changed to interleave. That is a
685-call-site edit that moves every absolute trace in the corpus by `3.8×`–`14.3×`,
and it needs an owner ruling, not a probe. This measurement is the thing that had
to come first: it establishes that the fix is *bounded* (one multiplicative
factor per atom, in closed form) and that the log-ratio surface is not at risk
either way.

## FIXED (2026-09-05, owner ruling: "fix atom_braid_word_3A now")

`atom_braid_word_3A` now emits `β_Bor` by default. The change is in
`pyhecke.atom.nucleon_word_letters` — a new WORD-level builder, because
`nucleon_gen_chains` returns the letters bucketed by generator and therefore
*structurally cannot* express an interleaving; that is why the bug survived a
comment (`# B₃ confinement: (σ₀·σ₁⁻¹)³`) sitting directly above the code that
contradicted it. `intra_order="grouped"` reaches the pre-2026-09-05 word, so
every published absolute number stays reproducible (verified to `6e-23`, the
precision of the literal I compared against).

### What the change did to the live suite, measured rather than assumed

- `the_character_ratio_derivation_path_is_the_bond_model_probe` — **numbers
  bit-identical**: `0.508229789376739`, `0.205135640448650`,
  `0.311386312072596`, `0.125684152895266`. A live confirmation of the
  invariance on production code, not a rebuild of it.
- `the_canonical_mass_trace_factorises_over_the_chain_probe` — 2 of 7 checks
  went red exactly as predicted (the per-generator factorisation and the Jones
  product); the bond constants, `L_pp + L_nn`, the 31 % figure and the offset
  inversion did not move. Both red checks are properties of the GROUPED word,
  so the probe now asks for it by name. Back to 7/7.
- `the_canonical_closure_is_a_chain_of_torus_links_probe` — same story, 5/5.
- float64 gate: **0 new hits** (26 pre-existing in `mass_at_3A_proper.py`,
  identical count at HEAD; not touched).

### A sharper fact the fix surfaced, which is not just bookkeeping

The chain form — "every generator in exactly one contiguous run", hence a
linear connected sum of `(2,k)` torus links — is *also* grouped-specific. Under
`β_Bor` each nucleon's block is the **Borromean rings**: prime, non-split, not a
torus link. This arc's own stated criterion for where many-body binding could
live is "a closure that fails to be composite — non-split, prime, with the kind
of irreducibly multi-component linking the Borromean rings have". The corrected
word satisfies that criterion — **at the wrong level**. The nucleons are still
strung on a chain, blocks still overlap in one strand, and `L` is unchanged to
`~1e-60`. So the Borromean structure is intra-nucleon and buys no many-body
binding. Recorded in the block, not overstated.

## FORMALISED (2026-09-05): `QOU.Mass.IntraOrderingInvariance`, sorry-free

Owner: "prove assertions in lean." Twelve theorems, all
`[propext, Classical.choice, Quot.sound]` — no `sorryAx`.

The load-bearing one is **`chainRatio_eq_of_intra`**: given the connected-sum
input (`tr_M(W_atom) = F · ∏ᵢ(z+dᵢ)`, `tr_M(W_free) = F`), two orderings with
intra factors `F₁` and `F₂` give the *same* ratio — and **no hypothesis relates
`F₁` to `F₂`**. That is the point. The measured factors are `14×` apart, and the
invariance still holds, because it is cancellation rather than a near-miss. Then
`L_chain_eq_sum_of_intra` / `L_chain_indep_of_intra` carry it to `L` via
`ChainTraceFactor.neg_log_prod`.

The other half: `chainDiff_scales` proves `F₁(1−P) = (F₁/F₂)·F₂(1−P)`, so
`binding_canonical`'s difference route scales exactly by the intra ratio, and
`chainDiff_ne` proves it genuinely differs when `F₁ ≠ F₂` and `P ≠ 1`.

**`grouped_ne_borromean`** settles that the two words are different objects
without appealing to `q₀` at all: at `q = 1`, where `h = 0` and both are
elementary, the per-generator product is `1/4` and the Borromean closed form
(reused from `QOU.BraidsAndKnots.BorromeanMarkovTrace`) is `1`. So the `82 %`
gap is not a deformation artefact.

### The definitions are pinned to the engine, which is the part that could have been fake

A Lean proof about `groupedConfinement` is worth nothing unless that definition
IS `tr_M(σ₀³σ₁⁻³)`. Probe §7 checks both against the 200-bit engine:

    groupedConfinement    Lean def 0.1800645395355010983036   rel 1.4e-59
    borromeanConfinement  Lean def 0.9985621638367872659512   rel 5.0e-60

So the theorems are about the measured words, not lookalike expressions.

### Scope, stated tightly

Connected-sum multiplicativity is **assumed, not proved** — same as
`ChainTraceFactor`, which says so too. This file proves everything that follows
from it, and nothing about whether the bond model is *right*: `B = α L` remains
the open interpretation of `rem:bond-log-ratio-is-a-free-energy`.

### Toolchain note for whoever builds this next

`lake exe cache get` **cannot run in this container**: the elan toolchain ships
without `libleancpp`/`libLean`, so linking the `cache` executable fails with
`/usr/bin/ld: cannot find -lleancpp`. Mathlib had to be built from source (3089
jobs, ~50 min). Nothing is wrong with the repo; budget for it or fix the
toolchain image.

`QOU.lean` now imports the new module, which also brings
`QOU.Mass.ChainTraceFactor` under the umbrella — nothing had imported it, so it
was invisible to every import-walking tool (blueprint, doc-gen) despite being
compiled by the `globs` target.
