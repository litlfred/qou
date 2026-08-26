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

## 3. The `Ξ_k` moment family — proposed, then RETRACTED the same day

Probes: [`qbeta_xi_moment_family_probe.py`](../../computations/qbeta/qbeta_xi_moment_family_probe.py)
(4/4) · [`qbeta_xi_kcycle_route_prune_probe.py`](../../computations/qbeta/qbeta_xi_kcycle_route_prune_probe.py)
(8/8) · [`qbeta_xi_family_collapses_to_h_probe.py`](../../computations/qbeta/qbeta_xi_family_collapses_to_h_probe.py)
(6/6). All exact over ℚ(q), all exit 0.

**What was proposed.** The proved loop-mean identity `2z − h = [2]_q·Ξ` uses the
ordinary `S_n` character at a *transposition*; nothing in the argument is. By
Frobenius the k-cycle classes give an `n`-independent, parameter-free, exactly
bar-even family `Ξ_k = (1+Q^k)/(1+Q)^k` with **cyclotomic** numerators
(`k = 1,2,3,4 → 1, Φ₈, Φ₁₂, Φ₁₆`), verified from actual Murnaghan–Nakayama
characters against the actual D weights for `n = 2..7`. Since the residual `ce`
is bar-**even** and KC20's no-root-of-unity exclusion concerns the bar-**odd**
carrier, this looked like the even channel's only derived source.

**🛑 It is withdrawn.** Measured exactly, `k = 1..8`:

```
Ξ_k  =  (q^k + q^-k) / [2]_q^k  =  2·T_k([2]_q/2) / [2]_q^k      (Chebyshev)
```

— a rational function of `[2]_q` **alone**; and `[2]_q² = h² + 4` exactly, so the
whole family is a function of `h²`. Concretely `[2]²·Ξ₂ = h²+2`,
`[2]²·Ξ₃ = h²+1`. **The ladder already carries `h`.** The family supplies nothing
new and cannot be the source of `ce`.

Two things misled, recorded because the mode recurs:

1. **The cyclotomic numerators are a property of the writing, not the content** —
   just the factorisation of `1 + q^{2k}`. A suggestive *form* was read as a
   suggestive *object*.
2. **The `k = 2` member is genuine content, but its content is about `z`, not
   `Ξ₂`.** It is the Markov condition `2z − h = [2]_q·Ξ₂`; `Ξ₂` itself is merely
   `(h²+2)/[2]²`. Re-derived: `2z_D − h = (h²+2)/[2]_q` exactly.

**This also supersedes the explanation of the intermediate prune.** The k-cycle
probe found `Ξ₃`'s coefficient came out free and read that as "the k-cycle route
does not reach `Ξ₃`". The real reason is that `Ξ₃ = (h²+1)/[2]²` is a **redundant
coordinate**, so any basis holding it beside `{1, h², [2]²}` is linearly
dependent and a free coefficient is forced. The prune's *conclusion* stands; its
stated mechanism was wrong.

**Net, and it is a useful negative:** `ce` is not reachable from the Markov
weights' moment structure at all, because that structure is a function of `h`.
Deriving `ce` requires something genuinely new — it is **not hiding in the
weights**. Scope-(a): this excludes the weight-moment family, not every
conceivable derivation.


## 4. The element `Q_A` rests on cannot exist as described — PROVED, scope-(b)

Following `qou-avt5` (which established that `ε(Δ)` has no exhibited element),
this settles the stronger question.

**A typed crossing is `σ_g + d`.** `word_to_mpfr` recognises four templates by
`d`: `0`, `−h`, `−h/2`, colour-weighted. The Hecke relation gives
`σ⁻¹ = σ − h`, so those read off as σ / σ⁻¹ / the average — which is what the
code calls them. The counit sends `σ ↦ q`, so

```
ε(σ_g + d) = q + d ∈ { q, 1/q, [2]_q/2 }   ⟹   ε(any typed word) = q^m·([2]_q/2)^c
```

**Side B confirmed a second time, now symbolically.** `ε(β_p) = q³([2]/2)²`,
`ε(β_n) = q([2]/2)²`, and

```
ε(β_n − β_p) = −(q−1)(q+1)(q²+1)²/(4q) = chi_block_3      [exact identity]
```

**The exclusion.** `epsNPq = h(h−2)/2 = (q²−1)(q²−2q−1)/(2q²)` carries the
irreducible factor `(q²−2q−1)`, whose root is the **silver ratio** `q = 1+√2`,
so it vanishes there. A typed-word difference vanishing at the silver ratio
forces `(1+√2)^{m₁−m₂} = (√2)^{c₂−c₁}`, because `[2]_q/2 = √2` **exactly** at
that point. Absolute norms in `ℤ[√2]` — `|N(1+√2)| = 1` (the fundamental unit),
`|N(√2)| = 2` — force `c₁ = c₂`, then `m₁ = m₂` since `1+√2` is not a root of
unity. The difference is then identically zero, which `epsNPq` is not. ∎

**Control, so the argument doesn't prove too much:** `chi_block_3` *is* such a
difference, so it must not vanish at the silver ratio — and
`chi_block_3(1+√2) = −12 − 8√2 ≠ 0`, with exponents `(1,2)` and `(3,2)`. A
bounded sweep (84 100 pairs, three generic `q`) independently returns zero
solutions for `epsNPq` and exactly that one for `chi_block_3`.

**The fork, not adjudicated here.** The corpus's description of `Δ` and its
asserted counit are mutually inconsistent: either the prose is wrong (`Δ` is not
a typed-crossing word difference, and the real element is still unexhibited), or
`epsNPq` is wrong — and with it `Q_A` and the ladder phase `ε − tr_M`. Deciding
needs the owner of the counit block.

**Scope discipline.** This is scope-(b): a structural exclusion on a *proved
invariant* (the norm form on `ℤ[√2]`), not a failed search. It excludes the
class "difference of two typed-crossing words" and nothing wider — a
colour-weighted crossing contributes `q − h(½ − δ/4)`, outside the
`q^m([2]/2)^c` normal form. A=1 nucleon words carry none, which is why the class
is the right one here; do not quote it for words that do.

## 5. Verdict

| gap | closeable now? | binding reason |
|---|---|---|
| Q_β | **no** | one bar-even scalar `ce`, resolved to only 1.45 %; closure must derive it, and the cosine that forces the shape is axiomatised |
| c₃^odd | **no — target not well-posed** | `S` is a defined residual on an underived (H1); bar-split not empirically accessible; value-level facts are C-frame |
| f-map | **no** | `c₃ = −2` fenced in both parities and on the amplitude leg during the last week |

Nothing here is wired, no `c_k` value is proposed, and no registry tier moves.
