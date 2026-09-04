# `Q_β` real forces `Im q = 0` on the substrate branch — and what that closes in `conj:im-q-physical-role`

**Date** 2026-09-04 · **Beans** `qou-c66b` (worked), `qou-kgtf` (session) ·
**Branch** `claude/im-q-physical-role-2026-09-04`

Reached on the author's instruction to *"research on where imaginary comes
from / chip away `conj:im-q-physical-role`"*.

## Summary

`conj:im-q-physical-role` lists three candidate physical roles for `Im(q)` and
says all three are blocked because the framework has no `Im(q)`-sensitive
observable — the mass formula projects through `|tr_M|`. **The framework does
have one, and it has had one all along: `Q_β`.** Its closed form carries the
modulus on a single factor, so the projection that makes the mass Im-blind
does not apply.

Running the conjecture's **own stated test for candidate (ii)** on that
observable closes it on the substrate branch. The result is proved twice —
exactly (sympy over `ℤ[x,y]`) and in Lean (`lean`-direct exit 0, eight
declarations, no `sorryAx`) — and, importantly, it does **not** depend on
resolving the one thing `qou-c66b` flagged as unresolved.

## What the conjecture says

[`conj-im-q-physical-role.md`](../../content/quantum-observable-universe/mass-theory/conj-im-q-physical-role.md),
§"Obstacles to a current proof":

> The framework's mass formula explicitly **projects away** Im(q) content via
> `|·|`, so no mass observable can detect Im(q) directly. The candidate roles
> are all in **non-mass observables**.
>
> - (ii) needs a second independent CAL-2-like constraint
> - (iii) needs a categorical formula for decay widths Γ

and candidate (ii)'s test, verbatim:

> **Testable**: does another CAL-2-like independent constraint (a second real
> equation from `m_τ/m_e`, or from a different observable) fix a unique complex
> `q₀`? **If only real solutions exist, candidate (ii) is closed**; if a
> complex solution is needed, the framework has missed an Im(q)-coupled
> measurement.

## The observable the conjecture overlooked

`Q_β` **is** a CAL-2-like constraint. Per `AGENTS.md`'s cheat sheet, CAL-2 is
the neutron β-decay width `𝔇_β`, and `Q_β = ℏ/𝔇_β` is its proxy — a decay
observable, in closed form, already in the framework. So candidate (iii)'s
stated obstacle ("needs a categorical formula for decay widths Γ") is not
where the β channel stands: it has one.

[`neutron-qvalue-symbolic.md`](../../content/quantum-observable-universe/nuclear-interactions/neutron-qvalue-symbolic.md)
gives it two ways, one line apart:

| | form | modulus covers |
|---|---|---|
| **E2** (the derivation) | `Q_β = \|Δ(net)\| · E₀`, `Δ(net) = h(h−2)/2`, `h = q − 1/q`, `E₀ = m_e/(q(q−1))` | `Δ(net)` only; `E₀` is unprojected |
| **E1** (the printed closed form, and the live code at `qbeta_utils.py:293`) | `Q_β = m_e·\|q²−2q−1\|·(q+1)/(2q³)` | one quadratic only |

Contrast the mass, where `|tr_M|` covers the whole expression. **That
structural difference is the whole finding**: two of E1's three factors, and
`E₀` in E2, are not under a modulus, so `Im q` survives into the answer.

**E1 is E2 simplified using `q` real and `q > 1`** — only then is
`(q²−1) = (q−1)(q+1)` positive and pullable out of the modulus. Extending E1
past the hypothesis that produced it is the shape `AGENTS.md` warns about under
"defined residual ≠ derived decomposition", one construction over. Hence both
are carried below, and neither is declared canonical.

## The measurement

[`qbeta_imq_reality_locus_probe.py`](../../computations/qbeta/qbeta_imq_reality_locus_probe.py),
8/8 assertions, witness
[`qbeta-imq-reality-locus.witness.json`](../../computations/qbeta/qbeta-imq-reality-locus.witness.json).
Exact symbolic over `ℤ[x,y]`; mpmath 50 dps spot-checks; no float64 anywhere.

`Q_β` is a measured Q-value in MeV, so it is real. With `q = x + iy`, both
readings are (real non-negative modulus factor) × (unprojected rational
function), so `Im Q_β = 0` reduces to that rational function being real:

```
E1   Im[(q+1)/(2q³)]  = −y(2x³ + 3x² + 2xy² − y²) / (2(x²+y²)³)
E2   Im[1/(q(q−1))]   = −y(2x − 1) / ((x²+y²)(x²−2x+y²+1))
```

Each zero set factors exactly as `y · (branch)`:

| | trivial branch | non-real branch | where the non-real branch is real |
|---|---|---|---|
| **E1** | `y = 0` | `y² = −x²(2x+3)/(2x−1)` | `x ∈ (−3/2, 0) ∪ (0, 1/2)` |
| **E2** | `y = 0` | `x = 1/2` exactly, `y` free | the single line `x = 1/2` |

**The substrate is in neither.** `Re q = q₀ ≈ 1.10998 > 1/2`, so E1's `y²` is
negative there and E2's line misses it. The third escape — the modulus factor
itself vanishing — supplies nothing either: `q² − 2q − 1 = 0` at `1 ± √2`, both
real.

## Stronger than "on the substrate branch" — candidate (ii)'s ENTIRE admissible set

"On the substrate branch" understates the result, and the understatement
matters, because candidate (ii) is not a claim about a point.

The conjecture posits that CAL-2 alone leaves an **Apollonius circle** of
admissible complex `q`, with `Im q` as *"the arc coordinate parametrizing the
other admissible q values"*, centre `≈ 1.010` and radius `≈ 0.100` *"per the
formal derivation"*. Reading CAL-2 with a modulus — which is what produces a
circle at all, since `ℏ_q² = k` real would already force `q` real — gives

```
|1 − 1/q| = √k,   k = Vol(4₁)/(m_μ/m_e)     ⟺     |q − 1| = √k·|q|
centre = 1/(1−k),   radius = √k/(1−k)
```

From the live CODATA-2022 ratio `m_μ/m_e = 206.7682827` and
`Vol(4₁) = 2·Cl₂(π/3)`:

| | derived here | conjecture states |
|---|---|---|
| `k` | `0.00981718852772` | — |
| centre | **`1.0099145212520`** | `≈ 1.010` |
| radius | **`0.1000640743907`** | `≈ 0.100` |

Reproducing both to the stated precision is what establishes that this reading
of CAL-2 **is** the conjecture's reading rather than a guess at it.

**Its leftmost point is `Re q = 0.909850`, a margin of `0.410` above `1/2`.** So
the entire admissible arc lies in the half-plane where both non-real branches
are empty. `Im Q_β = 0` therefore kills **every** non-real point of the circle
and leaves exactly its two real intersections, `0.9098504` and `1.1099785956`.

Two asides worth recording. The upper intersection is the live CODATA-2022 muon
`q₀` to every digit shown — as it must be, since the circle is built from that
ratio — and the **proton** pin sits `1.046e-8` off the circle in the
`|q−1|/|q|` residual, which is the μ–p substrate tension seen in this
coordinate. Neither is used in the argument; they are consistency checks that
the circle is the object the corpus already carries.

Lean: `cal2_circle_lies_in_substrate_half_plane` proves the general fact that
any circle with centre `> 9/10` and radius `< 2/5` lies strictly right of
`1/2`. The measured pair clears both bounds by an order of magnitude, so the
theorem applies with room to spare and nothing hinges on the last digits of the
CODATA input.

## Why running both extensions is the point, not a hedge

The two non-real loci are **disjoint**: E1's is an open strip and E2's is the
line `x = 1/2` bounding it. At `x = 1/2` the E1 factor evaluates to exactly `1`
for every `y` (`branches_disjoint`). So the extensions disagree about where
imaginarity is admissible **everywhere except on the answer that matters**.

That cuts both ways, and both are worth stating:

- It **corroborates** `qou-c66b`'s caveat that the choice of complex extension
  is genuinely unfixed and genuinely changes the answer.
- It **removes** that caveat as an obstacle to *this* conclusion, which holds
  under either reading.

## The Lean

