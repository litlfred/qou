# Bring-embedding magnitude — honest negative (2026-08-01)

**Question (owner method redirect, sharpened).** The S-channel sign flip
`S(muon) > 0 > S(proton)` is derived (disc-5 golden parity `N(φⁿ)=(−1)ⁿ`;
muon = 4₁ = w², proton = Borromean L6a4 = w³; 2/2 anchors,
`qbeta_disc5_parity_probe.py`). The **magnitude** `|S_proton/S_muon| ≈ 4.075`
is unresolved and was shown *not* to be a disc-12 cusp-lattice `G`-ratio (a fit
trap, 1833 chance pairs — [D4]). Owner redirect: embed the whole geometry into
**Bring's genus-4 surface** and let the magnitude fall out as a **Bring period /
X5-weight ratio** of the w²(4₁) vs w³(Borromean) embeddings, **evaluated at the
substrate modulus q₀ ≈ 1.10998**.

**Probe.**
[`computations/qbeta/qbeta_bring_embedding_magnitude_probe.py`](../../computations/qbeta/qbeta_bring_embedding_magnitude_probe.py)
(mpmath, 60 dps, exit 0, 4 assertions). Witness
`qbeta-bring-embedding-magnitude.witness.json`.

## Verdict: clean honest NEGATIVE (a win). Classification: **no-match / structural obstruction**

The owner's Bring-embedding route, taken literally, does **not** resolve the
magnitude. The probe pins down *why*, in four facts.

### [A1] The magnitude IS an anchor-offset ratio, not a period

`S(q) = c₃-target(q) + Vol(4₁)` is **the same function** at both anchors; the
"muon" and "proton" values are two evaluations of `S` at the muon-pinned and
proton-pinned q₀, which differ by only `Δq ≈ 1.28e-8`. Over that gap `S` is
hypersensitive (`dS/dq ≈ 3.84e6`) and **straddles a zero**:

| | value |
|---|---|
| S zero-crossing | `q* = 1.109978593031523` |
| muon anchor offset | `q_muon − q* = +2.52e-9` (S > 0) |
| proton anchor offset | `q_proton − q* = −1.03e-8` (S < 0) |

and the observed magnitude is exactly the ratio of these offsets:

```
|S_proton / S_muon| = 4.07512700  =  |(q_proton − q*)/(q_muon − q*)| = 4.07512449
```

(residual `6.2e-7`, from the tiny local curvature of `S`). The `4.075` is
**q-anchor arithmetic** — where the two substrate pins happen to fall relative to
the S-root — **not** a knot-embedding period.

### [A2] The X5 / Z5 weight is a categorical U(1) phase, not a magnitude

The Bring / X5 identification `xᵏ ↦ w₁ᵏ` (`x5-bring-weight-identification`,
`x5-z5-automorphism.lean`) is, per
[`x5-bring-weight-geometric-content.md`](../../content/quantum-observable-universe/brings-surface/x5-bring-weight-geometric-content.md),
*"categorical, not a morphism of curves … a single U(1) phase tube"*. The Z5
eigenvalue is `ζ₅⁻ᵏ`, of **unit modulus**, so `|ζ₅⁻³|/|ζ₅⁻²| = 1`. A phase
carries no magnitude — the X5 weight structurally cannot be the `4.075` source.

### [A3] The only forced numeric period misses; full battery reported

The SW periods `a_D^{(n)}` (`sw-period-residue-sum.lean`,
`jet-sw-tau-decomposition.lean`) are **abstract ℂ-valued fields with no numeric
realisation**, and their jet degree `n` is a Reeb/vertical order, **not** the
braid winding power. The **only** genuinely forced numeric period of the two
knots is the hyperbolic complex volume. Reported transparently (no cherry-pick):

| candidate (w³/w² datum, evaluated at q₀) | value | miss |
|---|---|---|
| **Vol(Bor)/Vol(4₁) = 8G / (2·Cl₂(π/3))** *(the forced period, q₀-indep)* | 3.6099 | **11.42 %** |
| \|ζ₅⁻³\|/\|ζ₅⁻²\| (X5 phase) | 1.0000 | 75.5 % |
| sinh(3 ln q₀)/sinh(2 ln q₀) | 1.5136 | 62.9 % |
| cosh(3 ln q₀)/cosh(2 ln q₀) | 1.0270 | 74.8 % |
| q₀³/q₀² = q₀ | 1.1100 | 72.8 % |
| sinh(3 lnφ)/sinh(2 lnφ) | 1.7889 | 56.1 % |
| φ³ (golden, n=3) | 4.2361 | 3.95 % |
| L₃/L₂ = 4/3 | 1.3333 | 67.3 % |
| F₃/F₂ = 2 | 2.0000 | 50.9 % |

