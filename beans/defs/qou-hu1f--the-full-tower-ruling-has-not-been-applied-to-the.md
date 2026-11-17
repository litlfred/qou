---
# qou-hu1f
title: The full-tower ruling has not been applied to the mass/binding surface, where H_3 is the whole object
status: in-progress
pr: 8295
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T20:54:56Z
updated_at: 2026-11-15T17:10:00Z
parent: qou-v2om
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

### ✅ THE PASS IS DONE (2026-09-05, owner-approved "go")

53 producers re-run, one run each, committed witness as the baseline.

    CHANGED (raw)   20      SAME  13      ERROR  16      TIMEOUT  4

**But 20 is not 20.** A binary changed/unchanged test conflates a 1.8× ordering
shift with library last-digit churn, so the raw verdict needed the same
discrimination guard everything else in this bean has needed. Two passes:

    relative magnitude > 1e-9        20 -> 11   (drops 9 metadata/mpmath churn,
                                                 worst case rel 5e-48)
    AND on a non-negligible value    11 ->  9   (drops 2 whose only changes are
                                                 residuals at 1e-17 and 1e-51,
                                                 i.e. numerical zeros)

**9 witnesses were genuinely stale.** The separation is not marginal: 47 orders
of magnitude between the noise ceiling and the material floor, relative shifts of
0.61–1.9 on values from 1e0 to 7.6e3. `h6-deuteron-free-word-chi-lambda` shows it
cleanly — `tr_M_bound` 0.5752 → 0.1520 and `tr_M_free` 1.1317 → 0.2990, a
consistent **3.8×**, exactly the intra-ordering factor measured on this bean.

Only the 9 are committed. The 11 non-material regenerations were reverted: each
would have traded a meaningless digit for a **degraded environment record** (this
container has no `pyhecke_native`, so 6 of the set drop it), and that is the wrong
side of the trade when no number moves.

### THE PAYOFF: the character-closure block is now correct on all three axes

`atomic-tr-m-mpfr-50dps.witness.json` was one of the 9. Its regeneration supplied
the values that block had been flagged for:

    atom       grouped (superseded)   borromean (the ruling)
    proton     1.14575978232          0.62932842249
    neutron    0.98774375682          0.47513351767
    deuteron   0.57517232973          0.15196834396
    tritium    0.22931014615          0.02914404235
    3He        0.40376713691          0.05859625835

A factor of **1.8 to 7.9, growing with A**. The block now carries convention D,
the borromean ordering, and the muon pin — all three from the producer.

### THE RULING BREAKS PRODUCERS, NOT JUST NUMBERS

The 16 errors are the finding this pass did not expect. They split three ways:

**(a) Genuinely broken BY the ruling — 6.** These are not stale numbers, they are
producers whose invariants the alternating word violates:

    classical_floor_derivation_probe      ValueError: non-monotone word: gen 0 after 1
    derived_chi_catalogue_build           duplicate catalogue cell ('borromean', (3,), ...)
    probe_canonical_braid_interface_...   Unrecognised interface d=-0.104458...
    he4_magnus_omega2_sign_sparse_probe   GATE FAIL: sign disagrees with triton
    qbeta_level_k_binding_operator_probe  KeyError: (3, 2, 1)
    qbeta_mixed_chain_closed_form_probe   KeyError: 'tr_M_at_q0'

`classical_floor_derivation_probe` is the clearest: it **asserts the word is
monotone in the generator index**, which the grouped order satisfied and the
alternating order cannot. That assertion encodes the superseded convention.

**(b) Container limitations — 6.** 4 need `pyhecke_native` (absent here, and the
build I made had an incompatible API); 2 fail importing `codata_constants`.

**(c) Witness-gate exits — 4.** These producers ran and emitted; the non-zero exit
is a raw-float64 or environment-record gate, not a computation failure. Their
content was reverted unread by the harness and is still unknown.

### THE RESIDUE PASS — and it grew the BROKEN count, not the regenerated one

The 4 gate-exit producers and the 4 timeouts, re-run (gates tolerated; 1200 s).