[`QOU/QBeta/ImQRealityLocus.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ImQRealityLocus.lean)
— `lean`-direct **exit 0**, nine theorems, `#print axioms` standard-3 on every
one, **no `sorryAx`**; code-level `sorry`/`axiom`/`native_decide` = 0/0/0.

The load-bearing pair is `e1_branch_pos` / `e2_branch_pos`: for `1/2 < x`,
`2x³ + 3x² + 2xy² − y²` regroups as `2x³ + 3x² + y²(2x−1)`, three terms each
non-negative and the first two strictly positive — **for every `y`**, which is
what makes the branch empty rather than merely small.

`im_q_zero_under_either_extension` states the conclusion as a **disjunction**
on purpose: not that both readings are needed to conclude, but that whichever
is canonical the answer is the same.

Two witnesses keep the theorems honest rather than vacuous:
`im_e2_locus_is_nonempty` (`x = 1/2`, `y = 1`) and `im_e1_locus_is_nonempty`
(`x = −1/2`, `y = 1/2`) exhibit complex `q` with real `Q_β`. **The `1/2 < x`
hypothesis is doing real work and cannot be dropped.**

## Correction to my own earlier claim

Bean `qou-c66b`, written earlier the same day, asserted without qualification:

> `Q_β` is experimentally a real Q-value in MeV. Requiring `Im Q_β = 0`
> therefore forces `Im q = 0`.

**That is too strong.** One real equation on two real unknowns has a *curve* of
solutions, not a point, and the non-real branch is non-empty under both
readings — the two Lean existence witnesses above are explicit counterexamples
to the unqualified form. The claim holds **on the substrate branch `Re q >
1/2`**, which is where it needed to hold, and the qualifier is not cosmetic:
without it the statement is false at `x = 1/2`.

A second slip, recorded because the failure mode is the point: the first draft
of `im_e1_locus_is_nonempty` offered `(x, y) = (−1, 1)`, where the factor is
`−2`, not `0`. An existence claim whose witness does not satisfy its own
equation reads fine to a human and is caught only by the kernel.

## What this closes, and what it does not

**Closes — candidate (ii), on its entire admissible set, scope-(b).** The
conjecture's own test is *"if only real solutions exist, candidate (ii) is
closed"*. Only real solutions exist anywhere on the CAL-2 Apollonius circle
that candidate (ii) names as its admissible set — forbidden by a proved
algebraic identity rather than a numerical near-miss. And it closes using an
observable the framework already carries, so the conjecture's "needs a second
independent constraint" was already satisfied.

**Corrects — candidate (iii)'s stated obstacle.** The framework has a
categorical decay-sector observable for the β channel. What candidate (iii)
still needs is a formula for the *widths* `Γ` of the other unstable states (W,
Z, top, resonances); the obstacle is narrower than written, not absent.

**Does not touch — candidate (i), chirality.** Unchanged, and it is now the
only one of the three with no closure argument against it from either
direction. The sibling
[`ImQCannotSupplyEllipticGenerator.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ImQCannotSupplyEllipticGenerator.lean)
says the same of the routes it closes.

**Does not touch — the fibre level.** This constrains the **archimedean
evaluation** only. `AGENTS.md`'s fibre-vs-observable banner explicitly leaves
`Im(q)` unconstrained on the fibre, and the whole point of that banner is that
`c_k(q)` may be complex-analytic there while every anchor evaluation is real.
What is new is that the archimedean `Im q₀ = 0` — previously an *assertion*,
`lusztig_q_0_imaginary_part_zero` — now **follows** from a decay observable.

**Does not fix which extension is canonical.** It shows the substrate answer
does not depend on that, which is a different and weaker statement. Deciding it
is still prerequisite to running candidate (iii)'s test properly off the
substrate.

## Where the imaginarity has to come from, then

Three independent directions now say the same thing about the archimedean
layer: the Kohno–Drinfeld character (`character_im_zero_iff`), the substrate
assertion (`lusztig_q_0_imaginary_part_zero`), and now a decay observable. Two
of the conjecture's three candidate roles are closed there.

So the remaining room is exactly where `AGENTS.md` already points and where
`qou-cds1` says a D-frame story must live: **the fibre**, plus candidate (i)'s
chirality, which no argument in the corpus yet reaches. A search for `Im(q)`
in an archimedean observable is a search in a place three separate proofs say
it is not.