Best of the whole battery is `φ³` at **3.95 %** — far above the `0.1 %` that would
be evidential, and a post-hoc pattern match, not a forced period. The forced
volume ratio (3.610) misses by 11.4 %.

### [A4] Structural wall — a q₀-evaluated period is smooth ⇒ ≈ identical at both anchors

Evaluating the *same* w³/w² boost datum at each anchor:

```
period(w³/w²) at muon q₀   = 1.5136063241099
period(w³/w²) at proton q₀ = 1.5136063211022
relative spread            = 1.99e-9   (≈ factor 1)
```

A period "evaluated at q₀" is by construction a **smooth** function of q₀; across
the `1.3e-8` anchor gap it changes by `~1e-9`, i.e. a factor ≈ 1. It **cannot**
produce a factor `4.075`. The magnitude lives entirely in the near-zero crossing
of `S` ([A1]) — a property of the c₃/Vol₄₁ function's root location relative to
the anchors — not in any Bring period. This is the **SP1 smoothness wall** of the
coordination doc, restated in the Bring frame: a smooth q₀-quantity is neither
`Im u > Re u` nor hypersensitive.

## What is missing to force a Bring period (per anti-fit discipline)

The corpus embeds 4₁ and Borromean into Σ₄ only via the **genus bound**
`g(K) ≤ 4` (`embeddability-closure.lean`) — an **existence** statement, not a
period-carrying cycle. To force a unique q₀-evaluated period ratio one would need
**both** of:

1. a canonical **homology class / cycle** on Bring's genus-4 Jacobian for each of
   w²(4₁) and w³(Borromean) — the genus bound does not supply one;
2. a **numeric realisation** of the abstract SW periods `a_D^{(n)}`, with the jet
   degree tied to the braid winding power (currently it is not).

Without these, any "period ratio" requires a **free choice** of cycle/winding —
exactly the dense-fit resource the [D4] discipline forbids (cusp shapes dense in
Teichmüller space, Dang–Purcell). No such choice was made here.

## Discipline compliance

Derive-then-check: computed once, no scan for 4.075. Anti-fit: all natural
forced candidates reported, none cherry-picked; the single closest (`φ³`, 3.95 %)
is named as a non-forced coincidence, not adopted. Anti-laundering: no
`SDeformedVolumeChannel` instance fabricated, no `c_k` wired, nothing to
production. The magnitude `|S_p/S_m|` / `u(q₀)` stay **OPEN**.

## Net for the redirect

The Bring-embedding route comes back a **clean negative**: the `4.075` magnitude
is an **anchor-offset artifact near an S-zero**, not a Bring period, and the
corpus does not pin a unique q₀-evaluated period to the w²/w³ embeddings anyway.
The sign result (disc-5 parity, 2/2) stands unaffected. The open frontier is
unchanged: the magnitude belongs to the **hypersensitive near-degeneracy** class
(SP2, `qou-4kr1`) — the anchors' offsets from the S-root — and a *smooth*
q₀-evaluated geometric quantity, Bring-intrinsic or otherwise, structurally
cannot supply it.

## Formalized invariant (the (b) behind the negative)

Per the anti-laundering "prove the invariant that would justify a (b)" rule, the
two structural facts behind this negative are now Lean-proved, sorry-free
(lean-verify exit 0), in
[`QOU/QBeta/SLeakMagnitudeOffsetRatio.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakMagnitudeOffsetRatio.lean):

- **`linear_ratio_slope_independent`** — for the leading-order linearization
  `S(q) = L·(q − q*)` at the simple zero, the ratio `S(qp)/S(qm) = (qp−q*)/(qm−q*)`
  is **independent of the slope `L`**. The "period-like" datum `L` *cancels*, so
  the magnitude carries anchor-placement information only — no period value can be
  read back from it. This is *why* the sign is a stable (q-insensitive) parity
  while the magnitude is q-hypersensitive: they are different data.
- **`smooth_period_excluded_as_magnitude`** — a Lipschitz `P` on the anchor
  interval with variation budget `K·|qp−qm|/|P(qm)| < 1` (any `O(1)` period over
  the `Δq ≈ 1.3e-8` gap) has `|P(qp)/P(qm)| < 2`, so it **cannot** equal the
  observed `|S_p/S_m| ≈ 4.075` (`|r| ≥ 2`). The SP1 smoothness wall, restated as a
  scope-(b) exclusion of *any* smooth q₀-evaluated period as the magnitude source.

Companion to [`QOU/QBeta/SLeakZeroCrossing.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakZeroCrossing.lean),
which proves the sign side (IVT zero-crossing + sign-definite-carrier exclusion).
Together: the sign is an IVT/parity invariant, the magnitude is provably not a
smooth period — both generic, neither takes the anchor values as fitted constants.

