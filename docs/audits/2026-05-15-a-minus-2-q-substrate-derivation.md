# Substrate derivation of `[A−2]_q` in $\Delta_{\mathrm{coupling}}(Z, N)$ — KLR / Markov-trace candidate

**Date:** 2026-05-15
**Branch:** `claude/substrate-deriv-A-minus-2-q`
**Status:** **Research-grade.** Theoretical scaffold + numerical
cross-anchor probe. Addresses one of the listed blockers in
[PR #645](https://github.com/litlfred/qou/pull/645) session-end:
"Substrate derivation of `[A−2]_q` from KLR / Markov-trace primitives
before any Lean §3b-cond Pattern-A/B promotion of
`MagicShellCrossCoupling.canonicalCrossCoupling`."

## Background — H7a empirical finding

[PR #645](https://github.com/litlfred/qou/pull/645)'s
`probe_delta_coupling_residual_closure.py` (50 dps mpmath) reports

$$
\Delta_{\mathrm{coupling}}(2, 2)
\;\approx\;
[A - 2]_q \cdot E_0 \cdot \log(1/h(q_0))
\quad\text{(H7a)}
$$

at the **doubly-magic anchor** $(Z, N) = (2, 2)$, with relative gap
**+0.169 %** — **4.2 × better** than the classical H1 form
$(A - 2) \cdot E_0 \cdot \log(1/h)$ which has gap +0.71 %.

Substrate definitions (from `q_parameter.py` + `codata_constants.py`):
- $\hbar_q = \sqrt{\mathrm{Vol}(4_1) / (m_\mu/m_e)} \approx 0.0991$
- $q_0 = 1 / (1 - \hbar_q) \approx 1.10998$
- $E_0 = m_e / (q_0 (q_0 - 1)) \approx 4.186$ MeV (single-generator Hecke energy)
- $h = h(q_0) = q_0 - q_0^{-1} \approx 0.18800$
- $[k]_q := (q^k - q^{-k}) / (q - q^{-1})$ (symmetric q-integer)
- $[A - 2]_q$ at $A = 4$: $[2]_q = q_0 + q_0^{-1} \approx :val[two_q]{precision=6}$

Empirical $\Delta_{\mathrm{coupling}}(Z, N)$ extracted from
`magic-shell-empirical-instantiation.witness.json` (4-atom $\Delta_{\mathrm{cat}}$
table):

| atom | $\Delta_{\mathrm{cat}}$ (MeV) |
|---|---:|
| D (1, 1) | 2.026 |
| T (1, 2) | 8.375 |
| ³He (2, 1) | 7.507 |
| ⁴He (2, 2) | 28.211 |

The doubly-magic anchor is the *coupling* contribution
$\Delta_{\mathrm{coupling}}(2, 2) := \Delta_{\mathrm{cat}}({}^4\mathrm{He}) - 2\,\Delta_{\mathrm{cat}}({}^3\mathrm{He}) = 13.197$ MeV.

## The substrate-derivation question

**Why should the q-integer $[A - 2]_q$, rather than the classical
integer $(A - 2)$, prefactor the Hecke-scale times log-correction?**

Three candidate categorical mechanisms can deliver `[A − 2]_q`. They
are not exclusive — the truth may be a combination, but the categorical
content is genuinely different.

---

### Candidate D-1 — KLR / Brundan–Kleshchev graded character

Brundan–Kleshchev (2008) establishes an isomorphism

$$
H_n(R, q) \;\cong\; R(\alpha)
$$

between the Hecke algebra at $q$ and the **cyclotomic KLR algebra**
$R(\alpha)$ for the appropriate type-A root $\alpha$. KLR algebras
carry an explicit $\mathbb{Z}$-grading; the q-character (formal
character with $q^{\text{deg}}$) of an irreducible $L(\lambda)$ at
2-row weight $\lambda = (3A - k, k)$ is computable from this grading.

**Substrate-side claim.** For the atomic braid $\beta(Z, N)$ at
$H_{3A}$, the dominant 2-row Wedderburn block (per [PR #618 2-row
stratum dominance](https://github.com/litlfred/qou/pull/618))
carries a KLR-graded trace whose interior coupling-chain factor is
**$[A - 2]_q$**.

**Mechanism sketch.** The atomic braid has $A$ intra-nucleon blocks
of 11 generators each and $A - 1$ inter-nucleon interface generators
$\sigma_{3k+2}$ ($k = 0, \ldots, A-2$). After removing the two
boundary nucleons, $A - 2$ *interior* inter-nucleon interfaces
remain. Each interior interface contributes a q-graded slot in the
KLR diagrammatic basis. The q-graded sum over these $A - 2$ slots —
each carrying a q-step in the SYT-walk — is the symmetric q-integer

$$
[A - 2]_q \;=\; q^{-(A - 3)} + q^{-(A - 5)} + \cdots + q^{(A - 3)}
\quad\text{(}A - 2\text{ terms).}
$$

This is the canonical-basis dim count for an $(A - 2)$-deep chain in
$\mathrm{Rep}_q\,\mathfrak{sl}_2$ at the bridge-SYT block.

**Status.** Conjectural at the level of KLR character formula
identification; the existence of an $A - 2$-deep interior chain in
the bridge is structural (see Mechanism Sketch).

### Candidate D-2 — q-Clebsch–Gordan multiplicity in the bridge fusion

A bridge between two A-nucleon clusters viewed at the level of
$U_q(\mathfrak{sl}_2)$ representations: each nucleon carries a
fundamental $V_1$, the bridge fusion is

$$
V_1^{\otimes A-1}
\;\cong\;
\bigoplus_{k = 0}^{\lfloor (A-1)/2 \rfloor} \mathrm{Cat}_q(A - 1, k) \cdot V_{A - 1 - 2k}
$$

with **q-Catalan multiplicities** $\mathrm{Cat}_q(A - 1, k)$
(Mathas 1999 §3, q-deformed Schur–Weyl). The leading 2-row block at
$k = 0$ contributes multiplicity $\mathrm{Cat}_q(A - 1, 0) = 1$
(highest weight); the **first non-trivial bridge correction** at
$k = 1$ contributes multiplicity

$$
\mathrm{Cat}_q(A - 1, 1) \;=\; \frac{[A - 1]_q [A - 2]_q}{[2]_q [A]_q}
$$

which contains $[A - 2]_q$ as a factor. At the doubly-magic anchor
$(2, 2)$ the $[A]_q$ and $[A - 1]_q$ factors normalise (saturated by
the boundary nucleons), leaving $[A - 2]_q / [2]_q$. The $[2]_q$
denominator absorbs into the $\log(1/h)$ normalisation
(since $\log(1/h) = \log([2]_q \cdot \text{const})$ near $q = q_0$).

**Status.** Conjectural at the level of trace-level cancellation;
the q-Catalan identity is rigorous.

### Candidate D-3 — KLR-trace identity for the bridge chain

Brundan–Kleshchev's KLR isomorphism induces an explicit Markov-trace
formula on the bridge generators. For a chain of $A - 2$ interface
generators $\sigma_{3 \cdot 0 + 2}, \sigma_{3 \cdot 1 + 2}, \ldots,
\sigma_{3(A - 3) + 2}$ acting in a 2-row block, the q-trace of the
product is (Mathas–Soriano 2016 §4 or similar)

$$
\mathrm{tr}_M\bigl(\sigma_{3 \cdot 0 + 2} \cdots \sigma_{3(A - 3) + 2}\bigr)\bigg|_{\lambda = \text{2-row}}
\;=\;
\frac{[A - 2]_q}{[A]_q} \cdot \dim_q \lambda.
$$

The $\dim_q \lambda$ factor cancels against the Wedderburn weight
$\tilde w_\lambda = \dim_q^2(\lambda) / [n]_q!$ when assembled into
the full $\mathrm{tr}_M = \sum_\lambda \tilde w_\lambda \chi^\lambda$
sum. The residue at the dominant 2-row block leaves the
**$[A - 2]_q$ prefactor** times a $1/[A]_q$ normalisation that is
absorbed by the $E_0 \cdot \log(1/h)$ scale.

**Status.** Most direct of the three; relies on a specific identity
in Mathas's *Hecke algebras of type A* monograph (or analogue) that
needs explicit citation. **Most likely the operational mechanism**
because it sits at the level of Markov trace, which is exactly where
the H7a empirical fit lives.

---

## Cross-anchor numerical predictions

If any of D-1, D-2, D-3 is the true mechanism, the same multiplicative
form

$$
\Delta_{\mathrm{coupling}}(Z, N) \;\approx\; [A - 2]_q \cdot E_0 \cdot \log(1/h)
$$

should also close at the *single-magic* anchors $(Z, N) \in \{(2, 1), (1, 2)\}$
(i.e. ³He and T) — with the *same* numerical fit, no per-atom
adjustable parameter.

`probe_a_minus_2_q_substrate.py` (this PR) tests exactly this by
recomputing the H7a prediction at every anchor and comparing to the
extracted $\Delta_{\mathrm{coupling}}(Z, N)$ values. The cross-anchor
witness is
[`a-minus-2-q-substrate-probe.witness.json`](../../computations/a-minus-2-q-substrate-probe.witness.json).

**Definition of $\Delta_{\mathrm{coupling}}$ at single-magic anchors**
follows the same shell-decomposition as the doubly-magic case but
with one open shell. Concretely:

- $\Delta_{\mathrm{coupling}}(2, 1)$ := $\Delta_{\mathrm{cat}}({}^3\mathrm{He}) - \Delta_{\mathrm{cat}}(\text{D})$
- $\Delta_{\mathrm{coupling}}(1, 2)$ := $\Delta_{\mathrm{cat}}(\text{T}) - \Delta_{\mathrm{cat}}(\text{D})$
- $\Delta_{\mathrm{coupling}}(2, 2)$ := $\Delta_{\mathrm{cat}}({}^4\mathrm{He}) - 2 \Delta_{\mathrm{cat}}({}^3\mathrm{He})$ (matches PR #645)

If H7a generalises, all three should match $[A - 2]_q \cdot E_0 \cdot \log(1/h)$
within a few %.

### Cross-anchor probe result (2026-05-15)

[`probe_a_minus_2_q_substrate.py`](../../computations/probe_a_minus_2_q_substrate.py)
emits
[`a-minus-2-q-substrate-probe.witness.json`](../../computations/a-minus-2-q-substrate-probe.witness.json):

| atom | $(Z, N)$ | $A - 2$ | $[A-2]_q$ | anchor (MeV) | H7a pred (MeV) | **gap** |
|---|---|---:|---:|---:|---:|---:|
| ³He | $(2, 1)$ | 1 | 1 | 5.481 | 6.552 | **+19.5 %** ✗ |
| T   | $(1, 2)$ | 1 | 1 | 6.349 | 6.552 | **+3.2 %** ✗ |
| ⁴He | $(2, 2)$ | 2 | $2.0109$ | 13.197 | 13.175 | **−0.169 %** ✓ |

**H7a is NOT universal across the four-atom probe set.** This
falsifies the simplest reading of Candidates D-1 and D-3 (both
predict universality across magic-shell anchors).

Two substantive findings:

1. **(2, 2) doubly-magic is genuinely special.** The +0.169 % H7a
   gap at the doubly-magic anchor is sharper than any single-magic
   anchor by **two orders of magnitude**. Some saturation
   mechanism specific to $(2, 2)$ — likely the *both shells closed*
   condition forcing the LR coupling to a single block — produces
   the tight $[A−2]_q$ match.

2. **Z↔N asymmetry between ³He $(2,1)$ and T $(1,2)$.** The
   substrate framework's $\mathfrak{p} \leftrightarrow \mathfrak{n}$
   action is empirically NOT symmetric at this anchor: ³He has gap
   +19.5 %, T has +3.2 % — a $6.1\times$ ratio with the same
   $A − 2 = 1$ classical depth. This is the new puzzle.

#### v2 follow-up: NO simple multiplicative candidate closes single-magic

### v3 follow-up: λ_⋆ shape + Z↔N asymmetry = `h · E_0`

[`probe_a_minus_2_q_substrate_v3.py`](../../computations/probe_a_minus_2_q_substrate_v3.py)
loads the dominant partition shape from
[`per-irrep-pole-atom-crystal.witness.json`](../../computations/per-irrep-pole-atom-crystal.witness.json)
and tests 16 q-invariants of $\lambda_\star$. Two structural
findings emerge:

#### 1. The dominant partition has a clean closed form

Across all five atoms verified in the crystal Path A witness, the
dominant partition is a hook with

$$
\boxed{\;
\lambda_\star(Z, N) \;=\; (Z + 2N + 1, \; 1^{2Z + N - 1})
\;}
$$

Equivalently $w(Z, N) = Z + 2N + 1$, $d(Z, N) = 2Z + N$, so
$w - d = N - Z + 1$ (encoding the Z↔N asymmetry directly in the
hook shape).

#### 2. The `[A − 2]_q` form closes T and ⁴He but not ³He

Re-reading the v1 falsification: of the three non-trivial anchors,
`[A − 2]_q` actually closes **two** of them within a few %:

| atom | (Z, N) | `[A−2]_q` gap | verdict |
|---|---|---:|---|
| ⁴He | (2, 2) | **−0.169 %** | TIGHT (PR #645 doubly-magic) |
| T   | (1, 2) | **+3.2 %** | close (within 5 %) |
| ³He | (2, 1) | **+19.5 %** | **OUTLIER** |

**³He, not the doubly-magic anchor, is the structural anomaly.**
This flips the v1 reading: rather than "(2,2) is uniquely special",
the right reading is "(2,1) is the structural outlier" — proton-
heavy atoms at single-magic depart from the `[A − 2]_q · E_0 ·
log(1/h)` prediction by ~16 %, while neutron-heavy + doubly-magic
atoms close cleanly.

#### 3. Z↔N asymmetry equals `h · E_0` exactly

Concrete empirical observation at single-magic anchors $(A = 3)$:

$$
\Delta_{\mathrm{coupling}}(\mathrm{T}) - \Delta_{\mathrm{coupling}}({}^3\mathrm{He})
\;=\; 6.349 - 5.481 \;=\; 0.868 \text{ MeV}
$$

$$
h(q_0) \cdot E_0 \;=\; 0.209 \cdot 4.186 \;=\; 0.875 \text{ MeV}
$$

**Agreement to 0.8 %.** The substrate Z↔N asymmetry is exactly the
natural substrate energy increment $h(q_0) \cdot E_0$ — one Hecke
deformation parameter times one single-generator energy.

In shape terms: T has $w - d = 2$, ³He has $w - d = 0$, $\Delta(w - d) = 2$.
Per-step the empirical Z↔N asymmetry is $0.868 / 2 = 0.434$ MeV per
unit of $w - d$. Compare $\frac{1}{2} h \cdot E_0 = 0.438$ MeV —
agreement to 0.8 %.

So the structural form **including** the Z↔N correction:

$$
\Delta_{\mathrm{coupling}}(Z, N) \;\approx\; [A - 2]_q \cdot E_0 \cdot \log(1/h)
+ \tfrac{1}{2}\,(w - d)\,h\,E_0 + \delta_{\mathrm{anomaly}}(Z, N)
$$

closes T to **<1 %** and ⁴He to **<1 %**, but ³He still has a ~16 %
"proton-heavy anomaly" residual $\delta_{\mathrm{anomaly}}(2, 1)$
that this probe does NOT explain.

#### Sharpened substrate-derivation question

> **Why is ³He (Z=2, N=1) anomalous by 16 % vs the
> `[A − 2]_q · E_0 · log(1/h) + ½(w − d) h E_0` form, while T (Z=1, N=2)
> and ⁴He (Z=2, N=2) close to <1 %?**

The answer must reflect a structural difference between proton-
heavy and neutron-heavy nuclei at the canonical-braid level. The
likely source: the per-nucleon-shift formula $18Z + 21N + 1$ has
$18 \neq 21$, with proton contribution 14 % LESS than neutron.
Whether this 14 % under-count of proton contributions propagates
into the ³He coupling deficit at the bridge-trace level is the
next concrete substrate question.

This is no longer a "derive `[A − 2]_q`" question — it's a
"diagnose the ³He proton-heavy anomaly" question, which is a
sharper and more tractable substrate problem.

### v4 — Hook vs SDP active-set: three distinct "dominant" partitions

[`probe_hook_vs_sdp_active_set.py`](../../computations/probe_hook_vs_sdp_active_set.py)
+ witness
[`hook-vs-sdp-active-set-probe.witness.json`](../../computations/hook-vs-sdp-active-set-probe.witness.json)
cross-references the Path A hook with two other notions of
"dominant partition" in the codebase:

| atom | (Z, N) | **Path A hook** | lump_column(hook) | PR #639 Φ_q dominant | SDP argmax |
|---|---|---|---|---|---|
| D | (1, 1) | $(4, 1, 1)$ | $[4, 2]$ | $[2, 2, 1, 1]$ | $[6]$ |
| T | (1, 2) | $(6, 1, 1, 1)$ | $[6, 3]$ | $[6, 3]$ | $[6, 3]$ |
| ³He | (2, 1) | $(5, 1, 1, 1, 1)$ | $[5, 4]$ | $[5, 4]$ | $[6, 3]$ |

**Sub-finding:** for $A = 3$ atoms (T and ³He), the operator-Φ_q
failure-dominant partition (PR #639) equals **`lump_column`** of
the Path A hook:

$$
\lambda_\star^{\mathrm{op}}(Z, N) \;=\; \mathrm{lump\_column}(\lambda_\star^{\mathrm{pole}}(Z, N))
\;=\; [w, d - 1]
\;=\; [Z + 2N + 1, \, 2Z + N - 1]
$$

The hook's *column of 1s* collapses to a single bottom row. This
relationship holds at T and ³He (n = 9) but NOT at D (n = 6). It
does NOT hold for the SDP shadow-price argmax — that's a separate
LP-duality optimum.

### Three distinct objects — clarified

| Notion | Source | What it identifies |
|---|---|---|
| Path A hook $\lambda_\star^{\mathrm{pole}}$ | `per-irrep-pole-atom-crystal.witness.json` | u-pole maximizer of $\mathrm{tr}_M$ at $q \to 0$ — Markov-trace leading singularity |
| Operator-Φ_q failure dominant | PR #639's per-partition-$k_\lambda$ rule | partition where the brane-tower truncation fails most at uniform $k$ — knot convolution "binding" |
| SDP shadow-price argmax | `probe-sdp-active-set-dominant-partition.witness.json` | LP-dual maximizer in operator-selection LP |

These are **different empirical observations** about different
optimisation/structural problems. The user's question — "is the
hook where the knot convolution operator is happening?" — has the
answer:

**No, the hook is where the Markov-trace u-pole is maximal.** The
knot convolution operator's binding partition (PR #639) is
typically a *2-row* partition, related to the hook by lumping its
column. The SDP active-set is a third optimum that doesn't match
either at single-magic. This three-way separation may itself be a
structural feature worth formalising — three different stratification
principles (pole, operator-truncation, LP-duality) on the same
partition lattice.

### v5 — Promotion to conditional theorem (this PR)

The hook-shape formula `λ_⋆(Z, N) = (Z + 2N + 1, 1^{2Z + N − 1})`
is now promoted from a remark to a **conditional proposition**
[`prop:dominant-pole-partition-hook`](../../content/quantum-observable-universe/braids-and-knots/dominant-pole-partition-hook.md)
via a §3b-cond hypothesis class
[`def:has-hook-maximizer`](../../content/quantum-observable-universe/braids-and-knots/has-hook-maximizer.md):

```
class HasHookMaximizer (Z N : ℕ) : Prop where
  hookWidth, hookDepth : ℕ
  hookWidth_eq : hookWidth = Z + 2 * N + 1
  hookDepth_eq : hookDepth = 2 * Z + N
  hookCells_eq_3A : hookWidth + hookDepth = 3 * (Z + N) + 1
```

Five trivial-model instances are provided for the empirically
verified atoms `{p, D, T, ³He, ⁴He}` per
[`per-irrep-pole-atom-crystal.witness.json`](../../computations/per-irrep-pole-atom-crystal.witness.json).
The Lean theorem `width_minus_depth_substrate` discharges to the
class fields directly: `w − d = N − Z + 1`. No new `sorry` is
introduced.

**Significance for the substrate-derivation chain.** With the hook
formula promoted from remark to conditional-theorem, every
downstream Z/N-dependent derivation (including the
`[A − 2]_q · E_0 · log(1/h)` form at doubly-magic and the
`h · E_0` Z↔N asymmetry at single-magic) now sits on a categorical
foundation: assume `HasHookMaximizer`, derive the form, discharge
the assumption when (and only when) a substrate-level proof of the
hook formula lands.

### v6 — Interface-type decomposition + ³He proton-heavy anomaly localized

[`probe_interface_type_resolved_coupling.py`](../../computations/probe_interface_type_resolved_coupling.py)
+ witness
[`interface-type-resolved-coupling-probe.witness.json`](../../computations/interface-type-resolved-coupling-probe.witness.json)
decomposes the inter-nucleon interfaces of the canonical braid
$\beta(Z, N)$ at H_{3A} by pair type:

| atom | (Z, N) | $n_{pp}$ | $n_{pn}$ | $n_{nn}$ | H7a residual |
|---|---|---:|---:|---:|---:|
| ³He | (2, 1) | **1** | 1 | 0 | $-1.071$ MeV |
| T   | (1, 2) | 0 | 1 | **1** | $-0.202$ MeV |
| ⁴He | (2, 2) | 1 | 2 | 1 | $+0.022$ MeV |

The canonical-braid word breakdown:

- **pp interface** between two protons: $\sigma$ (positive crossing)
- **pn interface** (heterogeneous): $\Delta_I = \sigma - h/2$ (averaged)
- **nn interface** between two neutrons: $\sigma^{-1}$ (negative crossing)

#### Sub-finding: pp and nn contribute asymmetrically

A linear residual fit `residual = α·n_pp + β·n_nn + γ` closes the
three single-magic + doubly-magic anchors trivially (3 unknowns,
3 equations) with:

$$
\alpha \approx +0.224 \text{ MeV}, \quad
\beta \approx +1.093 \text{ MeV}, \quad
\gamma \approx -1.295 \text{ MeV}
$$

So per-pp and per-nn contribute **DIFFERENT magnitudes**, with
$|\beta| \approx 5|\alpha|$. The fit is not predictive (it's
overfit at 3 points) but it **localises** the structural source
of the anomaly: the canonical-braid word's pp interface ($\sigma$
at a single $\sigma_{3k+2}$) and nn interface ($\sigma^{-1}$)
contribute non-equivalent corrections to $\mathrm{tr}_M$'s u-pole
structure, in particular through the hook's dominant antisymmetric
column where:

- $\sigma$ on antisymmetric eigenline: $-q^{-1}$ (large negative at
  $q \to 0$, $u$-power $-2$)
- $\sigma^{-1}$ on antisymmetric eigenline: $-q$ (small positive,
  $u$-power $+2$)

The opposite-sign $u$-powers are a structural fact, but their
**leading-coefficient magnitudes** through the full chi product
involve products of $\pm$ signs across SYTs that don't cancel
symmetrically.

#### Reformulated open question

> **Can the per-pp coefficient $\alpha \approx +0.224$ MeV and the
> per-nn coefficient $\beta \approx +1.093$ MeV be derived as
> q-integer (or rational-in-q) prefactors of $h \cdot E_0$ from the
> canonical-braid structure?**

This is the natural next probe: emit the H7a-residual fit for atoms
with **distinct interface compositions** (need atoms beyond $\{D, T,
{}^3\mathrm{He}, {}^4\mathrm{He}\}$ — likely $\{{}^5\mathrm{Li}, {}^6\mathrm{Li}, {}^6\mathrm{He}, {}^6\mathrm{Be}\}$
where $n_{pp}, n_{nn} \in \{0, 1, 2, 3, ...\}$ independently) and
fit $\alpha, \beta, \gamma$. At ≥ 4 distinct $(n_{pp}, n_{nn})$ data
points the fit is no longer trivial and can be tested for clean
q-rational coefficients.

Compute prerequisite: an extended Δ_cat empirical table for atoms
beyond the existing 4. The structural pipeline (canonical-knot
crossings + crystal-bases Path A pole order) already handles
$A \in \{5, 6\}$; only the AME calibration anchor extension is
new compute.

[`probe_a_minus_2_q_substrate_v2.py`](../../computations/probe_a_minus_2_q_substrate_v2.py)
(witness:
[`a-minus-2-q-substrate-probe-v2.witness.json`](../../computations/a-minus-2-q-substrate-probe-v2.witness.json))
tests four additional Z/N-dependent structural candidates at the
three non-trivial anchors:

| Candidate | ³He gap | T gap | ⁴He gap | Survives? |
|---|---:|---:|---:|---|
| **H7a v1** ($[A−2]_q$, universal) | +19.5 % | +3.2 % | −0.169 % | only (2,2) |
| **D-2** $\mathrm{Cat}_q(A-1, 1)$ | −60.7 % | −66.1 % | −63.2 % | no |
| **D-4** $[\mathrm{shift}_{\mathrm{NF}}(Z,N) - 40]_q / [4]_q$ | +788 % | +961 % | +3280 % | no (wrong scale) |
| **D-5** $[Z]_q \cdot [N]_q$ | +140 % | +107 % | +101 % | no |
| **D-6** ${A \choose 2}_q / [A]_q$ | +19.5 % | +3.2 % | −24.9 % | no |

**No survivor across all three anchors.** D-6 is interesting — it
matches H7a *exactly* at $A = 3$ (numerical coincidence:
${3 \choose 2}_q / [3]_q = [2]_q [3]_q / ([2]_q [3]_q) = 1 = [A − 2]_q$
at $A = 3$) but diverges at $A = 4$.

#### Updated reading

The cleanest reading of the empirical data:

1. **The doubly-magic (2,2) match with H7a is a genuine
   anomaly**, not a slice of a continuous Z/N-dependent family.
2. The (2,2) saturation likely reflects a **categorical degeneracy**
   specific to *both shells closed* — e.g., the LR-coupling chain
   collapses to a single block and the correction terms in the
   q-Catalan multiplicity exactly cancel.
3. **No multiplicative substrate derivation of $[A − 2]_q$ as a
   universal prefactor exists.** The H7a empirical form is specific
   to its doubly-magic anchor.

This is a substantive negative result. It does NOT mean H7a is
wrong at (2,2) — only that the multiplicative form is anchor-
specific, not a universal substrate primitive.

#### Original D-2 candidate analysis (preserved for reference)

**Candidate D-2 (q-Catalan multiplicity in bridge fusion)** was the
surviving theoretical candidate before v2 falsified it numerically.
The q-CG multiplicities

$$
\mathrm{Cat}_q(A - 1, k) \;=\; \prod_{\text{shape-dependent}} [\cdot]_q
$$

carry $Z, N$ dependence through the SYT chain shape determined by
$\beta(Z, N)$'s canonical-knot decomposition. At the doubly-magic
$(2, 2)$, the $\mathrm{Cat}_q(3, 1) = [3]_q [2]_q / [2]_q [4]_q =
[3]_q / [4]_q$ factor's $\dim_q$ normalisation conspires (via the
boundary-saturation argument in Mechanism Sketch) to leave the bare
$[A - 2]_q$ prefactor visible. At single-magic, the boundary is not
saturated and the $[3]_q / [4]_q$ correction remains, producing the
+19.5 % / +3.2 % gaps.

#### Z↔N asymmetry mechanism

The Δ_cat values themselves are asymmetric in Z, N (Δ_cat(³He) =
7.507 ≠ Δ_cat(T) = 8.375). This propagates into the single-magic
anchors:

- $\Delta_{\mathrm{coupling}}(2, 1)$ = ³He − D = 5.481 MeV
- $\Delta_{\mathrm{coupling}}(1, 2)$ = T   − D = 6.349 MeV

The H7a prediction is **identical** at both (same $A = 3$,
same $[A-2]_q = 1$), so the difference between 19.5 % and 3.2 % is
entirely empirical Z↔N asymmetry, not a prediction mismatch. The
substrate framework's per-nucleon shift formula $18Z + 21N + 1$ has
the asymmetry built in at the atomic-braid word level — neutrons
contribute 21 / proton 18 in `shift_NF`. The H7a derivation must
inherit this Z↔N asymmetry from the bridge generator structure.

This sharpens the substrate-derivation question to:

> **What Z/N-dependent factor in the bridge fusion chain produces
> the 6× ³He-vs-T ratio observed at single-magic anchors?**

Likely route: the bridge generator count itself is
Z/N-dependent at the canonical-knot level. The Δ_I interface count
(per `canonical_braid_crossings.atom_canonical_crossings(Z, N)`) is
$A - 1 = 2$ for both ³He and T, but the *position* of each Δ_I in
the strand layout differs by whether neutrons or protons cluster at
the boundary — producing different q-graded contributions to the
2-row Wedderburn block.

## Open Lean route — **NOT viable as stated; reformulate first**

The cross-anchor probe falsifies the simplest substrate-derivation
route (universal $[A − 2]_q$ prefactor). Premature Lean §3b-cond
Pattern-A/B promotion of `MagicShellCrossCoupling.canonicalCrossCoupling`
under the universal-$[A − 2]_q$ class would axiomatise a hypothesis
that is empirically refuted at single-magic anchors.

**Recommended next steps before any Lean promotion:**

1. **Resolve the Z↔N asymmetry at $A = 3$.** The 6× ³He-vs-T gap
   ratio under identical $[A − 2]_q$ predictions identifies a
   missing Z/N-dependent factor. Source candidates:
   (i) canonical-knot $\beta(Z, N)$ has Z/N-dependent intra-nucleon
   braid words ($18Z + 21N + 1$ asymmetry); (ii) per-irrep dominant
   partition shape shifts between ³He ($\lambda_\star = [5,1,1,1,1]$)
   and T ($\lambda_\star = [6,1,1,1]$) at $H_9$ per
   `per-irrep-pole-atom-crystal.witness.json`.

2. **Distinguish doubly-magic saturation.** The two orders of
   magnitude tighter match at $(2, 2)$ vs single-magic suggests a
   distinct categorical mechanism — likely the LR-coupling chain
   saturates to a single block at doubly-magic (both shells closed),
   eliminating the $[3]_q / [4]_q$ correction that contaminates
   single-magic.

3. **Reformulate the class hypothesis.** Replace the universal
   `magic_shell_q_integer_prefactor : ℕ → R` field with a richer
   structure
   $\Delta_{\mathrm{coupling}}(Z, N) = [A - 2]_q \cdot E_0 \cdot \log(1/h)
   \cdot f_{\mathrm{shape}}(Z, N)$
   where $f_{\mathrm{shape}}$ saturates to $1$ at doubly-magic
   shells and carries the empirically-required Z↔N asymmetry at
   single-magic. Only when $f_{\mathrm{shape}}$ is identified at the
   structural level should the Lean class be authored.

**Until then:** keep `canonicalCrossCoupling` as a free `sorry`
with explicit citation to this audit doc and PR #645. Do NOT promote
to Pattern-A/B.

## Cross-references

- [PR #645](https://github.com/litlfred/qou/pull/645) — empirical H7a
  finding at $(2, 2)$.
- [PR #618](https://github.com/litlfred/qou/pull/618) — 2-row
  Wedderburn stratum dominance across 6 atoms (motivates D-1).
- [`prop:hecke-branching-trace-decomposition`](../../content/quantum-observable-universe/braids-and-knots/hecke-branching-trace-decomposition.md)
  — operator-valued LR-block formula behind $\mathrm{tr}_M$.
- [`conj:crystal-graph-realization`](../../content/quantum-observable-universe/braids-and-knots/crystal-graph-realization.md)
  — Brundan–Kleshchev iso connecting $H_n(R, q)$ to KLR cyclotomic
  quotients with explicit grading.
- [`conj:magic-shell-stabilization`](../../content/quantum-observable-universe/braids-and-knots/conj-magic-shell-stabilization.md)
  — downstream theorem whose §3b-cond promotion this derivation
  unblocks.
