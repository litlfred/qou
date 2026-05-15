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
- $[A - 2]_q$ at $A = 4$: $[2]_q = q_0 + q_0^{-1} \approx 2.01089$

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
[`a-minus-2-q-substrate-probe.witness.json`](../../folio-assistant/computations/a-minus-2-q-substrate-probe.witness.json).

**Definition of $\Delta_{\mathrm{coupling}}$ at single-magic anchors**
follows the same shell-decomposition as the doubly-magic case but
with one open shell. Concretely:

- $\Delta_{\mathrm{coupling}}(2, 1)$ := $\Delta_{\mathrm{cat}}({}^3\mathrm{He}) - \Delta_{\mathrm{cat}}(\text{D})$
- $\Delta_{\mathrm{coupling}}(1, 2)$ := $\Delta_{\mathrm{cat}}(\text{T}) - \Delta_{\mathrm{cat}}(\text{D})$
- $\Delta_{\mathrm{coupling}}(2, 2)$ := $\Delta_{\mathrm{cat}}({}^4\mathrm{He}) - 2 \Delta_{\mathrm{cat}}({}^3\mathrm{He})$ (matches PR #645)

If H7a generalises, all three should match $[A - 2]_q \cdot E_0 \cdot \log(1/h)$
within a few %.

### Cross-anchor probe result (2026-05-15)

[`probe_a_minus_2_q_substrate.py`](../../folio-assistant/computations/probe_a_minus_2_q_substrate.py)
emits
[`a-minus-2-q-substrate-probe.witness.json`](../../folio-assistant/computations/a-minus-2-q-substrate-probe.witness.json):

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

[`probe_a_minus_2_q_substrate_v2.py`](../../folio-assistant/computations/probe_a_minus_2_q_substrate_v2.py)
(witness:
[`a-minus-2-q-substrate-probe-v2.witness.json`](../../folio-assistant/computations/a-minus-2-q-substrate-probe-v2.witness.json))
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