## Route A follow-up — the magnitude's symbolic form closed to 1 ppQ (L1)

The negative above says the magnitude is *not a period*; it does **not** say the
magnitude is unexplained. It is fully accounted for as the anchor-offset ratio
near `q*`, and that account can be sharpened from the ~6-digit leading identity to
a **1-ppQ symbolic form** by carrying the Taylor cofactor of `S` at its simple
zero. This is L1 compute precision (an internal cross-check), **not** an L2
observable, and it closes the *symbolic form*, not a closed form for `q*` itself.

**Probe.** [`computations/qbeta/qbeta_magnitude_taylor_qstar_probe.py`](../../computations/qbeta/qbeta_magnitude_taylor_qstar_probe.py)
(mpmath, 60 dps, exit 0, 4 assertions). Witness
`qbeta-magnitude-taylor-qstar.witness.json`. **Derive-then-check:** `q*` is derived
by `findroot` bracketed between the two anchors (opposite S-sign); the Taylor
coefficients `a = ½S''/S'`, `b = (1/6)S'''/S'` by `mpmath.diff`. Nothing is tuned.

Writing `δ = q − q*` and `g(δ) = 1 + a·δ + b·δ² + …` (the normalized cofactor,
`g(0) = 1`), the slope `S'(q*)` cancels and

```
|S_proton/S_muon| = |δ_p/δ_m| · g(δ_p)/g(δ_m).
```

| quantity | value |
|---|---|
| `q*` | `1.1099785930315232884023283427354933150988` |
| `S(q*)` residual | `8.0e-56` (< 1e-40) |
| DIRECT `|S_p/S_m|` | `4.07512700316204532552627382494` |

Residual of the symbolic form vs the direct evaluation, by Taylor order of `g`:

| order | form | residual vs direct |
|---|---|---|
| 0 | offset ratio `|δ_p/δ_m|` | `6.18e-7` (leading, ~6 digits — order of validity) |
| 1 | `1 + aδ` | `1.40e-13` |
| **2** | `1 + aδ + bδ²` | **`3.53e-20` ← first ≤ 1e-15 (1 ppQ)** |
| 3 | `1 + aδ + bδ² + cδ³` | `6.95e-27` |

Each Taylor order adds ~6–7 digits (`δ ~ 1e-8`); the **minimum order reaching
1 ppQ is `N = 2`** (order 1 = `1.4e-13 > 1e-15`).

**Formalized (sorry-free, lean-verify exit 0).**
[`QOU/QBeta/SLeakMagnitudeTaylorRatio.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/SLeakMagnitudeTaylorRatio.lean)
proves the exact algebraic identities the residual table rests on — all generic in
`(S, g, L, q*, q_p, q_m)`, none taking an anchor value or `4.075` as a constant:

- **`exact_ratio_factorization`** — `S(qp)/S(qm) = (qp−q*)/(qm−q*)·g(qp)/g(qm)`;
  the slope `L` cancels *exactly*, sharpening `linear_ratio_slope_independent` from
  the leading (`g ≡ 1`) case to the full cofactor.
- **`offset_ratio_error_is_cofactor`** — closed form of the order-0 residual: the
  leading offset-ratio miss is exactly `(qp−q*)/(qm−q*)·(g(qp)/g(qm) − 1)`.
- **`cofactor_is_normalized_deviation`** / **`linear_model_relative_error`** — `g`
  is the forced deviation `S(qp)/(L(qp−q*))`, and (using `g(q*) = 1`) the linear
  model's relative error is exactly `g(qp) − g(q*)`.

**Scope / what stays open.** Closed: the *symbolic form* of `|S_p/S_m|` to 1 ppQ.
Open: a **closed form for `q*`** (Route B — `q*` is obtained numerically here) and
the **`u(q₀)` map**. Anti-laundering: no `c_k` wired to production, no
`SDeformedVolumeChannel` instance fabricated, no `u(q₀)` claimed. `|S_p/S_m|`
remains an internal cross-check, not a measured prediction.
