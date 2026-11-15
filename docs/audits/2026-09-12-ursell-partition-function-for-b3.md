# The partition function behind the corpus $b_3$ — and its sign is Mayer's

> **2026-11-15 scoping note.** The magnitudes below are computed on the single-crossing interface letters of `atom_braid_word_3A`, which the γγ rule (owner, 2026-11-15) no longer treats as canonical. They stay as a record. The Lean theorems take generic bond weights and still stand. See [`2026-11-15-gg-rule-rescopes-old-letter-binding.md`](2026-11-15-gg-rule-rescopes-old-letter-binding.md).

**Date.** 2026-09-12
**Bean.** `qou-rwhv` (the one undone step of the 2026-08-30 arc); parent `qou-brng`.
**Scope.** **(a)** for the identification and the letter measurement; **(b)** for the
sign, invariant named in §4.
**Lean.** [`QOU/MassTheory/UrsellPartitionFunctionB3.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/UrsellPartitionFunctionB3.lean)
— `lean -DautoImplicit=false -s 65536` exit 0 against the restored
`lake-cache/qou-v4-24-0` (head `a792c46d01b`); `#print axioms` on all 13
declarations: `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`.
**Probe.** [`computations/probes/ursell_partition_function_for_b3_probe.py`](../../computations/probes/ursell_partition_function_for_b3_probe.py)
→ `ursell-partition-function-for-b3.witness.json`, **11/11**; exact `Fraction`
+ `sympy` where the claim is algebraic, 200-bit MPFR (`_exact_trace_engine`,
proton pin `Q_50_DIGIT_STR`, convention D) where it is numerical.
**Source.** Jansen & Kolesnikov, J. Stat. Phys. **189**:33 (2022),
`library/s10955-022-02992-6/`, p. 5 (definitions), §3.1 (alternation).

---

## 0. The question, and the one-line answer

`qou-rwhv` §"What would settle it": *exhibit the polymer / cluster model whose
activity expansion has the corpus's $b_3$ as its third Ursell coefficient —
name the polymer set, the weight, the compatibility relation, the ensemble.*

**It exists, it is the obvious one, and exhibiting it reverses the 2026-08-30
sign reading.** The corpus's $b_3$ is (minus) the third Ursell coefficient of a
hard-core lattice gas on the nucleon sites with the interface-letter traces as
pair weights. The Mayer expansion of the log-derived binding carries
$-\varphi^T_n$ at **every** order, so the corpus's negative $b_3$ is the
classical sign, not a missing $(-1)^{n-1}$. Restoring that factor is exactly the
same expansion at **negative activity**.

## 1. The partition function

| item | value |
|---|---|
| polymer set | the nucleons $i \in S$ of one fixed nucleus (sites) |
| activity | $z_i$ per site, **hard core** ($z_i^2 = 0$: each nucleon present at most once) |
| pair weight | $\mu_e = z_D + d_e$, the trace of the interface letter on bond $e$: $\mu_{pp} = 0.61269$, $\mu_{pn} = 0.50823$, $\mu_{nn} = 0.40363$ |
| Mayer variable | $g_e = \mu_e - 1 \in (-1, 0)$ |
| compatibility | the Mayer graph expansion on the bond set of the word (the chain, in production) |
| ensemble | **grand canonical over the sub-clusters** $T \subseteq S$ of the fixed nucleus |

$$
\Xi_S(z) = \sum_{T \subseteq S} z^T Z_T, \qquad
Z_T = \prod_{e \subseteq T} \mu_e = \frac{\mathrm{tr}_M(W_{\text{atom}}(T))}{\mathrm{tr}_M(W_{\text{free}}(T))}.
$$

The second equality is connected-sum multiplicativity of the Markov trace
(`QOU.MathlibExt.MonotoneWordFactorizes.tr_stabWord_eq_prod_tr`), **re-measured
on the live alternating-core word** (post 2026-09-05, `E.nucleon_word`), proton
pin, convention D:

| atom | $n$ | $Z_S = \mathrm{tr}(\text{atom})/\mathrm{tr}(\text{free})$ | $\prod \mu$ | $|\text{dev}|$ |
|---|---|---|---|---|
| ²H | 6 | 0.508229789376738962577995 | same | 2.5e-60 |
| ³H | 9 | 0.205135640448649768926850 | same | 1.6e-60 |
| ³He | 9 | 0.311386312072595652412888 | same | 6.2e-61 |
| ⁴He | 12 | 0.125684152895266269413878 | same | 1.6e-61 |

The multilinear logarithm of $\Xi_S$ is the Ursell series — the exponential
formula $\Xi = \exp_{\text{sq-free}}\bigl(\sum_T z^T \varphi^T_T\bigr)$ —
verified symbolically with the $\varphi^T_T$ *defined* by the cluster property
$Z_T = \sum_{\pi \in \Pi(T)} \prod_{B \in \pi} \varphi^T_B$: remainder of
$6\,\Xi - (6 + 6U + 3U^2 + U^3)$ modulo $(z_i^2)$ is $0$ at $n = 3$, of
$24\,\Xi - (24 + 24U + 12U^2 + 4U^3 + U^4)$ is $0$ at $n = 4$, and
$\partial^3 \ln \Xi / \partial z_1 \partial z_2 \partial z_3 |_0 = \varphi^T_3$
exactly. So the Mayer/Ursell vocabulary on this arc is not an analogy: $\Xi_S$
is a lattice gas, and its third Ursell coefficient is what the 2026-08-30
identity computed.

## 2. Why $b_3^{\text{corpus}} = -\varphi^T_3$ holds — and why it stops at $n=3$

The two cumulant families live on different lattices:

* the corpus cumulants (`QOU.Mass.PairwiseCumulantVanishing.b3`, `b4`) are
  **Boolean-lattice** (inclusion–exclusion over subsets) inversions of
  $W = 1 - Z$;
* the Ursell functions are **partition-lattice** inversions of $Z$ (the cluster
  property).

For a bond-multiplicative $Z$, expanding $\prod (1 + g_e)$ and summing the
alternating signs over supersets of each edge set's vertex support gives

$$
\text{Boolean}(Z)_S = \sum_{\substack{E \subseteq \binom{S}{2}\\ \text{no isolated vertex}}} g^E,
\qquad
\varphi^T_S = \sum_{\substack{E \subseteq \binom{S}{2}\\ \text{connected}}} g^E,
\qquad
b_S^{\text{corpus}} = -\,\text{Boolean}(Z)_S .
$$

The smallest isolated-vertex-free graph that is not connected is two disjoint
edges on four vertices. Measured in exact `Fraction` arithmetic, $n = 2..5$:

| $n$ | trials | Boolean $=$ no-isolated-vertex sum | connected sum $=$ cluster property | $b^{\text{corpus}} = -$Boolean | disconnected isolated-free graphs |
|---|---|---|---|---|---|
| 2 | 100 | 100 | 100 | 100 | **0** |
| 3 | 200 | 200 | 200 | 200 | **0** |
| 4 | 100 | 100 | 100 | 100 | **3** (the perfect matchings) |
| 5 | 20 | 20 | 20 | 20 | 40 |

Lean: `b3corpus_eq_neg_phi3`, `boolean3_eq_phi3`, and at $n = 4$

$$
b_4^{\text{corpus}} = -\varphi^T_4 - (g_{12}g_{34} + g_{13}g_{24} + g_{14}g_{23})
\qquad (\texttt{b4corpus\_eq}),
$$

which is the closed form of the 2026-08-30 probe's "matches neither
$+\varphi^T_4$ nor $-\varphi^T_4$, 200/200". `phi4_eq_connected_sum` checks the
cluster-property definition against the 38 connected spanning subgraphs of
$K_4$.

## 3. The sign — the reversal

The log-derived binding (§10a of the 2026-08-08 audit, the Cauchy argument) is
$B = -\alpha \ln(\Xi/\Xi_{\text{free}})$, and its Mayer coefficients are
therefore $-\varphi^T_T$ at **every** order (`mayerBinding_eq`):

$$
b_2 = -\varphi^T_2 = 1 - \mu > 0, \qquad b_3 = -\varphi^T_3 .
$$

The corpus's "uniform minus" **is** the Mayer expansion. Then the Ursell
alternation $(-1)^{n-1}\varphi^T_n \ge 0$ on $\mu \in (0,1)$ — proved at $n=3$
in strict form, `phi3_pos`:
$\varphi^T_3 = (1-f_{12})(1-f_{13})f_{23} + (1-f_{23})\bigl((1-f_{12})+(1-f_{13})\bigr) > 0$
— gives

$$
b_3^{\text{corpus}} < 0 \quad \text{for every bond triple in } (0,1)^3
\qquad (\texttt{b3corpus\_neg}).
$$

Three consequences.

1. **`MayerThreeBodySign`'s negative $b_3$ is not a missing $(-1)^{n-1}$.** It
   is the classical sign of the third Mayer coefficient of $-\ln\Xi$ for a gas
   whose pair factors all lie below $1$.
2. **The 2026-08-30 "restore the alternation" prescription,
   $b_n = (-1)^{n-1}\varphi^T_n$, is the same expansion at negative activity**
   (`restored_eq_neg_activity`: $\text{restored}(z) = \text{mayerBinding}(-z)$,
   also checked symbolically). No ensemble at positive activity produces
   $+\varphi^T_3$ from these weights. The prescription chose a sign per order
   against the data — one sign for $n=2$, the other for $n=3$ — which is the
   per-case dispatch the NO-FITTING directive names.
3. **The $2/3$ threshold was an artefact.** `lt_of_b3_pos` bounds $b_3$ using
   only $P_3 \ge 0$. With $P_3$ the bond product, $b_3(f,f,f) = -(1-f)^2(f+2)$
   (`b3corpus_uniform_closed_form`; `b3corpus_uniform_eq_mayerSign` ties the
   two definitions on the nose), so the threshold is never reached.

### 3a. What the Mayer expansion actually gives at the live bonds (no fit)

$A = 3$ chain words, $\alpha = m_e/(q_0(q_0-1)) = 4.185981$ MeV; the
deuteron-pinned scale is the 2026-08-30 convention ($B_{\text{AME}}(D)/(1-\mu_{pn})$).

| atom | bonds | $\varphi^T_3$ (chain $= g_{01}g_{12}$) | Mayer 3rd coeff, $\alpha$-scaled | deuteron-pinned | AME $b_3$ | $\lvert\text{ratio}\rvert$ ($\alpha$ / D) |
|---|---|---|---|---|---|---|
| ³H | pn, nn | 0.293278 | **−1.2277 MeV** | −1.3267 MeV | +1.8081 | 0.679 / 0.734 |
| ³He | pp, pn | 0.190468 | **−0.7973 MeV** | −0.8616 MeV | +1.0443 | 0.763 / 0.825 |

**Sign wrong at both; magnitude 68–83 % of AME.**

> **Frame note (2026-09-12, after #7193's flag), so two $b_3$'s are not quoted
> at each other.** The AME column above is the **per-nucleus** target under the
> uniform-$e_2$ inversion $b_3(X) = B_{\text{AME}}(X) - 3\,B_{\text{AME}}(^2\mathrm{H})$
> with $B(^2\mathrm{H}) = 2.2245662$: $1.8081$ (³H) and $1.0443$ (³He). The
> corpus witness `pair-locality-shortfall.witness.json` carries the **same**
> decomposition and sign convention (binding positive) on the **isospin-averaged**
> $A = 3$ target, $B_{\text{AME}}(A{=}3) = 8.09991876 = \tfrac12(8.4817962 + 7.7180413)$,
> giving $b_3 = 1.42622016$ — exactly the mean of the two per-nucleus values.
> The model side here is **typed** (pn + nn for ³H, pp + pn for ³He), which is
> why it is quoted per nucleus; against the averaged target the Mayer coefficient
> averages to $-1.0125$ MeV ($\alpha$-scaled). Frame difference, not an error.

The uniform-triangle figures
of 2026-08-30 reproduce exactly — $\varphi^T_3 = 0.3919$ at $f_{pn} = z_D$
($2.2511$ MeV) and $0.6066$ at $f_{pn} = \mu_{pn}$ ($2.7439$ MeV) — and are
the **negative-activity** coefficients; the Mayer-sign values are $-2.2511$ and
$-2.7439$ MeV. None of these is a postdiction of a derived quantity; they are
reported so the arc's numbers stay reproducible.

### 3b. The canonical ensemble is exactly pairwise

The fixed-$A$ nucleus is the canonical ensemble (Rebenko, `arxiv-2205.07095v1`).
Its partition function is the **top coefficient** $Z_S = \prod_e \mu_e$, and
$\ln Z_S = \sum_e \ln \mu_e$ — measured, $\ln Z_{012} - \ln Z_{01} - \ln Z_{12}$
is $1.2\times10^{-60}$ (³H) and $5.0\times10^{-60}$ (³He). So the connected
three-body part of the *derived* binding $-\alpha\ln Z_S$ is $0$
(`QOU.Mass.PairwiseCumulantVanishing`, re-measured), and $\varphi^T_3$ enters a
logarithm only through the grand-canonical sum over sub-clusters. There is no
positional integration in the framework to generate a canonical three-body
term the way the classical virial expansion does.

### 3c. Which object was tested

* **`tr_M` of the live alternating-core production word** — bond-multiplicative
  to $10^{-60}$ (§1); this is the object the identification applies to.
* **Per-block characters** $\chi_\lambda$: on ²H the ratio
  $\chi_\lambda(\text{atom})/\chi_\lambda(\text{free})$ deviates from $\mu_{pn}$
  by up to **1.45** across the four two-row blocks. Bond multiplicativity is a
  Markov-trace fact, not a per-block one, so there is **no per-block partition
  function** with these Ursell functions. Consistent with
  `intra_ordering_invariance_does_not_descend_to_blocks_probe`.
* `tr_stabWord_eq_prod_tr` is stated for monotone words of stabilising letters.
  The live word's nucleon *blocks* are not monotone (the alternating core), but
  the chain of blocks joined by single interface letters still factorises by
  connected-sum multiplicativity — that is what §1 measures and what the
  intra-ordering probe (`qou-hu1f`) established; the block-internal ordering
  moves the absolute traces, never the ratio.

## 4. Verdict and invariant

**Scope (b), invariant: the Ursell alternation $(-1)^{n-1}\varphi^T_n \ge 0$ on
bond factors in $(0,1)$**, proved at $n = 3$ (`phi3_pos`). It excludes a
positive connected three-body coefficient in the Mayer expansion of
$-\ln\Xi$ at positive activity **for every bond triple in $(0,1)^3$** — every
edge set, every like-pair typing, every convention, every scale, and *no*
threshold. This is strictly stronger than `MayerThreeBodySign`'s exclusion,
which needed $f_{pn} \le 2/3$.

**What it does not exclude (scope (a)):**

* an **attractive Mayer channel** — a bond factor above $1$, $g > 0$. Every
  interface letter of the production word has trace $z_D + d \in (0,1)$
  (measured: $0.61269$, $0.50823$, $0.40363$), so none is present; a letter
  $c\sigma + d$ with $cz + d > 1$ is not excluded by anything here;
* a **non-Mayer assembly** — anything that is not $-\ln$ of a bond-multiplicative
  partition function;
* **`PairwiseCumulantVanishing`** and **`MayerThreeBodySign`** as theorems —
  every statement in both remains true of its object. What changes is the
  *reading*: their dichotomy ($b_3 = 0$ on the log assembly, $b_3 < 0$ on the
  multiplicative one) is now the canonical / grand-canonical pair of one lattice
  gas, and neither side carries a sign error.

**The 2026-08-30 §3–§4 reading is withdrawn** — the sign obstruction is real,
and it is the classical one. What that earlier document got right stands: the
identity (§1), the alternation itself (§2), and the Boltzmann identification
$\mu = e^{-B/\alpha}$ (§5a).

## 5. What this error contaminated

The "missing sign" claim reached: the 2026-08-30 audit §3–§4 and its title;
bean `qou-rwhv` (the "RESOLVED" section); the docstring and item 3 of
`ursell_alternation_sign_identity_probe.py` and its witness `description`;
the PR #6152 body. It reached **no** Lean file and **no** content block.
This document and the bean append are the corrections; the 2026-08-30 audit is
left as a dated record with this forward pointer added at its head.

## 6. Proposed re-scoping (owner-facing)

**`MayerThreeBodySign.lean` docstring** — edited on this branch (corpus-derived:
the Lean here fixes it). The "What it excludes" paragraph now states the
alternation invariant, drops the threshold as the operative bound, and points
here.

**AGENTS.md "Extensive-term frontier" bullet 4** — *not* edited; the proposed
wording is in the PR #7198 body for the owner.

## 7. What is still open

* The extensive term (`qou-brng`) is untouched: this closes the *vocabulary*
  question, not the magnitude. The Mayer third coefficient is the wrong sign
  and 68–83 % of AME in magnitude at the live bonds.
* Whether any admissible Hecke letter has trace $> 1$ (an attractive channel)
  is a question about the word, not about the expansion — unmeasured beyond the
  three production letters.
