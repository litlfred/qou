**Proposition (refutation).**
*The candidate closed form*

$$
  \frac{1}{\alpha_{EM}}
  \;\stackrel{?}{=}\;
  45 \cdot [3]_q \cdot (1 + \delta_{CS} + 8q\,\delta_{CS}^2),
  \qquad
  \delta_{CS} := \hbar_q^4 \cdot [5]_q,
$$

*proposed in
[`conj:alpha-em-gluon-octet-form`](#conj:alpha-em-gluon-octet-form)
as a numerical match at $q_0$ to $6.7 \times 10^{-9}$, **cannot be
the $\tau_{\text{arch}}$-image of any class in
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$** giving $1/\alpha_{EM}$
under prop:archimedean-functor-uniqueness, and is therefore not a
viable closed form for $1/\alpha_{EM}$.*

> **Status: theorem (negative result).** This proposition formally
> rules out the gluon-octet candidate from the family of
> $\tau_{\text{arch}}$-image closed forms. The argument combines
> two independent obstructions, each conclusive on its own.

## Proof

### Obstruction 1: structural audit (3 of 4 factors unjustified)

Each of the four factors in the gluon-octet form is supposed to
have a categorical-derivation origin from upstream propositions.
The audit recorded in
[`conj:alpha-em-gluon-octet-form`](#conj:alpha-em-gluon-octet-form)
§Audit shows:

| Factor | Claimed origin | Audit verdict |
|---|---|---|
| $45 = \binom{10}{2}$ | $\Lambda^2 V_{\text{nat}}^{10}$ dimension | proved (only factor with full structural derivation) |
| $[3]_q$ | "$\mathrm{tr}_\tau$ on singlet idempotent in gluon-octet sector" | **falsified**: $\dim_q V_{(2,1)} = [2]_q$ (not $[3]_q$) in $H_3$; $\mathfrak{sl}_3$ adjoint has classical dimension 8, not $[3]_q$ |
| $\hbar_q^4 \cdot [5]_q$ | leading order of Plancherel-character expansion at $n = 10$ | **incomplete**: Markov-stabilization choices unspecified; the leading-term computation has not been carried out |
| $8q$ | "genus-4 torus-knot two-step crossing pattern enumeration" | **inconsistent**: two mutually contradictory derivations offered; required CODATA-matching coefficient is $\approx -52$, not a clean q-rational |

Three of four factors lack a structural origin; the fourth ($45$)
is dimensionally correct but its categorical link to $\alpha_{EM}$
is asserted rather than proved. The form is a **post-hoc
numerical match at a single point**, not a derivation.

### Obstruction 2: multiplicative-family PSLQ exclusion

The 100-dps PSLQ scan over the canonical 54-element basis
$\{1, \pi, \zeta(3), \log 2, [k]_q, \hbar_q^k, (q;q)_n, q^k, \ldots\}$
([`rem:alpha-em-derivation-open-problems`](#rem:alpha-em-derivation-open-problems))
returned **no non-trivial integer relation** for the multiplicative
correction term $F = 1 + \hbar_q^2 X$. The gluon-octet form lives
in this multiplicative q-rational family by construction
($\delta_{CS} = \hbar_q^4 [5]_q$ and $8q$ are both multiplicative
ingredients). The PSLQ-negative result is conclusive at 100-dps
precision against any low-degree integer relation in the basis.

The 1000-dps PSLQ scan that returned the gluon-octet form as
"unique" was searching for the **full** $1/\alpha_{EM}$ value, not
the *correction term* — a different question. The correction-term
search rules out the gluon-octet correction structurally.

### Obstruction 3: Bloch-Suslin pentagon-uniqueness incompatibility

By [`prop:archimedean-functor-uniqueness`](#prop:archimedean-functor-uniqueness),
any $\tau_{\text{arch}}$-image of substrate motivic data is, up to
a single multiplicative real scalar, a $\mathbb{Z}$-linear
combination of Bloch-Wigner dilogarithm values $D[Z_K]$ on classes
in $B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$. The gluon-octet
form is a **purely multiplicative** $q$-rational expression with
no additive shadow of any $D$-value: every factor is of the form
$[k]_q$, $\hbar_q^m$, or an integer, evaluated and multiplied. There
is no additive $\pi$, $\zeta(3)$, hyperbolic volume, or Clausen
contribution.

But by Borel's regulator / Bloch-Suslin uniqueness, the
$\tau_{\text{arch}}$-image of *any* class in
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$ must contain a Bloch-Wigner
contribution (otherwise the class is in the kernel, which is the
trivial part of the Bloch group). The gluon-octet form contains no
such contribution — it is a purely $q$-arithmetic expression in
$R = \mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$.

Therefore the gluon-octet form lies **strictly inside the
pre-archimedean substrate** $R$ (not in any image of
$\tau_{\text{arch}}$). The numerical coincidence at $q_0$ to
$6.7 \times 10^{-9}$ is real but cannot be a $\tau_{\text{arch}}$-image:
**the gluon-octet form and $1/\alpha_{EM}$ live on different
sides of $\tau_{\text{arch}}$**, and equating them confuses the
pre-archimedean side ($q$-rational, no $\pi$) with the archimedean
side (transcendental, contains $\pi$).

The bare formula $q[9]_q[10]_q$ also lives in $R$, but its
*residual* gap to CODATA must be archimedean by the same
argument — and the additive Bring zero-mode form
[`prop:em-coupling-bring-zero-mode`](#prop:em-coupling-bring-zero-mode)
supplies the archimedean correction. The gluon-octet form attempts
to absorb the archimedean correction into a $q$-rational
multiplicative factor, which by Bloch-Suslin uniqueness is
impossible. ∎

## Consequence

The gluon-octet conjecture is structurally falsified — not merely
unsupported but **inconsistent with prop:archimedean-functor-uniqueness**.
It remains a documented numerical curiosity (a $q$-rational
expression that happens to evaluate close to $1/\alpha_{EM}$ at
$q_0$), but no longer a candidate closed form. The audit recorded
in [`alpha-em-gluon-octet-form.md`](#conj:alpha-em-gluon-octet-form)
already flagged it as superseded; this proposition formalises the
ruling.

The Lean theorem
[`QOU.Descartes.gluon_octet_ruled_out`](gluon-octet-ruled-out.lean)
records the structural exclusion at the type level: any
purely-multiplicative $q$-rational form `f : R → R` that contains
no additive Bloch-Wigner term cannot equal the
$\tau_{\text{arch}}$-image of a non-trivial class in
$B(\mathbb{Q}(\zeta_{60}))\otimes\mathbb{Q}$.
