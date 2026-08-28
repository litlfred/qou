# The Lean and the compute are two different α_em derivations

Re-examination of the two knobs the 2026-08-22 red-team left open on
`m_K/m_π` — the framework's only scoreable L2 result. Reproduce with
[`computations/alpha_em_lean_vs_compute_divergence_probe.py`](../../computations/alpha_em_lean_vs_compute_divergence_probe.py).
Bean `qou-aemx`.

The headline is not a new number. It is that **the formalisation the paper
cites and the computation the scorecard uses are different constructions**,
and the more empirical of the two fits better.

## 1. Two constructions, no shared ingredient

| | prefactor | κ | α_em⁻¹ | vs CODATA |
|---|---|---|---:|---:|
| [`em-coupling-chern-simons.lean`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md) | `45·[3]_q` = 136.966779 | `8q` = 8.879829 | 137.035999532 | **+2.59 ppb** |
| [`meson_em_sinh_closed_form.py`](../../computations/meson_em_sinh_closed_form.py) | `q·[9]_q·[10]_q` = 136.823209 | det ratio = 1.721614 | 137.035935094 | **−467.64 ppb** |

Prefactors differ by **1049 ppm**, the κ's by a factor of **5.158**, the
results by **470 ppb**. All at the 50-digit proton pin; the gaps are eleven
orders of magnitude above float64 resolution, so this is not an arithmetic
artifact.

## 2. Three consequences

**The cited formalisation is not the computation.**
`per_observable_100x_status.py` imports `alpha_em_inv_derived` — the −467.6 ppb
construction. So the standard characterisation, *"`m_K/m_π` is conditional on
the Chern–Simons conjecture class in `em-coupling-chern-simons.lean`"*, names a
premise the number does not rest on. Whatever `m_K/m_π` is conditional on, it
is not that file.

**The empirical form fits 181× better, and says so about itself.** The `.lean`
docstring on `gluonOctetKappa`:

> The "8 = dim(su(3)) = gluon octet" interpretation is post-hoc; no structural
> derivation links su(3) gluon dimension to α_EM.

A construction that announces its own coefficient as post-hoc landing 2.6 ppb
from CODATA, while the derived Gram-determinant construction lands 468 ppb out,
is the anti-fit signature pointing the wrong way for the framework.

**The `.lean` docstring contradicts its own `def`.** It describes κ as *"a
Gram-determinant ratio from the Chern–Simons ..."* while the definition is
`8 * q`. The producer computes the actual determinant ratio and gets 1.7216.
The prose describes the producer's object; the code defines a different one.

## 3. Two corrections to the 2026-08-22 red-team

Both of that audit's knob-2 claims have moved. **Neither correction improves
the verdict**, and the second is easy to misreport as if it did.

**"α_em is imported experimental" — stale.** The literal
`mp.mpf("137.035944")` is gone from the producer; α_em is now built from
framework objects (CS invariants of `T_{2,9}` and `T_{3,5}`, self-linking 8,
linking 17) and resummed exactly. The dashboard consumes that.

**"conditional on an open Lean `sorry`" — stale in mechanism only.**
`em-coupling-chern-simons.lean` compiles `lean`-direct **exit 0** with **zero**
sorries. The single `sorry` token in the file is the word inside a comment
describing the file's own history (*"Was a `theorem` with `sorry`; demoted to
class after audit"*) — a `grep -c sorry` returns 1 and means nothing. What it
carries instead is two unproved conjecture classes with no instance,
`AlphaEmGluonOctetConjecture` and `ChernSimonsCorrectionConjecture`.

**That is the same epistemic status, not a better one.** AGENTS.md
§"Axiomatization is NOT a Proof" is explicit that a conditional class does not
discharge anything. **0/5 unconditionally-parameter-free stands.** Report the
change as a correction to the mechanism, never as progress.

## 4. Independent corroboration of the #5467 de-fit

Bean `qou-5ipv` (a sibling, 2026-08-02, still `todo`) measured the same EM
factor and reported *"the FULL log fits WORSE (+103 vs +47 ppb)"*. PR #5467
measured 23.45 → 51.48 ppb and reached the same verdict from the other
direction.

The two agree exactly once the observable is matched: `qou-5ipv` reports on
**m_K²/m_π²**, #5467 on **m_K/m_π**, and to first order the squared ratio's
error is twice the ratio's. 47/23.45 = 2.004; 103/51.475 = 2.001. Same
measurement, two agents, two normalisations — worth recording because the
factor of 2 reads as a discrepancy until the observable is checked, which is
the same trap as the `c₃` "3.47 % vs 3.35 %" pair in AGENTS.md.