**Gate-exits.** All four had genuine numeric change — verified by multiset
comparison, not just a length check, because two of them also gained a new
`invocation` block and a schema addition is not mathematics.
`per-irrep-pole-atom-crystal` shares **zero** numeric values with its
predecessor. But three of the four now have **FAILING ASSERTIONS**:

    markov_trace_axiomatic_multi_atom      char_fast_cross_check_ok
    per_irrep_pole_atom_crystal            asserted_atoms_match_closed_form_shift
    nastokes_multigen_cluster_additivity   R3_rel_lambda_robust_within_10pct

Those are **not stale numbers**. They are the same class as the six errors —
assertions that held under the grouped word and do not hold under the
alternating one. Reverted rather than committed: a witness recording
`passed: false` is a failure, and committing it would file a failure as a
result.

**Timeouts.** `atomic_tr_m_helium4` completed in 481 s and is a genuine
regeneration. `d_frame_interface_twelve_derivation_probe` completed in 450 s
with **no** change (reverted). Two still exceed 1200 s.

### RUNNING TOTALS

    regenerated (correct under the ruling)   11
    BROKEN BY the ruling                      9   <- was 6
    unchanged                                14
    container limitations                     6
    still timing out                          2

**The broken count is the headline.** Nine producers do not merely print
different numbers — they assert properties the alternating word does not have.
`classical_floor_derivation_probe` asserts the canonical word is **monotone in
the generator index**; `per_irrep_pole_atom_crystal` asserts its atoms match a
closed-form shift; `nastokes` asserts a 10 % robustness bound. Each encodes the
superseded convention as a claim about the mathematics.

- [x] Re-run and diff — 11 regenerated in total.
- [x] Gate-exit producers re-run tolerating the gate.
- [x] Timeouts retried at 1200 s — 1 completed, 1 no-change, 2 still over.
### 🛑 THE "9 BROKEN BY THE RULING" IS ACTUALLY 3. I MISATTRIBUTED SIX.

Owner-approved "fix broken producers / work monotonicity". The first thing that
had to go was my own classification, which was built by **reading error strings**
instead of testing.

The discriminator is obvious in hindsight: run each producer with the OLD
ordering forced (patching `atom_braid_word_3A`'s default, so the 332 producers
that never name `intra_order` are covered) and see whether the failure survives.

    fails under BOTH        -> pre-existing, merely surfaced by the pass
    fails only under borromean -> caused by the ruling

Exit code alone is not enough: three producers exit non-zero on a witness gate
under *both* orderings, which masks whether their assertions differ. Those were
re-tested at ASSERTION level.

    producer                                verdict
    nastokes_multigen_cluster_additivity    RULING   16/16 grouped, 15/16 borromean
                                                     (R3_rel_lambda_robust_within_10pct)
    qbeta_level_k_binding_operator_probe    RULING   KeyError: (3, 2, 1)
    classical_floor_derivation_probe        RULING, CONDITIONAL — see below
    markov_trace_axiomatic_multi_atom       pre-existing  char_fast_cross_check_ok
                                                          fails BOTH ways
    per_irrep_pole_atom_crystal             pre-existing  asserted_atoms_match_
                                                          closed_form_shift, BOTH ways
    derived_chi_catalogue_build             pre-existing  non-idempotent
    probe_canonical_braid_interface_comp.   pre-existing  convention mismatch
    qbeta_mixed_chain_closed_form_probe     pre-existing  KeyError: 'tr_M_at_q0'
    he4_magnus_omega2_sign_sparse_probe     UNDECIDED — grouped run timed out

**The two I got most wrong, and how:**

- `classical_floor_derivation_probe` does **not** assert monotonicity. It calls
  the dispatcher, which correctly routes the non-monotone word to the general
  kernel — which then fails on `ModuleNotFoundError: pyhecke_native`, absent from
  this container. So it is ruling-caused only *because* the ruling changes which
  kernel runs; with the native present it would work, slowly. My headline claim
  that it "asserts the canonical word is monotone" was wrong, and the whole
  "decide this first, the others follow" framing rested on it.
