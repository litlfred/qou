# Convention D: the two-row cap does not supply the correction, and `c_k` was hiding how close the forced projection gets

**Date:** 2026-08-18
**Bean:** `qou-cds1` (S1 — re-derive the Q_β `c_k` ladder under convention D)
**Branch:** `claude/convention-d-ck-rederivation-2026-08-18` (PR #5283)
**Probes:**
[`qbeta_d_frame_two_row_cap_prune_probe.py`](../../computations/qbeta/qbeta_d_frame_two_row_cap_prune_probe.py) ·
[`qbeta_ck_coordinate_magnifier_probe.py`](../../computations/qbeta/qbeta_ck_coordinate_magnifier_probe.py)

**The re-derivation is not done.** This closes the one input `qou-cds1` names as
outstanding, and corrects how the frame's progress is being *measured*.

---

## 0. Where the convention dependence actually lives

Worth stating first, because it bounds the whole problem:

```
Q_A  = m_e·|q²−2q−1|·(q+1)/(2q³)     ← closed form: NO z, NO trace
Q_N1 = Q_A · cos(α − b·ℏ_q²/2)        ← α = (z−1)h/2
Q_N2 = Q_N1 · (1 + c₂·u²)
```

`Q_A` carries no convention at all. **The entire C-vs-D dependence of the Q_β
chain enters through one factor**, `cos(α − u/2)`. So a D-frame re-derivation is
exactly the problem of supplying that factor — equivalently, of supplying

```
F(q) := Q_β(q)/Q_A(q),        target:  1 − F(q₀) = 1.6748e-3
```

which is the coordinate `qou-cds1` recommends, because the phase has a
square-root branch point 0.062 % above `q₀` that the cosine parameterisation
manufactures.

## 1. The two-row cap: folded in, and it does not supply the correction

`qou-cds1`'s *"Remaining piece"* names one landed-but-unused input:

> "The two-row cap. `WenzlWeightVanishing.lean` landed 2026-08-16 (sorry-free,
> all `n`; `z_D` is Wenzl level `r=2` exactly) … Under D the ≥3-row blocks are
> annihilated, so `χ₍₁,₁,₁₎` drops from the H₃ decomposition. **NOT folded in
> yet.**"

The candidate it suggests: if the correction were *"the part of the trace that D
discards"*, it would equal the C-frame weight of the block D annihilates.

Measured at `n = 3`, both anchors:

| quantity | value |
|---|---|
| target `1 − F_required` | `1.6748e-3` |
| `dim·y₍₁,₁,₁₎` in convention C | **`0.0227449`** |
| **ratio** | **13.6×** |
| `Σ dim·y` in C (three blocks) | `1` |
| `Σ dim·y` in D (two blocks) | `1` |

**Two independent reasons it cannot be the correction.** It is an order of
magnitude too large; and each frame is *already a complete normalised trace on
its own support* — `Σ dim·y = 1` holds in C over `{(3),(2,1),(1,1,1)}` and in D
over `{(3),(2,1)}` alone — so the cap leaves no residue to donate. The D
two-row weights close by themselves:

```
y₍₃₎ = (q⁴+1)/(q²+1)²,   y₍₂,₁₎ = q²/(q²+1)²,   1·y₍₃₎ + 2·y₍₂,₁₎ = 1  (exactly)
```

The class *"F = the two-row restriction fraction of the n=3 trace"* is pruned
**without running a search over it**, which is what the bean's Discipline
section asks for.

**Scope (a).** Per AGENTS.md §"Before declaring refuted": this is a
scope-limited negative — *this construction, alone, at the measured magnitude*.
It proves **no invariant** excluding the two-row cap as one ingredient of a
multi-term closure, and it derives nothing.

## 2. `c_k` is a bad coordinate too, and by an exact factor

`qou-cds1` established that the **phase** is a bad coordinate. The same is true
of the **`c_k`** coordinate, and it can be stated exactly rather than
impressionistically:

> **`c₂ + 1 = (F_required − F_N2) / (F_N1 · u²)`**
>
> with `F_N1 = cos(α − u/2)`, `F_N2 = F_N1(1 − u²)`, `F_required = Q_cod/Q_A`.
> Verified to `~1e-47` at 50 dps on both anchors.

The magnifier `1/u² = 13785` is **fixed** and carries no information about the
model — precisely the role the bean already identified for the `1/u³` magnifier
on `c₃`. A **1 %** error in `F` becomes a **137.6** absolute shift in `c₂`.

### What that does to this bean's own table

`qou-cds1` records the forced bar-odd projection — `a_odd = a − h²/4`, derived
with **no free parameter**, because the full-bar defect is `z`-independent — as
`implied c₂ = −1.733`, beside C's `−1.018`. In `c₂` units that reads as a 73 %
catastrophe. In `F`:

| object | `1 − F_N2` | rel. dev. from target |
|---|---|---|
| C, `α = (z_C−1)h/2` | `1.6735e-3` | **−0.076 %** |
| D, `z`-swap | `1.0733e-3` | **−35.9 %** |
| **D, bar-odd projection (forced)** | `1.6217e-3` | **−3.17 %** |

**The forced projection buys a factor ≈ 11 over the naive `z`-swap**, and the
`c₂` coordinate concealed it. Judging D-frame progress in `c_k` units overstates
the failure by ~10⁴.

### This is not a closure, and must not be read as one

−3.17 % is five orders from what L2 needs (`Q_β` target ≈ 7.8 ppb). The bean's
verdict on the bar-odd projection stands **unchanged** — *"NECESSARY and
derived, but NOT sufficient"* — as does its standing instruction: **do not search
for further corrections until one lands near −1; that is a fit.** Nothing here
derives `F`, proposes a `c_k` value, or wires anything.

The finding is about *measurement*, not about progress: the frame is 11× better
than the recorded number suggested, and still nowhere near closing.

## 3. A sharpening of a claim I made yesterday

[`2026-08-18-mass-binding-accuracy-what-is-closeable.md`](2026-08-18-mass-binding-accuracy-what-is-closeable.md)
says the 164× Q_β floor is "C-conditional". True, but understated. Wiring the
chain here reproduces the committed dashboard exactly — **163.98×** against the
witness's 164.0×, which validates the chain — and the sharper statement is:

> **Under D there is currently no Q_β prediction at all.** Not a worse one —
> none, because no D-frame ladder has been derived.

The only D-frame number available comes from the refuted `z`-swap route
(77,263×), and per this bean's standing warning about `c₃ ≈ −974` that is a
**sensitivity measurement, not a value**. Do not wire it or quote it as D's
accuracy.

## 3b. The bar-parity story does not hold up, in either convention

Two follow-on measurements, both cheap and both negative.

### The forced projection does not make the *phase* bar-odd

`qou-cds1` proved (sorry-free) that the eigenphase `a = (z−1)h/2` is bar-odd
exactly when `z` is bar-even, that `z_D` breaks this with a `z`-independent
defect, and concluded the projection `a_odd = a − h²/4` is *"forced with no free
parameter"*. But the ladder's phase is not `a` — it is `a − u/2`, and `u`'s
parity was never checked. Symbolically, under `q ↦ 1/q`:

| factor | parity |
|---|---|
| `h` | **bar-odd** (`→ −h`) |
| `h²`, `b` | bar-even |
| `ℏ_q` | neither (`→ −q·ℏ_q`) |
| `u = b·ℏ_q²` | **neither** (`→ q²·u`) |

So for **any** bar-odd `a`, `bar(a − u/2) + (a − u/2) = −u(1+q²)/2 ≠ 0`. Measured:

- the defect is **identical in C and D** (`−0.0095054571` for `a_C` and for the
  forced `a_odd` alike) — carried entirely by `u`, hence
  **convention-independent**. A ladder problem, not a D problem.
- replacing `u/2` by its bar-odd part moves `1 − F` by **15.1 %** of the
  required correction. Not a rounding term.

The bean's two Lean theorems are **correct as stated** — they concern `a`. What
does not follow is the motivation: making `a` bar-odd does not make the phase
bar-odd.

### …and the parity requirement is not available from the chain anyway

That left an open question: *is* `F` required to be bar-even? The corpus states
the requirement and names the involution —

> *"It is the bar-odd (`sinh`) partner of the bar-even (`cosh`) meson scale
> `m_π` **under the bar-involution `q ↦ q⁻¹`**"*
> — [`three-calibration-discipline.md:18`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md),
> and similarly `epistemic-status-of-calibrations.md:3`,
> `three-calibration-discipline-proof.md:36`, and AGENTS.md.

That is testable against the closed form the framework computes. Measured at
both anchors:

```
Q_A/m_e at q    = 1.5335566273012
Q_A/m_e at 1/q  = 2.5868438911015
bar(Q_A)/Q_A    = 1.686826456258      ← bar-odd would be −1; bar-even would be +1
```

**Neither**, and not marginally. No other natural involution rescues it either
(`q ↦ −q` and `q ↦ −1/q` both give non-constant ratios).

So a bar-parity constraint on the D-frame correction **cannot be derived from
"Q_β is bar-odd"**, because `Q_β` as computed is neither. The open question
resolves in the direction of *not available*.

**Scope, stated carefully because this contradicts four corpus sites.** The
measurement is of the closed form `Q_A = m_e|q²−2q−1|(q+1)/(2q³)` — what
AGENTS.md gives for `Q_β` and what `qbeta_utils` computes. If the parity claim
is meant for a *different* representation (an unevaluated `sinh` form, or the
width `𝔇_β` before inversion), it may hold there, and the defect is that the
corpus attaches it to this form. Either way the statement as written does not
hold of the computed object. Nothing here tests `m_π`'s claimed bar-evenness.

## 3c. SETTLED: the "sinh partner" is `Im 𝔙` — and my §3b conclusion was wrong

