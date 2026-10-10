# The Lean and the compute are two different α_em derivations

> **⚠ CONVENTION-C CONDITIONAL — scope note added 2026-09-06 (bean `qou-h6o3`).**
> This document's conclusions depend on the `c_k` precision ladder / `Q_β`, which
> AGENTS.md records as **convention-C-frame throughout and NOT re-derived** under
> the owner ruling of 2026-08-15 making convention D (`z = q³/(q²+1)`) canonical.
> Treat every `c_k`-dependent statement below as **C-conditional** until the
> ladder is re-derived (bean `qou-cds1`). The numbers here are correct *for C*
> and are kept as recorded — they need **scoping, not correction**. This note was
> applied mechanically to the 45 documents in this arc that reference the ladder;
> it asserts dependence on the ladder, not that any particular conclusion changes
> under D.


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


---

# 9. The `8` IS structural — `Vol(𝓑₃)/G`, exactly. Wrong gloss, right number.

Found by finally running the corpus-grep properly on the bean's open half
(*"nothing in the corpus argues for one prefactor over the other"* — a claim I
made without having run all six paths).

## 9a. The identity

The Borromean rings `L6a4` — **this framework's nucleon knot** — have

```
Vol(𝓑₃) = 2 · V_oct = 8G,        V_oct = 4G,        G = Catalan
```

Machine-checked to 30 digits in the probe: `V_oct/G = 4.0`, `Vol(𝓑₃)/G = 8.0`,
residual exactly 0.

**This is already live and load-bearing in the corpus** — not a new claim:

- [`fundamental-knots-operator-basis.md`](../../content/quantum-observable-universe/braids-and-knots/fundamental-knots-operator-basis.md),
  nucleon row: `Vol ≈ 7.328 = 8G`
- [`binding-knots-visual-inventory.md`](../../content/quantum-observable-universe/knots-particles-confinement/binding-knots-visual-inventory.md):
  the binding scale `α = m_e · 8G ≈ 3.7445 MeV`

And it is the reading `fsh-guts/deprecated/computations/alpha_em_q9_q10_derivation.py`
gives outright: **`κ = 8q = q · Vol(𝓑₃)/G`**.

## 9b. So the live `.lean` carried the weaker of two available readings

`em-coupling-chern-simons.lean` glossed the 8 as *"dim(su(3)) = gluon octet"*
and — correctly — called that **post-hoc, with no structural derivation**. That
assessment of *that* gloss stands. But the corpus had an exact one the whole
time and the file did not cite it. Docstring corrected in this tranche; the
honest caveats are kept.

## 9c. This revises §7, and my PR #5911

§7 reports that bare `κ = 8` misses at −220 ppb and concludes *"the `q` factor
does the work, not the 8."* Under the corpus reading that framing is wrong:
`κ = q · Vol(𝓑₃)/G` is **one object**, and the `q` is part of the claimed
structure rather than an unexplained fudge. The measurement is unchanged;
`κ = 8` missing is *consistent with* that reading, not damaging to it.

## 9d. What is still not derived — and it is not small

- **The combination.** Why `q · Vol/G` and not `Vol/G` or `q² · Vol/G`? The
  identity fixes the 8, not the power of `q` multiplying it.
- **The cross-sector step.** Why a **nucleon**-knot volume sets a coefficient in
  an **electromagnetic** coupling is unaddressed. This is the load-bearing gap.
- **The genericity window is unmoved.** κ ∈ [8.474, 9.265] still admits the
  integer 9 (33 ppb), so `8q` remains **in range, not forced**.

## 9e. And the prefactor question now has a chronology

The same deprecated file shows `45·[3]_q` **replaced** `q·[9]_q·[10]_q`:

> *"REFINED FORMULA (replaces the troublesome 1.6 mystery constant)"* … and, of
> the older form, *"OPEN: clean q-algebraic form for the '1.6' factor. PSLQ …
> finds no small-[relation]"*.

So the corpus does record an ordering, and **production compute uses the
superseded prefactor** — now with a Gram-determinant κ rather than the
unidentifiable 1.6, which is a later and different development. Whether that
revival supersedes the supersession is exactly the open canonical question, and
this does not settle it. But *"nothing in the corpus argues for one over the
other"* was wrong, and I withdraw it.


---

# 10. The cross-sector gap, stated in the framework's own terms — a dilemma

§9d named *"why should a nucleon-knot volume set an electromagnetic
coefficient"* as the load-bearing open item. Pursuing it does not close it; it
makes it sharper, and turns it into a dilemma with two costed horns.

## 10a. First: the identity is NOT generic

If many knots gave an integer `Vol(K)/G`, then `8 = Vol(𝓑₃)/G` would be a
re-description available for any number. Measured over the corpus's own volume
table plus five more hyperbolic knots:

| knot | Vol | Vol/G | |
|---|---:|---:|---|
| 4₁ figure-eight | 2.02988 | 2.21611 | |
| 5₂ three-twist | 2.82812 | 3.08759 | |
| 6₁ | 3.16396 | 3.45424 | |
| 6₂ | 4.40083 | 4.80458 | |
| 6₃ | 5.69302 | 6.21532 | |
| 7₄ | 5.13794 | 5.60932 | |
| 8₁₈ | 12.35091 | 13.48403 | |
| Whitehead = V_oct | 3.66386 | **4.0** | **integer** |
| L6a4 Borromean | 7.32772 | **8.0** | **integer** |

**2 of 9**, and both are the octahedral family. So the `8` is a genuinely
constrained topological number, not a re-description. **But the reason it is
constrained is octahedral decomposability** — standard knot theory, with no
bearing on electromagnetism.

## 10b. The corpus's own sector rule runs the other way

[`fundamental-knots-operator-basis.md`](../../content/quantum-observable-universe/braids-and-knots/fundamental-knots-operator-basis.md)
states the assignment explicitly, in the same table that carries the `8G`:

> Torus knots carry zero hyperbolic volume, representing the **massless,
> force-carrying sector**. Hyperbolic knots carry positive volume, which
> **translates to mass** via `Vol(K)/ℏ_q²`.

and places the **photon** — the electromagnetic force carrier — as *"not a
knot"*, a four-term Hecke element with `J = 1 (bare)`, in that **zero-volume**
sector. The nucleon sits in the other one, at `Vol = 8G`.

So using the **nucleon's hyperbolic volume** to set a coefficient inside the
**electromagnetic** coupling crosses the framework's own volume↔mass /
zero-volume↔force-carrier boundary. That is a stronger objection than
"unexplained": it runs against a rule the corpus states in the same breath as
the `8G` it is invoking.

## 10c. The dilemma — both horns cost something

- **If the volume is doing the work**, it crosses that stated boundary. The
  photon is explicitly volume-zero; volume is explicitly the mass channel.
- **If only the integer 8 is doing the work**, the knot-theoretic reading adds
  nothing over `κ = 8q`, and the post-hoc charge returns — merely aimed at a
  different gloss than su(3).

Nothing found in six grep paths resolves this. **It is not a numerical
question**, so no probe will settle it; it needs either a structural argument
for why a mass-channel invariant may enter a force-carrier coupling, or an
explicit statement that only the integer is meant.

## 10d. What §9 still gets right

None of this retracts §9. `8 = Vol(𝓑₃)/G` is exact, non-generic, live in the
corpus, and a better-grounded reading than the su(3) gloss the `.lean` carried.
The docstring correction stands. What §10 adds is that the *sector* question is
not a loose end to be tidied later — it is the whole remaining content of the
claim, and the framework's own table is evidence against the easy answer.
