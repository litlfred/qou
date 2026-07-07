<!-- FILE_START: substrate-cohomology-calibration-story.md -->
## The substrate, its cohomology, and the three units

Everything the framework predicts is built from one categorical substrate and a
single deformation parameter $q_0$. The geometry of that substrate is Bring's
curve, whose first cohomology $H^1$ is eight-dimensional and decomposes, under
the curve's $S_5$ symmetry, as two copies of one irreducible four-dimensional
representation, $H^1 = 2W$. This cohomology is rigid: once the curve is fixed,
$H^1$ and its polarised Hodge structure are determined. What is *not* fixed by
the categorical data alone is a small set of units — and it is exactly here that
measurement enters.

A polarised, weight-one Hodge structure of the shape $2W$ has precisely three
real degrees of freedom that are invisible to the categorical chain and must be
supplied as units when one crosses the substrate-to-archimedean wall (the
realisation functor $\tau$): the **scale** of the rank-two $W$-Hodge plane, its
**modulus**, and a third **scale** belonging to the meson sector, whose Hopf-link
topology has zero hyperbolic volume and therefore carries no scale derivable from
the other two. These three are the three calibration inputs of the framework, in
exact correspondence:

* **CAL-1, $m_e$** is the scale of the $W$-plane — the unprolonged ($n=0$)
  Seiberg--Witten period, the *electron period*. It is the base of the mass
  tower, propagated into every higher mass by the recurrence, not a prefactor
  pasted on at the end.
* **CAL-2, $q_0$** is the modulus of that plane — the trace
  $\tau = 2\cosh\theta$ of the Hodge monodromy. Because the monodromy preserves
  the curve's polarisation it lies in $\mathrm{SL}_2$, so its determinant is one
  and the modulus is the single number $\tau$.
* **CAL-3, $m_\pi$** is the scale of the meson sector — a cohomologically
  orthogonal class with no hyperbolic volume, hence genuinely independent of
  $(m_e, q_0)$.

Crossing the wall also fixes a parity. The two eigenvalues of a crossing,
$q$ and $-q^{-1}$, split as $\cosh\lambda \pm \sinh\lambda$ with
$\lambda = \log q$: the symmetric $\cosh$ part is curvature-free transport and
the antisymmetric $\sinh$ part is the curvature defect. Under the bar-involution
$q \mapsto q^{-1}$ these are the even and odd parities of one element. The
binding observables — masses and their averages — live on the $\cosh$, bar-even
side, where the modulus $\tau$ sits; the $\beta$-decay observable $\mathfrak{Q}_\beta$ and
its precision coefficients live on the $\sinh$, bar-odd side. They are not two
separate problems but the two parities of a single substrate element, so pinning
one constrains the other. That single element is the **complex volume**
$\mathfrak{V}$ ([`conj:binding-qbeta-complex-volume`](../mass-endomorphism/binding-qbeta-complex-volume.md)):
its bar-even part is $\operatorname{Re}\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$
(the mass/binding channel) and its bar-odd part is
$\operatorname{Im}\mathfrak{V} = \mathfrak{Q}_\beta$ (the decay channel), the QOU
analogue of the Neumann--Zagier $\operatorname{Vol} + i\,\mathrm{CS}$.

This is the whole shape of the theory in one breath: a rigid cohomology fixes
the structure; three units — a scale, a modulus, and an orthogonal scale — are
the only freedom, and they are the three measured calibrations; and the
even/odd split at the wall sorts every observable into the mass channel or the
decay channel. The remaining open numbers — the binding modulus and the decay
coefficients — are the two parities of one object, which is why closing one is
expected to close the other.
<!-- FILE_END: substrate-cohomology-calibration-story.md -->

<!-- FILE_START: electron-period-base.md -->
**Proposition (the electron mass is the base period of the tower).**

