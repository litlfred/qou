# Is `F = Q_β^exp / Q_A` required to be bar-even? — no, and it cannot be

**Bean:** `qou-cds1` (S1, re-derive the Q_β `c_k` ladder under convention D).
**Probe:** [`computations/qbeta/qbeta_f_bar_parity_requirement_probe.py`](../../computations/qbeta/qbeta_f_bar_parity_requirement_probe.py)
(symbolic, sympy end to end, no floats, no anchor; 5/5).
**Witness:** `computations/qbeta/qbeta-f-bar-parity-requirement.witness.json`.

## Why this question, and why first

`qou-cds1` names it as its own cheapest next step:

> whether `F` is REQUIRED to be bar-even … If bar-evenness is not required
> this is a curiosity; if it is, the ladder violates it in BOTH conventions by
> a 15 % term and the projection is incomplete rather than forced-and-final.
> Resolving that question looks like the cheapest next step, because it decides
> whether the `u/2` term needs replacing before any new functional form is
> attempted.

It is structural, not a search — so it is answerable without touching the
extractor, and it gates whether a new functional form is even the right move.

## Result

Write `Q_A = m_e·|q²−2q−1|(q+1)/(2q³)` for the framework's closed form for
`Q_β`, and `bar` for `q ↦ 1/q`. Then, as rational functions of `q`:

```
bar(Q_A)/Q_A = −q³·(q² + 2q − 1)/(q² − 2q − 1)
```

- **not bar-even** — the ratio is `+1` only at `q = 1`, where `bar` is the
  identity and the test is vacuous;
- **not bar-odd** — the ratio is `−1` at no positive real `q`;
- **not bar-definite up to a power of `q`** — stripping `−q³` leaves
  `(q²+2q−1)/(q²−2q−1)`, a ratio of two *distinct* irreducible quadratics
  (roots `−1+√2` and `1+√2`), which is not a monomial. No `q^n` normalisation
  restores a parity.

The third test is the one that matters here, because *"bar-definite up to a
power of `q`"* is already the channel's own working notion: `qou-cds1` records
`bar(z_D) = q⁻⁴·z_D`. So `z_D` is bar-covariant in that weaker sense and `Q_A`
is not covariant in it at all.

Controls confirm the test can see a parity when one is present: `h = q − 1/q`
gives `−1`, `[2]_q = q + 1/q` gives `+1`.

`Q_β^exp` is an experimental scalar, hence bar-even trivially, so
`bar(F)/F = Q_A/bar(Q_A)`. **`F` inherits `Q_A`'s non-parity: bar-evenness of
`F` is unsatisfiable, not merely un-required.**

## Consequence the bean asked for

**The `u/2` term does not need replacing on bar-parity grounds.** The bean's
"if it is required" branch is closed: there is no bar-evenness constraint for a
15 % term to violate, so the projection is not shown incomplete by this route.
Any case for replacing that term has to come from somewhere else.

Scope **(a)**, per AGENTS.md §"Before declaring refuted": this is a statement
about *this closed form*, proved symbolically. It is not a claim that the weak
sector has no bar-odd content.

## Flagged, NOT resolved — the "pure odd" attribution

The corpus describes this same object as bar-odd, in four places:

- [`AGENTS.md:1937`](../../AGENTS.md) — "the bar-odd `sinh` partner of the
  bar-even `cosh` meson scale m_π", attached to the closed form itself;
- [`observations/epistemic-status-of-calibrations.md:3`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md);
- [`observations/three-calibration-discipline-proof.md:36`](../../content/quantum-observable-universe/observations/three-calibration-discipline-proof.md);
- [`knots-particles-confinement/interaction-sector-taxonomy.md:20`](../../content/quantum-observable-universe/knots-particles-confinement/interaction-sector-taxonomy.md)
  — the strongest form: "in exact contrast to binding (pure even) and
  `𝔔_β` (**pure odd**)".

The Lean cited for the split does **not** establish that attribution.
[`mass-theory/bar-parity-split.lean`](../../content/quantum-observable-universe/mass-theory/bar-parity-split.lean)
proves `evenPart σ x + oddPart σ x = 2 • x` for an *arbitrary* `x` under an
*arbitrary* linear involution — the generic decomposition, true of everything.
The identification of `Q_β` with the odd part lives in that file's **docstring**
("the `Q_β` residue read off `F_odd`"), not in any theorem. So "pure odd" is an
interpretive attribution, and the scalar closed form does not satisfy it.

Two readings, both consistent with the evidence:

1. **The claim is about the channel.** `𝔔_β` is the `P_skew` component of some
   upstream Hecke element, and `Q_A(q)` is a downstream archimedean evaluation
   that need not retain the parity of its source. Then nothing is wrong — but
   the prose should be scoped to the channel rather than to the observable.
2. **The claim is about the observable.** Then it is refuted by the result
   above.

Deciding between them is a physics call about what `𝔔_β` names, so this audit
does not decide it. Recorded rather than assumed, per AGENTS.md §"Grep the
claim SHAPE": a set-level or channel-level property and a scalar's parity are
different claims, and reading one as the other is the arity conflation that
section exists to catch. In particular this is **not** a claim that the corpus
is inconsistent — that specific over-claim is a retracted error class here.

**Symbol collision, also flagged.** `bar-parity-split.lean`'s docstring writes
`F = F_even + F_odd` for an abstract Habiro element; `qou-cds1` writes
`F = Q_β^exp/Q_A` for a numerical correction factor. These are two objects
sharing a glyph in the same channel. Nothing here identifies them, and nothing
should, until someone does so deliberately.
