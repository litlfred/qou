# All of the c₃ anchor-dependence is in the `h·D → S` bridge, and the bridge changes sign

**Date:** 2026-08-19 · **Axis:** c₃ / Q_β bar-odd · **Tier:** scope-(a)
measurement of committed numbers · **Discipline:** no value derived, no `c_k`
wired, no fit, nothing bears on q₀ (forever-gated, `qou-eic1`).

## The question

`qou-qb8e`'s surviving one-line gate is *"the map from a bar-odd, anchor-blind
fibre-level object to an anchor-DEPENDENT number."* KC21 records `S = h·D(ũ)`
and the k=31 re-pin witness calls that relation *"schematic, not a tight
identity."*

**How schematic?** Both anchor evaluations are already committed, so this is
arithmetic, not research.

## The measurement

| | proton | muon | relative variation |
|---|---|---|---|
| carrier `h·D` | $-0.003486062405593$ | $-0.0034860636358261$ | $3.53\times10^{-7}$ |
| empirical `S` | $-0.0394593643$ | $+0.009682977798$ | $1.245$ |

Define the bridge as the quotient $B := S/(h{\cdot}D)$:

$$
B(\text{proton}) = +11.319, \qquad B(\text{muon}) = -2.778 .
$$

## Two things follow

**The bridge carries essentially all of the anchor-dependence** — $3.5\times10^6$
times more variation than the carrier. The ladder is blind to the anchor at the
$10^{-7}$ level, so any route hoping to explain the swing *from the ladder* is
looking where the signal provably is not.

**And it is not a mild factor: it changes sign.** So *"$S = h{\cdot}D$ up to a
factor"* understates the gap. No positive rescaling of the carrier — no
normalisation choice, no scalar convention — reaches `S` at both anchors.

## What this does not establish

`B` is a **quotient defined here**, not a decomposition anyone derived. Per
AGENTS.md §*"Defined residual ≠ derived decomposition"*, the three checks:

1. **Is the split empirically accessible?** **No.** There are exactly **two**
   anchors. Any 2-parameter family fits two points exactly, so `B`'s *form* is
   not constrained by this data. None is proposed, and fitting one would carry
   no information.
2. **Is the factor forced, or merely in range?** Merely in range — `B` is
   defined by division and its values are whatever `S` and `h·D` happen to be.
3. **Does the corpus carry a competing split?** The `S = h·D` relation is the
   corpus's own; this adds a measurement of the residual factor, not a rival
   decomposition.

## Why a negative-shaped result is the useful one here

The contribution is about **direction**, not content. It says where the
anchor-dependence is (entirely in the bridge) and, by the sign change, rules out
the cheapest class of explanation (a positive rescaling of the carrier). It says
nothing about what `B` is, and the two-anchor obstruction means this data never
could.

That obstruction is worth carrying forward: **more anchor-fitting is not a
route.** A third independent anchor, or a structural constraint on `B` from
outside the anchor data, is what would change the situation.

## Cross-references

- Probe: [`hd_to_s_bridge_anchor_dependence_probe.py`](../../computations/qbeta/hd_to_s_bridge_anchor_dependence_probe.py) (5/5, exit 0)
- Source of both anchors: [`qbeta-c3-qstar-k31-repin.witness.json`](../../computations/qbeta/qbeta-c3-qstar-k31-repin.witness.json) `data.carrier_anchor_blindness`
- The gate: bean `qou-qb8e` (read its two front-state corrections first)
- Registry: [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) KC21
- Bean: `qou-qiw9`

---

# Addendum (2026-08-19): what this is driving at, and what the literature offers

Added at the author's request. **Low priority — a lead, not a route to closure.**

## What "closing c₃" would mean

`c₃` sits at tier **`cal-anchored`**, and the point of this front is to move it
to **`derived`**. The two differ sharply:

- **Cal-anchored** — `c₃` is *extracted* from experimental Q_β by inverting
  `c₃ = (Q_β^{exp}/Q_{N2} − 1)/u³`. It carries no content independent of the
  measurement; it is a repackaging of it.