The prolonged Seiberg--Witten periods satisfy the one-parameter recurrence
$a_D^{(n+2)} = \tau\,a_D^{(n+1)} - a_D^{(n)}$
([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)). Its
$n=0$ term is the *unprolonged* period — the **electron period** $a_D^{(e)}$
([`prop:jet-sw-tau-decomposition`](#prop:jet-sw-tau-decomposition): "the $n=0$
term is the electron period"). Identifying $a_D^{(e)}$ with the leptonic scale
$m_e$ (CAL-1) makes the first calibration the **base of the tower**: every
period is generated from the triple $(m_e,\,a_D^{(1)},\,\tau)$, so $m_e$
propagates into *every* term through the recurrence — it is not an external
multiplicative prefactor bolted onto the geometry.

Concretely the $n=2$ period is $a_D^{(2)} = \tau\,a_D^{(1)} - m_e$: the electron
scale appears explicitly. This is the cohomological role of CAL-1 — the
**scale (normalisation) of the rank-2 $W$-Hodge plane**, the $h^0$ datum of the
archimedean realisation. The proposition's `lean.ref`,
[`QOU.Mass.electron_period_is_base`](#prop:electron-period-base), proves the
base identity; its companion `QOU.Mass.second_period_contains_me` (same Lean
file) proves the $n=2$ propagation — both sorry-free.
<!-- FILE_END: electron-period-base.md -->

<!-- FILE_START: calibration-cohomology-alignment.md -->
**Proposition (the three calibrations are the three cohomological data).**

The first cohomology of Bring's curve is $H^1 = 2W$ (rank $8$, two copies of
the irreducible $4$-dimensional $S_5$ representation $W$;
[`prop:prolonged-periods-fixed-depth`](#prop:prolonged-periods-fixed-depth)).
Its polarised Hodge structure has exactly **three** real degrees of freedom
that survive as observable units once the archimedean functor $\tau$ is applied:

| cohomological datum | calibration | channel |
|---|---|---|
| **scale** of the rank-2 $W$-Hodge plane $= a_D^{(e)}$ | CAL-1 $m_e$ ([`prop:electron-period-base`](#prop:electron-period-base)) | $h^0$ prefactor |
| **modulus** of that plane $=$ SL$_2$ trace $\tau = 2\cosh\theta$ | CAL-2 $q_0$ ([`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence)) | cosh / bar-even |
| **scale** of the $\operatorname{Vol}(\mathrm{Hopf})=0$ meson sector | CAL-3 $m_\pi$ | orthogonal class |

The rank-2 $W$-Hodge plane carries two invariants — a scale and a modulus — and
the meson sector (whose Hopf-link complement has zero hyperbolic volume, hence
no geometric scale derivable from $(m_e, q_0)$ — the meson scale-independence) contributes a third, orthogonal
scale: $2 + 1 = 3$, matching the three calibrations exactly. The alignment is
therefore not a coincidence of counting but the statement that **the three
calibration inputs are precisely the three undetermined cohomological data of
the Bring Hodge structure** — the choice of units forced at the
substrate-to-archimedean wall.

The Lean witnesses
[`QOU.Mass.calibrations_eq_cohomology`](#prop:calibration-cohomology-alignment)
(the calibration triple equals the cohomological triple) and
`cohomology_data_count` ($2+1=3$) record the correspondence and the count.
<!-- FILE_END: calibration-cohomology-alignment.md -->

<!-- FILE_START: bar-parity-split.md -->
**Proposition (binding and $\beta$-decay are the two bar-parities of one element).**

The bar-involution $\sigma$ ($q \mapsto q^{-1}$, $\sigma^2 = \mathrm{id}$;
[`def:bar-involution`](#def:bar-involution)) splits every element into a
$\sigma$-fixed **even** part and a $\sigma$-anti **odd** part:
$$
\mathrm{even}(x) = x + \sigma x \ (\sigma\text{-fixed}), \qquad
\mathrm{odd}(x) = x - \sigma x \ (\sigma\text{-anti}), \qquad
\mathrm{even}(x) + \mathrm{odd}(x) = 2x .
$$

Applied to the fibre Habiro element $F$ controlling the substrate, the two
parities carry the two observables:

- **even ($\cosh$, bar-symmetric)** — the binding trace
  $\tau = \operatorname{tr} B$ of
  [`prop:sl2-prolongation-recurrence`](#prop:sl2-prolongation-recurrence) (the
  curvature-free transport, $(q+q^{-1})/2 = \cosh\lambda$);
- **odd ($\sinh$, bar-antisymmetric)** — the $\mathfrak{Q}_\beta$ residue-A / $c_k$ ladder
  (the curvature defect, $(q-q^{-1})/2 = \sinh\lambda$), the bar-odd Habiro dual
  of $\alpha_{\mathrm{EM}}$.

So binding (mass-average) and $\beta$-decay ($\mathfrak{Q}_\beta$) are **not two problems
but one** — the even and odd parities of a single bar-graded element. Pinning
either parity (the keystone $\tau$, or the $c_k$ kernel) constrains the other
through the shared element. The Lean witnesses
[`QOU.Mass.evenPart_add_oddPart`](#prop:bar-parity-split), `evenPart_fixed`, and
`oddPart_anti` prove the decomposition and the parity of each part, sorry-free.

This bar-even/bar-odd split is precisely the real/imaginary split of the
**complex volume** $\mathfrak{V}$
([`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)). Continuing
$\lambda \mapsto i\theta$ (real $q$ rotated onto a root of unity) sends
$\cosh\lambda \mapsto \cos\theta$ and $\sinh\lambda \mapsto i\sin\theta$, so the
bar-even part becomes $\operatorname{Re}\mathfrak{V} = \mathfrak{E}_{\mathrm{bind}}$
and the bar-odd part becomes $\operatorname{Im}\mathfrak{V} = \mathfrak{Q}_\beta$. The
parity-split proposition here is the algebraic core of that unification: the
additive projections $x \mapsto x \pm \sigma x$ are exactly what lets a single
identity on $\mathfrak{V}$ descend to both channels at once.

Although the even/odd involution split is implemented using standard linear algebraic techniques, attributing this mathematical decomposition to a concrete physical dichotomy—where the even component describes binding and the odd component captures decay processes—represents a mathematically novel interpretive framework developed for the Quantum Observable Universe.
<!-- FILE_END: bar-parity-split.md -->

<!-- FILE_START: deuteron-binding-dressing-proton-net.md -->
**Proposition (conditional on [`conj:borromean-quark`](../observations/borromean-quark.md)).**
*Let $h = q - q^{-1}$ and $\mathfrak{E}_0 = m_e/(q(q-1))$. Write
$\mathrm{net}(p) = 1 - \tfrac{h}{2}$ and $\mathrm{net}(n) = 1 - \tfrac{3h}{2} + \tfrac{h^2}{2}$
for the single-wrap normal-form net coefficients of the proton $[u,u,d]$
and neutron $[u,d,d]$ in $H_3(q)$ (the conjectural inputs of
[`conj:borromean-quark`](../observations/borromean-quark.md)). Then for any
trace difference $\Delta\mathrm{tr}$,*

$$
\mathfrak{E}_0 \cdot \mathrm{net}(p) \cdot \Delta\mathrm{tr}
\;=\; \mathfrak{Q}_\beta \cdot \frac{\Delta\mathrm{tr}}{h},
$$

*i.e. the deuteron binding functional $\mathfrak{E}_0\,(1-\tfrac{h}{2})\,\Delta\mathrm{tr}$
dresses the energy scale $\mathfrak{E}_0$ by exactly the proton net
coefficient $\mathrm{net}(p)$, the bar-even partner of the $\beta$-decay
$Q$-value $\mathfrak{Q}_\beta$ under the single Hecke factor $h$.*

## Context

The trace-canonical deuteron binding on the $\mathfrak{E}_0$ route,
$\mathfrak{E}_0\,\Delta\mathrm{tr}$, over-binds by $+11.99\%$. The empirical
observation ([`docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md`](../../../docs/audits/2026-07-03-deuteron-from-scratch-error-ledger.md))
is that dressing it by $(1-\tfrac{h}{2})$ lands it at $+0.12\%$ of AME2020
with no fitted constant. This proposition removes the mystery from the
dressing: $(1-\tfrac{h}{2})$ is not a new object but $\mathrm{net}(p)$
itself.

## Derivation (all exact in the field)

The load-bearing step is the division-free identity

$$
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p)
\;=\; -\,h \cdot \mathrm{net}(p),
$$

verified by $-h(1-\tfrac{h}{2}) = -h + \tfrac{h^2}{2} = (1 - \tfrac{3h}{2} + \tfrac{h^2}{2}) - (1 - \tfrac{h}{2})$.
In the substrate regime $0 < h < 2$ the proton coefficient $\mathrm{net}(p) > 0$,
so $|\Delta(\mathrm{net})| = h\,\mathrm{net}(p)$, and the $Q$-value ansatz
$\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\,\mathfrak{E}_0$ of
[`prop:neutron-qvalue-symbolic`](../particle-interactions/neutron-qvalue-symbolic.md)
becomes

$$
\mathfrak{Q}_\beta \;=\; \mathfrak{E}_0 \, h \, \mathrm{net}(p).
$$

Dividing by $h \neq 0$ and multiplying by $\Delta\mathrm{tr}$ gives the
displayed identity: the bar-even binding dressing $\mathrm{net}(p)$ and the
bar-odd $Q$-value differ by exactly one factor of $h = q - q^{-1}$ (itself
bar-odd, $h \mapsto -h$ under $q \mapsto q^{-1}$). This is the
bar-parity split of [`prop:bar-parity-split`](../mass-theory/bar-parity-split.md)
read at the deuteron: binding sits in the bar-even channel, $\beta$-decay
in the bar-odd channel, and $h$ bridges them.

## Scope

The three identities are exact and Lean-formalized
(`QOU.Mass.DeuteronBindingDressing`). What remains observation-tier is the
*magnitude* claim $B_D \approx \mathfrak{E}_0\,\mathrm{net}(p)\,\Delta\mathrm{tr}$:
that the binding functional *should* carry the single-interface net
coefficient is supported at the deuteron ($+0.12\%$) but is D-specific — a
cross-$A$ discriminator shows the same dressing does not extend to $A \geq 3$
(the extensive deficit is a separate mechanism). The identification reduces
the open question "why $(1-\tfrac{h}{2})$?" to "why is the binding dressed by
the proton NF net coefficient?", and ties it to the already-conjectured
$\beta$-decay sector. It is not a wired binding law; the $\Delta_\lambda$
gate stands.
<!-- FILE_END: deuteron-binding-dressing-proton-net.md -->

<!-- FILE_START: lr-coefficient-hecke.md -->
**Proposition.**
*For partitions $\mu \vdash n_1$, $\nu \vdash n_2$, and $\lambda \vdash n_1 + n_2$,
the **Littlewood-Richardson coefficient** $c^\lambda_{\mu\nu}$ is the
multiplicity of the irreducible Iwahori-Hecke module $V_\lambda$ in the
restriction*

$$
  V_\lambda \;\downarrow_{\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q)}
  \;=\; \bigoplus_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}}
        c^\lambda_{\mu\nu} \cdot (V_\mu \boxtimes V_\nu)
$$

*Equivalently, $c^\lambda_{\mu\nu} = |\mathrm{LR}(\lambda/\mu, \nu)|$
is the number of Littlewood-Richardson skew tableaux of shape $\lambda/\mu$
and content $\nu$ whose reverse-reading word is Yamanouchi
(every prefix has $\#i \geq \#(i{+}1)$).*

*The coefficient is a non-negative integer:
$c^\lambda_{\mu\nu} \in \mathbb{Z}_{\geq 0}$, with $c^\lambda_{\mu\nu} = 0$
if $\mu \not\subseteq \lambda$ (as Young diagrams) or
$|\lambda| - |\mu| \neq |\nu|$.*

## Categorical interpretation

The LR coefficient is the multiplicity of $V_\lambda$ in the
**outer tensor product** $V_\mu \boxtimes V_\nu$ pulled back through
the standard inclusion
$\mathbf{H}_{n_1}(q) \otimes \mathbf{H}_{n_2}(q) \hookrightarrow \mathbf{H}_{n_1 + n_2}(q)$
(omitting the inter-block generator $\sigma_{n_1}$).
This is the Hecke-deformed counterpart of the classical
Littlewood-Richardson rule for symmetric groups
(\cite{ariki1996} §6, \cite{ram1991}).

## Role in the operator-valued Wenzl branching

The Wenzl 1988 sub-lemma 2.1 (operator-valued form, per
[`prop:crystal-r-matrix-sub-lemma`](crystal-r-matrix-sub-lemma.md))
sums **per $(\mu, \nu)$ block** with multiplicity $c^\lambda_{\mu\nu}$:

$$
  \chi^\lambda(W_{\mathrm{inner}} \cdot I \cdot \beta_{\mathrm{block}})
    = \sum_{\substack{\mu \vdash n_1 \\ \nu \vdash n_2}}
      c^\lambda_{\mu\nu} \cdot
      \mathrm{Tr}\bigl(A^\lambda_{\mu\nu}(I) \cdot
                       (\rho_\mu(W_{\mathrm{inner}}) \otimes \rho_\nu(\beta_{\mathrm{block}}))\bigr)
$$

The LR coefficient $c^\lambda_{\mu\nu}$ is therefore the
**integer multiplicity** that the operator-valued combiner consumes;
the operator $A^\lambda_{\mu\nu}(I)$ acts on the
$c^\lambda_{\mu\nu}$-dimensional multiplicity space.

## Computational realisation

the formalism
the canonical formalism
computes $c^\lambda_{\mu\nu}$ via direct LR-tableau enumeration with
Yamanouchi pruning. Precomputed tables exist for the canonical
A=2/3/4 atomic decompositions
(`LR_TABLE_3_3_TO_6`, `LR_TABLE_3_6_TO_9`, `LR_TABLE_6_6_TO_12`).
The skew-SYT primitive
the canonical formalism
(PR [#1515](https://github.com/litlfred/qou/pull/1515)) is a
related-but-distinct quantity ($f^{\lambda/\mu} = $ # SYT of skew
shape, weights all chains; $c^\lambda_{\mu\nu}$ counts only the
Yamanouchi-valid SSYT of content $\nu$).
<!-- FILE_END: lr-coefficient-hecke.md -->

<!-- FILE_START: hecke-1d-irrep-closed-form-character.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — 1-dimensional Hecke irrep character, universal closed form).**

For any $n \geq 2$ and any typed braid $\beta \in B_n$ encoded as a
sequence of crossings of three types
$\{\sigma_i,\, \sigma_i^{-1},\, \sigma_i - h/2\cdot\mathbf{1}\}$
(the `operator-valued interface`
with $h = q - q^{-1}$), the $q$-character on each 1-dimensional
irreducible representation of $H_n(q)$ is given by the **universal
closed form**

$$
\boxed{
  \chi^{(n)}_q(\beta)
   \;=\;
   q^{w(\beta)} \cdot \bigl(\tfrac{[2]_q}{2}\bigr)^{m(\beta)}
  \qquad\text{and}\qquad
  \chi^{(1^n)}_q(\beta)
   \;=\;
   \bigl(-q^{-1}\bigr)^{w(\beta)} \cdot \bigl(-\tfrac{[2]_q}{2}\bigr)^{m(\beta)},
}
$$

where:

- $w(\beta) = \#(\sigma_i) - \#(\sigma_i^{-1})$ is the **writhe**
  (signed crossing count of the typed braid),
- $m(\beta)$ is the number of **averaged** (operator-valued
  $\sigma_i - h/2$) crossings,
- $[2]_q = q + q^{-1}$ is the standard quantum integer (so
  $[2]_q / 2 = (q + q^{-1})/2$ is the q-half-integer).

**The closed form is independent of $n$.** Only the choice of which
1-d irrep ($V_{(n)}$ trivial or $V_{(1^n)}$ sign) toggles the
sign of the eigenvalue $\lambda_\sigma \in \{+q,\, -q^{-1}\}$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: hecke-1d-irrep-closed-form-character.md -->

<!-- FILE_START: hoefsmit-V21-cos-symmetrization.md -->
**Proposition (conditional on [`conj:borromean-quark`](#conj:borromean-quark) — Hoefsmit V_(2,1) Markov-symmetrized cos resummation, non-trivial Markov machinery for the 2-dimensional irrep).**

The 1-d Hecke irreps admit the universal closed form
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character).
The 2-d irrep $V_{(2,1)}$ of $H_3(q)$ is the first non-trivial case
and requires the **Hoefsmit seminormal action**:

$$
  \rho_{(2,1)}(\sigma_0) \;=\; \begin{pmatrix} q & 0 \\ 0 & -q^{-1} \end{pmatrix},
  \quad
  \rho_{(2,1)}(\sigma_1) \;=\; \begin{pmatrix} d_1 & b \\ c & d_2 \end{pmatrix},
$$

where the matrix entries are Hoefsmit's standard Young tableau (SYT)
formulas:

$$
\begin{aligned}
  d_1 &= \frac{q^3}{q^2 + 1}, \qquad d_2 = -\frac{q^{-1}}{q^2 + 1}, \\
  b &= \sqrt{d_1 \cdot d_2 + 1} \quad\text{(off-diagonal coupling)}, \qquad c = b.
\end{aligned}
$$

(The off-diagonal $b^2 = d_1 d_2 + 1$ identity is the Hecke-quadratic
constraint on $\sigma_1$; the choice $c = b$ is a gauge convention.)

Both Hoefsmit matrices satisfy the **matrix-level Hecke quadratic**
$M^2 = (q - q^{-1}) \cdot M + I$:

| quantity | $\sigma_0$ (diagonal) | $\sigma_1$ (off-diagonal) |
|---|---|---|
| trace | $q - q^{-1}$ | $d_1 + d_2 = q - q^{-1}$ |
| determinant | $-1$ | $d_1 d_2 - b^2 = -1$ |
| $M^2$ | $(q-q^{-1}) M + I$ | $(q-q^{-1}) M + I$ |

The trace/determinant equalities reduce the off-diagonal matrix
identity to Cayley-Hamilton on $\mathbb{R}^{2 \times 2}$ — formalized
in `hoefsmit_sigma1_trace_eq`, `hoefsmit_sigma1_det_eq`, and
`hoefsmit_sigma1_hecke_quadratic`.

## Markov symmetrization at single wrap

For a typed braid $\beta = c_1 c_2 \cdots c_L$ on $V_{(2,1)}$, the
**Markov-traced character** symmetrizes over the two eigenphases of
$\rho_{(2,1)}$ along the braid evolution. At leading order, the
single-wrap eigenphase is

$$
  \alpha \;=\; \frac{(z - 1) \, h}{2}, \qquad
  z = \tfrac{1}{\sqrt q + 1/\sqrt q}, \quad h = q - q^{-1},
$$

per [`prop:beta-decay-transfer-matrix`](#prop:beta-decay-transfer-matrix).
The symmetrized character is

$$
  \chi^{(2,1),\mathrm{symm}}_q \;:=\;
   \tfrac{1}{2}\bigl(\mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot e^{+i\alpha}
                     + \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot e^{-i\alpha}\bigr)
   \;=\; \mathrm{tr}\,\rho_{(2,1)}(\beta) \cdot \cos\alpha.
$$

In the Markov-trace context, this is exactly the form that emerges
from the cyclic constraint $\tau_M(xy) = \tau_M(yx)$ combined with
the bar involution $q \leftrightarrow q^{-1}$ — see
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

## Closed-form decomposition (joint with 1-d closed forms)

At single wrap for any $\beta \in B_n$ encoded as a typed-crossing
list with writhe $w$ and averaged-count $m$, the full Markov trace
decomposes as

$$
\boxed{
  \tau_M(\beta)
   \;=\;
   y_{(n)} \cdot \chi^{(n)}_q(\beta)
   \;+\;
   \sum_{\substack{\lambda \vdash n \\ \dim V_\lambda \geq 2}}
     y_\lambda \cdot \chi^{\lambda,\mathrm{symm}}_q(\beta)
   \;+\;
   y_{(1^n)} \cdot \chi^{(1^n)}_q(\beta),
}
$$

with the 1-d closed forms from
[`prop:hecke-1d-irrep-closed-form-character`](#prop:hecke-1d-irrep-closed-form-character)
and the dim-2 cos symmetrization from
[`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation).

For $H_3$ this is fully closed-form substrate-derivable (only one
2-d irrep, $V_{(2,1)}$). For $H_5$ and beyond, additional 2+-dim irreps
appear ($V_{(3,2)}, V_{(2,2,1)},$ etc.); each requires its own
Hoefsmit matrix and Markov-symmetrized cos analog.

## Empirical anchor

At $q_0$, the Hoefsmit V_(2,1) matrix entries (from
the canonical formalism
and the existing `hecke_characters.build_seminormal_matrices` infrastructure):

| quantity | value at $q_0$ |
|----------|---:|
| $\chi^{(2,1)}_q(\mathcal{B}_p)$ | $+1.8077033201$ |
| $\chi^{(2,1)}_q(\mathcal{B}_n)$ | $+1.7008888501$ |
| $\Delta \chi^{(2,1)}_q$   | $+0.1068144700$ |
| $y_{(2,1)} \cdot \Delta \chi^{(2,1)}_q$ | $+0.0913335577$ |
| Markov-symmetrized factor $\cos\alpha$ | $0.99863..$ |

After symmetrization the V_(2,1) contribution combines with the 1-d
contributions to give $\mathfrak{Q}_\beta = \mathfrak{Q}_\beta^A \cdot \cos((z-1)h/2)$ at
the cos-resummation level (305 ppm residual against CODATA).
<!-- FILE_END: hoefsmit-V21-cos-symmetrization.md -->

