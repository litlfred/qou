# Can c₃^odd, Q_β or the f-map be closed? — assessment, and one confirmed defect

**Date:** 2026-08-26 · **Branch:** `claude/math-gaps-analysis-faydin` ·
**Beans:** `qou-ckwt` (the defect), `qou-ximf` (the moment family) ·
**Tier:** one confirmed defect + one derived structural family; **nothing wired,
no `c_k` value proposed, no tier moved.**

Asked: *"lots of new math in last week — can we close c₃^odd, Q_β or the f-map
gaps? new attack options?"*

Short answer: **no, none of the three is closeable now**, and the reason is
different in each case and is *already established in the corpus* — the last
week's work narrowed all three rather than opening any. What this pass adds is
(1) a **confirmed** live defect on the canonical `c_k` producer, and (2) one
derived structural family for the single undetermined object in the Q_β chain.

---

## 1. The defect — CONFIRMED, and it is the canonical `c_k` producer

`computations/qbeta/qbeta_ck_cache.py` is the producer of the framework's
headline **derived-tier** Q_β number. At HEAD its single Markov-parameter
assignment (line 85) is

```python
z = q**3 / (q**2 + 1)          # convention D
```

while its committed witness `qbeta-ck-cache.witness.json` carries the
**convention-C** value `c_3 = −2.06934257711516783787971951725`.

**The producer no longer reproduces its own witness.** Run on `main` today
(tree restored afterwards; `git status` clean):

| quantity | committed witness (C) | producer re-run today (D) |
|---|---|---|
| `c_3` | −2.0693425771 | **−974.4318877** |
| derived-tier `Q_N2` error | 1278.6 ppb | **602 433.2 ppb** |

That is a **471× regression in the derived Q_β prediction**, sitting one
`python3 qbeta_ck_cache.py` away from landing in the canonical cache.

### What was already known, and what is new here

The **class** is known and instrumented: `convention-frame-staleness-audit`
reports 155 producers with a D-form, 47 suspect witnesses — and
`qbeta-ck-cache.witness.json` **is already in its `candidates` list**. So this
is not a new discovery.

What is new is that it was **only a candidate**: 2 of the 47 carried a
`confirmed_by_decisive_test` entry, and this was not one of them. This pass ran
the decisive test on the highest-value candidate in the list and confirms it,
with the magnitude measured.

**Harness calibration, done before any conclusion.** A verbatim mpmath
re-implementation at 60 dps reproduces the committed witness at `z_C` to
**1.8e-31** relative, and independently reproduces all three of bean
`qou-cds1`'s recorded numbers (`c_3` = −2.0693 / −974.43 / −86.08; implied
`c_2` = −1.0176 / −9.2989 / −1.7331). Only then was the producer run.

### Why this matters beyond one file

Bean `qou-cds1` lists the "live C sites in the decay channel" as
`qbeta_utils.py::markov_parameter` + `substrate_ladder_quantities`, and its own
2026-08-25 adjudication already retracted that count as incomplete after a
sibling found a third inline site. This is a **fourth** site, and it is the
opposite polarity from the other three: not a C site awaiting migration, but a
producer **already migrated to D** whose witness was never regenerated — so the
C→D detectors, which hunt for C spellings, are looking the wrong way. The
`markov_convention` field is absent from the witness, exactly as
`substrate_ladder_quantities`' own docstring predicted ("of 278 `c_k`-bearing
witnesses, **0** declared a frame").

**Disposition is a judgement call and is NOT taken here.** Regenerating the
witness would publish −974 as the canonical `c_k`; reverting the producer to C
would re-introduce an excised convention. Both are wrong. The correct fix is
whatever `qou-cds1` concludes, and until then the file needs a **guard** so the
producer cannot be run into the cache by accident. Flagged, not fixed.

---

## 2. Where each gap actually stands

### Q_β — narrowed to one bar-even scalar; not closeable numerically

The chain is `Q_β = Q_A·cos(α − u/2)`, `α = (z−1)h/2`. The last week established:

- `α` is **not** a function of the weights (proved-lean, scope-(b)); it is
  weights + `h`, with `α = (h/4)([2]_q·Ξ + h − 2)` and `Ξ` `n`-independent.
- Bar-parity forces the odd half **uniquely** (`co = −h/2`) and constrains the
  even half **not at all** (`generalShift_bar_defect`).
- The derived D bar-odd projection gives implied `c₂ = −1.7331` — 11× better
  than the banned z-swap, still not the `−1` band.
- The residual is a single bar-even scalar `ce = z* − z_D^even = −0.0090534`.

**Why it cannot be closed by measurement:** `σ(Q_β)/Q_β = 7.8e-7` resolves `ce`
to only **1.45 % (68.8σ)**. Any identification quoted to better than 1.5 % is
arithmetic, not measurement. Closure must be a *derivation* of `ce`.

Two independent findings say the shape itself is wrong, not just the value:
`α_required` and `α_C` **cross transversally** with opposite slopes (ratio −91),
and moving to the smooth `F` coordinate — the fix the bean itself nominated —
leaves all six candidates with the **wrong sign** on `dF/dq`. The disagreement
is in the candidates, not the parameterisation.