- `derived_chi_catalogue_build`'s duplicate cell is `('borromean', (3,),
  'borromean-baryon')` — a **knot** named borromean, word `[-1,+2,-1,+2,-1,+2]`,
  nothing to do with `intra_order="borromean"`. Its committed catalogue is dated
  **2026-06-07**, months before the ruling, and already holds the key. I flagged
  it by matching a string.

**So five of the "broken" producers are pre-existing failures the regeneration
pass merely surfaced** — they are not in CI, so nobody was running into them.
That is a finding in its own right and a better one than the count I reported.

### MONOTONICITY: answered — it is a COST, not a breakage

`chi_monotone_transfer.py` carried, as a "KEY FACT (verified, every atom D…⁷Li)",
that the atom braid word has a monotone non-decreasing generator sequence.
Measured under both orderings:

    grouped     [0,0,0,0,0,0,0,1,1,1,1,2,3,3,…]   monotone
    borromean   [0,1,0,1,0,1,0,0,1,0,0,2,3,4,…]   NOT monotone

**The ruling falsifies it.** Monotonicity *is* contiguity, so this is a fourth
instance of the pattern `docs/audits/2026-09-06-canonical-extremality-is-grouped-
specific.md` documents, alongside per-letter factorisation, the six `c₁` values
and the `f₁/f₀` extremality. Docstring corrected to say so.

It is not breakage. `chi_all_lambda_any` dispatches on `word_is_monotone` and
routes non-monotone words to a general kernel that is **correct but `d_λ`-bound**
— A=3 costs 0.36 s, A=4 costs 621 s, A≥5 impractical (`qou-wdij`). **That is
exactly why two producers time out at 1200 s.** The ruling's real cost is
scalability, and the fix that restores `O(A)` is the three-level-window transfer
that `chi_kernel_conformance_harness` was written to be the oracle for.

### FIXED

- `interface_composition.py` accepted only `d = -h/2` for a pn junction, while
  `atom_braid_word_3A` defaults to `pn_convention="bring_color_weighted"` and
  emits `-h(1-δ/2)/2 = -0.104458…`. Verified to 1e-12 against
  `flavor_split_leading`. Both spellings now accepted, δ derived rather than
  hardcoded so the two cannot drift.
  `probe_canonical_braid_interface_composition` now passes **6/6**, "all atoms
  closed-form == from-word: True". Confirmed pre-existing: it failed identically
  under grouped.

- [x] Classification corrected — 3 ruling-caused, 5 pre-existing, 1 undecided.
- [x] Monotonicity settled and the false KEY FACT corrected.
- [x] The pn convention mismatch fixed.
- [ ] `he4_magnus_omega2_sign_sparse_probe` — needs >300 s under grouped to
      decide which bucket it is in.
### ✅ BOTH GENUINE BREAKAGES FIXED — and each was hiding a finding

**`qbeta_level_k_binding_operator_probe` — `KeyError: (3, 2, 1)`.** Section [5]
hardcodes `(3,2,1)` and `(2,2,1,1)` and looks them up in `small`, the shapes
carrying a sub-unit eigenphase. Under the ruled word `small` is **empty** — the
probe's own stdout says so — and the lookup raised.

**The absence is the result.** That section exists to show the 0.13 % sum
coincidence is a degeneracy-wall artefact; under the ruled word the coincidence
*does not arise at all*, which is stronger. The guard reports that and the
assertion passes on the absence rather than being skipped — skipping drops a
check. With the crash gone the probe reports what it was hiding:

    grouped     8/8
    borromean   6/8
      binding_character_is_largest_in_a_tl_kernel_block   fails
      the_only_small_eigenphases_are_in_blind_blocks      fails

**`nastokes_multigen_cluster_additivity` — `R3_rel_lambda_robust_within_10pct`.**
One boolean over `max(spreads)` across three independent measures, so a single
one moving turned the flag red without saying which:

    measure       grouped   borromean
    (0,1)         1.034x    1.059x     robust under both
    (3,4)         1.099x    1.065x     robust under both
    band-local    1.044x    2.099x     GROUPED-SPECIFIC

Per-measure flags added alongside the aggregate (kept, so nothing silently
loosens). Witness now reads 17/19 with `[band-local]` named. Note `(3,4)` sits
at **1.099 under grouped** — 0.001 from the threshold — so the old single flag
was one digit of noise from failing for an unrelated reason.

### THE GROUPED-SPECIFIC LIST IS NOW SEVEN

    1. per-generator/per-letter factorisation      (prior)
    2. the six c₁ values                           (prior)
    3. f₁/f₀ extremality                           (prior)
    4. MONOTONICITY of the generator sequence      (this pass)
    5. binding character largest in a TL-kernel block   (this pass)
    6. small eigenphases confined to blind blocks       (this pass)
    7. band-local λ-robustness within 10 %              (this pass)

Each was a property of **contiguity**, and each read as evidence of
correctness until the ruling separated the two. Three of them were only
visible because a crash was removed.

Corroboration from a sibling: `docs/audits/2026-09-06-the-classical-floor-is-
interface-parity.md` measures the ℏ_q⁰ floor **invariant** under both
`intra_order` and `pn_convention` — which independently confirms that
`classical_floor_derivation_probe`'s failure cannot be mathematical, exactly
as the discriminator found.

- [x] Both genuine ruling breakages fixed.
- [ ] `he4_magnus_omega2_sign_sparse_probe` — still undecided; needs >300 s
      under grouped to place it in a bucket.
- [ ] The three pre-existing failures with no obvious fix
      (`derived_chi_catalogue_build` non-idempotency,
      `markov_trace_axiomatic_multi_atom` and `per_irrep_pole_atom_crystal`
      failing their own assertions both ways) are unrelated to this bean and
      want beans of their own.

### METHOD NOTE, EARNED TWICE

A blanket `git checkout -- computations/` run to clean witness churn destroyed
the qbeta source fix **twice** before it landed. Commit the source change
BEFORE cleaning generated files; the two live in the same directory and a path
that matches one matches the other.
- [ ] `binding_combiner_markov_peel_fallback` and `triton_magnus_omega2_sign_probe`
      need >1200 s, or a smaller case.
- [ ] Decide whether `intra_order` should have defaulted at all. A
      behaviour-changing default across 339 callers is invisible by construction;
      an explicit-argument-required signature would have surfaced all 332 at
      import time instead of silently changing their numbers.

## Last undecided producer classified — the pass is closed

`he4_magnus_omega2_sign_sparse_probe` was the one producer left unplaced after
the regeneration pass. Forced to the OLD `grouped` ordering it ran **33+
CPU-minutes without completing** inside a 2700 s budget — the same outcome it
has under `borromean`.

    fails/does-not-complete under BOTH orderings  ->  PRE-EXISTING

So it is not a breakage of this ruling. Its cost is structural: it dispatches
over all 77 partitions of 12, building `sigma_csr`/`germ_csr` at dimensions to
d_λ = 7700, and its weight family (`d_q²/[n]_q!`, Plancherel) vanishes nowhere,
so the row cap that bought 99.5x on the Wenzl bridge (`qou-fq0f`) cannot be
applied to it as written. Recorded separately as **`qou-za3q`**, which also
raises whether that weight is the intended one — it is named `y_λ` in its own
docstrings while being a different family.

Final tally for the pass: two genuine breakages (both fixed), and every other
failure pre-existing — `qou-pdfx`, `qou-g94g`, `qou-4sqq`, and now `qou-za3q`.

## One producer the sweep missed

`binding_canonical.py` was still emitting **grouped** values and nothing caught
it: deuteron `tr_M_atom` 0.57517224391777 (grouped) where the ruling gives
0.15196833920423. Surfaced only when it was re-run as a smoke-test of an
unrelated change, not by the 56/57-witness sweep — because its witness does not
reference `atom_braid_word_3A` by name, which is how that sweep selected its
targets. Regenerated; tritium, helium-3 and helium-4 moved with it.

That is a gap in the sweep's selector, not a one-off: any producer that reaches
the canonical word indirectly was invisible to it. Worth re-running the sweep
on a selector that keys on the VALUES (a grouped-era tr_M is recognisable) rather
than on the import name — the same argument
`y_lambda_convention_c_fingerprint_audit.py` makes for convention detection.
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

## Overclaim corrected at rebase (2026-09-05) — the retraction was right, and it caught me too

The 2026-09-05 ordering work said `atom_braid_word_3A` "emits `β_Bor`" and that
"each nucleon's block **is** the Borromean rings". Both are wrong, in exactly the
way the retraction section above names, and they are corrected in the code
docstrings, the probe docstring and the content block.

- The block is **eleven** letters, two of them averaged, hence not a braid and
  not `β_Bor` under any arrangement. Only its six-letter confinement **core**
  changed order.
- "The block is the Borromean rings" was worse than loose: a block with averaged
  letters has no single closure at all — `tr_M` of it is a weighted sum of
  branch closures — so there is no link to identify.
- The follow-on claim that the corrected block therefore satisfies this arc's
  "non-split, prime, irreducibly multi-component" criterion is **withdrawn**. It
  fails twice: a weighted sum of closures is not one link, and containing
  `β_Bor` as a subword is not being prime. What is measured is only that `L` is
  unchanged to `~1e-60`.

The measurements were never affected — probe §2 rebuilds both arrangements and
reproduces `atom_braid_word_3A`'s own trace to `1e-60` under each, and the
retraction's `1.145759692457300869689082` is the same number as this bean's
`R_quark grouped` proton. It was the *prose* that outran them, which is the
identical failure the retraction records one section up. Twice in one day on one
bean is the signal: **do not name an object from how it was constructed.**

## 🛑 THE 5.045e-4 RESIDUAL WAS A COINCIDENCE — this bean's founding number is retracted

Found at rebase, because fixing the ordering made
`nf_vs_canonical_word_order_probe` go **3/5**. The failure was correct and the
probe was wrong.

**This bean concluded "the A=1 residual IS the word order". Withdrawn.**
Decomposed at 200 bits:

    grouped intra, no electron   (pre-fix canonical)  1.1457596924573008697
    interleaved intra + electron (the NF route)       1.1463376906350050736
      -> rel 5.044672e-04                             the "known residual"

    grouped intra + electron                          1.5534762115753358114
      -> ordering alone, electron held fixed:  6.38x
    interleaved intra, no electron (canonical now)    0.6293284022029219182
      -> electron alone, ordering held fixed:  0.82

`build_atom_nf` adds `Z` electron crossings on gen 1; `atom_braid_word_3A`
deliberately does not — it is the **nucleus**. So the two routes differed by
**both** the ordering and the electron, and two large unrelated discrepancies
landed within `5e-4` of each other. `build_atom_nf_mp(1,0)` is now verified to
be exactly `atom_braid_word_3A(1,0)` plus one `σ₁⁻¹`, to `1e-40` — 25 digits
agreeing, so this is identification, not a fit.

The ordering fix removed one term and exposed the other at full size. That is
why the probe went red, and the red was informative.

### How it survived a day: a hardcoded transcription

Check 4 compared the canonical word against a **hardcoded** `nf_seq` literal
transcribed from `build_atom_nf`'s source — and that transcription omitted the
electron. So it asserted "same multiset, different order" against a word whose
trace it does not reproduce. Nobody noticed because the two errors cancelled
into a plausible-looking `5e-4`.

**Third instance on this bean of the same error class** — naming an object from
how it was constructed rather than instrumenting it. The first two are recorded
above; this one had been passing CI. The rule that keeps failing to stick:
*if a probe prints a word, it must have obtained that word from the producer,
not from reading the producer.* Both checks are now measurements, 5/5.

### What is NOT retracted

The ordering finding itself. `(σ₀σ₁⁻¹)³` is still `β_Bor` to `7e-61`, the
grouped arrangement is still `82 %` away, and the two arrangements still give
production blocks differing by `6.38×` at `A = 1`. What changes is the *story
about the residual*: it was never evidence for the ordering, because it was
never a pure ordering effect. The ordering finding rests on the Lean closed
form, which is untouched by any of this.

## GATED (2026-09-05): `scripts/word-provenance-gate.py`

Three instances of the same error on one bean in two days, one of them green in
CI — that is a gate, not another bean note. Owner: "add the gate."

**What it catches.** A hardcoded braid word — a list of 2- or 3-tuple crossing
letters, including `+`/`*` forms — assigned to a name, in a file that also
references a word producer or a Markov-trace entry point. Escape hatch
`# word-literal-ok: <reason>`, which may head a multi-line provenance note.

