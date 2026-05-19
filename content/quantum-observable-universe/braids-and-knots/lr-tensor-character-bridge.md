**Proposition (LR comultiplication bridge for Hecke characters on
tensor-product braids).**
*Let $H_n(R, q)$ denote the type-$A$ Iwahori--Hecke algebra over a
commutative ring $R$ in the symmetric (Hoefsmit) convention
$\sigma_i^2 = (q - q^{-1})\sigma_i + 1$, and let $\chi^\lambda_{H_n}$
denote the seminormal character indexed by $\lambda \vdash n$. The
parabolic embedding*

$$
  H_{n_1}(R, q) \otimes_R H_{n_2}(R, q) \otimes_R \cdots \otimes_R
    H_{n_k}(R, q)
  \;\hookrightarrow\;
  H_{n_1 + n_2 + \cdots + n_k}(R, q),
  \qquad n := \textstyle\sum_i n_i,
$$

*sends a tensor-product element
$\beta = \beta_1 \otimes \beta_2 \otimes \cdots \otimes \beta_k$
to a braid in $H_n(R, q)$. For every partition $\nu \vdash n$,*

$$
  \boxed{\;
    \chi^\nu_{H_n}(\beta_1 \otimes \cdots \otimes \beta_k)
    \;=\;
    \sum_{(\lambda_1, \ldots, \lambda_k)} c^\nu_{\lambda_1, \ldots, \lambda_k}
      \cdot \prod_{i=1}^{k} \chi^{\lambda_i}_{H_{n_i}}(\beta_i)
  \;}
$$

*where the sum runs over $\lambda_i \vdash n_i$ and
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the iterated
Littlewood--Richardson coefficient*

$$
  c^\nu_{\lambda_1, \ldots, \lambda_k}
  \;=\;
  \sum_{\mu_2, \ldots, \mu_{k-1}}
    c^\nu_{\lambda_1, \mu_2} \cdot c^{\mu_2}_{\lambda_2, \mu_3}
      \cdots c^{\mu_{k-1}}_{\lambda_{k-1}, \lambda_k},
$$

*the structure constant of the Schur basis of the ring of symmetric
functions $\mathrm{Sym}$ under the iterated coproduct.*

## Algebraic context

The ring $\mathrm{Sym}$ of symmetric functions is a self-dual graded
Hopf algebra under the Hall inner product, with the Schur basis
$\{s_\lambda\}$ orthonormal and simultaneously diagonalising the
product and the coproduct ([macdonald1995] §I.5; PSH-algebra in
the sense of Zelevinsky). The Littlewood--Richardson coefficients
$c^\nu_{\lambda\mu}$ realise both structures:

$$
  s_\lambda \cdot s_\mu
  \;=\; \sum_{\nu \vdash |\lambda|+|\mu|} c^\nu_{\lambda\mu}\, s_\nu,
  \qquad
  \Delta s_\nu
  \;=\; \sum_{\substack{\lambda \vdash n_1\\\mu \vdash n_2\\n_1+n_2 = |\nu|}}
        c^\nu_{\lambda\mu}\, s_\lambda \otimes s_\mu.
$$

Under the Frobenius characteristic map, $\mathrm{Sym} \cong
\bigoplus_{n\geq 0} R(S_n) \otimes_\mathbb{Z} \mathbb{Q}$, the basis
element $s_\lambda$ corresponds to the irreducible character
$\chi^\lambda$ of $S_n$, and the Schur product / coproduct realise the
induction / restriction along the parabolic embedding $S_{n_1} \times
\cdots \times S_{n_k} \hookrightarrow S_{n_1 + \cdots + n_k}$.

## Proof

By [geck-pfeiffer2000] Theorem 9.1.5 and the quantum
Frobenius--Schur duality (compare [ram1991], Theorem 5.1), the
classical induction--restriction formulas lift to the type-$A$
Iwahori--Hecke algebra: for every $\nu \vdash n_1 + n_2$ and every
$\beta_i \in H_{n_i}(R, q)$,

$$
  \chi^\nu_{H_{n_1+n_2}}(\beta_1 \otimes \beta_2)
  \;=\;
  \sum_{\substack{\lambda \vdash n_1\\\mu \vdash n_2}}
    c^\nu_{\lambda\mu}\,
    \chi^\lambda_{H_{n_1}}(\beta_1) \cdot \chi^\mu_{H_{n_2}}(\beta_2).
$$

The two-factor identity is the Hecke-algebra image of the Schur
coproduct $\Delta$. Iterating gives the $k$-factor identity, with the
iterated LR coefficient
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ exactly equal to the
$k$-fold composition
$(\Delta \otimes \mathrm{id}^{\otimes (k-2)}) \cdots
 (\Delta \otimes \mathrm{id}) \, \Delta\, s_\nu$ expressed in the
Schur basis, by induction on $k$. $\square$

## Applicability in QOU

Two structural features of the QOU substrate make this proposition
the engine of every tractable atomic mass prediction.