`qou-5ipv`'s stated action — *"re-scope the corpus claim (α_em-anchored, not
parameter-free)"* — is partly discharged by #5467 (the tracker row is now
CONDITIONAL) and partly superseded here: α_em is no longer anchored on the
experimental value at all, it is anchored on an unproved conjecture class.

## 5. Knob 1 is untouched

The `(3,4)` in `[3]_q·[4]_q` remains scan-selected. The corpus block
`meson-qcg-fusion-identity` gives `[3]_q·[4]_q = [2]_q + [4]_q + [6]_q`, which
is the standard q-Clebsch–Gordan rule and is true — but it *re-expresses* the
product rather than deriving why 3 and 4. Nothing found in `docs/audits/`,
`content/`, `computations/`, the coordination ledgers, `library/` or `.beans/`
derives the pair. It is open.

Worth noting the derived α_em brings **its own** discrete selections — the
crossings `(9,10)`, the torus knots `T_{2,9}` and `T_{3,5}`, `sl = 8`,
`linking = 17` — so replacing the imported α_em with a derived one did not
remove selected integers from the closure, it added more.


---

# Follow-on, same day: they are not one object — and my own emphasis was wrong

Bean `qou-aemx` asked: *decide which construction is canonical, or establish
that they are the same object under a reparametrisation.* Both halves are now
measured. Reproduce with the two functions appended to the probe.

## 6. Not the same object — settled symbolically, so it needs no anchor

| | closed form |
|---|---|
| Lean | `45(q⁶ − 1) / (q²(q² − 1))` |
| compute | a degree-32 cyclotomic product over `q¹⁶` |

`sympy` confirms the difference is not identically zero, and evaluation away
from `q₀` makes it obvious:

| q | Lean | compute | ratio |
|---|---:|---:|---:|
| 1.0001 | 135.000 | 90.009 | 1.500 |
| 1.05 | 135.429 | 101.403 | 1.336 |
| **q₀** | **136.967** | **136.823** | **1.00105** |
| 1.5 | 166.25 | 4 783.7 | 0.0348 |
| 2 | 236.25 | 466 031.6 | 0.000507 |

**They cross at `q* = 1.11015574`, which is 0.016 % from `q₀`.** So the 1049 ppm
agreement is a fact about where `q₀` sits relative to a crossing, not about
shared structure. That is *expected* rather than surprising: both constructions
target ≈137 near the same point, so proximity there is not evidence for either.

**Answer to the bean: they are two different objects.** Which is canonical is
not resolved here — but "they might be the same thing written twice" is
excluded.

## 7. Is either κ forced? The genericity test

AGENTS.md asks of any such offset: *is it forced, or merely in range?* Window
of κ giving |err| < 100 ppb:

| | claimed κ | window | width | as % of claimed | claimed inside? |
|---|---:|---|---:|---:|:--:|
| Lean `8q` | 8.8798 | [8.4744, 9.2648] | 0.790 | **8.9 %** | **yes** |
| compute Gram | 1.7216 | [1.8739, 1.9567] | 0.083 | **4.8 %** | **no** |

Two facts that pull opposite ways, and both belong in the record:

- **`8q` is IN RANGE, not FORCED.** Its window is relatively *wider* and also
  admits the integer **9** (33 ppb). Landing inside a ±4.5 % window is weak
  evidence.
- **But the `8` alone does not work.** Bare `κ = 8` — the *"8 = dim su(3) =
  gluon octet"* reading the file itself offers, and calls post-hoc — gives
  **−220 ppb** and **misses the window**. It is the `q` factor doing the work,
  not the 8. So the stated interpretation is not what makes the number land.
- **The Gram κ misses a tighter window by 10 %.** A parameter-free construction
  that misses is behaving like a *prediction*. That is what an unfitted
  quantity looks like when it is not quite right.

## 8. Correcting my own emphasis, from §2 and PR #5886

§2 above, and the body of the PR that merged it, called the 181× gap an
**"anti-fit signature pointing the wrong way for the framework"**. That was
over-stated, and §7 is why.

A **loosely-constrained** empirical parameter fitting better than a
**tightly-constrained** derived one is close to what you would expect on
neutral assumptions. `8q` sits in a window twice as wide, relatively, as the
one the Gram κ has to hit. The measured facts in §2 stand — 470 ppb apart,
181× closer, and the docstring-vs-`def` mismatch is real — but "the empirical
one fits better, therefore something is wrong" does not follow from them.

The sharper and better-supported statement is the one in §7: the derived κ is
the one making a real, falsifiable, currently-failing claim; the empirical κ is
the one whose agreement carries the least information. Neither observation
settles which construction is canonical, and this audit does not claim to.

**Unchanged by any of this:** the scorecard still consumes the −467.6 ppb
construction, the cited formalisation is still not the computation, and
**0/5 unconditionally-parameter-free stands.**