§3b concluded that a bar-parity constraint on `F` is *"not available from the
chain as written"*. **That was wrong, and the correction matters** — the
constraint is available; I had not found the object carrying it. It lives in
q-hyperbolic geometry.

### Where the description comes from

`three-calibration-discipline.md:18` cites
[`substrate-cohomology-calibration-story.md`](../../content/quantum-observable-universe/mass-theory/substrate-cohomology-calibration-story.md),
whose line 11 gives the whole story:

> *"A crossing has two eigenvalues, `q` and `−q⁻¹`. Setting `λ = log q`, these
> split as `cosh λ ± sinh λ`. … The binding observables sit on the `cosh`,
> bar-even side. The β-decay observable `𝔔_β` and its precision coefficients sit
> on the `sinh`, bar-odd side. … That single element is the **complex volume**
> `𝔙`. Its bar-even part is `Re 𝔙 = 𝔈_bind`. Its bar-odd part is `Im 𝔙 = 𝔔_β`,
> forming the QOU analogue of the Neumann–Zagier `Vol + i CS`."*

and `conj:binding-qbeta-complex-volume` states it:

```
𝔙(K) = E₀·tr_M((Π_free − 1)∘ℳ) ∈ ℂ,   𝔈_bind = Re 𝔙,   𝔔_β = Im 𝔙
```

So the sinh/cosh split is the `q = e^λ` split of the **crossing eigenvalues**,
and `bar` (`q ↦ 1/q`) *is* `λ ↦ −λ`; sinh/cosh parity is exactly
bar-odd/bar-even. **The "sinh partner" is `Im 𝔙`, the Chern–Simons-analogue
part of the complex volume** — not the rational closed form.

### It is conjectural, and the four sites omit that

`conj:binding-qbeta-complex-volume` is a **conjecture**, class-axiomatised in
Lean (`ComplexVolumeMatch` / `SingleFrakVAssembly` / `StageCSigma3Lift`). Per
AGENTS.md §"Conditional-proved ≠ premise-established", the bar-odd property of
`Q_β` is therefore **conditional on it**. The four sites assert it as
established fact.

### The constraint, and the chain fails it

Writing the prediction `Q_β^pred(q) = Q_A(q)·F(q)`, the requirement is **not**
that `F` be bar-even. It is:

> **`Q_A·F` must be bar-odd**, i.e. `Q_β(1/q) = −Q_β(q)`.

Measured, both anchors:

| object | bar-ratio | required |
|---|---|---|
| `Q_A` alone | `+1.686826` | `−1` |
| `Q_β^C = Q_A ·` ladder | `+1.687595` | `−1` |
| **ladder's effect on the ratio** | **0.046 %** | — |

Two readings, both worth keeping. The chain **violates** the conjecture's parity
requirement outright (`+1.69`, not `−1`); and the **entire precision ladder
moves the ratio by 0.05 %**, so the violation is inherited wholesale from `Q_A`
and the ladder does essentially nothing to restore bar-oddness.

So either `Q_A` is not `Im 𝔙` — the closed form is a different object from the
one the parity claim is about — or the conjecture's parity claim fails for the
computed object. **The corpus does not currently distinguish these**, and that
is the thing to settle before another candidate `F` is tried.

This is a far sharper filter than matching `1 − F(q₀) = 1.6748e-3` at a single
point, and it is available to any D-frame attempt.

## 4. Routes now pruned, and what remains

| route | status | source |
|---|---|---|
| `z_D` substituted into `α = (z−1)h/2` | refuted — ~1000 window-widths off | bean |
| any **analytic-in-q** phase ansatz | refuted — `α_req` has a √ branch point | bean |
| exact bridge `(1−h/2)/(1−zh/2)` | 25–32× too large in both frames | prior + re-measured here |
| **two-row cap restriction fraction** | **13.6× too large; no residue** | **§1, here** |
| bar-odd projection `a − h²/4` | forced, necessary, **not sufficient** (−3.17 %) | bean + §2 |
| bar-parity as a *constraint* on F | **not available** — `Q_β` as computed has neither parity | §3b |

**What a D-frame ladder still needs** is unchanged from the bean's own
statement: a correction of a *different functional form*, derived from the
representation rather than axiomatised. Note that the eigenphase identification
forcing the cosine is **axiomatised** (`QOU.Interactions.QBetaCosResummation`),
so dropping the cosine costs nothing proved — and §2 adds that the `c_k`
readout should be dropped alongside it, since both coordinates distort the
residual by fixed magnifiers.

## What this audit did NOT do

- It **derived nothing**. Both results are negatives or measurement
  corrections.
- It ran **no search** over correction families, per the bean's Discipline
  section.
- It did **not** touch Lean, regenerate any witness, or propose any `c_k`.
- The `n = 3` restriction in §1 is the decay channel's own; the two-row cap was
  **not** swept over other `n`, deliberately — scanning `n` for one that matches
  `1.6748e-3` would be exactly the fit this bean forbids.