**Tensor-product factorisation of the canonical atomic braid.**
The canonical $(Z, N)$-braid
([atomic braid](#def:atomic-braid), with
[interface composition](#def:canonical-braid-interface-composition))
factors as

$$
  \beta_{Z,N}
  \;=\; \beta_{\mathrm{disjoint}} \cdot \beta_{\mathrm{interface}},
$$

where $\beta_{\mathrm{disjoint}} = \beta_1 \otimes \cdots \otimes
\beta_A$ is the parabolic tensor of the $A := Z + N$ per-nucleon
$H_3$ canonical sub-braids, and $\beta_{\mathrm{interface}}$ is a
short word in the inter-nucleon Hecke generators $\sigma_{3k+2}$
($0 \leq k < A-1$), one factor per adjacent nucleon pair. The
per-pair factor is $\sigma$ on a proton--proton arc, $\sigma^{-1}$
on a neutron--neutron arc, and the averaged half-sum
$\tfrac{1}{2}(\sigma + \sigma^{-1})$ on a mixed proton--neutron arc. The
proposition applies directly to $\beta_{\mathrm{disjoint}}$; the
interface factor multiplies the seminormal representation matrix at
$H_{3A}$ after the LR sum has been evaluated.

**Cost asymmetry: small per-nucleon $H_3$ vs. large $H_{3A}$.**
At each nucleon, $\lambda_i \vdash 3$ with $\dim \lambda_i \leq 2$, so
every per-nucleon character $\chi^{\lambda_i}_{H_3}(\beta_i)$ costs
$O(\dim^2 \cdot \ell(\beta_i)) = O(\ell(\beta_i))$. The total
LR-bridged cost is

$$
  T_{\mathrm{LR}}(Z, N)
  \;=\; O\!\left( p(3)^A \cdot A \cdot \ell_{\mathrm{intra}}
                 + p(3A) \cdot \dim_{\max}^2(3A) \cdot \ell(\beta_{\mathrm{interface}}) \right),
$$

with the first term --- the LR sum --- dominated by $3^A$ choices of
per-nucleon partition, and the second term --- the interface
multiply --- carrying a single power of $\dim_{\max}^2(3A)$
(roughly $6700^2$ at $A = 10$) but only $A - 1$ averaged crossings
rather than the $\sim 3A$ crossings of the full atomic braid.
The direct Hoefsmit path costs

$$
  T_{\mathrm{direct}}(Z, N)
  \;=\; O\!\left( p(3A) \cdot \dim_{\max}^2(3A) \cdot \ell(\beta_{Z,N}) \right).
$$

For $A = 4$ (helium-4, $H_{12}$, $p(12) = 77$), the ratio
$T_{\mathrm{direct}} / T_{\mathrm{LR}} \approx 5 \cdot 10^2$. For
$A = 10$ (boron-10, $H_{30}$, $p(30) = 5604$), the ratio reaches
$\approx 10^6$, converting an
otherwise-intractable evaluation into one of minutes.

## Convolutional structure

The iterated LR coefficient
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the matrix element of the
$(k-1)$-fold coproduct
$\Delta^{(k-1)} \colon \mathrm{Sym}_n \to
 \mathrm{Sym}_{n_1} \otimes \cdots \otimes \mathrm{Sym}_{n_k}$
on the Schur basis. The bridge therefore expresses the $H_n$
character as a *convolution* of $H_{n_i}$ characters against the
coalgebra of $\mathrm{Sym}$. Because $\mathrm{Sym}$ is self-dual, the
same coefficient table $c$ that prescribes the product of Schur
polynomials prescribes the comultiplication --- the algebra and
coalgebra structures share a single rank-three tensor of structure
constants. This is the categorical content of the speedup: a
$k$-factor character on $H_n$ is computed from $\sum n_i = n$ small
characters by a single contraction against $c$, without ever
constructing the $H_n$ seminormal matrices.

## Witness

[`folio-assistant/computations/markov_trace_via_wenzl_lr.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/markov_trace_via_wenzl_lr.py)
is the Python entry point; the per-partition LR sum is dispatched to
the Rust implementation in
[`tools/hecke-engine/src/wenzl_lr.rs`](https://github.com/litlfred/qou/blob/main/tools/hecke-engine/src/wenzl_lr.rs)
for cache locality at large $A$.
[`folio-assistant/computations/cross_check_trM_wenzl_lr_1ppb.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/cross_check_trM_wenzl_lr_1ppb.py)
verifies the bridge against the direct Hoefsmit path on $H_6$ (D, T)
and the self-conjugate sub-stratum of $H_9$ ($^3\mathrm{He}$):
per-partition $\chi^\nu$ agreement is at the machine-precision limit
($\sim 10^{-14}$ relative).

Witnesses
[`markov-trace-via-wenzl-lr.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/markov-trace-via-wenzl-lr.witness.json)
and
[`cross-check-trM-wenzl-lr-1ppb.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/cross-check-trM-wenzl-lr-1ppb.witness.json)
record the LR-bridged character tables on
$\beta_{\mathrm{disjoint}}$ for the $(Z, N) = (1, 0), (0, 1), (1, 1),
(2, 1), (1, 2), (2, 2)$ atoms.

## Scope of applicability

The identity holds for tensor-product (parabolic) braids only. The
non-tensor inter-nucleon factor $\beta_{\mathrm{interface}}$ does not
factor through the parabolic embedding, and its contribution to the
canonical character must be applied as a separate seminormal-basis
multiplication; the LR bridge is the correct primitive for the
disjoint factor, not for the entire canonical braid. The convention
adapter
[`folio-assistant/computations/wenzl_lr_convention_adapter.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/wenzl_lr_convention_adapter.py)
splits a $(Z, N)$ specification into the LR-compatible per-nucleon
factor list and the interface residue, recording the partition
of the canonical word that this proposition strictly governs.
