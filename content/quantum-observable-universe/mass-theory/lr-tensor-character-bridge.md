**Corollary (k-factor parabolic specialisation of
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)).**
*Specialise the branching identity to the trivial interface
$I = \mathbf{1}$ and iterate $k-1$ times across the parabolic chain
$H_{n_1}(R, q) \otimes \cdots \otimes H_{n_k}(R, q) \hookrightarrow
H_n(R, q)$, where $n := \sum_i n_i$. For every
$\nu \vdash n$ and every
$(\beta_1, \ldots, \beta_k) \in H_{n_1}(R, q) \times \cdots \times
H_{n_k}(R, q)$, the tensor-product Hecke character factors as*

$$
  \boxed{\;
    \chi^\nu_{H_n}(\beta_1 \otimes \cdots \otimes \beta_k)
    \;=\;
    \sum_{(\lambda_1, \ldots, \lambda_k)} c^\nu_{\lambda_1, \ldots, \lambda_k}
      \cdot \prod_{i=1}^{k} \chi^{\lambda_i}_{H_{n_i}}(\beta_i)
  \;}
$$

*where the sum runs over $\lambda_i \vdash n_i$, and
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the iterated
Littlewood–Richardson coefficient*

$$
  c^\nu_{\lambda_1, \ldots, \lambda_k}
  \;=\;
  \sum_{\mu_2, \ldots, \mu_{k-1}}
    c^\nu_{\lambda_1, \mu_2} \cdot c^{\mu_2}_{\lambda_2, \mu_3}
      \cdots c^{\mu_{k-1}}_{\lambda_{k-1}, \lambda_k},
$$

*the structure constant of the Schur basis of $\mathrm{Sym}$ under
the iterated coproduct.*

## Proof

Setting $I = \mathbf{1}$ in
[`prop:hecke-branching-trace-decomposition`](hecke-branching-trace-decomposition.md)
collapses the operator-valued coefficient $A^\lambda_{\mu,\nu}(\mathbf{1})$
to the identity on $V_\mu \otimes V_\nu$, so the trace splits across
the tensor factors and the scalar prefactor reduces to the
two-factor LR coefficient $c^\lambda_{\mu,\nu}$. Iterating $k-1$
times across the parabolic chain stacks the LR coefficients into
the iterated form $c^\nu_{\lambda_1, \ldots, \lambda_k}$. ∎

## Algebraic context

The ring $\mathrm{Sym}$ of symmetric functions is a self-dual graded
Hopf algebra under the Hall inner product, with the Schur basis
$\{s_\lambda\}$ orthonormal and simultaneously diagonalising the
product and the coproduct ([macdonald1995] §I.5; PSH-algebra in the
sense of Zelevinsky):

$$
  s_\lambda \cdot s_\mu
  \;=\; \sum_{\nu \vdash |\lambda|+|\mu|} c^\nu_{\lambda\mu}\, s_\nu,
  \qquad
  \Delta s_\nu
  \;=\; \sum_{\substack{\lambda \vdash n_1\\\mu \vdash n_2\\n_1+n_2 = |\nu|}}
        c^\nu_{\lambda\mu}\, s_\lambda \otimes s_\mu.
$$

Under the Frobenius characteristic, the Schur product / coproduct
realise the induction / restriction along the parabolic embedding
$S_{n_1} \times \cdots \times S_{n_k} \hookrightarrow S_{n_1 + \cdots + n_k}$,
and the quantum lift to $H_n(R, q)$ ([geck-pfeiffer2000] §9.1.5,
[ram1991] Theorem 5.1) preserves the coefficients.

## Applicability in QOU

Two structural features of the QOU substrate make this corollary
the engine of every tractable atomic mass prediction.

