---
# qou-hu1f
title: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the whole object
status: in-progress
type: task
priority: normal
created_at: 2026-09-04T20:54:56Z
updated_at: 2026-09-05T05:59:38Z
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


## LOCALISED: the invariant HOLDS; the two routes build the same letters in a DIFFERENT ORDER

### Step 1 — the per-element check clears all the trace machinery

`tr_M(b_i)` vs `Σ_λ y_λ χ_λ(b_i)` on all six NF basis elements at `n = 3`:

| `b_i` | `TR_M[i]` | `Σ_λ y_λ χ_λ` | abs diff |
|---|---|---|---|
| `1` | 1.0 | 1.0 | 1.07e-50 |
| `σ₀` | 0.6126880371464653 | 0.6126880371464653 | 8.11e-17 |
| `σ₁` | 0.6126880371464653 | 0.6126880371464654 | 1.11e-16 |
| `σ₀σ₁` | 0.3753866308623884 | 0.3753866308623887 | 2.89e-16 |
| `σ₁σ₀` | 0.3753866308623884 | 0.3753866308623887 | 2.89e-16 |
| `σ₀σ₁σ₀` | 0.6911664783584445 | 0.6911664783584451 | 5.39e-16 |

**The invariant holds to the float64 floor on every element.** So the 5.045e-4 is
NOT in `TR_M`, NOT in `y_λ`, NOT in `χ`. (Characters computed in float64 via
`chi_lambda_braid_word`; adequate to LOCALISE a signal 12 orders above that
floor, and not offered as a precision claim.)

Incidental: `y_λ(1,1,1) = 0.0` exactly at `n = 3` — the fully antisymmetric
channel carries zero Jones-Markov weight. Noted, not chased.

### Step 2 — by elimination it is the WORD, and it is

`atom_braid_word_3A(1, 0)` (canonical) against the proton branch of
`build_atom_nf_mp` (NF), as `(d-tag, generator)`:

    canonical gen sequence:  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    NF        gen sequence:  [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]

    canonical multiset: {('-h',1):3, ('-h/2',0):1, ('-h/2',1):1, ('0',0):6}
    NF        multiset: {('-h',1):3, ('-h/2',0):1, ('-h/2',1):1, ('0',0):6}

    MULTISETS EQUAL : True
    SEQUENCES EQUAL : False

**Same eleven letters, different order.** The canonical word applies all seven
generator-0 letters and then all four generator-1 letters; the NF word
interleaves them (three `σ₀ σ₁⁻¹` pairs, then uu / ud / ud / gluon / gluon).
`H_3` is non-commutative, so these are different elements and the Markov trace
has no reason to agree — which accounts for the 5.045e-4 with **no defect
anywhere in the trace machinery**.

### Scope, and a stated limitation

- This says the two routes trace **different braid words for a single nucleon**.
  It does **not** say which ordering is correct. That is a physics/convention
  judgement about what the nucleon braid IS, not something to assert from a
  numerical disagreement.
- **The NF sequence was transcribed BY HAND** from `compound_shift_nf.py`'s
  proton branch, not extracted programmatically (that function returns the
  reduced vector, not its word). The exact multiset match is strong evidence the
  transcription is faithful — a wrong transcription reproducing all four letter
  classes at the right multiplicities would be a coincidence — but it is a
  transcription, and anyone building on this should re-derive it from the source.
- The A>=2 rows remain uninterpretable for the separate colour-weighting reason
  recorded above. This localisation is A=1 only.


## 🛑 CORRECTION — "same eleven letters, different order" is WRONG. The caveat bit.

The entry above says the two routes apply the **same multiset** of letters in a
different order, and flags that the NF sequence was **transcribed by hand**.
Retired that caveat by recording the letters from the RUNNING code (wrapping the
module-level `compound_shift_nf.hm_mp`, no source change), and the hand
transcription was **wrong**:

    canonical  11 letters
    NF         12 letters      <- not 11
    MULTISETS EQUAL: False     <- not True

The exact difference at (Z=1,N=0) is **one letter**:

    canonical multiset: {('-h',1):3, ('-h/2',0):1, ('-h/2',1):1, ('0',0):6}
    NF        multiset: {('-h',1):4, ('-h/2',0):1, ('-h/2',1):1, ('0',0):6}

"Different order" was the *shape* of an answer I reached by eye, and the multiset
match that made it convincing was an artifact of my own miscount. Recording it
because I had explicitly named the transcription as the weak link and was still
persuaded by the thing it undermined.

## What is actually there: TWO structural differences, both in closed form

### 1. A per-proton trailing letter, uncommented

At the very end of `build_atom_nf_mp`, after the per-nucleon and interface loops:

    for _ in range(Z):
        nf = hm_mp(nf, one, -h, 1, h)

One extra `('-h', 1)` **per proton**. Every other letter in that function carries
a comment (`σ₀`, `σ₁⁻¹`, `uu pair`, `ud mixed`, `gluon 1`, `gluon 2`); this loop
has none.

