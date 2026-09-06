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

---

# STRENGTHENING (same day): the partial projection kills the WHOLE locus, not just its roots of unity

**Probe:** [`computations/qbeta/qbeta_fibre_partial_projection_kills_whole_locus_probe.py`](../../computations/qbeta/qbeta_fibre_partial_projection_kills_whole_locus_probe.py) (5/5).

## The scope line above was too weak

The section "What this does and does not close" says:

> **Does not close route 5.** `|q| = 1` is a great deal more than its roots of
> unity […]

**True about the locus, irrelevant to the argument.** The reality condition

```
Im[q² − q]  =  sin 2φ − sin φ  =  sin φ (2 cos φ − 1)  =  0
```

is imposed at **every** point of `|q| = 1` — it was never a condition applied
only at roots of unity. Its solution set on `[0, 2π)` is exactly

```
{ 0, π/3, π, 5π/3 }
```

four points, all of which happen to be roots of unity. So the "great deal more"
is already excluded, *by reality*, before degeneracy is mentioned. I described
the non-rational phases as open when nothing had left them open.

Verified two ways: `sympy.solveset` returns exactly those four, and an
independent dense scan (20,000 points, sign-change bracketing, bisection to
1e-45) finds no fifth zero.

> **A trap inside the check itself.** The first scan reported **five** zeros.
> That was the dedup, not the mathematics: `φ = 0` and `φ = 2π` are the same
> point, and a linear `|a − b|` calls them `2π` apart, so the zero found near
> the top of the interval never collapsed onto the one at the bottom. On a
> circle, dedup with `min(d, 2π − d)`. Recorded because the false reading was
> "there is a fifth solution `solveset` missed" — a spurious *finding*, not a
> spurious failure.

## All four die, and `φ = 0` dies twice

| `φ` | `q` | why it is degenerate |
|---|---|---|
| `0` | `1` | `h = q − 1/q = 0` kills `Δ(net)` **and** `q(q−1) = 0` is a pole of `E_0` |
| `π/3` | primitive 6th root | `q⁴+q²+1 = 0` ⇒ Hoefsmit `b² = 0` |
| `π` | `−1` | `h = 0` |
| `5π/3` | primitive 6th root | `q⁴+q²+1 = 0` ⇒ Hoefsmit `b² = 0` |

The section above dismissed `φ = 0` in one word as "the pole" and checked only
that. Both facts hold; at the sixth roots `|q²+1| ≠ 0`, so the `b²` vanishing is
the numerator's rather than an indeterminate form.

## The dichotomy, and neither branch predicts anything

```
PARTIAL projection  →  reality leaves 4 points, ALL degenerate
                       ⇒ the ENTIRE fibre locus is excluded
FULL projection     →  |Δ(net) · E_0| is real for every q
                       ⇒ no condition at all, nothing selected
```

So **route 5's N-selection mechanism yields no prediction under either reading
of the projection.** That is a scope-**(a)** negative on the *mechanism*.

## What it does NOT say

It says nothing about route 5's underlying idea — a fibre-level Habiro element
whose archimedean evaluation reproduces the anchor. That is untouched here.

And the whole argument is **conditional on the reality assumption route 5's
N-selection already rests on**: that `𝔔_β` must be real *at the fibre evaluation
point*, not merely after the archimedean functor. Per the fibre-vs-observable
banner in `AGENTS.md`, `Im(q)` is unconstrained at fibre level, so that
assumption is the load-bearing one — and dropping it removes the reality
condition, which is the only thing selecting anything. **The honest reading is
that this closes the mechanism as posed and reopens the question of whether
reality should have been imposed there at all.**

---

# 🛑 RETRACTION — owner ruling 2026-09-06: "Does not need to be real in fiber."

**The reality premise that both sections above rest on is rejected.** It was
inherited from #6875 and never examined until the strengthening section flagged
it as load-bearing; the owner has now resolved that flag **against** the premise.

## What is withdrawn

| claim | status |
|---|---|
| "reality selects `N` on the fibre locus" (#6875, both readings) | **withdrawn** — there is no reality condition on the fibre |
| "the root-of-unity sublocus is EMPTY" *because reality admits only 3 phases* | **withdrawn as stated** — reality admits every phase |
| "the partial projection excludes the ENTIRE fibre locus" (strengthening) | **withdrawn** — the exclusion ran entirely through the rejected premise |
| "route 5 predicts nothing under either reading" | **half survives** — see below |

Reality of `𝔔_β` is an **archimedean** constraint on the evaluation at `q₀` —
the corpus already says so (`lusztig_q_0_imaginary_part_zero`, and a sidecar
note on `complex-substrate-interpretation` flagging that "fibre-vs-observable
level of `Im(q)` is exactly the AGENTS.md 2026-06-01 distinction"). It is **not**
a condition on the fibre. Imposing it on `|q| = 1` was precisely the
level-conflation that banner warns against, and I did it twice.

## What survives, unchanged

Every *measurement* stands. None of it depended on the premise:

- **The written `Q_A` form is real-axis-only.** Gap `0` at `q = 1.1`, **2.407**
  at `e^{i/3}`. #6875's `N = 5` / `N = 4` stay withdrawn — now for two
  independent reasons rather than one.
- **The block's projection is the modulus on `Δ(net)`, and it is partial.**
  A structural fact about `neutron-qvalue-symbolic`, not a consequence of
  anything about reality.
- **The arithmetic.** `Im[q²−q] = sin φ (2 cos φ − 1)`; solution set exactly
  `{0, π/3, π, 5π/3}`; no fifth zero.
- **The four degeneracies are real and structural** — `b² = 0` at the primitive
  6th roots, `h = 0` at `−1`, the double degeneracy at `q = 1`. These are
  *not* reality-based and survive the ruling intact.

## What changes about the degeneracies — the weight, not the fact

Under the rejected premise those four points were the **entire admissible set**,
so excluding them closed the locus. Under the ruling they are **four excluded
points out of a continuum**. The same measurement goes from decisive to nearly
vacuous. That inversion is the substantive consequence of the ruling, and it is
the opposite of the weight both sections above gave it.

## The state route 5 is actually in

- **The fibre locus `|q| = 1` is intact**, less four degenerate points.
- **Nothing selects `N` there.** Not reality — it does not apply. The `1/111`
  candidate recorded in #6755 is neither selected nor excluded.
- The half of the dichotomy that survives is the *full*-projection half, and it
  now holds unconditionally rather than as one branch: **no reality argument
  selects anything on the fibre.**

## The open question, restated honestly

If reality is not the constraint, **what does constrain the fibre element?**
That is route 5's real open problem, and it is now cleanly separated from the
archimedean question it had been entangled with. Answering it needs a
fibre-level structural condition — a Habiro-integrality or an
`H_n(q)`-representation-theoretic one — not an evaluation condition.

**Nothing was wired, at any stage of this arc. No `c_k` moved.** The cost of the
error is three commits of analysis, all of whose measurements remain reusable.