**The mechanism is the annotation, not the detection.** Writing down *why* a
literal is trustworthy is the moment the author looks for the electron. An
annotation reading "transcribed from `<producer>`" is the defect restated, and
the gate's message says so.

### Validated against the real defect, not a mock

Run against the actual committed `nf_vs_canonical_word_order_probe.py` at
`08cb80478a9`, it flags `nf_seq` at line 182. **The gate would have caught the
thing that shipped green.**

### Precision: 151 -> 20, by narrowing three times

The first predicate fired on every isotope table in the corpus (`(Z, N)` pairs,
`("2H", 1, 1)` rows, decay tables). A gate at 151 hits, mostly noise, is one
nobody can adopt. Narrowed to three routes — word-ish NAME, crossing-string
VOCABULARY, `(c, d, gen)` SHAPE in a file naming a trace — with a `tabular`
exclusion for literals carrying non-crossing strings. Every surviving hit is a
genuine word literal.

### The self-test caught me twice, which is the point of having one

- The escape hatch silently did not work for a marker heading a multi-line
  comment block — the shape a real provenance note takes. Found because my own
  annotation failed to suppress its hit.
- **The first negative control did not discriminate.** Deleting the whole NAME
  route left the self-test green, because the known positive `nf_seq` was also
  caught by the crossing-string route. A self-test with one known positive
  proves only that *something* matches. Now each route has its own positive, and
  all five negative controls (disable NAME / TOKEN / SHAPE / detection / the
  tabular exclusion) fail the self-test as they must.
