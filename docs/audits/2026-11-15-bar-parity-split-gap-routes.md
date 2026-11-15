# Closing the bar-parity-split gap: four routes, verdicts

**Context.** `prop:bar-parity-split` was demoted to `conj:bar-parity-split` on
2026-11-15 (owner, option (a); PR #7857). Its Lean proved only the generic
even/odd decomposition. No `Q_β` functional on record is bar-odd
([`2026-11-15-one-sided-weak-vertex.md`](2026-11-15-one-sided-weak-vertex.md) §4).
This note asks whether the gap can be closed.

**Beans:** `qou-hlx8` (the question); new gaps `qou-2djn` and `qou-z08b`; epic `qou-qs0e`.
**Probe:** [`computations/qbeta/qbeta_bar_parity_split_gap_probe.py`](../../computations/qbeta/qbeta_bar_parity_split_gap_probe.py).
It is exact sympy in `q`, writes no witness and does not touch the dashboard; 18/18 checks pass.
**Lean:** [`QOU/Mass/BarParitySplitGap.lean`](../../folio/quantum-observable-universe/lean/QOU/Mass/BarParitySplitGap.lean).

## Notation

- `h = q − q⁻¹`, `z_D = q³/(q²+1)`, and `bar` is `q ↦ q⁻¹`.
- On a letter `c·σ + d`, bar sends `σ ↦ σ⁻¹ = σ − h` and `h ↦ −h`. So `u ↔ d`, and the
  mixed letter `ud = σ − h/2` is fixed.
- `f(q) := tr^{z_D}(Δ)`, where `Δ = n − p` on `nuc11_interleaved`; this is the ruled cell. Its closed form is
  `f = (q²−1)(q⁴+1)P₁₂/(4q⁷(q²+1)²)`, with `P₁₂ = 2q¹² − 6q¹⁰ + 3q⁸ − 6q⁶ + 5q⁴ − 5q² + 2`.

## Route 4: when does a bar-odd letter difference give a bar-odd trace? (DERIVED)

**Step 1. The trace intertwines bar with `q ↦ q⁻¹` exactly when `z(q) − z(q⁻¹) = h`.**
Define `tr'(w) := bar(tr_z(bar w))`. Bar is a semilinear algebra automorphism, so
`tr'` is a trace. Its Markov step is
`tr'(xσ) = bar(tr_z(bar x · (σ − h))) = bar(z − h)·tr'(x)`.
By uniqueness of the Ocneanu trace with given parameter, `tr' = tr_{bar(z−h)}`.
So `tr' = tr_z` iff `bar(z − h) = z`, that is iff `z(q) − z(q⁻¹) = h`.

- `z_D` satisfies this identity. In Lean it is `zD_bar_shift`, which is `tr(σ⁻¹)(q) = tr(σ)(q⁻¹)`.
- `z_C` fails it, because `z_C(q) − z_C(q⁻¹) = 0`.
- The probe checks the identity on both full 11-letter words, exactly.

**Step 2. Given intertwining, `tr Δ` is bar-odd iff `tr(Δ + bar Δ) = 0`.** In Lean this is `trace_anti_iff`.

**Step 3. Reduce to the context words.** The p and n tails differ in two letters: `ud − u = −h/2` and
`d − ud = −h/2`. So, exactly,

    f = h · g,   g = −(T₁ + T₂)/2,

where `T₁` and `T₂` are the traces of the two context words that remain when each differing
letter is removed (probe check `f_equals_h_times_g`). Since `bar h = −h`, the parts are

    f_odd = h · g_even,    f_even = h · g_odd      (Lean `odd_mul_of_anti`).

**Condition.** A bar-odd letter difference lifts to a bar-odd trace **iff the context trace `g` is
bar-even**. Bar-fixedness of the context as an element is sufficient for this, but it is not necessary.

**On the ruled word the condition fails**, scope (a):
`g_odd = −h·[2]_q·(q² + q⁻²)/8 ≠ 0`. Hence `f_even = −h²[2]_q(q²+q⁻²)/8`, which is the
figure 9c recorded, now explained.

The context is not bar-fixed in two places. The `CORE` alternates `u, d` and bar sends it
to `d, u`. The gluon pair `u, u` goes to `d, d`. Which part produces `g_odd` is open
(bean `qou-z08b`). The element is ruled (`qou-ales`), so no replacement word was tested.

## Route 2: is `Q_β/h` bar-even? (REFUTED, scope (a), ruled trace)

- `f/h = g`, and `g` is not bar-even, as shown above.
- **Not bar-definite up to any power of `q` either.** `bar(f)/f = −P₁₂^rev/P₁₂`, which is not a monomial,
  because `P₁₂` is neither palindromic nor anti-palindromic: `q¹²P₁₂(q⁻¹) − P₁₂ = q²(q²−1)(q²+1)³`.
  For the retired forms, the 2026-09-04 audit found the same obstruction. There it was a pair of distinct
  quadratics, `q² ∓ 2q − 1`.

Reason each normalisation was tried:

| normalisation | reason |
|---|---|
| `÷ h` | `h` is the n − p letter difference |
| `× qᵏ` | this is the channel's own covariance notion, `bar(z_D) = q⁻⁴ z_D` |

The order-zero `E₀ = m_e/(q(q−1))` is itself not bar-covariant. So even a bar-odd trace
would not give a bar-odd `Q_β` without a statement of which factor carries the parity.

## Route 3: what is the bar-odd projection? (DERIVED meaning; use OPEN)

Steps 1–3 give `f_odd = ½ tr(Δ − bar Δ) = h · g_even`. In words, it is the n − p letter difference
times the bar-symmetrised context trace. This is an identity, not a selection.

The value at `q₀` is reported whatever it is, as `qou-hlx8` requires:

| part of `f` | value at `q₀` | `·E₀` | vs CODATA |
|---|---|---|---|
| `f` (scored cell, for reference) | `−0.15419488504724` | `0.65185631006` MeV | −16.678 % |
| `f_odd` | `−0.131742555488903` | `0.556939460557` MeV | −28.811 % |
| `f_even` | `−0.0224523295583365` | `0.094916849503` MeV | −87.868 % |

All three were computed at 60 dps, with no float64.

No derivation says the decay width reads only `f_odd`. Adopting it would be a choice, and on
these numbers it would also be the worse one. **Not proposed.**

## Route 1: find the element `F` (REFUTED with identity readouts, scope (b); OPEN otherwise)

- **Identity readouts.** `exists_parts_iff`: an `F` with even part `2τ` and odd part `2r` exists
  iff `τ` is σ-fixed and `r` is σ-anti. The invariant is that the odd part of anything is
  σ-anti (`oddPart_anti`).
  The ruled trace is not bar-odd: `f(2) + f(1/2) = −765/128` (`ruledTrace_not_bar_odd`).
  So no `F : ℚ → ℚ` works (`no_F_with_ruledTrace_odd`). This is a structural exclusion with a
  proved invariant, for this functional and these readouts.
  The retired Form A and the retired z = 1 trace fail the same test (9c, symbolic).
- **Natural non-fitted candidate.** Take `F = Δ ∈ H₃(q)` with readout `tr_{z_D}`. This is Route 4
  exactly, and it fails on the ruled word, scope (a).
- **Other readouts.** These are open (bean `qou-2djn`). Any `F` or readout chosen *because* its parts
  then match `τ` and `Q_β` is a fit.

## What this does not touch

- `conj:binding-qbeta-complex-volume`.
- The `Q_β`-sinh / m_π-cosh label sites, which sibling 9c owns.
- The dashboard.