**Tensor-product factorisation of the canonical atomic braid.**
The canonical $(Z, N)$-braid
([atomic braid](#def:atomic-braid), with
[interface composition](#def:canonical-braid-interface-composition))
factors as

$$
  \mathcal{B}_K
  \;=\; \mathcal{B}_K^{\mathrm{vac}} \cdot \bowtie_K,
$$

where $\mathcal{B}_K^{\mathrm{vac}} = \mathcal{B}_p^{(1)} \otimes \cdots
\otimes \mathcal{B}_n^{(N)}$ is the parabolic tensor of the
$A := Z + N$ per-nucleon $H_3$ canonical sub-braids (constituent
vacuum) and $\bowtie_K$ is the
(electroweak interface knot) --- a short
word in the inter-nucleon Hecke generators $\sigma_{3k+2}$
($0 \leq k < A-1$), one single-generator crossing per adjacent
nucleon pair, with sign $\sigma$ on a proton--proton arc and
$\sigma^{-1}$ on a neutron--neutron arc. The present proposition
applies directly to $\mathcal{B}_K^{\mathrm{vac}}$; the interface
contribution is governed by the
([Markov-axiom interface identity](#prop:interface-knot-markov-z))

$$
  \frac{\tau_M(\mathcal{B}_K)}{\tau_M(\mathcal{B}_K^{\mathrm{vac}})}
  \;=\; z(q)^{p_+(K)} \cdot \bigl(z(q) - h(q)\bigr)^{p_-(K)},
$$

a closed scalar form in the substrate parameters
$z = 1/(\sqrt q + 1/\sqrt q)$ and $h = q - q^{-1}$ (with $p_\pm(K)$
the counts of positive / negative interface generators). The mixed
proton--neutron averaged-half-sum case
$\tfrac{1}{2}(\sigma + \sigma^{-1})$ enters as a sign-balanced
combination of the closed identities above.

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
(roughly $6700^2$ at $A = 10$) but only $A - 1$ inter-nucleon
crossings rather than the $\sim 3A$ crossings of the full atomic
braid. The direct Hoefsmit path costs

$$
  T_{\mathrm{direct}}(Z, N)
  \;=\; O\!\left( p(3A) \cdot \dim_{\max}^2(3A) \cdot \ell(\beta_{Z,N}) \right).
$$

For $A = 4$ (helium-4, $H_{12}$, $p(12) = 77$), the ratio
$T_{\mathrm{direct}} / T_{\mathrm{LR}} \approx 5 \cdot 10^2$. For
$A = 10$ (boron-10, $H_{30}$, $p(30) = 5604$), the ratio reaches
$\approx 10^6$, converting an otherwise-intractable evaluation into
one of minutes.

## Convolutional structure

The iterated LR coefficient
$c^\nu_{\lambda_1, \ldots, \lambda_k}$ is the matrix element of the
$(k-1)$-fold coproduct
$\Delta^{(k-1)} \colon \mathrm{Sym}_n \to
 \mathrm{Sym}_{n_1} \otimes \cdots \otimes \mathrm{Sym}_{n_k}$
on the Schur basis. The corollary therefore expresses the $H_n$
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

[`computations/markov/markov_trace_via_wenzl_lr.py`](https://github.com/litlfred/qou/blob/main/computations/markov/markov_trace_via_wenzl_lr.py)
is the Python entry point; the per-partition LR sum is dispatched to
the Rust implementation in
[`tools/hecke-engine/src/wenzl_lr.rs`](https://github.com/litlfred/qou/blob/main/tools/hecke-engine/src/wenzl_lr.rs)
for cache locality at large $A$.
[`computations/cross_check_trM_wenzl_lr_1ppb.py`](https://github.com/litlfred/qou/blob/main/computations/cross_check_trM_wenzl_lr_1ppb.py)
verifies the bridge against the direct Hoefsmit path on $H_6$ (D, T)
and the self-conjugate sub-stratum of $H_9$ ($^3\mathrm{He}$):
per-partition $\chi^\nu$ agreement is at the machine-precision limit
($\sim 10^{-14}$ relative). The convention adapter
[`computations/wenzl_lr_convention_adapter.py`](https://github.com/litlfred/qou/blob/main/computations/wenzl_lr_convention_adapter.py)
splits a $(Z, N)$ specification into the LR-compatible per-nucleon
factor list and the interface residue and records the partition of
the canonical word that this corollary strictly governs.

## Scope of applicability

The identity holds for tensor-product (parabolic) braids only. The
interface knot $\bowtie_K$ does not factor through the parabolic
embedding; its contribution is the $I \neq \mathbf{1}$ regime
governed by the
(branching trace decomposition)
in the operator-valued form, and admits the closed scalar form of
the
([Markov-axiom interface identity](#prop:interface-knot-markov-z))
on the Markov-trace ratio. The LR bridge is the correct primitive
for the constituent-vacuum factor, not for the entire canonical
braid; the convention adapter keeps the partition explicit so
downstream consumers do not silently apply LR to a non-tensor
braid.