- The self-test count is derived, not written down: a hardcoded `4/4` was wrong
  within an hour, which is the same stale-literal failure the gate is about.

### Wiring, and why it is not blocking on the whole tree

`.github/workflows/word-provenance-gate.yml` is **diff-scoped and blocking**,
exactly as `probe-float64-gate.yml` is and for the same reason. It stops the
number growing.

`scripts/precision-gates.sh` carries it **advisory**, red at 20, to keep the
backlog visible. Those 20 are essentially all legitimate first-principles
constructions (`(σ₀σ₁⁻¹)³` and friends) that need a one-line annotation — and
they are deliberately **not** bulk-annotated here: writing "trustworthy
because…" for a file I have not read is the same defect the gate catches. Drain
per file, by whoever owns it. Two are annotated, in the probe I actually worked.

### What it does not reach

Prose. Instances 1 and 2 were sentences in a bean and a docstring, and no static
check touches those. The gate narrows the class; the rule still stands — **if
you state what word a producer emits, you must have called it.**


## 2026-09-05 — a CONSUMER THAT STOPS, not one that scales: the alternating word
## is non-monotone and `reduced_block_kernel` refuses it

Found while sweeping the downstream of the chi-cache regeneration (`qou-92u9`),
which this ruling made necessary.  Recorded here because it is a consequence of
the ordering change, not of that bean.

