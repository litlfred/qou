# Faddeev–Niemi $|Q_H|^{3/4}$ vs the QOU binding gap — pre-registered verdict

**Date:** 2026-08-26 · **Bean:** `qou-thtm` · **PR:** [#5799](https://github.com/litlfred/qou/pull/5799)
**Pre-registration:** [`2026-08-26-faddeev-niemi-prereg.md`](2026-08-26-faddeev-niemi-prereg.md),
committed at **`d3819883225e50cb66a59efa3f7f1676ac2bd4ae`** and pushed **before** the
probe was written or any number computed.
**Probe:** [`computations/probes/faddeev_niemi_qh34_binding_prereg_probe.py`](../../computations/probes/faddeev_niemi_qh34_binding_prereg_probe.py)

## Verdict

**The class is DEAD for the binding gap as a term of the form $c\,|Q_H|^{3/4}$ in a
single global topological charge — scope (b), two independent invariants — and
UNFALSIFIABLE, hence not a scientific claim, in the version where $Q_H$ is left
free.** Every pre-registered refutation criterion fired, on every target, and the
one post-hoc check that could have rescued it refuted too.

Nothing about the Faddeev–Niemi *paper* is impeached. What is retired is the transfer
of its energy bound into this corpus as the missing binding term.

## The structural result, which settles it without a fit

Two arguments, both established before the numbers and both confirmed by them.

### S1 — no pure power law in $A$ can have the right shape

For any real $p$, $B = c\,A^{p}$ gives $B/A = c\,A^{p-1}$, which is **strictly
monotone** in $A$ for $p \neq 1$ and **constant** for $p = 1$. The measured
$B_{\mathrm{AME}}/A$ is **non-monotone**: it rises from 1.1123 MeV/nucleon at ²H to an
**interior maximum of 8.7904 at ⁵⁶Fe**, then falls to 7.5701 at ²³⁸U. A strictly
monotone function cannot equal a non-monotone one.

So the exponent $3/4$ was never the issue — **the entire one-parameter power-law
family is excluded, for every exponent simultaneously.** This is why the numerical
step below is a confirmation and not a search: it could not have gone the other way,
and it was pre-registered as retractable if it had.

The invariant cited: strict monotonicity of $A \mapsto A^{p-1}$ for $p \neq 1$.
S1 applies to the residual $R = B_{\mathrm{AME}} - B_{\mathrm{sym}}$ as well — $R/A$
is also non-monotone with an interior maximum at ⁵⁶Fe (5.8924).

### S2 — sign. The one the pre-registration did not see coming

The Faddeev Hamiltonian $H = \int d^3x\,\tfrac{g}{2}(\partial_\mu\vec n)^2 + e^2F^2$
is a **sum of squares**, hence $H \ge 0$; Vakulenko–Kapitanski bound it from *below*
by $c\,|Q_H|^{3/4}$ with $c > 0$. So $c\,|Q_H|^{3/4} \ge 0$ **identically, for every
$c$ and every $Q_H$.**

The residual the class would have to supply is **mixed-sign**: the corpus's
$B_{\mathrm{sym}}$ *overshoots* at ²H, giving $R(^2\mathrm{H}) = -0.6074$ MeV against
$R(^4\mathrm{He}) = +19.6157$ MeV. A non-negative functional cannot equal a
sign-changing target — no choice of $c$, no choice of $Q_H$, no reparametrisation.

This is the licensed shape of a scope-(b) exclusion under AGENTS.md — the same
mixed-sign-target-vs-non-negative-weight structure as the KL-positivity prune of
Option-E PROBE 4. It is the strongest result here and it was **not** anticipated by
the pre-registration; it surfaced as the log-space fit going complex, and is reported
rather than repaired.

### What is *not* claimed

"No functional of a single global charge can work" is **false as stated**, and saying
it would be an arity conflation. With $Q_H$ free, $F \circ Q_H$ is a reparametrisation:
one may set $Q_H = (B/c)^{4/3}$ and reproduce *any* target, so the exponent $3/4$
constrains nothing. The honest statement is the disjunction:

- $Q_H$ **pinned** to a topological power of $A$ ⇒ excluded by S1 (shape) and, on the
  residual, by S2 (sign);
- $Q_H$ **free** ⇒ the claim is unfalsifiable and is not evidence for anything.

There is no third branch in which the class is both testable and alive.

## Pre-registered numerical outcome

19 nuclides, ²H → ²³⁸U. $B_{\mathrm{AME}}$ from `codata_constants.ame_binding_mev`
(vendored AME2020, exact route). Log-space least squares, closed form, `mpmath.mpf`
at 60 dps end to end. Three forms per target, exactly as pre-registered; no fourth.

### Primary target — total binding $B_{\mathrm{AME}}$

| form | free params | fitted | max rel. residual | worst | verdict |
|---|---|---|---|---|---|
| **F1** $c A^{3/4}$ ($Q_H \propto A$) | 1 | $c = 12.4613$ | **8.4208** | ²H | REFUTE (R-i) |
| **F2** $c A^{3/2}$ ($Q_H \propto A^2$) | 1 | $c = 1.4560$ | **1.9673** | ²³⁸U | REFUTE (R-i) |
| **F3** $c A^{p}$ | 2 | $p = 1.26205$, $c = 2.8773$ | **2.1021** | ²H | REFUTE (R-i **and** R-ii) |

F3 carries *more* freedom than the hypothesis allows and still misses by 210 %. Its
exponent lands at **1.262**, far outside the pre-registered window $[0.70, 0.80]$ —
so R-ii fires independently of the residual bound. Both refutation criteria, on the
form built to flatter the class.

### Secondary target — residual $R = B_{\mathrm{AME}} - B_{\mathrm{sym}}$

$B_{\mathrm{sym}}/A$ read from §4 of
[`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md),
**not recomputed here**.

| iso | $A$ | $B_{\mathrm{sym}}/A$ (audit) | $R$ (MeV) | $R/A$ |
|---|---|---|---|---|
| ²H | 2 | 1.416 | **−0.6074** | −0.3037 |
| ⁴He | 4 | 2.170 | +19.6157 | 4.9039 |
| ¹²C | 12 | 2.673 | +60.0857 | 5.0071 |
| ⁵⁶Fe | 56 | 2.898 | +329.9720 | **5.8924** |
| ²⁰⁸Pb | 208 | 2.991 | +1014.3022 | 4.8765 |
| ²³⁸U | 238 | 2.998 | +1088.1660 | 4.5721 |

**REFUTED on sign, scope (b)** — see S2. The pre-registered fit is *undefined* on a
mixed-sign target, so no fit was performed and no residual number is quoted for it.

### Post-hoc check — explicitly not evidence

Restricting $R$ to the five rows with $R > 0$ is a **deviation from the
pre-registration**: a subset chosen after seeing which row broke the fit is exactly
the freedom the pre-registration exists to remove. It is recorded only because it
**also refutes**, and it is stated plainly that had it supported the hypothesis it
would not have counted.

| form | fitted | max rel. residual | verdict |
|---|---|---|---|
| F1 $cA^{3/4}$ | $c = 12.8213$ | 0.8487 | REFUTE (R-i) |
| F2 $cA^{3/2}$ | $c = 0.7750$ | 1.6151 | REFUTE (R-i) |
| F3 $cA^{p}$ | $p = 0.99182$ | 0.1480 | REFUTE (R-ii; S-ii bound missed) |

Note F3's exponent here is **0.9918 — essentially 1, i.e. purely extensive**, not
$3/4$. The data's own preference, given maximum freedom, is a volume term. That is
the SEMF's $a_V A$ and the shape the corpus's `B_sym` already has (at 2.93× too small
a coefficient); it is not a knot-soliton bound.

## S1 was put at risk and survived

The pre-registration committed to retracting S1 if F3 reached $\le 0.10$ max relative
residual. It reached **2.1021** (primary) and **0.1480** (post-hoc subset). S1 stands
on both. The non-monotonicity premise was checked rather than assumed: interior
maximum at ⁵⁶Fe on both targets, rises somewhere and falls somewhere on both.

## Why the class looked plausible, and why that was not evidence

The attraction recorded in
[`2026-08-25-recent-knot-particle-uploads-vs-our-identifications.md`](2026-08-25-recent-knot-particle-uploads-vs-our-identifications.md) §3
was that $|Q_H|^{3/4}$ is **neither per-block nor pairwise**, which is the right
*class* for a term that must exceed the complete-graph pairwise ceiling at ⁴He by
11.12 MeV. That observation stands and is untouched. What does not follow is that
this particular non-additive functional is the term.

Three things pointed the other way before any fit, all recorded in the
pre-registration:

1. The direction is wrong — $Q^{3/4}$ is sub-linear, so $Q_H \propto A$ makes binding
   *per nucleon* fall like $A^{-1/4}$ where the corpus needs it to rise.
2. The corpus's own `rem:hopf-link-non-magic` has $\mathrm{Vol}(\mathrm{Hopf}) = 0$
   (Seifert-fibered, not hyperbolic) and puts the Hopf link entirely in
   $E_\infty^{0,*}$ — the descended-Markov-trace slot that contributes $\lesssim 0.5\%$
   of magic-shell binding. The Hopf object is already degenerate here.
3. That $3/4$ sits between the SEMF surface exponent $2/3$ and volume exponent $1$ is
   a remark about two *other* numbers, not support.

The one honest use of the paper remains what §3 of the uploads audit already claimed
for it: a **citable precedent** that a knot-energy functional need not be additive
over blocks, and a named lower bound to compare a future closure against.

## Scope discipline

- **Scope (b)**, invariant *strict monotonicity of $A^{p-1}$*: no pure power law in
  $A$ — any exponent — reproduces a non-monotone $B/A$. Excludes $c|Q_H|^{3/4}$
  whenever $Q_H$ is a fixed power of $A$.
- **Scope (b)**, invariant *non-negativity of the Faddeev energy*: $c|Q_H|^{3/4} \ge 0$
  identically cannot equal the mixed-sign residual $R$.
- **Not excluded, and deliberately so:** non-additive knot-energy functionals as a
  *class*; any construction with genuine $(Z,N)$ or shell dependence; anything where
  $Q_H$ is derived from the QOU braid closure rather than posited as a power of $A$.
  This audit retires one functional form, not an ingredient.
- **No item is newly declared open.** GAP-1 and GAP-2 of the 2026-08-25 audit are
  unchanged; this narrows the candidate space for GAP-2 without closing it.
- **No fit is proposed or wired.** The probe emits no witness and touches no
  production path.

## Precision

`mpmath.mpf` end to end at 60 dps; no `float` arithmetic anywhere; means via
`mp.fsum`, never `statistics.mean`; `float()` appears nowhere in the probe. No
agreement is reported as "exact" or "to $N$ digits" — every figure here is a relative
residual of order $10^{-1}$ or larger, where the arithmetic is nowhere near its floor.