- **Derived** — the framework produces `c₃` from its own structure, and Q_β
  becomes a **prediction to check** rather than the input that was inverted.

The near-match that motivates the attempt is `c₃ = −2 = J_{Hopf}(q=1)`, sitting
$3.47\%$ from the extracted value: close enough to look structural, far enough
that closing it is real work.

## The fit this audit is written to prevent

Concretely, and it would take about twenty minutes. `B` has two known values.
Posit $B(q) = \alpha + \beta\,g(q)$ for any plausible categorical $g$ — a
bracket, a volume, a power of $\hbar_q$ — and solve the $2\times2$ system. It
fits both anchors **exactly**, sign change and all, and produces a clean
formula.

It would be worth nothing. Two free parameters against two data points leaves
**zero** degrees of freedom, so there is nothing left over to be right or wrong
about. That is not a derivation; it is a coordinate change on the two numbers
one started with.

The subtler form is harder to spot and therefore more dangerous: take a genuine
categorical object carrying **one** free normalisation, tune that normalisation
to the proton anchor, then present the muon anchor as an independent
cross-check. It is not independent — the normalisation absorbed the freedom.
`qou-qb8e`'s guardrail states the requirement directly: *a derived `c₃` must come
out of the construction with its normalisation pinned in advance.*

Admissible-parameter budget, stated so it can be checked rather than argued:
with two anchors, a candidate form may carry **at most one** free parameter, and
one is already generous.

## What the library offers — one lead, unverified

The obstruction is not difficulty; it is **information**. Two points cannot
constrain a functional form. So the question worth asking the literature is not
"what is `B`" but **"what object supplies more than two evaluations?"**

The library holds a direct candidate shape:

> **Garoufalidis–Zagier, *Knots, Perturbative Series and Quantum Modularity***
> ([`arxiv-2111.06645v3`](../../library/arxiv-2111.06645v3/)) — *"an invariant of
> a hyperbolic knot which is a map $\alpha \mapsto \Phi_\alpha(h)$ from
> $\mathbb{Q}/\mathbb{Z}$ to matrices with entries in $\mathbb{Q}[[h]]$"*.

**A family indexed by $\mathbb{Q}/\mathbb{Z}$ is exactly the shape of thing that
dissolves a two-point obstruction** — one object with infinitely many
evaluations, rather than one number read at two anchors. Related holdings in the
same direction: [`arxiv-1411.6062v2`](../../library/arxiv-1411.6062v2/)
(evaluation of state integrals at **rational points**) and
[`arxiv-2304.07001v3`](../../library/arxiv-2304.07001v3/) (resurgence for Habiro
elements from radial limits).

**What is checked and what is not.** Checked: all five candidate papers are
already registered in `references.ts` and cited across `docs/` and
`computations/` — 2111.06645 alone appears in 24 files. So there is **no missing
paper**, consistent with the 2026-08-18 R2/R3 triage
([`2026-08-18-5two-survey-r2-r3-triage.md`](2026-08-18-5two-survey-r2-r3-triage.md)).
The $\mathbb{Q}/\mathbb{Z}$ statement is verified against the paper's own text,
not an index summary.

**Not checked, and this is the whole of the lead:** whether `B` has any
counterpart in the $\Phi_\alpha$ family. The corpus uses 2111.06645 for a
different purpose — arbitrating the colored-Jones tower — and nobody has asked
whether its indexed family bears on the bridge. That question is well defined
and currently unexamined.

It is also **not** obviously admissible: a route that explains the anchor swing
may be deriving $q_0$ under another name, and that is permanently gated
(`qou-eic1`). Anyone opening this should settle the gate question first, on the
shape of the proposal, before computing anything.

## Honest expectation

I do not think this front is closeable from the anchor data, and the addendum is
written to save effort rather than to encourage it. The one thing that would
change the situation is a **third independent evaluation** — from the
$\mathbb{Q}/\mathbb{Z}$ family or anywhere else — and until such a thing exists,
further fitting against two numbers is not a route however sophisticated the
form.
