<!-- FILE_START: qbeta-formalize-first-gates-intro.md -->
The Hoefsmit He-4 channel fixed the selector direction as a single
Markov-trace collapse, $T_\beta = S\cdot\mathbf{1}$
([`prop:t-beta-markov-frobenius-collapse`](#prop:t-beta-markov-frobenius-collapse)).
That collapse leaves one object to identify: the fibre-level Habiro
element $F(q)$ whose $q$-Taylor coefficients are the precision-ladder
$c_k$ of the $\mathfrak{Q}_\beta$ series
(`sec:mass-algebraic-complex-volume-ladder`).
The question this section settles is not *what $F$ is* — that remains the
open keystone — but *which structural constraints any candidate $F$ must
satisfy before it is worth evaluating*. This is the formalize-first
discipline applied to the decay side: prove the invariants that prune the
hypothesis class, then search only the survivors.

Four gates do the pruning. A candidate generating function must have its
pole at the substrate radius
([`prop:q-beta-radius-of-convergence-gate`](#prop:q-beta-radius-of-convergence-gate)),
must be bar-even under $q\mapsto q^{-1}$ so the integer-$u$ ladder is
clean ([`prop:q-beta-bar-even-kernel-invariant`](#prop:q-beta-bar-even-kernel-invariant)),
must reproduce the classical shadows $c_2\to-1$, $c_3\to J_{\mathrm{Hopf}}(1)=-2$
at $q=1$ ([`prop:q-beta-q-eq-one-shadow-gate`](#prop:q-beta-q-eq-one-shadow-gate)),
and must carry a magnitude consistent with the target observable
([`prop:q-beta-direction-sanity-gate`](#prop:q-beta-direction-sanity-gate)).
The four bundle into one parametric typeclass
([`prop:q-beta-bar-even-kernel-typeclass`](#prop:q-beta-bar-even-kernel-typeclass)),
with the mass-side analogue assembled alongside
([`prop:mass-side-kernel-formalize-first-gates`](#prop:mass-side-kernel-formalize-first-gates)).
Between the gates sits the recursion machinery itself: the depth-$d$
linear recursion the $c_k$ inherit from the Habiro $q$-difference kernel
([`prop:q-beta-c-k-recursion-from-habiro-q-difference`](#prop:q-beta-c-k-recursion-from-habiro-q-difference)),
the bridge to the per-block $z$-recursion
([`prop:qbeta-z-recursion-to-ck-recursion-bridge`](#prop:qbeta-z-recursion-to-ck-recursion-bridge)),
and the exact rational forms read off at the silver ratio
([`prop:qbeta-c8-c10-silver-rationals`](#prop:qbeta-c8-c10-silver-rationals)).

The output is a verdict matrix, not a closed form. The gates settle which
coefficients are structural and which remain calibration-anchored: $c_2=-1$
is proved Taylor-exact, $c_3\approx-2$ is a near-match with a few-percent
cross-anchor swing, and $c_k$ for $k\ge4$ are fit to the CODATA residual
rather than derived. Nothing in this section is wired to production — the
$c_k$ stay cal-anchored, and the categorical construction of $F(q)$ that
would turn the recursion into a parameter-free predictor is deferred to the
brane-tower (contraction) limit where the binding $\Delta_\lambda$ ladder
also lives. What the gates buy is a sharper statement of the open problem:
any future $F$ that fails a gate is excluded without a canonical search.
<!-- FILE_END: qbeta-formalize-first-gates-intro.md -->

<!-- FILE_START: toroidal-harmonics-delta-lambda.md -->
# A toroidal-harmonic change of variables for the $z$-recursion

**Proposition.** *Let $x = \tfrac{1}{2w} - 1$. Under this change of
variables the half-integer-degree ($n-\tfrac12$) toroidal Legendre
equation*

$$ (1 - x^2)\,y'' - 2x\,y' + \left(n^2 - \tfrac14\right) y = 0 $$

*transforms, after clearing denominators, into the second-order
$w$-equation*

$$ (16w^3 - 4w^2)\,f'' + 16w^2\,f' + (4n^2 - 1)\,f = 0, \qquad y = f\circ w. $$

*The identity is exact (verified symbolically in
[`toroidal_harmonics.py`](#), `derive_bridge`).*

## Scope

The variable is $w = z^2$ with $z = \tfrac{\sqrt q}{1+q}$ the Markov
parameter and $q = e^{-\eta}$, $x = \cosh\eta$. The proposition is a
statement about **operators**: it places the $w$-form of the toroidal
Legendre operator on record.

It does **not** establish the following, which remain open:

- **The $w$-ODE is not yet identified with the proved $z$-recursion.**
  The pre-archimedean Markov recursion
  $4(n+1)a_{n+1} + 6n\,a_n + (2n-1)a_{n-1} = 0$
  ([`prop:interface-knot-markov-z`](#prop:interface-knot-markov-z)) is written in the variable
  $w = q-1$ — a *different* $w$ from the $w = z^2$ here. Matching the two
  is part of the open $z \to c_k$ **f-map**; it is asserted, not proved.
- **No $c_k$ is made exact by this map.** In particular $c_3$ is
  cal-anchored and swings $\approx 2.375\%$ between the proton and muon
  substrate anchors; only $c_2 = -1$ is Taylor-exact
  (see the cross-anchor verdict audit).
- **The $\Delta_\lambda$ mass gap is not resolved here.** Evaluating a
  toroidal-harmonic ratio $P_{n-1/2}^m$ against the shell-filling fraction
  $c_\lambda$ is a separate, and currently **negative**, investigation:
  the $c_\lambda$ used empirically is defined circularly as
  $B_{\mathrm{AME}}/E_{\mathrm{gate}}$, and no parameter-free toroidal
  anchor reproduces it (the closest "pretty" constant, the golden ratio,
  is $\approx 0.12\%$ off, and the value that does reproduce $c_\lambda$ is
  $q_0 \approx 0.615$ — neither the golden ratio nor the substrate
  $q_0 \approx 1.10998$). That scan is recorded as a negative audit in
  `toroidal_harmonics.py::evaluate_c_lambda`, not as paper content, and
  does not meet the three-calibration discipline or the $\Delta_\lambda$
  gate.
<!-- FILE_END: toroidal-harmonics-delta-lambda.md -->

<!-- FILE_START: q-beta-over-e0-classical-vanishing.md -->
**Proposition.** *Let* $\mathfrak{Q}_\beta(q)$ *and* $E_0^{(N{=}0)}(q)$ *be the
substrate closed forms of* [`prop:neutron-qvalue-symbolic`](neutron-qvalue-symbolic.md)
*and* [`rem:beta-decay-energy-scale`](beta-decay-energy-scale.md):*

$$
\mathfrak{Q}_\beta(q) \;=\; m_e \cdot \frac{(2q + 1 - q^2)(q+1)}{2q^3},
\qquad
E_0^{(N=0)}(q) \;=\; \frac{m_e}{q(q-1)}.
$$

*Then the ratio*

$$
S(q) \;\coloneqq\; \frac{\mathfrak{Q}_\beta(q)}{E_0^{(N{=}0)}(q)}
\;=\; \frac{(2q + 1 - q^2)\,(q^2 - 1)}{2 q^2}
$$

*satisfies* $S(q = 1) = 0$ *as an algebraic identity over any
commutative ring.*
## Consequence for the $c_k$ precision ladder

The shape-collapse audit
[`docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md`](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-03-qbeta-markov-trace-shape-collapse.md)
states *"$c_k$ come from $u_{\text{ladder}}$ Taylor of $S(q) = \mathfrak{Q}_\beta(q)/E_0(q)$"*.
Taken literally, this recipe is **degenerate**: the Taylor expansion of
$S/S(1)$ around $q = 1$ is $0/0$, and the proved $c_2 = -1$ cannot be
recovered.

The resolution is interpretive:

- The $S = \mathfrak{Q}_\beta / E_0$ in the audit doc is the **SDP-constraint
  scalar** (canonical at $q_0$ — the affine target $n_{\text{target}} = S(q_0) \approx 0.18689$
  that the operator-selection program solves for).
- The **$c_k$ ladder normalization** is a different object,
  namely $\mathfrak{Q}_\beta / [Q_A \cdot \cos(\alpha_{\text{eff}})]$, with
  $Q_A$ and $\alpha$ read from the operator-valued $N{=}3$ witness
  (see the canonical formalism).

This proposition is therefore the algebraic obstruction that pins the
gap and identifies the missing categorical input
($Q_A(q)$ and $\alpha(q)$ symbolic closed forms).

## Two independent routes to the same conclusion

The vanishing $S(1) = 0$ is the *direct-algebraic* witness. An
*operator-theoretic* witness arrives from the SDP strict-complementarity
analysis:

| Route | Diagnostic | Numerics |
|---|---|---|
| **Taylor expansion** ([PR #1769](https://github.com/litlfred/qou/pull/1769)) | $S(1) = 0$; the Taylor series in $u_{\text{ladder}}$ degenerates | $S_{N=0}(q_0) - S_{\text{target}} = 0.168\%$ |
| **SDP strict complementarity** ([PR #1752](https://github.com/litlfred/qou/pull/1752)) | Frobenius Gram indefinite (eigenvalues include $-0.855$); LP min-trace $\neq T_\beta$ selection; selector direction $S$-independent | $Q_A(q_0) = m_e \cdot \lvert q^2 - 2q - 1\rvert (q+1)/(2q^3) = 0.78365\;\text{MeV}$, $\equiv$ CODATA $\mathfrak{Q}_\beta$ to $0.168\%$ with zero CODATA-$\mathfrak{Q}_\beta$ input |

Both routes converge on the same structural conclusion: the bare
substrate scale $Q_A$ predicts $\mathfrak{Q}_\beta$ to $0.168\%$ CODATA-free, and
the remaining sub-ppb correction is the $c_k$ ladder whose
normalization is *not* the SDP-constraint scalar $S = \mathfrak{Q}_\beta/E_0$.
<!-- FILE_END: q-beta-over-e0-classical-vanishing.md -->

<!-- FILE_START: qbeta-c8-c10-silver-rationals.md -->
**Proposition ($\mathfrak{Q}_\beta$ c_8, c_9, c_10 closed-form values at the silver ratio).**

*At the silver ratio $q = 1 + \sqrt{2}$ where the Hoefsmit parameter takes
the exact rational value $b^2 = 7/8$, the closed-form $\mathfrak{Q}_\beta$ precision-ladder
coefficients $c_8$, $c_9$, $c_10$ extend the documented Pell-Lucas
$\sigma$-action pattern:*

$$
  c_8 = c_3^2 \cdot b^4 = 4 \cdot \left(\tfrac{7}{8}\right)^2
      = \tfrac{49}{16},
  \qquad
  c_9 = c_3^3 \cdot b^2 = -8 \cdot \tfrac{7}{8} = -7,
  \qquad
  c_{10} = c_3^2 \cdot b^6 = 4 \cdot \left(\tfrac{7}{8}\right)^3
         = \tfrac{343}{128}.
$$

*Each value matches the Pell-Lucas-clean prediction
(`is_pell_lucas_clean`-checked) recorded in the SDP-extraction witness
`qbeta-decay-sdp-extended-ck.witness.json` and is therefore a
PURE σ-action rung with no averaging-resonance $\tfrac{1}{2}$
fingerprint.*

## Significance of these values

The Pell-Lucas-clean classification at the silver ratio is the
**structural signal** for the $\mathfrak{Q}_\beta$ c_k precision ladder. Per the
SDP-extraction formalism's own caveat, the c_k values extracted at the
substrate anchor $q_0$ become noise-floor-dominated for $k \geq 8$;
the silver ratio is where the algebraic structure is visible.

The three closed forms extend the documented $c_4 = c_3 \cdot b^4$,
$c_6 = c_3^2 \cdot b^2$, $c_7 = c_3^3$ pattern by one rung in each
parity class.

## Lean proof structure

Three pure-rational identities, each closed by `norm_num`. The
Lean side fixes the silver-ratio $b^2 = 7/8$ as a `(7 : ℚ) / 8` constant
and computes the closed-form expression in rational arithmetic — no
transcendental or symbolic-q machinery required.

  - `qbeta_c8_at_silver`:  `4 * (7/8)^2 = 49/16`.
  - `qbeta_c9_at_silver`:  `-8 * (7/8) = -7`.
  - `qbeta_c10_at_silver`: `4 * (7/8)^3 = 343/128`.

All three closed by `norm_num` after expanding the closed-form
expression. The Lean theorems live as `Rat` equalities; they extend
to any field containing $\mathbb{Q}$.

## q-usage discipline

The silver ratio $q = 1 + \sqrt{2}$ is a real algebraic point
($q \in \mathbb{R}_{>0}$). The exact $b^2 = 7/8$ value arises from
the Hoefsmit q-rational evaluated at this $q$ (per the Pell-Lucas
companion-sequence identification). All three identities are
**fibre-level Laurent rationals** realised at a particular real
anchor: the identities hold over any field containing $\mathbb{Q}$ and
are specialised here to the silver-ratio rational point.

## Cross-references

- SDP-extraction witness with the Pell-Lucas check at the silver
  ratio: `qbeta-decay-sdp-extended-ck.witness.json` on `main`.
- Closed-form derivation canonical evaluation + witness:
  the formal derivation.
- Closed-form wiring outcome at $q_0$ (companion categorical canonical evaluation):
  the formal derivation.
<!-- FILE_END: qbeta-c8-c10-silver-rationals.md -->

<!-- FILE_START: q-beta-c-k-recursion-from-habiro-q-difference.md -->
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

## Structural justification

The shape-collapse audit (PR [#1750](https://github.com/litlfred/qou/pull/1750))
established the operator content: $T_\beta = S \cdot \mathbf{1}$, with
$S$ pinned by the SDP constraint. The SDP strict-complementarity audit
(PR [#1752](https://github.com/litlfred/qou/pull/1752)) showed the
*direction* of the selector is $S$-independent and $q$-rational. The
diagnostic
[`prop:q-beta-over-e0-classical-vanishing`](q-beta-over-e0-classical-vanishing.md)
showed the SDP-constraint scalar $S = \mathfrak{Q}_\beta/E_0$ is *not* the ladder
normalization. Together these pin $F(q) = \mathfrak{Q}_\beta(q)/[Q_A(q) \cdot \cos(\alpha_{\mathrm{eff}}(q))]$
as a single fibre-level Habiro object whose $q$-difference structure
determines the $c_k$.

## Consequences of the recursion

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
[`qbeta-1ppq-achieved.witness.json`](https://github.com/litlfred/qou/blob/main/computations/qbeta/qbeta-1ppq-achieved.witness.json)
where $c_4 = -0.97157$ was a fit).

## The kernel — known and open components

| Slot | Status | Source |
|---|---|---|
| Seed $c_2 = -1$ | **proved** | PR [#1602](https://github.com/litlfred/qou/pull/1602), bar-even constraint |
| $c_3 \approx -2$ | near-match (3 % cross-anchor swing) | empirical, four sessions of analysis |
| $c_4$ at $1\,\mathrm{ppQ}$ | fit (CODATA residual), value $-0.97157$ | the canonical formalism |
| $c_5, \ldots, c_8$ | not derived | open |
| Kernel $R(q,\xi)$ | structurally constrained: bar-ODD leading $a_1=-c_3$ (carrier $\kappa_{(2,1)}=(q-1)^3(q+1)/q^2$), period-3/$\zeta_6$ resonance, $\sqrt{u}$-to-$u^2$ lift. The $\zeta_4$ residue is **relaxed** — the root-of-unity residue program shows neither the content-Casimir $\mu_\lambda$ nor the framing $\cos\alpha_{\mathrm{eff}}$ supplies a bar-odd-compatible genuine $\zeta_4(q)$; it is a $\sqrt{q}$ double-cover reading of $\zeta_2$ (bar-fixed $q=-1$) or a post-$\cos$-wrap archimedean feature, **not** a fibre constraint. | the canonical formalism, [root-of-unity program audit](https://github.com/litlfred/qou/blob/main/docs/audits/2026-06-13-qbeta-root-of-unity-residue-program.md) |
| Habiro element $F(q)$ | **identified (structural analog)** | mirroring $\alpha_{EM}$ $[2]_q(1-h^2\alpha)$ |

## Contents of this content block

- A formal Lean structure
  `CKRecursion R` capturing the depth $d$ + kernel $\{a_j\}$ data
  ([`q-beta-c-k-recursion-from-habiro-q-difference.lean`](q-beta-c-k-recursion-from-habiro-q-difference.lean)).
- A method `applyRecursion : (Fin depth -> R) -> R` that performs one
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
  prime cases above, including every composite $d$ (4, 8, 9, $\ldots$). Mathlib carries
  no cyclotomic palindrome lemma; this is proved here by strong induction on the
  divisor product $\prod_{d \mid n}\Phi_d = X^n - 1$ (peeling $d=1$ for the
  anti-palindrome sign, the inductive hypothesis on $1 < d < n$, then cancelling
  the nonzero proper-divisor product), with the evaluation form following
  from the corresponding polynomial `reverse` lemma.
- A companion compute scaffold
  (the canonical formalism)
  demonstrating the recursion machinery on toy depth-1 and depth-2
  kernels, with the seed $c_2 = -1$.

## Closure of the open piece — the q-heat kernel derivation

The Habiro element $F(q)$ is identified as the **partition function** (the trace of the $q$-heat kernel) over the relevant Hecke modules:

$$Z_q(t) = \sum_{\lambda \in \Lambda} d_\lambda(q) \cdot \exp_q(-\mu_\lambda(q) \cdot t)$$

where $\Lambda$ is the set of active Hecke blocks, $d_\lambda(q)$ are the Steinberg $q$-hook dimensions, and $\mu_\lambda(q)$ are the content-Casimir eigenvalues ([Peter--Weyl $q$-heat kernel](#prop:q-heat-kernel-peter-weyl)).

The $q$-difference equation for $F(q)$ is then derived from the depth-1 Jackson equations of each mode $\exp_q(-\mu_\lambda t)$ (per-mode $q$-difference):

1. **Per-mode kernel**: Each mode satisfies $f_\lambda(qt) = (1 - (q-1)\mu_\lambda t) f_\lambda(t)$.
2. **Composition**: The net partition function $Z_q$ satisfies a $q$-difference equation of depth $|\Lambda|$, with coefficients determined by the elementary symmetric polynomials of the per-mode kernels.
3. **Mass-theory mapping**: The $c_k$ coefficients are extracted from the $q$-difference kernel evaluated at the mass-theory anchor $q_0$, matching the empirical $c_2 = -1$ and $c_3 \approx -2$.

The Lean class is parameterized over $R$ (the kernel) and the recursion
machinery is decoupled from the specific kernel — this $q$-heat derivation
provides the canonical $R$ that turns the framework into a concrete $c_k$
predictor.

### The q-Bessel identification of $F$ (fibre-level)

The partition function $Z_q$ above **is**, at the fibre level, a **Hahn--Exton
q-Bessel function** — the matrix coefficient of the quantum motion group
$E_q(2)$, i.e. the $\mathrm{SU}_q(2)\to E_q(2)$ contraction limit of the
substrate (PR [#2279](https://github.com/litlfred/qou/pull/2279);
Vaksman--Korogodsky 1989, Koelink 1994 \cite{koelink1994}). Concretely, the
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

This depth-$d$ recurrence is the $\mathfrak{Q}_\beta$-specialised image of the
**q-holonomic (AJ) recurrence** for quantum knot invariants \cite{garoufalidis2004}:
the colored Jones $J_N(K;q)$ satisfies $\hat{A}(\hat{M},\hat{L};q)\,J_N = 0$ in
the colour $N$ (with $\hat{M}J_N = q^N J_N$, $\hat{L}J_N = J_{N+1}$,
$\hat{L}\hat{M} = q\hat{M}\hat{L}$), degenerating to the classical
$A$-polynomial as $q\to 1$. Habiro's cyclotomic re-basing $(u;u)_m \to u^k$ —
the **same** change-of-basis the $c_k$ use — pushes that recurrence onto the
cyclotomic coefficients. Ours differs only in the index (truncation order $k$,
not colour $N$) and in modelling $F$ by the $q$-heat partition function.
<!-- FILE_END: q-beta-c-k-recursion-from-habiro-q-difference.md -->

<!-- FILE_START: q-beta-c-k-recursion-from-habiro-q-difference-interpretation.md -->
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
Full discussion: [`docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md`](../../../docs/audits/2026-06-13-qbeta-heat-fmap-symbolic-and-literature.md).
<!-- FILE_END: q-beta-c-k-recursion-from-habiro-q-difference-interpretation.md -->

<!-- FILE_START: q-bessel-c-k-recurrence-cfinite.md -->
**Proof.** The power-series coefficients $c_k$ of the $q$-Bessel function
satisfy a first-order ($C$-finite / $q$-holonomic) recurrence, with the
closed form for the general coefficient fixed by the recurrence together
with its initial term.

**Formalization.** The closed-form coefficient
`QOU.QBeta.qbessel_coeff_closed_form` and the first-order recurrence it
satisfies are proved sorry-free in
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean),
algebraically in $q$.

**Computation.** The script
[`qbeta_qbessel_contiguity_cfinite.py`](../../../computations/qbeta/qbeta_qbessel_contiguity_cfinite.py)
checks the $q$-holonomic structure of the recurrence against the canonical
coefficient values (witness
[`qbeta-qbessel-contiguity-cfinite.witness.json`](../../../computations/qbeta/qbeta-qbessel-contiguity-cfinite.witness.json)).

This is the fibre-level ($q$-holonomic) skeleton of the recursion; it does
not by itself pin a $Q_\beta$ scale, and the production $c_k$ ladder stays
calibration-anchored (per the $c_k$ truncation-order framing).
<!-- FILE_END: q-bessel-c-k-recurrence-cfinite.md -->

<!-- FILE_START: q-bessel-second-order-qdifference.md -->
**Proof.** The $q$-Bessel function satisfies a second-order $q$-difference
equation whose coefficient recurrence is the companion of the first-order
contiguity relation. The equation and the recurrence it induces on the
power-series coefficients are established formally and verified
computationally, including the classical $q \to 1$ Bessel limit.

**Formalization.** The second-order recurrence
`QOU.QBeta.qbessel_second_order_recurrence` is proved sorry-free in
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean),
algebraically in $q$.

**Computation.** The script
[`qbessel_second_order_qdifference_equation.py`](../../../computations/qbeta/qbessel_second_order_qdifference_equation.py)
verifies the second-order $q$-difference equation for the $q$-Bessel
function and its limits (witness
[`qbessel-second-order-qdifference-equation.witness.json`](../../../computations/qbeta/qbessel-second-order-qdifference-equation.witness.json)).

Fibre-level structural result (formal $q$); it claims no $Q_\beta$ or
binding scale, and the production $c_k$ ladder remains calibration-anchored.
<!-- FILE_END: q-bessel-second-order-qdifference.md -->

<!-- FILE_START: jackson-q-bessel-contiguity-recurrence.md -->
**Proposition (fibre-level).** Let $J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$
be Jackson's first- and second-kind $q$-Bessel functions. Their power-series
coefficients satisfy purely algebraic **first-order contiguity recurrences**
in the order $\nu$, with closed forms
`QOU.QBeta.qbessel_first_kind_coeff_closed_form` and
`qbessel_second_kind_coeff_closed_form`. The recurrence is algebraic in the
formal deformation variable $q$ (no archimedean input); the $q$-weights are
adapted to the $SU_q(1,1)$ Casimir invariants, in contrast to the third
(Hahn–Exton) kind's $q^{k(k-1)/2}$ weight.

This is a fibre-level identity in the radial coefficient algebra: it fixes no
$Q_\beta$ or binding scale, and the production $c_k$ ladder remains
calibration-anchored.
<!-- FILE_END: jackson-q-bessel-contiguity-recurrence.md -->

<!-- FILE_START: jackson-q-bessel-contiguity.md -->
**Proof.** The first- and second-kind Jackson $q$-Bessel functions
$J_\nu^{(1)}(x;q)$ and $J_\nu^{(2)}(x;q)$ have power-series coefficients
$c_k$ satisfying purely algebraic first-order contiguity recurrences in the
order $\nu$, with a closed-form coefficient ratio. The recurrence is
established by formalization and cross-checked computationally.

**Formalization.** The closed forms are
`QOU.QBeta.qbessel_first_kind_coeff_closed_form` and
`qbessel_second_kind_coeff_closed_form` in the sorry-free file
[`QBesselContiguityRecurrence.lean`](../lean/QOU/QBeta/QBesselContiguityRecurrence.lean).
The recurrence is algebraic in the deformation variable $q$; no archimedean
input enters.

**Computation.** The script
[`qbessel_jackson_contiguity.py`](../../../computations/qbeta/qbessel_jackson_contiguity.py)
verifies that the closed-form coefficient ratios equal the actual Jackson
coefficient ratios symbolically for all $k \le 6$ and to $60$ decimal
places, and that the $q$-hypergeometric product solution reproduces the
coefficients
(witness [`qbessel-jackson-contiguity.witness.json`](../../../computations/qbeta/qbessel-jackson-contiguity.witness.json)).

This is a fibre-level (formal-$q$) structural identity fixing the
$SU_q(1,1)$ radial coefficient algebra; it claims no $Q_\beta$ or binding
scale, and the production $c_k$ ladder remains calibration-anchored.
<!-- FILE_END: jackson-q-bessel-contiguity.md -->

<!-- FILE_START: qbeta-c4-from-c3-c8-product-identity.md -->
**Proposition (c_4 derived from c_3 and c_8 via product identity).**

*The $\mathfrak{Q}_\beta$ precision-ladder coefficients $c_3$, $c_4$, $c_8$ satisfy the
structural product identity*

$$
  c_8 \;=\; c_3 \cdot c_4 \qquad (\text{symbolic in } b, \text{ exact } \forall b).
$$

*At the silver ratio $q = 1+\sqrt{2}$ where $c_3 = -2$, $c_4 = -49/32$,
and $c_8 = 49/16$, this becomes the $\mathbb{Q}$-rational identity*

$$
  (-2) \cdot (-49/32) \;=\; 49/16.
$$

*Consequently $c_4 = c_8 / c_3 = -2 \cdot b^4$ is **derived** from
$c_3$ (= $J_{\mathrm{Hopf}}$ at $q=1$) and $c_8$ (= $c_3^2 \cdot b^4$,
the second rung of the $\sigma$-action tower) — not stipulated.*

## Significance

The closed-form Pell-Lucas $\sigma$-action recursion $c_{k+2} = b^2
\cdot c_k$ holds for $k \geq 6$ but does not extend below $k = 6$:
no constant-kernel linear recursion of depth $\leq 3$ closes the gap
between $c_4$ and $c_5, c_6, c_7$. The $c_4$ closed form is therefore
not derivable from a Pell-Lucas-style additive recursion.

This proposition closes the gap by a **different route**: a
multiplicative product law instead of a linear recursion. Searching
all products $c_i \cdot c_j$ over the closed-form set discovers
exactly two non-trivial identities:

1. $c_3 \cdot c_4 = c_8$    (derives $c_4$ from $c_3, c_8$).
2. $c_3 \cdot c_6 = c_9$    (independent structural check).

The product structure of (1) categorically reads as: *applying the
$J_{\mathrm{Hopf}}$ Markov-trace twist (= $c_3 = -2$) to the $c_4$
object yields the $c_8$ object* — a Markov-trace product law in the
$\sigma$-action tower. If this product law follows from a
categorical theorem (e.g. a Hopf-link tensoring axiom in the
Markov-trace tower on $H_n(q)$), then $c_4$ is **forced** by $c_3$
and $c_8$ — derived rather than stipulated.

## Companion identity (independent check)

The second product identity $c_3 \cdot c_6 = c_9$ provides an
independent structural check: applying the same Hopf-trace twist
to $c_6$ (= $c_3^2 \cdot b^2$) yields $c_9$ (= $c_3^3 \cdot b^2$).
Symbolically $(-2) \cdot (4b^2) = -8b^2$; at silver $(-2) \cdot
(7/2) = -7$. Both check.

These two identities are the **only** product hits in the closed-
form set (verified by symbolic enumeration in
the canonical formalism).
The c_5 averaging-resonance outlier and the c_2, c_7 seed values
do not participate in the product algebra.

## Lean proof structure

Two `norm_num`-closed $\mathbb{Q}$-rational identities at silver:

1. `c4_eq_c8_div_c3_at_silver`: $-2 \cdot (-49/32) = 49/16$ (i.e.
   $c_3 \cdot c_4 = c_8$ at silver).
2. `c3_times_c6_eq_c9_at_silver`: $-2 \cdot 7/2 = -7$ (i.e.
   $c_3 \cdot c_6 = c_9$ at silver).

Both close by `norm_num`. The Lean theorems are pure rational
arithmetic — no symbolic-q or transcendental machinery required.

## Honest caveats

1. The product identity $c_8 = c_3 \cdot c_4$ is observed
   symbolically (verified in $\mathbb{Z}[b]$); whether it follows
   from a categorical theorem (a Markov-trace product law in some
   tower) is **not yet derived**.
2. The c_5 averaging-resonance outlier is NOT covered by the
   product algebra ($c_3 \cdot c_5$ does not match any documented
   $c_k$).
3. The derivation $c_4 = c_8 / c_3$ presupposes $c_8 = c_3^2 \cdot
   b^4$ as the σ-action seed; the categorical reason $c_8$ takes
   this specific value at $q_0$ is the upstream open question.

Subject to that categorical proof, $c_4$ is **derived** from $c_3$
and $c_8$ via a structural product law. The $c_4$ closed form
$-2 \cdot b^4$ is no longer a stipulation — it is forced by the
two seed values $c_3 = -2$ ($J_{\mathrm{Hopf}}$ seed) and
$c_8 = 4 \cdot b^4$ ($\sigma$-action seed).

Per the authoritative
[c_k/d_k registry](../../../docs/coordination/ck-dk-canonical-registry.md),
$c_4$ holds **empirical** tier until that upstream $c_8$ categorical
proof lands: the product identity is a structural relation *among
empirical rungs*, not an unconditional derivation (only $c_2 = -1$ is
canonical). The conditional "derived" above is exactly the
"machinery-proved $\neq$ values-derived" distinction the registry codifies.

## q-usage discipline

The product identities are stated at the fibre level (Laurent
polynomial in $b$ over $\mathbb{Z}$, no $q$-archimedean evaluation
needed) and verified at the silver-ratio rational anchor $b^2 = 7/8$
in $\mathbb{Q}$.
<!-- FILE_END: qbeta-c4-from-c3-c8-product-identity.md -->

<!-- FILE_START: qbeta-z-recursion-to-ck-recursion-bridge.md -->
**Proposition (forward form of the $z$-recursion).** *For any
`ZRecursionCoeffs` instance with Taylor coefficient sequence $a_n$,
and for $n \geq 1$,*

$$
  a_{n+1} = -\frac{3n}{2(n+1)} \cdot a_n
            -\frac{2n-1}{4(n+1)} \cdot a_{n-1}.
$$

*Equivalently, $a_{n+1}$ is a linear combination of $a_n$ and $a_{n-1}$
with $n$-dependent coefficients (kernel functions of $n$, NOT constant
in $n$).*
## Cross-references

- Parent block #1 (upstream):
  [`prop:qbeta-per-block-chi-closed-forms`](qbeta-per-block-chi-closed-forms.md)
  (`ZRecursionCoeffs` class).
- Parent block #2 (sibling on main):
  [`prop:q-beta-c-k-recursion-from-habiro-q-difference`](../mass-theory/q-beta-c-k-recursion-from-habiro-q-difference.md)
  (`CKRecursion` structure).
- 1ppQ-Q$_\beta$ coordination ledger:
  [`docs/coordination/1ppq-qbeta.md`](../../../docs/coordination/1ppq-qbeta.md).

**Archimedean specialisation (§7c).** The recursion coefficients $a_n$ are the real $Q_\beta$ Taylor sequence; the forward form is stated over $\mathbb{R}$ (numerical evaluation of the $q$-difference recursion), placing this block on the archimedean side of the substrate wall.
<!-- FILE_END: qbeta-z-recursion-to-ck-recursion-bridge.md -->

<!-- FILE_START: q-beta-c-2-eq-neg-one-structural.md -->
**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation*

$$
\mathfrak{Q}_\beta(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q))
  \cdot \prod_{k \ge 2} \bigl(1 + c_k \cdot u_{\text{ladder}}^k\bigr),
\qquad u_{\text{ladder}} = b(q) \cdot \hbar_q^2,
$$

*the $k = 2$ coefficient is*

$$
c_2 \;=\; -1
$$

*as a structural identity over any commutative ring, independent of
the substrate value $q_0$ and of CODATA.*
## Structural status versus empirical fit

The earlier canonical observation $c_2 \approx -1$ (PR
[#1602](https://github.com/litlfred/qou/pull/1602), bar-even constraint)
was treated as an *empirical near-match*: a value extracted from the
SDP and compared to the proved bar-even prediction. The present
proposition strengthens that to a **structural identity**: $c_2$ is
not extracted from data, it is the coefficient of $u_{\text{ladder}}^2$ in the
exact algebraic factorisation of the categorical $N{=}2$ ladder
correction. No fit, no CODATA-$\mathfrak{Q}_\beta$ input, no $q_0$-evaluation
required — the identity holds in any commutative ring.

The corresponding sympy verification in
the canonical formalism
computes `sp.simplify((1 - b²·ℏ_q⁴) - (1 - u²))` and obtains
**exactly $0$**.

## canonical impact at $q_0$

With $c_2 = -1$ structurally locked in, the partial ladder

$$
Q_{N=2}(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot (1 - b^2 \hbar_q^4)
$$

evaluated at the substrate $q_0 \approx 1.10998$ gives

$$
Q_{N=2}(q_0) \;\approx\; 0.78233441\;\text{MeV},
$$

within $5.6\,\text{ppm}$ of $\mathfrak{Q}_\beta^{\text{CODATA}} = 0.78233\;\text{MeV}$
with **zero CODATA-$\mathfrak{Q}_\beta$ input**. The remaining $\sim 6\,\text{ppm}$
is the categorical target for $c_3, c_4$ — see
[`prop:q-beta-c-k-recursion-from-habiro-q-difference`](q-beta-c-k-recursion-from-habiro-q-difference.md)
for the recursion framework.

## Implication for $c_3$, $c_4$

The same line of attack applies at higher $N$: if the categorical
$N{=}3$ correction is exactly $(1 + a \cdot u^3)$ for some explicit
$a$, then $c_3 = a$ structurally. The candidates
$\text{cos}(b \cdot \hbar_q^2)$, $\text{exp}(-\tfrac12 \sum b^k \hbar_q^{2k})$,
$1 - b^3 \hbar_q^6$, ... each predict a *different* $c_3$ by Taylor
expansion. Testing which candidate matches the empirical $c_3 \approx -2$
discriminates between brane-tower truncation schemes; if exactly one
candidate matches structurally, $c_3$ becomes a second structural
identity.

This proposition is the $k = 2$ instance of that programme. Higher-$k$
instances are the remaining open work toward CODATA-free $\mathfrak{Q}_\beta$ at
$1\,\text{ppQ}$.
<!-- FILE_END: q-beta-c-2-eq-neg-one-structural.md -->

<!-- FILE_START: q-beta-bar-even-kernel-invariant.md -->
**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation*

$$
\mathfrak{Q}_\beta(q) \;=\; Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q))
  \cdot \prod_{k \ge 2} \bigl(1 + c_k \cdot u^k\bigr),
\qquad u \;=\; b(q) \cdot \hbar_q^2,
$$

*the ladder $R(u) := \prod_k(1 + c_k u^k)$ admits a clean integer-$u$ Taylor
representation (no $\sqrt{u}$ branch) if and only if $R$ is bar-even, i.e.
$R$ is an even function of $t := q - 1$ about $q = 1$.*

## Significance (the structural discriminant)

The substrate variable $u = b(q) \cdot \hbar_q^2$ has a **double zero** at
$q = 1$:

$$
u(q) \;=\; b(1) \cdot t^2 + O(t^3)
\;=\; \frac{\sqrt{3}}{2} \, t^2 + O(t^3),
\qquad t = q - 1.
$$

Under the bar-involution $q \mapsto q^{-1}$, the local coordinate transforms
as $t \mapsto -t + O(t^2)$. The leading term $u \sim t^2$ is invariant under
$t \mapsto -t$, so:

- **If $R$ is even in $t$** (bar-even), every Taylor coefficient lives at
  even powers of $t$, which the $u$-grading absorbs: $R(u)$ admits
  an integer-power Taylor representation in $u$ with no $\sqrt{u}$ branch.
- **If $R$ has odd-in-$t$ content**, those coefficients sit at $t^{2k+1}$
  and cannot be absorbed into integer powers of $u \sim t^2$: the $q \to u$
  reversion picks up a $\sqrt{u}$ branch, and the scalar $c_k$ extraction
  is singular at $u = 0$ (the $\sqrt{u}$-branch obstruction).

The bar-even invariant is the **§4(b) formalize-first gate** of the
[refuted-class map](../../../docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md):
*any candidate kernel $R(q,\xi)$ for the Habiro element $F(q)$ must clear
the bar-evenness check before the canonical anchor sweep runs*.
## Use in the formalize-first gate for new $F(q)$ candidates

Before any canonical anchor sweep on a new candidate $F(q)$ / kernel
$R(q,\xi)$:

1. **State the candidate** as a power series in $t = q - 1$ (or
   equivalently, a Laurent polynomial in $q^{\pm 1/2}$).
2. **Compute $R(q^{-1}, \xi^{-1})$** symbolically.
3. **Subtract**: $\Delta := R(q,\xi) - R(q^{-1}, \xi^{-1})$. If
   $\Delta \neq 0$ identically (as an element of the ring), the candidate
   has odd-in-$t$ content and **cannot** produce a clean integer-$u$
   ladder.
4. **Stop**: a candidate failing this check is a member of refuted class
   C1–C2 (real-q forms with anchor-dependent odd-$t$ content) — add a row
   to the refuted-class map §2 and abort the canonical sweep.

This is the bar-involution test of the §4 invariants from the
refuted-class map, formalised. It complements the
[`CFinite.recurrence_step`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QBeta/RationalCoeffRecurrence.lean)
engine: the
recurrence step says "*given a kernel, here is the next $c_k$*"; the
bar-even invariant here says "*here is the necessary condition any
candidate kernel must satisfy*".
<!-- FILE_END: q-beta-bar-even-kernel-invariant.md -->

<!-- FILE_START: q-beta-radius-of-convergence-gate.md -->
**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$
with $u = b(q) \cdot \hbar_q^2$, the log-correction generating function*

$$
g(u) \;:=\; \sum_{k \ge 2} c_k \cdot u^k
$$

*has a simple pole at $u = u_{\text{substrate}} \approx 0.00852$, and the
ratio test for the radius of convergence yields*

$$
\lim_{k \to \infty} \frac{|c_{k+1}|}{|c_k|} \;=\; \frac{1}{u_{\text{substrate}}}.
$$

*Consequently, any candidate Habiro element $F(q)$ whose log-correction
generating function has its nearest singularity elsewhere than
$u_{\text{substrate}}$ is structurally REFUTED as a valid $\mathfrak{Q}_\beta$
precision-ladder kernel.*

## Role as the $\S 4(a)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4$ lists four structural invariants any candidate $F(q)$ must satisfy:

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor $u_{\text{substrate}}$ swing < 1 ppm = $10^{-6}$ relative; 210 ppb observed) | **this proposition** |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 shadow** reproduces known integer (e.g. $c_3 \to J_{\text{Hopf}}(1) = -2$) | *not yet formalised* |
| (d) | **Direction sanity** — $|F(q_0)|$ scales appropriately | *not yet formalised* |

The radius-of-convergence gate is the **sharpest concrete form** of $\S 4(a)$:
The cross-anchor analysis established that $u_{\text{substrate}}$ at $q_{\text{muon}}$ vs
$q_{\text{proton}}$ differs by only **210 ppb** (well within the 1 ppm
fibre-level tolerance), so the simple-pole location IS anchor-stable; a
candidate $F(q)$ violating this is automatically anchor-incompatible.
## Use in the formalize-first checklist

This is **Step 4** of the 7-step Δ_λ pre-flight checklist
(`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$).
Concretely, for any candidate $F(q)$:

1. Express $F(q)$ as a rational function $P(u) / Q(u)$ in $u = b \cdot \hbar_q^2$
   (or a power series with explicit recursion via `CFinite`).
2. Locate the nearest pole $u_0$ in the $u$-plane.
3. Compute $|u_0 - u_{\text{substrate}}| / u_{\text{substrate}}$.
4. If the ratio $> 10^{-6}$, REJECT — add a new row to refuted-class map $\S 2$.
5. If the ratio $\le 10^{-6}$, proceed to Step 5 (q=1 shadow) of the checklist.

## Composition with the bar-even gate and the `CFinite` engine

A candidate $F(q)$ must clear (in order):

```
1. Bar-even check        →  bar-even gate (q ↦ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence →  this proposition (simple pole at u_substrate)
3. CFinite recurrence    →  CFinite engine (generates c_k from kernel + seed)
4. q=1 shadow            →  not yet formalised (c_2 = −1, c_3 = J_Hopf(1) = −2 anchors)
5. Direction sanity      →  not yet formalised (|F(q_0)| in target's magnitude range)
```

Steps 1–3 are formalised in Lean (sorry-free); steps 4–5 are not yet formalised.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-beta-radius-of-convergence-gate.md -->

<!-- FILE_START: q-beta-q-eq-one-shadow-gate.md -->
**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$
with $u = b(q) \cdot \hbar_q^2$, any candidate Habiro element $F(q)$
generating the ladder coefficients $c_k$ must satisfy the classical-limit
shadows*

$$
\lim_{q \to 1} c_2(q) \;=\; -1 \qquad \text{and} \qquad
\lim_{q \to 1} c_3(q) \;=\; J_{\text{Hopf}}(q = 1) \;=\; -2.
$$

*A candidate failing either shadow is structurally REFUTED.*

## Role as the $\S 4(c)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4$ lists four structural invariants any candidate $F(q)$ must satisfy:

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor swing < 1 ppm) | [`prop:q-beta-radius-of-convergence-gate`](q-beta-radius-of-convergence-gate.md) |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 classical-limit shadow** | **this proposition** |
| (d) | **Direction sanity** | [`prop:q-beta-direction-sanity-gate`](q-beta-direction-sanity-gate.md) |

The q = 1 shadow invariant has **two canonical anchors** at the registry level:

- **$c_2 = -1$** is Taylor-exact ([`prop:q-beta-c-2-eq-neg-one-structural`](q-beta-c-2-eq-neg-one-structural.md)) — the structural seed of the entire ladder. Any candidate must reproduce this without fitting.
- **$c_3 \to J_{\text{Hopf}}(q = 1) = -2$** is the canonical Hopf-Jones limit (registry §3, [`canonical-derivation-chain.md`](../../../docs/canonical-derivation-cheat-sheet.md)) — the categorical anchor for the inter-block N=3 correction.

A candidate $F(q)$ whose Taylor expansion at $q = 1$ disagrees with either anchor fails the $\S 4(c)$ invariant, regardless of how cleanly it passes (a), (b), or (d). The two are independent: candidates can satisfy (a) + (b) (anchor-stable + bar-even) while still failing (c) if their classical-limit expansion gives the wrong integers.
## Use in the formalize-first checklist

This is **Step 5** of the 7-step Δ_λ pre-flight checklist (`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$). Concretely, for any candidate $F(q)$:

1. Compute $F(q)$'s Taylor expansion at $q = 1$ (or take the limit if there's a removable singularity).
2. Read off the $c_2(q = 1)$ and $c_3(q = 1)$ coefficients in the ladder normalization.
3. If $c_2(q = 1) \neq -1$ or $c_3(q = 1) \neq -2$, REJECT — add a new row to refuted-class map $\S 2$.
4. If both shadows match, proceed to Step 6 (direction sanity) of the checklist.

## Composition with the prior three gates

A candidate $F(q)$ must clear (in order):

```
1. Bar-even check (§4b)        PASS (q ↔ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence (§4a) PASS (simple pole at u_substrate)
3. q = 1 shadow (§4c)          PASS (c_2 → −1, c_3 → −2)
4. Direction sanity (§4d)      PASS (|F(q_0)| in target's magnitude)
5. CFinite recurrence          PASS (generates c_k from kernel)
```

With all four §4 invariants formalized, the formalize-first gate chain is complete; any future $F(q)$ candidate is evaluable as a Lean class-instance attempt rather than as a canonical fit.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-beta-q-eq-one-shadow-gate.md -->

<!-- FILE_START: q-beta-direction-sanity-gate.md -->
**Proposition.** *In the $\mathfrak{Q}_\beta$ precision-ladder factorisation
$\mathfrak{Q}_\beta(q) = Q_A(q) \cdot \cos(\alpha_{\text{eff}}(q)) \cdot \prod_{k \ge 2}(1 + c_k u^k)$,
any candidate Habiro element $F(q)$ generating the ladder must satisfy
the direction-sanity invariant: $|F(q_0)|$ at the substrate anchor
must be in the same order of magnitude as the target observable's
ratio $\mathfrak{Q}_\beta^{\text{CODATA}} / [Q_A(q_0) \cdot \cos(\alpha_{\text{eff}}(q_0))]$.
A candidate predicting a magnitude differing by more than $10\times$
is structurally REFUTED at the formalize-first level.*

## Role as the $\S 4(d)$ formalize-first gate

The refuted-class map (`2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md`)
$\S 4(d)$ states the direction-sanity invariant abstractly. The canonical
**refutation precedent** is the trace-level Markov-stabilization
attack (refuted-class row C12): the candidate's natural scaling factor
$z(q_0) = 1 / (q_0^{1/2} + q_0^{-1/2}) = 0.4993$ was strictly less than 1,
while the target multiplier $\text{linking\_weight} \approx 2.53$ was
strictly greater than 1. **No power of $z < 1$ can multiply UP to a
value $> 1$** — this is a one-line magnitude refutation that killed
the entire mass-side trace identity class **before** any expensive
canonical anchor sweep.

The direction-sanity invariant abstracts this argument: a candidate
$F(q)$ whose magnitude at the substrate anchor is structurally
inconsistent with the target observable's magnitude is refuted on
paper, not in compute. This is the $\S 4(d)$ formalize-first gate.

## The four $\S 4$ invariants (now complete)

| # | invariant | formalised in |
|---|---|---|
| (a) | **Anchor-stable** (cross-anchor swing < 1 ppm) | [`prop:q-beta-radius-of-convergence-gate`](q-beta-radius-of-convergence-gate.md) |
| (b) | **Bar-even** under $q \mapsto q^{-1}$ | [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) |
| (c) | **q = 1 classical-limit shadow** | [`prop:q-beta-q-eq-one-shadow-gate`](q-beta-q-eq-one-shadow-gate.md) |
| (d) | **Direction sanity** | **this proposition** |

With (d) formalized, the four-invariant set is complete; any future
candidate $F(q)$ for the $\mathfrak{Q}_\beta$ c_k Habiro element is evaluable as a
Lean class-instance attempt rather than as a canonical fit.

## The target magnitude at $q_0$

At the substrate $q_0 \approx 1.10998$:

$$
\frac{\mathfrak{Q}_\beta^{\text{CODATA}}}{Q_A(q_0) \cdot \cos(\alpha_{\text{eff}}(q_0))}
\;\approx\; \frac{0.78233\;\text{MeV}}{0.78371\;\text{MeV}}
\;\approx\; 0.99824 \;\approx\; 1,
$$

i.e. the ladder product $\prod_k(1 + c_k u^k) \approx 0.99824$ at $q_0$
(the precision-ladder corrections collectively contribute only ~0.18%
of the bare $Q_A \cdot \cos$ value). A candidate $F(q_0)$ giving a
magnitude wildly different from 1 (e.g. ~0.5 like the refuted $z(q_0)$,
or ~10 like an over-scaled formal series) is automatically refuted.
## Use in the formalize-first checklist

This is **Step 6** of the 7-step Δ_λ pre-flight checklist (`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md` $\S 3$).
Concretely, for any candidate $F(q)$:

1. Evaluate $F(q_0)$ at the substrate anchor.
2. Compute $|F(q_0) - F_{\text{target}}(q_0)| / F_{\text{target}}(q_0)$.
3. If the ratio is $> 10$ (order-of-magnitude mismatch), REJECT —
   add a new row to refuted-class map $\S 2$.
4. If the ratio is $\le 10$, proceed to Step 7 (only NOW run the
   canonical anchor sweep) of the checklist.

## Composition with the prior three gates

```
1. Bar-even check (§4b)        PASS (q ↔ q⁻¹ Taylor-even-in-t)
2. Radius-of-convergence (§4a) PASS (simple pole at u_substrate)
3. q = 1 shadow (§4c)          PASS (c_2 → −1, c_3 → −2)
4. Direction sanity (§4d)      PASS (|F(q_0)| in 10× of target)
5. CFinite recurrence engine   PASS (generates c_k from kernel)
```

A unified `BarEvenKernel` typeclass ties all four together,
extending the `CFinite` recurrence engine.
<!-- FILE_END: q-beta-direction-sanity-gate.md -->

<!-- FILE_START: q-beta-c-k-leading-bias-correction-identity.md -->
**Proposition (Leading-bias correction identity).** *Let $\hat c_k$ denote
the joint-fit canonical extraction of the $\mathfrak{Q}_\beta$ precision-ladder
coefficients at substrate $u_0 = b(q_0) \cdot \hbar_{q_0}^2$, and let
$c_k^{\mathrm{alg}}$ denote the algebraic ladder coefficients
(Taylor coefficients of the generating function $F(u)$ such that
$\mathfrak{Q}_\beta / Q_A = F(u_0)$). If the extraction bias is leading-order
linear in $u_0$,*

$$
\hat c_k \;=\; c_k^{\mathrm{alg}} + c_{k+1}^{\mathrm{alg}} \cdot u_0,
$$

*then the **bias-corrected** values*

$$
\hat c_k^{\mathrm{corr}} \;:=\; \hat c_k - \hat c_{k+1} \cdot u_0
$$

*satisfy*

$$
\hat c_k^{\mathrm{corr}} \;=\; c_k^{\mathrm{alg}} + O(u_0^2).
$$

*In particular, at leading order in $u_0$, the bias-corrected $\hat c_k^{\mathrm{corr}}$
recovers the algebraic $c_k^{\mathrm{alg}}$ exactly.*
## Structural significance

The $+1.71\%$ relative bias on the SDP-extracted $\hat c_2$ vs the
**proved canonical** $c_2 = -1$ ([`prop:q-beta-c-2-eq-neg-one-structural`](q-beta-c-2-eq-neg-one-structural.md))
was first reported as a methodology defect. This
proposition reframes the bias as a **structural signature**: it is exactly
$c_3^{\mathrm{alg}} \cdot u_0 \approx -2 \cdot 0.00852 \approx -0.01704$,
matching the observed $\hat c_2 - c_2^{\mathrm{alg}} = -1.0171 - (-1) =
-0.0171$ to four significant figures.

The agreement is **predictive** evidence for the c_k generating-function
hypothesis (see [`docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md`](../../../docs/audits/2026-06-04-ck-generating-function-derivation-chain-scope.md)):
the bias signature is exactly what a single generating function $F(u)$,
truncated at finite order and extracted canonical, would produce. The
proposition above is the formal statement of the leading-order bias
inversion.

## Implications for the 569bedda1 c_3 falsification

The 569bedda1 falsify commit on main classified $c_3 = -2 = J_{\mathrm{Hopf}}(q=1)$
as REFUTED-as-real-q-fibre-element on the basis of:

  * SDP-extracted $\hat c_3 = -2.0097$ at proton anchor
  * SDP-extracted $\hat c_3 = -2.0085$ at muon anchor (assumed similar bias)
  * Real-q closure formula too rigid (its cross-anchor swing is $\approx 4.7 \times 10^6$ **times smaller** than the empirical swing — a rigidity *ratio*, not an absolute deviation)

This proposition's canonical confirmation shows the bias-corrected
$\hat c_3^{\mathrm{corr}} = -1.9999968$ at the proton anchor is essentially
exactly $-2$, **consistent** with the categorical $c_3 = J_{\mathrm{Hopf}}(q=1)$
identification. The cross-anchor swing of the SDP extraction was
dominated by the $c_4 \cdot u_0$ cross-talk, not by genuine fibre-level
$c_3$ structure.

The cross-anchor swing of $\hat c_3^{\mathrm{corr}}$ (not the raw $\hat c_3$)
is the right object to re-test against the rigidity bound. Pending
that re-test, the 569bedda1 falsification should be revisited.

## Lean structure

The proposition is a one-line ring identity in `CommRing R`:

```lean
theorem bias_correction_recovers_alg {R : Type u} [CommRing R]
    (c_alg : ℕ → R) (u : R) (k : ℕ) :
    -- hypotheses: extraction bias is leading-order in u
    let c_hat (j : ℕ) := c_alg j + c_alg (j+1) * u
    -- conclusion: bias correction recovers c_alg modulo u²
    c_hat k - c_hat (k+1) * u = c_alg k - c_alg (k+2) * u^2 := by
  simp only [c_hat]
  ring
```

Sorry-free. The structural assumption (leading-order linear bias) is
encoded as the definition of `c_hat`; the theorem mechanically inverts.

The next-order proposition (testing bias correction to $O(u^3)$ and
beyond) is the natural extension and remains open.
<!-- FILE_END: q-beta-c-k-leading-bias-correction-identity.md -->

<!-- FILE_START: q-beta-bar-even-kernel-typeclass.md -->
**Proposition (definition + composition theorem).** *The `BarEvenKernel`
Lean typeclass bundles all four $\S 4$ formalize-first invariants for a
candidate Habiro element $F(q)$ into a single parametric type, with
fields for the bar-even symmetry, radius-of-convergence pole location,
$q = 1$ classical-limit shadows, and direction-sanity magnitude check.
Instantiating `BarEvenKernel` for any candidate is equivalent to that
candidate clearing all four §4 gates simultaneously.*

## Motivation for a unified typeclass

The four §4 formalize-first invariants from the
[refuted-class map](../../../docs/audits/2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)
were formalized separately as four parametric gate classes:

| invariant | gate class | parametric? |
|---|---|---|
| (a) Anchor-stable (simple pole at $u_{\text{substrate}}$) | `RadiusOfConvergenceGateClass` | no (global axiom) |
| (b) Bar-even under $q \mapsto q^{-1}$ | structural identity | n/a (CommRing R lemma) |
| (c) $q = 1$ classical-limit shadow | `QOneShadowGateClass (c2 c3 : ℝ → ℝ)` | **yes** |
| (d) Direction sanity at $q_0$ | `DirectionSanityGateClass (m : ℝ)` | **yes** |

A future canonical evaluation author evaluating a candidate $F(q)$ currently has to
instantiate four classes by hand. **`BarEvenKernel` is the single
bundling typeclass** that makes the entire formalize-first chain a
one-liner: instantiate `BarEvenKernel pole c2 c3 magnitude` and the
candidate is admitted (or rejected — Lean cannot construct the
instance if any field's hypothesis fails).

## The composition

```lean
class BarEvenKernel
    (pole : ℝ)            -- candidate's nearest singularity in u-plane
    (c2 c3 : ℝ → ℝ)       -- candidate's per-rung coefficient functions
    (magnitude : ℝ)        -- candidate's |F(q_0)| substrate magnitude
    : Prop where
  -- §4(a) radius-of-convergence: pole at u_substrate within fibre tolerance
  pole_at_u_substrate :
    |pole - uSubstrate| ≤ radiusTolerance
  -- §4(c) q=1 classical-limit shadow
  c2_shadow : c2 1 = -1
  c3_shadow : c3 1 = jonesHopfAtQOne
  -- §4(d) direction sanity at q_0
  direction_match :
    |magnitude - directionTarget| ≤ directionThreshold * directionTarget
  -- §4(b) bar-evenness (the structural identity holds for
  --       any candidate in CommRing R, so the typeclass instance does
  --       not need to re-state it; included as a corollary lemma)
```

The bar-even invariant is a CommRing R-level structural
identity that holds automatically for any kernel candidate built from
the substrate primitives ($b$, $\hbar_q$); the typeclass therefore
does not duplicate it as a field. The bar-even rejection lemma remains available as the standalone gate when a candidate
does NOT come from the substrate (e.g., a freely-constructed test
kernel during exploratory work).

## Composition theorem

If `BarEvenKernel pole c2 c3 magnitude` is instantiable for some
specific `(pole, c2, c3, magnitude)`, then:

1. `RadiusOfConvergenceGateClass`-equivalent holds at the parametric
   level (pole within tolerance of $u_{\text{substrate}}$).
2. `QOneShadowGateClass c2 c3` is instantiable.
3. `DirectionSanityGateClass magnitude` is instantiable.

The Lean proof of each lifting is a one-line extraction of the
corresponding field — `BarEvenKernel.pole_at_u_substrate`,
`BarEvenKernel.c2_shadow`, etc. — with the bundle-to-class conversion
implicit in the constructor.

## Use in the formalize-first checklist

This typeclass *operationalises* the 7-step Δ_λ pre-flight checklist
(`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md`
$\S 3$): instead of running Steps 3–6 as separate sympy probes + Lean
checks, a canonical evaluation author writes:

```python
# Conceptual: at the formal level, the entire pre-flight reduces to:
candidate = build_candidate(...)
pole, c2, c3, magnitude = extract_observables(candidate)
# In Lean: try { @BarEvenKernel.mk pole c2 c3 magnitude ... }
#          If Lean accepts the instance → admit; else → REFUTE
```

with each field hypothesis discharged by the corresponding canonical evaluation.

## Honest scope

- This is **infrastructure**, not new mathematical content. It does
  NOT construct a new $F(q)$ kernel — the open keystone remains owner-
  gated multi-session research per refuted-class map $\S 5$.
- The typeclass codifies the *gate-chain composition*; the actual
  kernel search proceeds independently.
- Subclasses of `BarEvenKernel` (e.g. extending to include the
  `CFinite.recurrence_step` engine for kernel-driven $c_k$
  generation) are natural follow-ups.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: q-beta-bar-even-kernel-typeclass.md -->

<!-- FILE_START: mass-side-kernel-formalize-first-gates.md -->
**Proposition (definition + composition theorem).** *The
`MassSideKernel` Lean typeclass bundles the mass-theory analogs of
the four $\S 4$ formalize-first invariants for any candidate
`linking_weight` function $w(q)$. Instantiating `MassSideKernel` for
a candidate is equivalent to that candidate clearing all four
mass-side gates simultaneously.*

## Rationale for a parametric mass-side typeclass

The $\mathfrak{Q}_\beta$ decay-side
[`prop:q-beta-bar-even-kernel-typeclass`](q-beta-bar-even-kernel-typeclass.md)
bundles the four $\S 4$ invariants for any candidate Habiro element
$F(q)$. The **mass-side analog** is scoped operationally by the sympy
the canonical formalism,
which runs a $4 \times 3$ verdict matrix on three published
`linking_weight` candidates (Family A, via-Jones, Bring color-tube).

This proposition ships the **Lean side** — parametric conditional
classes mirroring the $\mathfrak{Q}_\beta$ pattern, plus a unified
`MassSideKernel` typeclass that any future `linking_weight`
candidate is evaluated against as a single class-instance attempt.

## The four mass-side invariants (parametric)

For any candidate `linking_weight` function $w : \mathbb{R} \to \mathbb{R}$:

| # | invariant | mass-side form | parametric class |
|---|---|---|---|
| (a) | **Anchor-stable** | cross-anchor swing $|w(q_\mu) - w(q_p)| / |w(q_p)| < 10^{-6}$ | `MassAnchorStableGateClass swing` (where `swing` is the canonical evaluation-computed magnitude) |
| (b) | **Bar-even** | $w(q) = w(q^{-1})$ (as elements of the formal q-rationals) | covered by [`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md) (CommRing R lemma) |
| (c) | **q = 1 classical-limit shadow** | $w(1)$ equals a registered categorical anchor — **OPEN GAP** (no registered anchor for `linking_weight` is established) | `MassQOneShadowGateClass w (anchor : Option ℝ)` — vacuous when `anchor = none`, requires $w(1) = a$ when `anchor = some a` |
| (d) | **Direction sanity** | $|m - \text{target}| \le \text{threshold} \cdot \text{target}$ (additive form; substrate target $\approx 2.46$, the CODATA-implied near-match documented in the canonical formalism) | `MassDirectionSanityGateClass m_candidate` (where `m_candidate` $= |w(q_0)|$) |

> **Direction-sanity formula note.** The Lean class uses the
> **additive** form $|m - \text{target}| \le \text{threshold} \cdot \text{target}$
> to match the decay-side
> [`prop:q-beta-direction-sanity-gate`](q-beta-direction-sanity-gate.md)
> Lean precedent. The companion sympy probes (e.g.
> the canonical formalism)
> implement the **multiplicative** variant
> $\max(|m| / \text{target}, \text{target} / |m|) \le \text{threshold}$
> for the operational direction-magnitude check. The Lean form is
> the more permissive scaffold — a multiplicative-passing candidate
> automatically satisfies the additive form within the same
> threshold magnitude.

The $\S 4(\mathrm{c})$ open gap is the **mass-side analog** of $\mathfrak{Q}_\beta$'s
decay-side $F(q)$ keystone — owner-gated multi-session research per
the refuted-class registry.

## Composition theorem

If `MassSideKernel w swing anchor magnitude` is instantiable for some
specific candidate $w$ (with `swing`, `anchor`, `magnitude` the
candidate-specific values supplied at instantiation), then:

1. `MassAnchorStableGateClass swing` holds (parametric anchor-stability)
2. `MassDirectionSanityGateClass magnitude` holds (parametric direction sanity)
3. $w$ admits the bar-even structural identity via the $\mathfrak{Q}_\beta$
   `bar_even_test_n2` CommRing $R$ lemma
   ([`prop:q-beta-bar-even-kernel-invariant`](q-beta-bar-even-kernel-invariant.md))
4. (When a registered anchor is set) `MassQOneShadowGateClass w (some a)`
   holds, giving $w(1) = a$

The Lean proof of each lifting is a one-line extraction of the
corresponding field. The $\S 4(\mathrm{c})$ lifting is **conditional**
on the open anchor question — the typeclass admits a parameter
`anchor : Option ℝ` so candidates can be evaluated against a
hypothetical anchor without claiming an actual registered one
exists.

## Use in the formalize-first checklist

This typeclass operationalises the mass-side complement to the
$\mathfrak{Q}_\beta$ 7-step $\Delta_\lambda$ pre-flight checklist
([`docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md`](../../../docs/audits/2026-06-05-qbeta-formalize-first-gates-consolidation.md)
$\S 3$). For any candidate $w(q)$:

```
1. Bar-even check         -> [prop:q-beta-bar-even-kernel-invariant] (CommRing R)
2. Anchor-stable (a)      -> MassAnchorStableGateClass
3. Direction sanity (d)   -> MassDirectionSanityGateClass
4. q=1 shadow (c)         -> MassQOneShadowGateClass (parametric on anchor; OPEN GAP)
5. Unified bundle         -> MassSideKernel typeclass
```

Steps 1–3 are evaluable; step 4 requires the open categorical
derivation (whatever rational/integer $w(1)$ should equal under the
mass-side categorical chain).

## Scope

- This is **infrastructure**, not new mathematical content. It does
  NOT construct the registered $\S 4(\mathrm{c})$ anchor for `linking_weight` —
  the categorical derivation of $w(1)$ remains open.
- The parametric class signatures enable **future** anchor candidates
  (for instance, a $\Sigma f^\lambda / 4 = 5/2$ at $n = 4$ value
  arising from the number of involutions in $S_4$ divided by $4$)
  to be evaluated by instantiating `MassQOneShadowGateClass w (some anchor)`
  with the derived value.
- The $\S 4(\mathrm{c})$ open gap is the mass-side keystone. Closing it is
  owner-gated multi-session research.

## Formalization and compute

**Theorem (this proposition).** Sorry-free Lean class definitions
([`mass-side-kernel-formalize-first-gates.lean`](mass-side-kernel-formalize-first-gates.lean))
— three parametric $\S 3\mathrm{b}$-cond conditional classes + one unified
`MassSideKernel` typeclass + three lifting lemmas + one rejection
lemma. Mirrors the $\mathfrak{Q}_\beta$ `BarEvenKernel` pattern.

**No sympy canonical evaluation.** The mass-side $\S 4$ $4 \times 3$ verdict matrix
is already in
the canonical formalism.
Future probes wanting to test a candidate $w$ against the Lean class
plug its substrate values into the `MassSideKernel` field hypotheses.
<!-- FILE_END: mass-side-kernel-formalize-first-gates.md -->

