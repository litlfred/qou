# `Im(q)` is not the elliptic source — and what "no tower" means

**Date:** 2026-08-31 · **Beans:** `qou-pdix` (route 5) / `qou-cds1` (branch 3) ·
**Scope:** (b) for the exclusions, (a) for the tower measurement.

**Artifacts.**
[`QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean)
(4 theorems, sorry-free) ·
[`qbeta_imq_elliptic_generator_refutation_probe.py`](../../computations/qbeta/qbeta_imq_elliptic_generator_refutation_probe.py)
(8/8). Sequel to
[the sign obstruction](./2026-08-31-qbeta-holonomy-spectrum-sign-obstruction.md).

---

## Part 1 — `Im(q)` cannot supply the elliptic generator

The sign obstruction left route 5 needing an **elliptic** generator, and the
imaginarity has to come from somewhere. `conj:im-q-physical-role` is the corpus's
name for that somewhere: *"a substrate moduli parameter **not constrained by
current QOU observables**, with three candidate roles (chirality / phase
coordinate / non-Hermitian deformation)."* Two of the three bear on this.

### Route A — `Im(q)` as a phase coordinate

The Kohno–Drinfeld generator eigenvalues are `±ln q`, purely imaginary only if
`|q| = 1`. But `Re q = 1.10998 > 1`, so `|q|² = x² + y² > 1` for **every** `y`.
**A purely elliptic generator is impossible outright.**

The only remaining move is to allow a complex character and keep its real part.
It costs more than it buys:

| | |
|---|---|
| bare threshold for `Re[character] < 1` | `\|Im q\| > 0.122819` (11.07 % of `Re q`) |
| `Im q` needed to hit `Re[character] = 0.998399` | **±0.139956** (12.61 % of `Re q`) |
| resulting `Im[character]` | **0.014069** |
| …as a multiple of the deviation being explained | **8.40×** |
| …in σ of the measurement | **18074** |

`Q_β` is real, so that imaginary part must vanish — and with `s = \|q\|² > 1` the
factor `1 − 1/s` is strictly positive, so it vanishes **only** at `y = 0`
(`character_im_zero_iff`). That returns `q` to real and the character to `≥ 1`,
which the sign obstruction already excludes
(`no_complex_q_gives_real_subunit_character`).

### Route B — a non-Hermitian deformation

An elliptic generator has spectrum `±iλ`, so braiding eigenvalues
`exp(±iħλ/2)` lie on the **unit circle**. Kohno–Drinfeld fixes `ħ = 2 ln q`
precisely by matching the Hecke pair `{q, −q⁻¹} = {1.109979, −0.900918}`, and
neither has modulus 1 (`hecke_eigenvalues_not_unit_modulus`). Route B does not
fail on the data — **it fails by dissolving the scale-fixing the route depends
on.**

### What this does not settle

It does **not** refute `conj:im-q-physical-role`. The chirality role is untouched
and `Im q` may be physical for other reasons. What is settled is that `Im q` is
not the source of the elliptic generator — the "phase coordinate" role cannot do
this job, and "non-Hermitian deformation" cannot do it without discarding the
Drinfeld–Kohno matching.

## Part 2 — what "retire the tower" means, in numbers

**The tower** is the infinite sequence `c₂, c₃, c₄, …` in powers of
`u = b·ℏ_q²`, i.e. `Q_β = Q_A·cos(θ)·(1 + c₂u²)(1 + c₃u³)…`. It is what
`c₂ = −1`, `c₃ ≈ −2 = J_Hopf(1)`, the Habiro-element search and the whole rung
programme are about.

**Retiring it does not mean dropping the correction.** Measured at the proton pin:

| | value | in σ |
|---|---|---|
| correction needed | 0.998325 | — |
| `1 − θ²/2` (no cosine, no tower) | 0.998399 | — |
| residual `δ` left over | **−7.3394e-5** | **94.29** |
| what `c₂ = −1` predicts, `−u²` | −7.2543e-5 | **98.84 %** of `δ` |
| left for `c₃` **and every coefficient above** | −8.5042e-7 | **1.09** |

So `δ` is real and large; `c₂ = −1` consumes almost all of it; and what remains
to determine `c₃` and the entire rest of the series is **one marginal number**.
The absolute bar is `σ/u³ = 1.2598`, reproducing Step 15's independently
propagated **1.2619**.

### And `c₃`'s central value is an artefact, not merely imprecise

| extraction | `c₃` |
|---|---|
| through `cos` + the `c₂` rung (the corpus's) | **−2.069343** — reproduces the committed `−2.06934258` |
| through `1 − θ²/2` instead of `cos` | **−1.376381** |
| shift | **33.49 %** |

That shift is produced by a choice the data resolves at only **0.549 σ**
(Step 17). So `c₃` is not just poorly measured: its central value depends on a
parametrisation the anchor cannot see.

### "No tower", stated

```
Q_β = Q_A · (1 − θ²/2) · (1 + δ),      δ = −7.3394e-5   measured
```

— keeping `δ` as **one number the anchor determines**, instead of asserting
`δ = c₂u² + c₃u³ + …` with `c₂ = −1` exact and `c₃` read off what is left. *One
measurement determines one number; it cannot determine a series.*

## Where the fork now stands

Both arms of the fork I put to the owner have now been priced:

| arm | status |
|---|---|
| take `conj:im-q-physical-role` as the elliptic source | **refuted here** — neither candidate role can do it |
| retire the cosine, state the correction as `1 − θ²/2` | **coherent**, and costs only the tower, not the correction |

Route 5 is not closed — a connection with an elliptic generator from some *other*
source is still logically open — but the one place the corpus had already named
as a source of imaginarity is now excluded.

Anchor: experimental (proton) pin, per the 2026-08-07 owner directive.
