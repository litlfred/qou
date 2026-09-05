# The fibre-compute-then-project mechanism — it exists, it is PARTIAL, and its root-of-unity sublocus is empty

**Bean:** `qou-cds1` / `qou-pdix` route 5.
**Probe:** [`computations/qbeta/qbeta_fibre_projection_and_rou_sublocus_probe.py`](../../computations/qbeta/qbeta_fibre_projection_and_rou_sublocus_probe.py) (5/5).
**Scope:** **(a)** for the reality arithmetic; the degeneracy exclusion is exact and `θ`-independent.
**This corrects my own merged [#6875](2026-09-05-cds1-fibre-reality-selects-n.md).**

## 🛑 The correction first

[#6875](2026-09-05-cds1-fibre-reality-selects-n.md) derived `N` from the reality of

```
Q_A / m_e  =  |q² − 2q − 1| · (q + 1) / (2q³)
```

on `|q| = 1`, getting `N = 5` with the modulus kept and `N = 4` under analytic
continuation. **That form is valid only on the real axis, so both answers are
archimedean artifacts.**

The block that defines the quantity —
[`neutron-qvalue-symbolic`](../../content/quantum-observable-universe/nuclear-interactions/neutron-qvalue-symbolic.md)
— does not write it that way. It writes

```
Δ(net) = h(h − 2)/2 ,   h = q − 1/q ,   E_0 = m_e / (q(q − 1)) ,   𝔔_β = |Δ(net)| · E_0
```

and with `h = (q²−1)/q`, `h − 2 = (q²−2q−1)/q`,

```
|Δ(net)| · E_0 / m_e  =  |q² − 1| · |q² − 2q − 1| / (2q² · q(q − 1))
```

The written form follows from this **only** by `|q² − 1| = (q − 1)(q + 1)`, which
needs `q` real and `> 1`. Measured gap between the two expressions:

| `q` | gap |
|---|---|
| `1.1` (real) | **0** |
| `e^{i/3}` | **2.4072132337744674** |
| `e^{iπ/3}` | **1.1860578654784908** |

So the very step that carries a formula onto the fibre is the step where the
simplification is illegal. #6875's `N = 5` / `N = 4` are withdrawn.

## What the projection mechanism actually is

The question "does the framework have a fibre-compute-then-project mechanism"
has an answer sitting in the block already: **the projection is the modulus**,
and it is applied to `Δ(net)` alone. `E_0` is carried through unprojected.

That partiality is not incidental — **it is the entire source of the reality
condition.** `|Δ(net)|` is real by construction whatever `q` is, so on `|q| = 1`
with `q = e^{iφ}`,

```
𝔔_β real   ⟺   Im[ 1/(q(q−1)) ] = 0
           ⟺   Im[ q² − q ] = 0
           ⟺   sin 2φ − sin φ = sin φ (2 cos φ − 1) = 0
```

zero exactly at `φ ∈ {0, π/3, π, 5π/3}`, and `φ = 0` is the pole `q = 1`. So the
partial projection selects

> **`φ ∈ {π/3, π, 5π/3}` — the SIXTH roots of unity.**

Not the fifth (#6875 reading A), not the fourth (reading B).

**A full projection selects nothing.** `|Δ(net) · E_0|` is a modulus, hence real
for *every* `q`, so it imposes no condition at all. This is worth stating
plainly: **the projection question and the N question are the same question.**
Which of the two projections the framework intends is exactly what fixes whether
`N` is determined or free.

And so: adopting the full projection *because* it is the one that admits the
required phase would be fitting the mechanism to the target. It is named here and
**not taken**.

## The root-of-unity sublocus is EMPTY

Reality admits three phases. **Every one of them is degenerate**, on grounds that
have nothing to do with the target:

| `φ` | `q` | degeneracy |
|---|---|---|
| `π/3` | primitive 6th root | `q⁴ + q² + 1 = 0` ⇒ Hoefsmit `b² = 0` |
| `5π/3` | primitive 6th root | `q⁴ + q² + 1 = 0` ⇒ Hoefsmit `b² = 0` |
| `π` | `−1` | `h = q − 1/q = 0` — the substrate degenerates |

The `b²` vanishing is an identity, not a coincidence: `q⁶ − 1 = (q² − 1)(q⁴ + q²
+ 1)`, so at a primitive 6th root `q⁶ = 1` with `q² ≠ 1` forces `q⁴ + q² + 1 = 0`,
and the Hoefsmit off-diagonal coupling on `V_{(2,1)}` is

```
b² = (q⁴ + q² + 1) / (q² + 1)²   →   0     (denominator ≠ 0 there)
```

so the two-dimensional rep decouples. Verified numerically (`4.139e-41` at 40 dps)
and exactly (`sympy` `expand_complex` → `0`); note `sympy.simplify` alone returns
`1 − (−1)^{1/3} + e^{2iπ/3}` and reports a **false** non-degeneracy — do not trust
it here.

**So reality admits exactly three phases and non-degeneracy excludes all three.
There is no admissible root of unity on the fibre locus.**

## θ is not the binding constraint

For the record, the required phase is `θ = 0.056617300794061032363`, and the
nearest reality-admissible phase `π/3` sits **18.496069867506741093×** above it.
But that ratio is *not* what excludes the sublocus — the emptiness above is
established before `θ` is mentioned and does not depend on it. Reporting the ratio
as the exclusion would misattribute a structural fact to a numerical near-miss.

## What this does and does not close

**Does:** the mechanism is identified and is already in the corpus; its partial
form selects the sixth roots; its root-of-unity sublocus is empty; #6875's `N`
values are withdrawn.

**Does not close route 5.** `|q| = 1` is a great deal more than its roots of
unity, and the full projection remains structurally available at the price of
selecting nothing. Both remain open.

## Reproduce

```bash
python3 -u computations/qbeta/qbeta_fibre_projection_and_rou_sublocus_probe.py
```

Proton pin (`q_at`), `q₀ = 1.1099785827513808076`, `dps = 50`, no float64.
