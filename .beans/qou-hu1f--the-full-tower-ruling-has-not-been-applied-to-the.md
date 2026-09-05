---
# qou-hu1f
title: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the whole object
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:54:56Z
updated_at: 2026-09-04T21:09:29Z
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
