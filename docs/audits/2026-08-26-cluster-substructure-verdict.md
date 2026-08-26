# Cluster substructure vs the light-isotope binding residual — pre-registered verdict

**Date:** 2026-08-26 · **Bean:** `qou-52x7` (parent epic `qou-v2om`) · **PR:** [#5812](https://github.com/litlfred/qou/pull/5812)
**Pre-registration:** [`2026-08-26-cluster-substructure-prereg.md`](2026-08-26-cluster-substructure-prereg.md),
committed at **`843391340b7511f131fcd8342f1e1ea1e925384b`** and **pushed before** the
probe was written or any number computed.
**Probe:** [`computations/probes/cluster_substructure_edgeset_prereg_probe.py`](../../computations/probes/cluster_substructure_edgeset_prereg_probe.py)
· **Witness:** [`cluster-substructure-edgeset.witness.json`](../../computations/probes/cluster-substructure-edgeset.witness.json)

## Verdict in one line

**Cluster substructure, implemented as an edge-set restriction, is DEAD for the
residual as a whole — scope (b) — because ⁴He *is* the α: it is a single cluster under
every scheme, so its edge set is `K₄` identically and its ratio 1.6470 cannot move by
so much as one part in 10⁵⁰. It is LIVE but OVER-CORRECTING for the A ≥ 6 half.**

The `A ≥ 6` half is not settled either way: the best pre-registered evaluation reaches
`max|r−1| = 0.1806`, which is above the 0.10 support threshold and below the 0.25
refutation threshold — it lands in the band the pre-registration declared as neither.

## The four pre-registered evaluations, all reported

`r = B_AME / B_model`. `r > 1` = model too weak, `r < 1` = model too strong. All
`mpmath.mpf` at 60 dps; `α = E₀ = 4.185981363` MeV; convention D, proton pin,
colour-weighted, writhe-normalised; **zero fitted constants in every row**.

| iso | `K_A` (baseline) | C1+E1 | C1+E2 | C2+E1 | C2+E2 |
|---|---|---|---|---|---|
| ²H | 0.785282 | 0.785282 | 0.785282 | ∞ (`B = 0`) | 0.672703 |
| ³H | 0.945304 | 0.945304 | 0.945304 | ∞ (`B = 0`) | 0.854958 |
| ³He | 0.940395 | 0.940395 | 0.940395 | ∞ (`B = 0`) | 0.777972 |
| **⁴He** | **1.647031** | **1.647031** | **1.647031** | **1.647031** | **1.647031** |
| ⁶Li | 0.743339 | 1.598690 | 1.371980 | 1.862300 | 1.180570 |
| ⁷Li | 0.638546 | 1.500630 | 1.332180 | 2.284370 | 1.060070 |

C1 = maximal-α (²H = d, ³H = t, ³He = h, ⁴He = α, ⁶Li = α+d, ⁷Li = α+t);
C2 = α-plus-free-nucleons. E1 = intra-cluster only; E2 = E1 plus one inter-cluster bond
per cluster pair, typed to **maximise** `B` (computed to be `nn`, `αL_nn = 3.3069` MeV).
The `K_A` column reproduces §5 of
[`2026-08-25-low-isotope-binding-error-staleness-vs-gap.md`](2026-08-25-low-isotope-binding-error-staleness-vs-gap.md)
(0.945 / 1.647 / 0.743 / 0.639) from the accessors, independently.

## S-C1 — the pre-registered structural claim: CONFIRMED, with one correction I owe

**Premise checked, not assumed.** All three derived per-bond energies are strictly
positive: `αL_pp = 2.541586`, `αL_pn = 2.832825`, `αL_nn = 3.306906` MeV. So a genuine
edge-subset of `K_A` can only carry **less** binding.

**S-C1 (i) — CONFIRMED, and it is the whole result.** Under C1, ²H, ³H, ³He and ⁴He
are each a **single cluster**, so `E = K_A` exactly and `r` is **unchanged** — verified
by exact string equality of the 18-digit ratios, not by a tolerance. Clustering is a
**no-op on four of the six** isotopes.

**S-C1 (ii) — holds for E1, FAILS for E2, and the failure is my construction, not the
mathematics.** `r_E ≥ r_{K_A}` pointwise holds for **E1** (a faithful typed subgraph)
across both schemes. It **fails** for **E2** at C2's ²H, ³H, ³He. The reason: E2
assigns the **B-maximising type** to every inter-cluster bond — pre-registered
deliberately, but that **re-types** a pair rather than removing it. Under C2, ²H is
p + n and its single bond becomes an inter-cluster bond typed `nn`; since
`αL_nn > αL_pn`, `B` goes *up* (3.3069 > 2.8328) and `r` goes *down*. **E2 is therefore
not a subgraph at all — it is an UPPER BOUND on `B` for any inter-cluster typing.**
Recorded rather than repaired, and the probe now reports S-C1(ii) split by rule.

That correction turns out to *strengthen* the numerical section: see the bound below.

## R-ii fires — H_all is REFUTED, scope (b)

**⁴He's ratio is 1.647031 in every one of the four evaluations, and in the baseline.**
The invariant, which is what licenses scope (b) rather than scope (a):

> ⁴He **is** the α. In any scheme that admits an α at all — which is the defining
> content of α-clustering — ⁴He is a *single* cluster, so its edge set is `K₄`
> identically, so `B` is unchanged, so `r` is unchanged. No choice of scheme, no choice
> of inter-cluster bond type, no ordering of nucleons.

⁴He carries the **largest** deviation of the six (`|r − 1| = 0.647`), and it is the one
in the *opposite* direction from every other isotope. A class that provably cannot move
it does not explain the residual. This composes with the pre-existing scope-(b) result
in §5 of the motivating audit — ⁴He exceeds the complete-graph pairwise maximum by
**11.12 MeV = 39.3 %** of its binding, by the exact `K_A` Laplacian spectrum
`det_A(m) = (1 + (A−1)m)(1 − m)^{A−1}` — to give: **the ⁴He excess is outside the
pairwise family *and* outside every edge-set restriction of it.**

**The sharpest statement of the verdict.** Under C1 the *immovable* set is
{²H, ³H, ³He, ⁴He} with `r` = 0.7853, 0.9453, 0.9404, **1.6470** — which **already
straddles 1 in both directions**. The non-monotonicity that motivated this front lives
**entirely inside the set clustering cannot touch.**

## S-i / R-i — H_partial: NEITHER supported nor refuted

| evaluation | `max\|r−1\|` over {⁶Li, ⁷Li} | S-i (≤ 0.10) | R-i (> 0.25) |
|---|---|---|---|
| C1+E1 | 0.59869 | no | — |
| C1+E2 | 0.37198 | no | — |
| C2+E1 | 1.28440 | no | — |
| **C2+E2** | **0.18057** | **no** | **does not fire** |

S-i is **false** (nothing reaches 0.10). R-i is **false** (C2+E2 is inside 0.25). The
result lands in the middle band the pre-registration fixed in advance, and is reported
as such rather than rounded to whichever side reads better.

**S-ii:** C1+E1, C1+E2 and C2+E2 leave {²H, ³H, ³He, ⁴He} no worse than the `K_A`
baseline (worst `|r−1| = 0.647032`, i.e. ⁴He, unchanged). **C2+E1 fails S-ii** (three
isotopes at `B = 0`).
**R-iii:** C2+E1 is **disqualified** — ²H, ³H and ³He get *zero* edges, below the
linear-chain minimum. Its ⁶Li/⁷Li numbers are edge-count arithmetic, not clustering.

## The finding worth keeping: clustering OVER-corrects, and truth is bracketed

Because E2 bounds `B` **above** for any inter-cluster typing, it bounds `r` **below**.
So the following hold for *every* inter-cluster bond assignment, not just the one tried:

| scheme | `r(⁶Li) ≥` | `r(⁷Li) ≥` |
|---|---|---|
| C1 (maximal-α) | 1.37198 | 1.33218 |
| C2 (α + free nucleons) | 1.18057 | 1.06007 |

**Both are > 1 under both schemes.** The pairwise family with the complete graph is
*too strong* at A = 6, 7 (0.743, 0.639); restricted to a cluster edge set it becomes
*too weak* (≥ 1.18, ≥ 1.06). **Clustering moves the ratio in the right direction and
then past the target.** In bond-weight units (`Σ L` required = `B_AME/α`):

| iso | required | C1+E1 | C1+E2 | `K_A` | required as fraction of `K_A` |
|---|---|---|---|---|---|
| ⁶Li | 7.643127 (—) | 4.780866 (7 edges) | 5.570862 (8 edges) | 10.282153 (15 edges) | **0.7433** vs E1 0.4650, E2 0.5418 |
| ⁷Li | 9.375360 (—) | 6.247603 (9 edges) | 7.037598 (10 edges) | 14.682363 (21 edges) | **0.6385** vs E1 0.4255, E2 0.4793 |

The truth sits **strictly between** the cluster edge set and the complete graph, at both
isotopes, in the same direction. That is a real constraint on the A ≥ 6 half — and
**tuning an edge count or an inter-cluster weight to land on it would be a fit**, barred
by (e)(1) of the pre-registration, so it is stated as a bracket and nothing is fitted.

## The structural argument the front asked for is NOT available as posed — and the reason matters

The front asked for a proof that *"a per-block/pairwise functional over `A`
undifferentiated nucleons provably cannot reproduce a non-monotone
`B_AME/B_allpairs`"*. That claim **cannot be proved, because its premise does not hold
of the corpus's model** — flagging this as the arity check AGENTS.md §"Grep the claim
SHAPE" asks for, rather than manufacturing an exclusion:

- `B_allpairs = α[C(Z,2)L_pp + Z·N·L_pn + C(N,2)L_nn]` is **not** over undifferentiated
  nucleons. It is differentiated by `(Z, N)` and carries **three distinct** bond
  constants. It knows ⁶Li has 3 protons and 3 neutrons.
- With `a, b, c` treated as free, the family has three parameters against six data
  points, so no counting argument excludes it; and with them **derived** (as they are)
  there is nothing to exclude — the ratios are simply measured, which is what the
  motivating audit did.
- Non-monotonicity of a *ratio* is not by itself obstructive. The Faddeev–Niemi S1
  argument worked because `cA^p` forces `B/A` strictly monotone; there is no analogous
  forcing here, because `B_allpairs` is quadratic in `A` with `(Z, N)`-dependent
  coefficients and its ratio to `B_AME` is under no monotonicity constraint at all.

What **is** provable, and is proved above, is a statement about the **correction class**
rather than the base class: S-C1 plus R-ii. That is a narrower claim than the one
requested, and it is stated narrowly on purpose.

## What is NOT excluded — stated so the verdict is not over-read

**Cluster structure implemented as a NEW MANY-BODY TERM is untouched by this audit and
remains open in the corpus.** It has a different arity: it adds a term rather than
restricting an edge set, so S-C1 says nothing about it. Specifically still live:

- the **connected-sum / split-union volume-additivity** reading
  ([`alpha_cluster_volume_additivity_probe.py`](../../computations/deltalambda/alpha_cluster_volume_additivity_probe.py),
  ⁸Be validating to +0.16 %) — this is the "connected-sum / satellite decomposition of
  the braid closure" the front asked about, and it **already exists in the corpus**;
- the **SU(4) `[1⁴]` supermultiplet term**, whose gate
  `QOU.MassTheory.su4_supermultiplet_dim_vanishes_iff` (`dim[1^A] = C(4,A)`) is
  Lean-proved and supplies the *categorical origin* of α-clustering — with the
  **magnitude** (~29.8 MeV/α) explicitly still empirical, per
  [`2026-08-02-alpha-cluster-su4-extensive-term.md`](2026-08-02-alpha-cluster-su4-extensive-term.md);
- the **inter-cluster bond term**, whose three zero-freedom hypotheses were already
  reported NEGATIVE in
  [`2026-07-13-inter-cluster-bond-term-derive-or-refute.md`](2026-07-13-inter-cluster-bond-term-derive-or-refute.md),
  leaving the structural finding that the deficit is ~linear in light-cluster nucleon
  count and is *not* a function of bond spin.

Indeed a ≥ 3-body term is what the ⁴He result **points to**: since ⁴He's excess is
invariant under the whole edge-set class and already exceeds the `K_A` pairwise maximum,
whatever carries it is irreducibly many-body. That is the same object §5 of the
motivating audit identified, reached here from a second direction.

## Deuteron

Under C1, ²H = d is a single cluster, so `r(²H) = 0.785282` is **immovable** — clustering
cannot address the one *negative* residual either (`R(²H) = −0.61` MeV, the only
negative one; a non-negative correction fails there by the sum-of-squares sign argument
of [`2026-08-26-faddeev-niemi-qh34-verdict.md`](2026-08-26-faddeev-niemi-qh34-verdict.md) §S2).
The deuteron is held by bean `qou-39bx`; nothing here duplicates it, and no new claim
about it is made.

## Route status, with scope labels

| route | status | scope |
|---|---|---|
| cluster substructure as an **edge-set restriction**, for the residual as a whole | **DEAD** | **(b)** — ⁴He is the α ⇒ single cluster ⇒ `E = K₄` ⇒ ratio invariant; composes with the exact `K_A` Laplacian spectrum result |
| same, for the **A ≥ 6 over-binding only** | **LIVE, over-correcting** — inconclusive under the pre-registered thresholds (best 0.1806, band 0.10–0.25) | **(a)** — scope-limited: this construction, alone, with these derived constants |
| cluster substructure as a **new many-body term** | **UNTESTED here** (out of scope by construction); already **open** in the corpus | — |

## Discipline notes

- `mpmath.mpf` end to end at 60 dps. The production accessor
  `mass_binding_dashboard._bond_type_L` returns **`float`** (it casts at the return), so
  it is **not** used for arithmetic; the identical expression is re-formed in `mpf`. The
  cross-check against the production floats agrees to `|Δ| ≲ 3.5e−17` — **that is the
  limit of the binary64 the production path returns and establishes nothing beyond it**;
  it is not reported as "exact" or "to N digits", and it is stored in the witness as
  `repr()` strings so no raw float64 enters the witness.
- `bash scripts/precision-gates.sh --changed`: **all blocking gates green.**
- **Nothing is newly declared open.** Every open item cited was already open in a
  committed audit or bean. No fit is proposed; no constant is tuned; the isotope set,
  the two schemes, the two edge rules and all four thresholds were fixed before the
  first number was computed, and all four evaluations are reported including the
  disqualified one.