The one genuinely promising structural handle is the corpus's own
`ε(Δ) − tr_M(Δ) = h(z−1) = 2α`: the ladder is **transporting the evaluation
from the counit to the Markov trace**, and `α` measures that gap's generator.
The unjustified step is then precisely the **cosine** — exponentiating a
difference — which is the axiomatised `QOU.Interactions.QBetaCosResummation`,
so dropping it costs nothing proved.

### c₃^odd — the target object is not well-posed yet

`S := c₃ + Vol(4₁)` is a **defined residual**, and AGENTS.md's own
"Defined residual ≠ derived decomposition" rule applies verbatim: (H1)
`c₃^even = −Vol(4₁)` is not derived, the bar-split is not empirically accessible
(no anchor supplies `q ≈ 0.901`), and the offset is not forced (a sign flip
occurs for every `V` in a window of width 0.049).

Structure is nonetheless real and largely settled: `S = h·D(ũ)`, `D` convergent
with radius `ρ = ũ(q*_ρ)`, closed form `D(w) = φ(w)log(1−w/ρ) + ψ(w)` with
`φ(ρ) = 1/(2h*_ρ)` pinned and no free parameters, and non-holonomicity certified
across every tested class including the log-closure. **All of it is
convention-C-frame at value level** and inherits `qou-cds1`.

So "close c₃^odd" is premature as a target: it asks for the odd part of a
quantity whose *split* is an assumption and whose *frame* is excised.

### f-map — fenced from four directions in the last week

`c₃ = J_Hopf(1) = −2` is now shown **not forceable** from any tried route:
bar-odd (A/B) by a proved parity invariant, scope-(b); bar-even by q=1
genericity, scope-(a); and the amplitude leg (route C) by a structural
one-scale/two-target obstruction `4λ₂³ + λ₃² = 6.088 ≠ 0`, a sum of two
positives. It is a genuine near-match, fenced with a clean reason from every
direction. A derivation would have to come from outside all of them.

**Note the ledger is stale:** `docs/coordination/z-ck-fmap-keystone.md`'s session
log stops at 2026-07-11 and its §2 "proved inputs" still carry
`z(q) = √q/(1+q)` — convention C — as the keystone's upstream datum. KC13 is
correctly re-scoped in the registry; the ledger is not.

---

## 3. The one new structural item — the `Ξ_k` moment family

Probe: [`qbeta_xi_moment_family_probe.py`](../../computations/qbeta/qbeta_xi_moment_family_probe.py)
(4/4, exact over ℚ(q), exit 0).

The proved loop-mean identity `2z − h = [2]_q·Ξ` uses the ordinary `S_n`
character at a **transposition**. Nothing in the argument is special to a
transposition. For any class `μ`, Frobenius gives `Ξ_μ = p_μ(1,Q)/(1+Q)^n`, and
for the k-cycle classes this collapses to an `n`-independent family:

```
Ξ_k  =  (1 + Q^k) / (1 + Q)^k ,        Q = q² .
```

Verified from actual Murnaghan–Nakayama characters against the actual D weights
for `n = 2..7`, `k = 1..n`; `k = 2` reproduces the corpus's proved identity
(that assertion is the harness calibration). Every member is **exactly bar-even
(twist 1)**, and the numerators `1 + q^{2k}` are **cyclotomic**
(`k = 1,2,3,4 → 1, Φ₈, Φ₁₂, Φ₁₆`).

**Why it is worth recording.** The Q_β residual `ce` is bar-even, and a
four-path corpus grep finds no other **derived, parameter-free, `n`-independent**
family of bar-even weight functionals. Registry **KC20**'s "the bar-odd carrier
is not a root-of-unity object" does **not** bind it — KC20 is a statement about
the bar-**odd** carrier, and the bar-even channel has never been examined
cyclotomically.

> **🛑 Anti-fit fence, stated before anyone uses this.** `ce` is resolved to
> 1.45 %. A family with a free index `k` will supply a member inside a 1.45 %
> window **by arithmetic alone**. The probe therefore deliberately does not
> compare any `Ξ_k` to `ce`, and no such comparison may be quoted as evidence.
> The value is structural — a derived source the even channel may draw on — not
> a match. Selecting `k` against the data is a fit and is banned by `qou-cds1`'s
> own discipline.

This is a one-line corollary of an already-proved identity, not new mathematics.
It is recorded because it is *derived* and the even channel currently has
nothing else.

---

## 4. Verdict

| gap | closeable now? | binding reason |
|---|---|---|
| Q_β | **no** | one bar-even scalar `ce`, resolved to only 1.45 %; closure must derive it, and the cosine that forces the shape is axiomatised |
| c₃^odd | **no — target not well-posed** | `S` is a defined residual on an underived (H1); bar-split not empirically accessible; value-level facts are C-frame |
| f-map | **no** | `c₃ = −2` fenced in both parities and on the amplitude leg during the last week |

Nothing here is wired, no `c_k` value is proposed, and no registry tier moves.