`reduced_block_kernel.chi_all_lambda_reduced_block` (line ~147) raises

    ValueError: non-monotone word: gen {g} after {last}

when a word's generator indices are not non-decreasing.  Measured directly on
`atom_braid_word_3A` under both orderings:

    atom       grouped monotone   borromean monotone
    proton           True               False
    deuteron         True               False
    tritium          True               False
    helium-3         True               False
    helium-4         True               False

**Every atom, both directions.**  So for this route the ordering change is not a
factor to divide out — the code refuses the input.  `he3_pairknot_composite_lp`
is the producer that hits it.

**This is the executable form of a fact this bean already records.** The
blast-radius section notes that `rem:canonical-trace-factorises-over-chain`'s
per-generator form *"assumes the grouped ordering — it needs each generator's
letters contiguous"*, and measured the factorisation failing by 2.8x (A=2) to
13.3x (A=4).  Contiguity of each generator's letters **is** monotonicity of the
generator sequence.  The bean measured the identity degrading; this is a
consumer that halts on the same premise.

**Why it is worth adding rather than folding into that note.** The existing
entry frames the consequence as an accuracy claim about one stated identity,
with the arc's conclusion "unaffected" because it rests on connected sum.  That
is right for the identity.  It does not predict that a *producer* becomes
unrunnable, which is a different kind of cost and lands on a different owner.

