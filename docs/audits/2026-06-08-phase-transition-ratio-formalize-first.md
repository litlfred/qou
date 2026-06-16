# Phase-transition ratio: a formalize-first scoping analysis

**Date:** 2026-06-08
**Branch:** `claude/gallant-bohr-w9f6a6` (PR #1999)
**Discipline:** CLAUDE.md §"Formalize-first probe discipline" — narrow the
search *before* running a wide numerical phase-point fit.
**Status:** preliminary — the consistency-condition resolution (§5) is
not yet closed; this doc exists to prune the naive probe before build.

## 0. Why this doc exists

The owner asked to "use phase transition from QOU and q₀ to reproduce
freezing / boiling / sublimation points." The tempting move is a wide
numerical fit of the existing critical-temperature formulas to the
measured triple of (freeze, boil, sublimate) for H₂O. Formalize-first
says: **find the scale-free invariant first**, test it cheaply, and let
the result tell us whether the wide fit is even well-posed. It is not
(yet) — see §4.

## 1. The hypothesis class (existing proven machinery)

From [`prop:phase-transition-boundary`](../../content/quantum-observable-universe/information-theory/phase-transition-boundary.md)
(has a Lean sibling proving positivity + ordering):

$$
T_q^{(g\to l)} = \frac{S_q^{(\partial)}}{[2]_q},
\qquad
T_q^{(l\to s)} = \frac{S_q^{(\partial)}}{[2]_q\,[n_K]_q},
$$

where $S_q^{(\partial)}$ is the $S^3$ boundary action (a region-dependent
categorical surface integral), $[2]_q = q+q^{-1}$, and $n_K$ is "the
crossing number of the particle knot." Gas/liquid/solid are the
symmetric / mixed / antisymmetric Hecke channels
([`rem:phase-transition-interpretation`](../../content/quantum-observable-universe/information-theory/phase-transition-interpretation.md)).

## 2. The scale-free invariant

$S_q^{(\partial)}$ is the messy, substance- and region-dependent factor —
the part a naive fit would chase. **It cancels in the ratio:**

$$
\boxed{\;\frac{T^{(g\to l)}_q}{T^{(l\to s)}_q} \;=\; [n_K]_q\;}
$$

So the **boiling-to-freezing absolute-temperature ratio is predicted to
equal a single q-integer** $[n_K]_q$, depending only on the substrate $q$
and the knot crossing number $n_K$ — no boundary-action calibration
needed. This is the cheap, decisive test.

## 3. The cheap test (existing chapter-12 molecules)

Evaluated at the canonical substrate $q_0 = 1.1099785955541805$
(50-dps value; $q_0 - q_0^{-1} = 0.209060$, $[2]_{q_0} = 2.010897$):

| substance | $T_{\text{boil}}$ (K) | $T_{\text{freeze}}$ (K) | ratio | implied $n_{\text{eff}}$ |
|-----------|----:|----:|----:|----:|
| H₂   |  20.28 |  13.99 | 1.4496 | 1.447 |
| CO   |  81.60 |  68.13 | 1.1977 | 1.197 |
| CH₄  | 111.65 |  90.69 | 1.2311 | 1.230 |
| C₆H₆ | 353.24 | 278.68 | 1.2675 | 1.266 |
| H₂O  | 373.15 | 273.15 | 1.3661 | 1.364 |
| CO₂  | sublimes at 1 atm (triple point above 1 atm) | — | — | — |

(All six molecules already have braid constructions in Chapter 12.)
$n_{\text{eff}}$ solves $[n_{\text{eff}}]_{q_0} = \text{ratio}$ via
$n = \operatorname{asinh}(\text{ratio}\cdot(q_0-q_0^{-1})/2)/\ln q_0$.

## 4. The finding — the integer-crossing reading is REFUTED

- $[1]_{q_0} = 1.0000$ exactly (degenerate: boiling = freezing, no
  liquid range).
- $[2]_{q_0} = 2.0109$.
- **Every real substance has ratio $\in (1.20, 1.45)$**, strictly
  between $[1]_q$ and $[2]_q$. No *integer* $n_K$ reproduces any of them;
  the smallest non-trivial integer crossing number ($n_K = 2$, the Hopf
  link / single covalent crossing pair) **over-predicts the ratio by
  ~50 %** ($2.01$ vs measured $1.2$–$1.45$).
- The implied $n_{\text{eff}}$ is **not monotonic in molecular size**:
  H₂ (smallest) has the *largest* ratio (1.45), CO the smallest (1.20).
  So $n_{\text{eff}}$ is not "number of crossings in the molecular
  braid" in any literal sense.

**Conclusion:** the class "ratio $= [n_K]_q$ with $n_K \in \mathbb{Z}_{\ge 2}$
the literal molecular crossing number, evaluated at fixed $q_0$" is
**refuted**. Do **not** run the wide fit of $S_q^{(\partial)}$ to absolute
temperatures against this reading — it is mis-specified.

## 5. What the refutation points at (candidate resolutions)

Two structural subtleties, either of which dissolves the tension. Both
are formalizable and should be settled *before* any numerical phase build:

1. **Self-referential temperature (running q).**
   [`def:quantum-temperature`](../../content/quantum-observable-universe/information-theory/quantum-temperature.md)
   fixes $T_q = \hbar_q = (q-1)/q$ — temperature *is* a function of $q$.
   The freezing transition sits at a *lower* temperature, hence a
   *different effective $q$*, than the boiling transition. So $[2]_q$ in
   the numerator and $[n_K]_q$ in the denominator are **not evaluated at
   the same $q$**, and the clean cancellation in §2 is only the
   fixed-$q$ shadow of a fixed-point condition
   $T_q^{(c)} = (q_c-1)/q_c$ that pins each $q_c$ separately. The true
   ratio is $[n_K]_{q_s}\cdot(\text{running-}q\text{ correction})$ — which
   can land in $(1,2)$ for $n_K = 2$.

2. **Effective / normalized crossing number.** $n_K$ in the formula may
   be a *Markov-trace-normalized* crossing count (writhe per strand, or
   the Hecke "energy level" $[n_K]_q$ read off the antisymmetric channel
   weight), not the raw diagram crossing number. Under that reading
   $n_{\text{eff}} \in (1,2)$ is expected and the ordering across
   substances becomes the real predictive content.

Settling which one requires reading the Boltzmann/gas-constant scale
blocks ([`boltzmann-constant`](../../content/quantum-observable-universe/information-theory/boltzmann-constant.md),
[`gas-constant-derivation`](../../content/quantum-observable-universe/information-theory/gas-constant-derivation.md))
and the `phase-transition-boundary.lean` ordering proof, then deriving
the fixed-point form of the ratio. That is a Lean-adjacent structural
task, not a numerical scan.

## 6. Decision for the build

- ✅ **Keep** the scale-free ratio as the headline observable — it is the
  right, calibration-free test and it is already *interesting* (the
  measured ratios cluster tightly at $1.2$–$1.45$, a near-universal
  q-integer signature).
- ✅ **Report tiered** per CLAUDE.md: the ratio prediction is a
  **structural near-match pending the running-q fixed point**, NOT a
  fitted absolute temperature.
- ❌ **Do not** fit $S_q^{(\partial)}$ to reproduce 373.15 K / 273.15 K
  under the fixed-$q_0$ integer reading — refuted here.
- ➡️ **Next**: derive the running-q fixed-point form of the ratio
  (§5.1), then re-test; only then attempt absolute temperatures (which
  additionally need the Kelvin scale from the Boltzmann block).

## 7. Reproduction

The numbers in §3 come from a 12-line standalone script (q-integer +
`asinh` inversion at $q_0$); to be promoted to a witnessed compute
(`computations/`) routed through `qou_substrate` for the
canonical $q_0$ once §5 is resolved and the observable is final.
