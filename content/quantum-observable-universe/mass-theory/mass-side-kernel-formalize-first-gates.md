**Proposition (definition + composition theorem).** *The
`MassSideKernel` Lean typeclass bundles the mass-theory analogs of
the four $\S 4$ formalize-first invariants for any candidate
`linking_weight` function $w(q)$. Instantiating `MassSideKernel` for
a candidate is equivalent to that candidate clearing all four
mass-side gates simultaneously.*

## Why a parametric mass-side typeclass

The $Q_\beta$ decay-side `BarEvenKernel` typeclass
([`prop:q-beta-bar-even-kernel-typeclass`](q-beta-bar-even-kernel-typeclass.md), PR #1893)
bundles the four §4 invariants for any candidate Habiro element
$F(q)$. The **mass-side analog** was scoped via the sympy
[`mass_theory_formalize_first_invariants_probe.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/mass_theory_formalize_first_invariants_probe.py)
(PR #1896, Track 3) which runs a 4×3 verdict matrix on three
published `linking_weight` candidates (Family A, via-Jones, Bring
color-tube).

This proposition ships the **Lean side** — parametric conditional
classes mirroring the $Q_\beta$ pattern, plus a unified
`MassSideKernel` typeclass that any future `linking_weight`
candidate is evaluated against as a single class-instance attempt.

## The four mass-side invariants (parametric)

For any candidate `linking_weight` function $w : \mathbb{R} \to \mathbb{R}$:

| # | invariant | mass-side form | parametric class |
|---|---|---|---|
| (a) | **Anchor-stable** | cross-anchor swing $|w(q_\mu) - w(q_p)| / |w(q_p)| < 10^{-6}$ | `MassAnchorStableGateClass swing` (where `swing` is the probe-computed magnitude) |
| (b) | **Bar-even** | $w(q) = w(q^{-1})$ (as elements of the formal q-rationals) | covered by [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) (CommRing R lemma) |
| (c) | **q = 1 classical-limit shadow** | $w(1)$ equals a registered categorical anchor — **OPEN GAP** (no registered anchor for `linking_weight` per PR #1896) | `MassQOneShadowGateClass w (anchor : Option ℝ)` — vacuous when `anchor = none`, requires $w(1) = a$ when `anchor = some a` |
| (d) | **Direction sanity** | $\|m - \text{target}\| \le \text{threshold} \cdot \text{target}$ (additive form; substrate target $\approx 2.46$, the CODATA-implied near-match per PR #1850) | `MassDirectionSanityGateClass m_candidate` (where `m_candidate = |w(q_0)|`) |

> **Direction-sanity formula note.** The Lean class uses the
> **additive** form $|m - \text{target}| \le \text{threshold} \cdot \text{target}$
> to match the PR #1890 `q-beta-direction-sanity-gate.lean` Lean
> precedent. The companion sympy probes (e.g.
> `mass_theory_formalize_first_invariants_probe.py`, PR #1896)
> implement the **multiplicative** variant
> $\max(|m| / \text{target}, \text{target} / |m|) \le \text{threshold}$
> for the operational direction-magnitude check. The Lean form is
> the more permissive scaffold — a multiplicative-passing candidate
> automatically satisfies the additive form within the same
> threshold magnitude.

The §4(c) open gap is the **mass-side analog** of Q_$\beta$'s
decay-side F(q) keystone — owner-gated multi-session research per
refuted-class map §5.

## Composition theorem

If `MassSideKernel w` is instantiable for some specific candidate
$w$, then:

1. `MassAnchorStableGateClass w` holds (parametric anchor-stability)
2. `MassDirectionSanityGateClass w` holds (parametric direction sanity)
3. $w$ admits the bar-even structural identity via the Q_$\beta$
   `bar_even_test_n2` CommRing R lemma (PR #1875)
4. (When a registered anchor is set) `MassQOneShadowGateClass w anchor`
   holds

The Lean proof of each lifting is a one-line extraction of the
corresponding field. The §4(c) lifting is **conditional** on the
open anchor question — the typeclass admits a parameter
`anchor : Option ℝ` so candidates can be evaluated against a
hypothetical anchor without claiming an actual registered one
exists.

## Use in the formalize-first checklist

This typeclass operationalises the mass-side complement to the
$Q_\beta$ 7-step $\Delta_\lambda$ pre-flight checklist
([`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md`](../../../docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md)
$\S 3$). For any candidate $w(q)$:

```
1. Bar-even check         → PR #1875 (CommRing R structural identity)
2. Anchor-stable (a)      → this PR: MassAnchorStableGateClass
3. Direction sanity (d)   → this PR: MassDirectionSanityGateClass
4. q=1 shadow (c)         → this PR: MassQOneShadowGateClass (parametric on anchor; OPEN GAP)
5. Unified bundle         → this PR: MassSideKernel typeclass
```

Steps 1–3 are evaluable; step 4 requires the open categorical
derivation (whatever rational/integer $w(1)$ should equal under the
mass-side categorical chain).

## Honest scope (per refuted-class map §5)

- This is **infrastructure**, not new mathematical content. It does
  NOT construct the registered §4(c) anchor for `linking_weight` —
  the categorical derivation of $w(1)$ remains open.
- The parametric class signatures enable **future** anchor candidates
  (e.g. the **$\Sigma f^\lambda / 4 = 5/2$ at $n=4$** finding from
  [PR #1899](https://github.com/litlfred/qou/pull/1899)'s mass-side
  anchor hunt — number of involutions in $S_4$ divided by 4) to be
  evaluated by instantiating `MassQOneShadowGateClass w (some anchor)`
  with the derived value.
- The §4(c) open gap is the mass-side keystone. Closing it is
  owner-gated multi-session research.

## Status

**Theorem (this proposition).** Sorry-free Lean class definitions
([`mass-side-kernel-formalize-first-gates.lean`](mass-side-kernel-formalize-first-gates.lean))
— three parametric §3b-cond conditional classes + one unified
`MassSideKernel` typeclass + three lifting lemmas + one rejection
lemma. Mirrors the Q_$\beta$ `BarEvenKernel` pattern (PR #1893).

**No sympy probe.** The mass-side §4 4×3 verdict matrix is already
in [`mass_theory_formalize_first_invariants_probe.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/mass_theory_formalize_first_invariants_probe.py)
(PR #1896). Future probes wanting to test a candidate $w$ against
the Lean class plug its substrate values into the
`MassSideKernel` field hypotheses.