**Not fixed here.**  Whether `reduced_block_kernel` should be generalised to
non-monotone words, or whether its callers should be re-routed, is a design
question for whoever owns that module.  Tracked as an open item on
`qou-92u9`'s sweep triage; noted here so the ordering ruling carries its own
consequence.

### Item 2 of the grouped-specific list now has its canonical replacement (2026-09-06, PR #6920)

Cross-reference for whoever works this ledger next: **"the six c1 values" (item 2) is no longer
just a hole.** The closed form on the CANONICAL word is derived and verified on 44 isotopes:

    c1(Z,N) = (Z*S_p + N*S_n)/2 * (2^(-A-1) - 2^(-2A)) - 4*(I_pp - I_nn)*2^(-2A)

with S_X the per-nucleon deletion sum on that nucleon's own three strands. The ONLY
ordering-dependent input is (S_p, S_n): **borromean (6, -4)** -> (3Z - 2N), grouped (42, 32) ->
(21Z + 16N). Verified A = 1..8, exact Fractions, both halves ([*](free) and [*](atom)) separately,
44/44 each under BOTH orderings; A = 8 held out of the pattern search.

**This is direct quantitative support for this bean's "each was a property of contiguity" reading.**
Per-letter deletion contributions for one proton:

    grouped     +2^3 +2^3 +2^3 +2^3  .  +2^3 +2^3 -2^1 -2^1 -2^1  .   = 48 - 6 = 42
    borromean   +2^1 -2^1 +2^3 -2^1 +2^1 -2^3 +2^1  .  .  +2^1 +2^1   =          6

Contiguous sigma runs leave the same cycle count and add COHERENTLY; alternation interleaves them
with opposite-sign sigma^-1 deletions and they CANCEL. So contiguity is not merely correlated with
the seven properties — for this one it is the arithmetic mechanism, and the cancellation is
computable per letter.

Note the neutron sum CHANGES SIGN (32 -> -4), so canonical c1 is negative for neutron-rich isotopes
where the grouped one was positive throughout. Any item on the list involving a p/n asymmetry is
worth re-checking for a sign flip rather than just a magnitude change.

Also relevant to this ledger: the interface term -4(I_pp - I_nn)2^(-2A) is UNCHANGED by the
reordering, and that is verified rather than assumed — interfaces are single letters outside the
nucleon blocks, so nothing reordered within a nucleon can reach them. A candidate rule for triaging
the rest of the list: a quantity built only from INTER-nucleon structure should survive the ruling;
one built from intra-nucleon letter positions should be assumed broken until measured.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-06 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-15 — re-scoped by the γγ rule

The owner ruled that the γγ selection rule also covers the nuclear bond letters. Any number in this bean computed on the single-crossing interface letters of `atom_braid_word_3A` (`d_k`, `μ_e`, the chain law `∏(z_D + d_k)`, the `b₃` magnitudes −1.2277 / −0.7973 MeV, or a sign map on that word) is now a record of a superseded word, not a current result. Lean results stated for generic bond weights are unaffected. The redo waits on a γγ-selected word per nucleus (PR #7876). Record: `docs/audits/2026-11-15-gg-rule-rescopes-old-letter-binding.md`. The bean stays open.
