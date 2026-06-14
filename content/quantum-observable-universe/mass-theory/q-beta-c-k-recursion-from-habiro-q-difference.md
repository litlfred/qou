**Proposition (scaffolding).** *Let* $F(q) \in \mathbb{Z}[q, q^{-1}]^\wedge$
*be a fibre-level Habiro element associated to the operator-valued $T_\beta$
selection
([`prop:t-beta-markov-frobenius-collapse`](t-beta-markov-frobenius-collapse.md))
satisfying a $q$-difference equation of depth $d$:*

$$
F(q\xi) \;=\; R(q,\xi)\cdot F(\xi),
\qquad R(q,\xi) \in \mathbb{Q}(q)[\xi, \xi^{-1}] \text{ of degree} \le d.
$$

*Then the precision-ladder coefficients $c_k$ of
[`prop:q-beta-over-e0-classical-vanishing`](q-beta-over-e0-classical-vanishing.md)
satisfy a depth-$d$ linear recursion*

$$
c_{k+1} \;=\; \sum_{j=1}^{d} a_j(q_0)\cdot c_{k+1-j},
\qquad a_j(q_0) \in \mathbb{Q}(q_0),
$$

*with kernel coefficients $\{a_j\}$ extracted from $R(q_0, \xi)$ via the
$(u;u)_m \to u^k$ change-of-basis of the Habiro ring (Habiro 2004).*

## Why this is the right structure