### 2. The interface schedules differ — and this one connects to a proved result

Measured word lengths over 7 configurations, and both closed forms reproduce
**all seven exactly**:

| Z,N | A | canonical | `12A-1` | NF | `11A + C(A,2) + Z` |
|---|---|---|---|---|---|
| 1,0 | 1 | 11 | 11 | 12 | 12 |
| 0,1 | 1 | 11 | 11 | 11 | 11 |
| 1,1 | 2 | 23 | 23 | 24 | 24 |
| 2,1 | 3 | 35 | 35 | 38 | 38 |
| 1,2 | 3 | 35 | 35 | 37 | 37 |
| 2,2 | 4 | 47 | 47 | 52 | 52 |
| 3,1 | 4 | 47 | 47 | 53 | 53 |

    gap = C(A,2) - A + Z + 1

The `C(A,2)` is **read from the code, not fitted**: `for prev in range(k)` runs
over every previous nucleon, i.e. the complete graph. The canonical `12A-1` IS a
fit over four values of A and should be confirmed at the source before being
leaned on.

**Why that matters beyond bookkeeping.** `QOU.Mass.CoordinationSaturation`
(sorry-free) refutes `M = C(A,2)` as a coordination law — it gives `B/A =
ε(A-1)/2`, unbounded, no plateau, so observed saturation forces bounded degree.
The NF route's interface schedule is exactly that refuted complete graph, while
the canonical route's is linear in A. So the two routes differ on precisely the
axis a proved Lean result already rules on.

### Scope

- This does **not** say the NF route is wrong. It says the two routes build
  different braids, in two identified ways, and that one of those ways
  (complete-graph interfaces) is the shape `CoordinationSaturation` excludes as
  a *law*. Whether `build_atom_nf_mp` intends to be a coordination law at all is
  not established here.
- The A=1 residual (5.045e-4) is now fully explained by difference 1 alone: at
  A=1 there are no interfaces, and the words differ by exactly the one trailing
  proton letter.


## The last fitted quantity is now measured — and BOTH schedules are already excluded in Lean

`12A-1` was the one number above obtained by fitting four points. Confirmed at
the source and extended to A=6. Interface count = total minus `11A`:

| Z,N | A | total | 11A | interfaces | A-1 | C(A,2) |
|---|---|---|---|---|---|---|
| 1,0 | 1 | 11 | 11 | 0 | 0 | 0 |
| 1,1 | 2 | 23 | 22 | 1 | 1 | 1 |
| 2,1 | 3 | 35 | 33 | **2** | 2 | 3 |
| 2,2 | 4 | 47 | 44 | **3** | 3 | 6 |
| 3,1 | 4 | 47 | 44 | **3** | 3 | 6 |
| 3,2 | 5 | 59 | 55 | **4** | 4 | 10 |
| 3,3 | 6 | 71 | 66 | **5** | 5 | 15 |

**Canonical interfaces = A-1 exactly: a LINEAR CHAIN.** Independently corroborated
by the function's own docstring, which accounts for `2A + 1` non-braid letters as
"two per nucleon ... plus one per interface" — one interface at A=2, i.e. a chain.
So `11A + (A-1) = 12A - 1`; the fit was right and is now derived.

### The two routes sit on the two coordination laws the corpus has ALREADY excluded

    canonical:  11 letters/nucleon + (A-1) interfaces        <- LINEAR CHAIN
    NF:         11 letters/nucleon + C(A,2) interfaces + Z   <- COMPLETE GRAPH

And AGENTS.md records a proved, sorry-free Lean exclusion for **each**:

- **Complete graph** — `QOU.Mass.CoordinationSaturation`: `M = C(A,2)` gives
  `B/A = eps(A-1)/2`, unbounded, no plateau; observed saturation forces bounded
  degree, so `z = A-1` is refuted **structurally**, not merely at 4He. That is
  the NF route's schedule.
- **Linear chain** — `QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff`:
  the chain bond sum is arrangement-invariant iff `L_pp = L_pn = L_nn`, and a
  nucleus has no arrangement (scope-(b), bean `qou-m07y`). That is the canonical
  route's schedule.

**Neither schedule is a coordination law the corpus can hold.** The two routes are
not "one right, one wrong" — they are the two shapes the extensive-term arc has
separately proved cannot carry the binding law.

### Scope — what this does NOT say

- Those Lean results exclude these graphs **as coordination laws for the
  extensive binding term**. They do not, by themselves, say a word builder may
  not use such a schedule for some other purpose. Whether either builder claims
  to be a coordination law is **not** established here, and asserting it would be
  the set-level-to-truth-value slide AGENTS.md names as `da-arity-conflation`.
- It does not identify a defect in either builder, and does not say which word is
  the nucleon.


---

## 🛑 RESOLVED, and it was never a defect: the per-proton letter is the ELECTRONS

I called the trailing `for _ in range(Z)` loop "the only letter in that function
with no comment" and put it to the author as an open question. **It is fully
explained**, and the explanation is in the corpus — just not in the Python file.

