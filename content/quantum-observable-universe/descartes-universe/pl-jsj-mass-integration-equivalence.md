**Conjecture (PL/JSJ mass-integration equivalence — synthesis form).**
*The inertial mass of a transient categorical state is identically
evaluated on both sides of the Archimedean boundary $\tau$:*

- *(**Algebraic side, $R$.**) The Markov trace of the transfer
  matrices up the active filtration shell — equivalently, the
  Frobenius-paired evaluation of the $q$-Pochhammer partial product
  $\Phi_n(x; q_0)$
  ([definition](#def:q-pochhammer-partial-product)).*

- *(**Archimedean side, $\mathbb{C}$.**) The integral of the prolonged
  Seiberg–Witten differential $\lambda_{\mathrm{SW}}^{(k)}$
  ([prolonged SW differential](#prop:sw-period-thimble-equivalence))
  over Picard–Lefschetz thimbles $\mathcal{J}_{z_c}$ bounded by
  the rigid Jaco–Shalen–Johannson cusps of the active JSJ piece
  ([Φ$_q$-tower JSJ bridge](#conj:phi-q-tower-jsj-bridge)).*

*The two presentations agree under $\tau$:*

$$
  \boxed{\;
  \tau\bigl(
    \mathfrak{m}^{(k)}_{\mathrm{trans}}(T_w)
  \bigr)
  \;=\;
  \sum_\sigma n_\sigma^{(k)}
    \oint_{\mathcal{J}_{z_{c,\sigma}}}
      \lambda_{\mathrm{SW}}^{(k)}(z; T_w)\, dz,
  \;}
$$

*where the thimble base points $z_{c,\sigma}$ are the
$\tau_{\mathrm{arch}}$-images of the algebraic denominator zeros of
$\Phi_n(x; q_0)$
([denominator zeros = SW critical points](#conj:denominator-zeros-as-sw-critical-points))
and the thimble integration domain is bounded by the rigid JSJ cusps
of the descended Borromean nucleon substructures.*

## What is new vs. existing PL infrastructure

The PL framework on Bring's surface is already in place:

- **PL setup**: ([Picard–Lefschetz thimble](#def:picard-lefschetz-thimble)) defines
  the thimble decomposition of the integration contour at the
  color-tube discriminant locus.
- **Algebraic-archimedean equivalence**: ([SW-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence))
  identifies the Markov–Frobenius pairing with the SW thimble
  integral, modulo five hypotheses A2.1–A2.5.
- **Abelianisation**: ([MI–SW abelianisation](#prop:mi-sw-abelianisation),
  [MI–SW abelianisation Cartan](#lem:mi-sw-abelianisation-cartan))
  show that the nonabelian multiplicative integral trivialises on
  exceptional divisors and reduces to the abelian SW differential.
- **GB / jet / PL correspondence**: ([jet-GB-PL correspondence](#prop:jet-gb-pl-correspondence))
  matches the GB filtration to the PL critical-point order under
  $\tau$.

This synthesis block adds the **JSJ-bounded** structure — the
explicit statement that the thimble integration domain is **not the
full color-tube cubic**, but the **active JSJ piece** carved out by
the rigid Borromean cusps of the descended (memoised) nucleon
substructures
([Φ$_q$-tower JSJ bridge](#conj:phi-q-tower-jsj-bridge)). Together
with
([denominator zeros = SW critical points](#conj:denominator-zeros-as-sw-critical-points)),
this gives the QOU-native form of the Kashaev limit:

$$
  \begin{array}{ccc}
   \text{Algebraic Markov trace} &
   \xleftrightarrow{\;\tau\;} &
   \text{SW thimble integral} \\
   \text{at }\Phi_n(x; q_0)\text{ poles} & &
   \text{at }z_c \in \tau_{\mathrm{arch}}(\text{poles}) \\
   \text{depth } n = k_\star(T_w) & &
   \text{thimbles bounded by JSJ cusps}
  \end{array}
$$

## Memoisation: descended vs. transient (the central efficiency)

The conjecture exploits the QOU memoisation pattern in both pipelines:

1. **Algebraic memoisation.** The descended (memoised) Borromean
   nucleon transfer matrices $T_p, T_n$ are stable; their internal
   GB reductions are computed once and cached. Building a heavy
   nucleus inductively along the GB filtration, the algorithm
   multiplies cached blocks rather than recomputing the global
   braid word — squashing $\sim 10^{10}$ raw terms to $\sim 128$
   normal-form terms for $^{16}\mathrm{O}$
   ([categorical mass as Markov trace](#prop:categorical-mass-markov)).

2. **Geometric memoisation.** The descended nucleons are realised
   geometrically as Borromean rings $\mathcal{B}_3$. By Mostow
   rigidity, their internal hyperbolic shape parameters are unique
   and fixed, with volume exactly $8G$ (Catalan's constant). They
   are computed once and cached; the JSJ decomposition of a heavy
   nucleus pastes the cached pieces together along incompressible
   tori
   ([sw-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence) §strict archimedean split).

Under $\tau$, the algebraic and geometric memoisations are the same
operation: cached descended substructures act as **rigid boundaries**
(rigid algebraic transfer matrices on one side, rigid hyperbolic cusps
with fixed holonomies on the other). The Newton–Raphson solver only
has to evaluate the **transient** pieces — the new, active inter-
nucleon crossings — bounded to the active filtration shell.

## Equivalence statement (mass formula)

For a categorical mass class $T_w \in H_n(R, q)$ at GB-depth
$k_\star(T_w) = n$, write the active filtration shell as
$\mathcal{T}(T_w) = \bigl\{S \subseteq \{0, \dots, n-2\} :
\lvert S \rvert \leq 2,\, K_S \subset \text{transient}\bigr\}$ and
the descended JSJ pieces as $\mathcal{D}(T_w)$. Then the conjecture
asserts the **two-piece** equality:

$$
  \tau\bigl(\mathfrak{m}^{(k)}(T_w)\bigr)
  \;=\;
  \underbrace{\sum_{P \in \mathcal{D}(T_w)}
    \rho_F(P) \cdot \mathrm{Vol}_{\mathrm{hyp}}(P)}_{\text{descended (memoised)}}
  \;+\;
  \underbrace{\sum_{S \in \mathcal{T}(T_w)} n_\sigma^{(k)}
    \oint_{\mathcal{J}_{z_{c, S}}}
      \lambda_{\mathrm{SW}}^{(k)}(z; T_w)\, dz}_{\text{transient (active)}},
$$

where the first sum is the cached JSJ piecewise sum and the second
sum is the transient SW thimble integral, with thimble base points
$z_{c, S}$ at the algebraic denominator zeros of the corresponding
$\Phi_{|S|}$.

## Categorical license

The conjecture relies on the same Yekutieli non-abelian Stokes
theorem [`yekutieli2015`] that licenses
([sw-period $\equiv$ thimble integral](#prop:sw-period-thimble-equivalence)):
the categorical surface integral
([Yekutieli–Stokes remark](#rem:yekutieli-stokes))
collapses to a sum of point residues at the discriminant locus,
which under the present conjecture is the algebraic image of the
$\Phi_n$ denominator zeros — thimble base points bounded by JSJ
cusps. The four-piece chain

$$
  \text{categorical surface integral}
  \xrightarrow{\text{Yekutieli–Stokes}}
  \text{point residues}
  \xrightarrow{\tau_{\mathrm{arch}}}
  \text{SW thimble integral}
  \xrightarrow{\text{Mostow rigidity}}
  \text{JSJ piecewise sum}
$$

is the synthesis: each arrow is a license already in the manuscript;
the present conjecture asserts they compose to a closed
mass-evaluation pipeline.

## Status (CLAUDE.md §3b)

This conjecture is downstream of
([denominator zeros = SW critical points](#conj:denominator-zeros-as-sw-critical-points)),
([Φ$_q$-tower JSJ bridge](#conj:phi-q-tower-jsj-bridge)), and
([algebraic-geometric dilog equivalence](#conj:algebraic-geometric-dilog-equivalence)),
so it is a `conjecture` in the manuscript and a `class` in Lean. No
proof is supplied; the statement is intended as a structural target
that ties together existing PL/SW/JSJ infrastructure into a single
QOU-native mass-integration formula.