The shape-collapse audit (PR [#1750](https://github.com/litlfred/qou/pull/1750))
established the operator content: $T_\beta = S \cdot \mathbf{1}$, with
$S$ pinned by the SDP constraint. The SDP strict-complementarity audit
(PR [#1752](https://github.com/litlfred/qou/pull/1752)) showed the
*direction* of the selector is $S$-independent and $q$-rational. The
diagnostic
[`prop:q-beta-over-e0-classical-vanishing`](q-beta-over-e0-classical-vanishing.md)
showed the SDP-constraint scalar $S = Q_\beta/E_0$ is *not* the ladder
normalization. Together these pin $F(q) = Q_\beta(q)/[Q_A(q) \cdot \cos(\alpha_{\mathrm{eff}}(q))]$
as a single fibre-level Habiro object whose $q$-difference structure
determines the $c_k$.

## What the recursion buys

Once a *single* $F$ is identified, the seven scalar coefficients
$c_2, \ldots, c_8$ (required for the $1\,\mathrm{ppQ}$ truncation
target, per [`docs/precision-goals.md`](https://github.com/litlfred/qou/blob/main/docs/precision-goals.md))
collapse to:

- One **seed** $c_2 = -1$, proved categorically (bar-even constraint, PR [#1602](https://github.com/litlfred/qou/pull/1602)).
- One **kernel** $R(q_0, \xi)$ of bounded degree $d$, determined by the
  categorical structure of $T_\beta$ and the Habiro embedding.
- The recursion produces $c_3, c_4, \ldots, c_8$ automatically.

Compare to the brute force: each $c_k$ ($k \ge 3$) currently requires
its own derivation (see the four-session $c_3$ flip-flop in
[`docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md))
or is extracted from the CODATA residual (the caveat of
[`qbeta-1ppq-achieved.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta-1ppq-achieved.witness.json)
where $c_4 = -0.97157$ was a fit).

## The kernel — what's known, what's open

| Slot | Status | Source |
|---|---|---|
| Seed $c_2 = -1$ | **proved** | PR [#1602](https://github.com/litlfred/qou/pull/1602), bar-even constraint |
| $c_3 \approx -2$ | near-match (3 % cross-anchor swing) | empirical, four sessions of analysis |
| $c_4$ at $1\,\mathrm{ppQ}$ | fit (CODATA residual), value $-0.97157$ | [`qbeta_1ppq_achieved.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta_1ppq_achieved.py) |
| $c_5, \ldots, c_8$ | not derived | open |
| Kernel $R(q,\xi)$ | structurally constrained: bar-ODD leading $a_1=-c_3$ (carrier $\kappa_{(2,1)}=(q-1)^3(q+1)/q^2$), period-3/$\zeta_6$ resonance, $\sqrt{u}$-to-$u^2$ lift. The $\zeta_4$ residue is **relaxed** — the root-of-unity residue program shows neither the content-Casimir $\mu_\lambda$ nor the framing $\cos\alpha_{\mathrm{eff}}$ supplies a bar-odd-compatible genuine $\zeta_4(q)$; it is a $\sqrt{q}$ double-cover reading of $\zeta_2$ (bar-fixed $q=-1$) or a post-$\cos$-wrap archimedean feature, **not** a fibre constraint. | [`habiro_ladder_bridge.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/habiro/habiro_ladder_bridge.py), [root-of-unity program audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md) |
| Habiro element $F(q)$ | **identified (structural analog)** | mirroring α_EM `[2]_q(1-h²α)` per PR #1911 |

## What this content block provides

- A formal Lean structure
  `CKRecursion R` capturing the depth $d$ + kernel $\{a_j\}$ data
  ([`q-beta-c-k-recursion-from-habiro-q-difference.lean`](q-beta-c-k-recursion-from-habiro-q-difference.lean)).
- A method `applyRecursion : (Fin depth → R) → R` that performs one
  step of the recursion given the last $d$ values of the $c_k$
  sequence.
- The **parity-alternation theorem** `esymm_bar_parity` (sorry-free):
  writing the recursion coefficients as elementary symmetric polynomials
  $a_j = e_j(\{r_\lambda\})$ of the per-mode rates
  $r_\lambda = (q-1)\mu_\lambda$, then for any involutive ring
  homomorphism (the bar $q \mapsto q^{-1}$) under which the rates are
  bar-odd, $\overline{e_j} = (-1)^j e_j$ — so $a_j$ alternates bar-parity
  (bar-ODD for odd $j$, bar-EVEN for even $j$), *independent of which
  modes are active*. This is the structural law behind the ladder's
  parity bookkeeping (bar-even seed $c_2 = -1$ driven by a bar-odd
  $a_1 = -c_3$). Proof: $e_j(-x) = (-1)^j e_j(x)$ (`esymm_neg`). The corollaries
  `esymm_bar_odd` / `esymm_bar_even` specialise the alternation to the explicit
  forms $\overline{a_j} = -a_j$ for odd $j$ (the $\zeta$-carrying rungs $a_1, a_3$)
  and $\overline{a_j} = a_j$ for even $j$ (the seed rung $c_2 = -1$).
- The **cyclotomic bar-stability lemmas** `cyclotomic_two_bar_stable`,
  `cyclotomic_three_bar_stable`, `cyclotomic_six_bar_stable` (sorry-free):
  each cyclotomic factor $\Phi_d$ ($d \in \{2,3,6\}$, $\varphi(d) = 1,2,2$) is
  self-reciprocal, $\Phi_d(1/q)\,q^{\varphi(d)} = \Phi_d(q)$, so divisibility by
  $\Phi_d$ is invariant under the bar involution $q \mapsto q^{-1}$. This is the
  formal backing for the period-3/$\zeta_6$ closure: because $\overline{\Phi_6}$
  is a unit multiple of $\Phi_6$, the bar-odd projection of a single
  $\zeta_6$-carrier still carries $\zeta_6$ (no cross-mode cancellation needed).
- The **general prime case** `cyclotomic_prime_bar_stable` (sorry-free): for
  *every* prime $p$, $\Phi_p(1/q)\,q^{p-1} = \Phi_p(q)$ — subsuming the $d=2,3$
  lemmas above and extending to $p = 5, 7, 11, \dots$. Because
  $\Phi_p = \sum_{i<p} X^i$, the identity is the index reflection
  $\sum_{i<p} q^{p-1-i} = \sum_{i<p} q^i$, with no per-prime computation.
- The **fully general case** `cyclotomic_self_reverse` and
  `cyclotomic_bar_stable_general` (sorry-free): for *every* $n > 1$ (over any
  integral domain) $\Phi_n$ is self-reciprocal —
  $\operatorname{reverse}(\Phi_n) = \Phi_n$, equivalently
  $\Phi_n(1/q)\,q^{\varphi(n)} = \Phi_n(q)$ — subsuming **all** the explicit and
  prime cases above, including every composite $d$ (4, 8, 9, …). Mathlib carries
  no cyclotomic palindrome lemma; this is proved here by strong induction on the
  divisor product $\prod_{d \mid n}\Phi_d = X^n - 1$ (peeling $d=1$ for the
  anti-palindrome sign, the inductive hypothesis on $1 < d < n$, then cancelling
  the nonzero proper-divisor product), with the eval form following via
  `eval₂_reverse_mul_pow`.
- A companion compute scaffold
  ([`qbeta_c_k_recursion_scaffold.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/qbeta/qbeta_c_k_recursion_scaffold.py))
  demonstrating the recursion machinery on toy depth-1 and depth-2
  kernels, with the seed $c_2 = -1$.

## Closing the open piece — the q-heat kernel derivation

The Habiro element $F(q)$ is identified as the **partition function** (the trace of the $q$-heat kernel) over the relevant Hecke modules:

$$Z_q(t) = \sum_{\lambda \in \Lambda} d_\lambda(q) \cdot \exp_q(-\mu_\lambda(q) \cdot t)$$

where $\Lambda$ is the set of active Hecke blocks, $d_\lambda(q)$ are the Steinberg $q$-hook dimensions, and $\mu_\lambda(q)$ are the content-Casimir eigenvalues ([Peter--Weyl $q$-heat kernel](#prop:q-heat-kernel-peter-weyl)).

The $q$-difference equation for $F(q)$ is then derived from the depth-1 Jackson equations of each mode $\exp_q(-\mu_\lambda t)$ ([per-mode $q$-difference](#thm:heat-mode-depth-one-kernel)):

1. **Per-mode kernel**: Each mode satisfies $f_\lambda(qt) = (1 - (q-1)\mu_\lambda t) f_\lambda(t)$.
2. **Composition**: The net partition function $Z_q$ satisfies a $q$-difference equation of depth $|\Lambda|$, with coefficients determined by the elementary symmetric polynomials of the per-mode kernels.
3. **Mass-theory mapping**: The $c_k$ coefficients are extracted from the $q$-difference kernel evaluated at the mass-theory anchor $q_0$, matching the empirical $c_2 = -1$ and $c_3 \approx -2$.

The Lean class is parameterized over $R$ (the kernel) and the recursion
machinery is decoupled from the specific kernel — this $q$-heat derivation
provides the canonical $R$ that turns the framework into a concrete $c_k$
predictor.

### The q-Bessel identification of $F$ (fibre-level)

The partition function $Z_q$ above **is**, at the fibre level, a **Hahn–Exton
q-Bessel function** — the matrix coefficient of the quantum motion group
$E_q(2)$, i.e. the $\mathrm{SU}_q(2)\to E_q(2)$ contraction limit of the
substrate (PR [#2279](https://github.com/litlfred/qou/pull/2279);
Vaksman–Korogodsky 1989, Koelink 1994 \cite{koelink1994}). Concretely, the
ladder coefficients $c_k$ are its q-Bessel power-series coefficients, obeying
the first-order q-recurrence $c_k(1-q^k)(1-q^{\nu+k}) = -q^{k-1}c_{k-1}$ —
equivalently the **second-order q-difference equation** (the q-Bessel
equation), with $g(w)=\sum_k c_k w^k$:

$$q^{\nu}\,g(q^2 w) \;-\; (1+q^{\nu}-w)\,g(qw) \;+\; g(w) \;=\; 0,$$

proved sorry-free as `QOU.QBeta.qbessel_second_order_recurrence`
([`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean)).
The linear-in-$w$ middle term is the *source* of the descending ladder: every
"quadratic correction" in the framework ($c_2=-1$, $\alpha_{\mathrm{EM}}$'s
$[2]_q(1-h^2\alpha)$) is a second-order truncation of one of these q-Bessel
tails.

**Discipline (fibre vs archimedean).** This identification is **fibre-level
only**. The *real-$x$ archimedean* closure of $c_3$ via a substrate-fixed
q-Bessel is **refuted** (PR [#2300](https://github.com/litlfred/qou/pull/2300):
the cross-anchor slope $dc_3/dq_0\approx 4.66\times10^{6}$ is unreachable by any
smooth real $x$). And the finite per-$n$ content-Casimir spectrum
$\{\mu_\lambda\}$ is the **compact $\mathrm{SU}_q(2)$ q-Casimir**, *not* a
q-Bessel zero spectrum ($p(n)\neq n$; algebraic vs transcendental). The q-Bessel
object — and the **q-Lommel** three-term recurrence that truncates its zeros —
lives in the $n\to\infty$ brane-tower (contraction) limit, the open keystone
direction, where the binding $\Delta_\lambda$ ladder also lives. Nothing here is
wired to production; $c_k$ stays cal-anchored.

## Literature — AJ-recurrence parent + a quantum-modularity remark

This depth-$d$ recurrence is the $Q_\beta$-specialised image of the
**q-holonomic (AJ) recurrence** for quantum knot invariants \cite{garoufalidis2004}:
the colored Jones $J_N(K;q)$ satisfies $\hat{A}(\hat{M},\hat{L};q)\,J_N = 0$ in
the colour $N$ (with $\hat{M}J_N = q^N J_N$, $\hat{L}J_N = J_{N+1}$,
$\hat{L}\hat{M} = q\hat{M}\hat{L}$), degenerating to the classical
$A$-polynomial as $q\to 1$. Habiro's cyclotomic re-basing $(u;u)_m \to u^k$ —
the **same** change-of-basis the $c_k$ use — pushes that recurrence onto the
cyclotomic coefficients. Ours differs only in the index (truncation order $k$,
not colour $N$) and in modelling $F$ by the $q$-heat partition function.

**Remark (quantum-modularity of the bar-involution; conjectural, not proven).**
The bar-involution $q\mapsto q^{-1}$ that fixes the leading coefficient
$a_1 = -c_3$ as **bar-odd** is conjecturally the fibre-level avatar of the
**quantum-modular $S$-transform** $q\mapsto\tilde q$ \cite{zagier2010}: the
Kashaev / colored-Jones asymptotics near roots of unity are quantum modular,
with a $\sqrt{2\pi/\hbar}$ radial prefactor (the framework's $\sqrt{u}$) and an
$\hbar$-series of Ohtsuki periods. Under this reading the bar-odd requirement on
$a_1$ is the *odd part under the $S$-transform*, the $\sqrt{u}$ prefactor is the
radial asymptotic, and the failure of the naive $q$-dilogarithm route is the
vanishing of the modular cocycle's Bloch–Wigner (volume) term on the
**non-hyperbolic** Hopf link. This is a motivated analogy, **not a theorem** —
establishing it would require exhibiting $F(q)$ as a quantum modular form.
Full discussion: [`docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md).