`tools/hecke-engine/src/gram.rs:673 build_atom_nf` is the Rust original of the
same construction, and there the loop reads:

    // Electrons: pe crossing (EM channel, gen=1)
    for _ in 0..z_count {
        nf = hm(&nf, 1.0, -h, 1, h);
    }

**One proton-electron crossing per proton** — a neutral atom has `Z` electrons.
The Python port dropped the comment; nothing else.

### The real finding this exposes: the two builders model DIFFERENT OBJECTS

Measured: `mass_at_3A_proper.py` contains **zero** occurrences of
`electron` / `EM channel` / `pe`. Its own docstring accounts for every letter as
"two per nucleon ... plus one per interface", with no electron term, and its name
says `3A` — three strands per nucleon, nothing else.

    build_atom_nf / build_atom_nf_mp   nucleus + Z electron crossings  -> the ATOM
    atom_braid_word_3A                 3A strands, no electrons        -> the NUCLEUS

So the A=1 residual of 5.045e-4 is **the hydrogen electron**. Not a bug, not a
convention mismatch — the two routes were never computing the same object, and
comparing their traces was comparing an atom against a nucleus.

**A naming trap worth recording:** `atom_braid_word_3A` has "atom" in its name and
contains no electrons, while `build_atom_nf` has "atom" in its name and does. That
function already carries a `NAME IS A MISNOMER` banner for a different reason (it
returns Hecke elements, not a braid word); this is a second way the name misleads.

### What this does and does not change

- **Retires** the "uncommented per-proton letter" as a question for the author.
  The Python port should carry the Rust comment; that is a docs fix, not a
  decision.
- **Does NOT** explain the interface-schedule difference (chain `A-1` vs complete
  graph `C(A,2)`). That is inter-nucleon, has nothing to do with electrons, and
  remains exactly as recorded above.
- **Does NOT** retract the probe: every assertion in
  `nucleon_word_route_divergence_probe.py` still holds as measured. What changes
  is the INTERPRETATION of the one-letter difference at A=1.

## 🛑 THE RULING'S REAL BLAST RADIUS IS `atom_braid_word_3A`, AND IT IS 339 CALLERS

Found 2026-09-05 from `qou-i229`/`qou-46ab`, by trying to regenerate an unrelated
witness and getting a different number.

This bean scoped consumers of **`build_atom_nf_mp`** and measured **7**. But the
intra-ordering default the ruling changed lives on **`atom_braid_word_3A`**:

    339  live Python callers (excluding _deprecated)
      7  that name `intra_order` explicitly
    332  that SILENTLY take the new `borromean` default
     57  committed witnesses referencing it

**Every witness among those generated before 2026-09-05 and not regenerated is
now stale**, and stale invisibly — the producer still runs, still passes its own
assertions, and returns a different number.

### The worked example

`atomic-tr-m-mpfr-50dps.witness.json` (computed 2026-08-29) records
`tr_M(proton) = 1.14575978231523894`. Re-running the producer today gives
`0.62932842249489294`. Same pin, same anchor, same 11-letter word length, same
kernel. Measured directly:

    intra_order=grouped     1.1457598292260762   <- reproduces the witness
    intra_order=borromean   0.6293284926174815   <- the ruling

A factor of **1.82** on the proton and **2.08** on the neutron. Not the kernel
(`--method hoefsmit-python` agrees) and not a native-extension issue (the
pure-Python fallback gives the same).

### It has already propagated into published content

`prop:q-hecke-seminormal-character-closure` was migrated C → D earlier the same
day **from that stale witness**, so its five nuclei are now right in convention
and wrong in ordering. The block is flagged rather than re-substituted: those
figures moved once already today on a witness that predates a ruling, and moving
them again before the ordering question is settled for that quantity would
compound rather than fix.

### Date-partitioned (2026-09-05)

    witnesses referencing atom_braid_word_3A (live)   57
      computed BEFORE the ruling                      56   <- candidate stale
      computed on/after                                1
      no computedAt                                    0

Oldest run to 2026-05-09, so this is not a recent-drift problem — it is the whole
history of the function's consumers.

**56 is an UPPER BOUND, not the answer.** A witness referencing the function is
only stale if the intra-word core actually reaches a value it records: a producer
may call it for a crossing count, at a size where the core is degenerate, or pass
`intra_order` explicitly. Confirming each means re-running its producer and
diffing — which is the job, and which is why the number to act on is smaller than
56 and cannot be got at by grep.

- [ ] Re-run the 56 and diff. Mechanical but not cheap; worth doing as one
      tracked pass rather than opportunistically, because a half-regenerated set
      is harder to reason about than an un-regenerated one — the same lesson the
      `q₀` refresh learned about per-block completeness.
- [ ] Decide whether `intra_order` should have defaulted at all. A
      behaviour-changing default across 339 callers is invisible by construction;
      an explicit-argument-required signature would have surfaced all 332 at
      import time instead of silently changing their numbers.
