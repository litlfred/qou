**Conjecture (weak-sector spectral completeness — Hoefsmit
$n=6$ form).**
*Over the categorical ring $R$ with $q$ generic (not a root of
unity in $R$ — note $q = 1$ IS excluded), the EW/Higgs
force-carrier sector $\{T(2,4), T(2,6), T(2,8)\}$
(electroweak/Higgs torus-link triplet)
admits a **categorically complete idempotent decomposition** in
$\mathrm{End}_R(V^{\otimes 6})$ via the disjoint-strand-pair
Hoefsmit assignment*

$$
  W \leftrightarrow \sigma_1^4, \qquad
  Z \leftrightarrow \sigma_3^6, \qquad
  H \leftrightarrow \sigma_5^8
$$

*([`thm:hoefsmit-ew-cell-content`](#thm:hoefsmit-ew-cell-content)).
Eight pairwise-orthogonal pure-eigenspace projectors of
$(\sigma_1, \sigma_3, \sigma_5)$ — labelled by sym/alt patterns —
exhaust the EW Wedderburn content with cell-content
multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$ summing to $20$ (out
of $\sum_{\lambda \vdash 6} f_\lambda = 76$ seminormal-basis
vectors). The substrate-level structural quantity is the
**bar-self-dual cell-content trace***

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + \bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
  \;\in\; R
$$

*— derivable directly from cell-content multiplicities, **without
invoking Plancherel weights**.*

### Statement (formal)

Over the categorical ring $R$ with $q$ generic (not a root of
unity), the Hecke algebra $H_2(q)$ has Wedderburn decomposition
$H_2(q) \cong R \oplus R$ with two 1-dimensional blocks (sym and
alt), summing to a 2-dimensional algebra over $R$. Each torus
link $T(2, 2k) = \sigma_1^{2k}$ acts on these two blocks with
eigenvalues $(q^{2k}, q^{-2k}) \in R^\times \times R^\times$
(prop:even-twist-torus-link-psd-feasibility).

Define the **per-link block projectors**:
- $e_W^{+} := $ sym block of $T(2, 4)$, $e_W^{-} := $ alt block
- $e_Z^{+} := $ sym block of $T(2, 6)$, $e_Z^{-} := $ alt block
- $e_{T(2,8)}^{+} := $ sym block of $T(2, 8)$, $e_{T(2,8)}^{-} := $ alt block

The $T(2,8)$ pair is indexed by its link rather than by $H$, to keep it distinct from the Higgs idempotent $e_H$ of [conj:g-action-on-substrate](#conj:g-action-on-substrate), which is a rank-one idempotent on $A^{(H)}$ and not a Wedderburn block of $H_2(q)$.

The three torus links **all embed in the same Bring-surface
genus-$4$ Seifert fiber**
([prop:torus-embeddable-complete](#prop:torus-embeddable-complete)),
since their Seifert genera $1, 2, 3$ are each $\leq 4$. So the
six projectors live in $H_2(q)$ in the same ambient host as the
saturating EM/strong carriers $\{T_{2,9}, T_{3,5}\}$. The
completeness statement asserts that within the EW sector, the
direct sum $e_W^{+} \oplus e_W^{-} \oplus \cdots \oplus e_{T(2,8)}^{-}$
exhausts the Wedderburn-block content of the EW Hecke action on
Bring's surface.

### Proof sketch (parallels EM spectral completeness)

The argument mirrors
[`thm:em-spectral-completeness`](#thm:em-spectral-completeness)
applied to the two-strand idempotent decomposition $w_+ + w_- = 1$
on the EM sector:

**Step 1 — Per-host two-strand completeness.**
For each $T(2, 2k)$, the two-strand braiding
$\sigma_1 \in B_2$ has the standard Hecke decomposition
$w_+^{(k)} + w_-^{(k)} = \mathbf{1}_{H_2(q)}$ where $w_\pm^{(k)}$
are the (sym, alt) idempotents acting on $V \otimes V$ for the
$k$-th host's natural representation $V_k$.

**Step 2 — EW sector decomposes by even-twist parity within
$H_2(q)$ on Bring.**
All three carriers live in **the same** $H_2(q)$ over $R$ (one
host: Bring's surface). They are distinguished by their
even-twist parameter $k \in \{2, 3, 4\}$, which selects different
generalized eigenspaces under $\sigma_1^{2k}$ — specifically, the
six idempotents $e_X^\pm$ are pairwise orthogonal as elements of
$H_2(q)$ because the eigenvalues $(q^{2k}, q^{-2k})$ for $k = 2,
3, 4$ are pairwise distinct in $R$ (as $q$ is not a root of
unity). The EW total Hecke action is therefore
$\bigoplus_{k=2,3,4} H_2(q)|_{T(2, 2k)\text{-spectrum}}$, with
completeness across the direct sum following from per-link
completeness in Step 1 + pairwise orthogonality of the six
$e_X^\pm$ in $H_2(q)$.

**Step 3 — Cell-content trace, not Plancherel weight.**

The substrate-level structural quantity is the cell-content
trace, computed directly from the eight pure-pattern
multiplicities $(4, 2, 1, 3, 3, 1, 2, 4)$:

$$
  \mathrm{tr}_{\rm pure}\bigl(\sigma_1^4 \sigma_3^6 \sigma_5^8\bigr)
  \;=\;
  4\bigl(q^{18} + q^{-18}\bigr)
  + 2\bigl(q^{10} + q^{-10}\bigr)
  + \bigl(q^{6} + q^{-6}\bigr)
  + 3\bigl(q^{2} + q^{-2}\bigr)
  \;\in\; R.
$$

This expression is **bar-self-dual** under
$\iota \colon q \mapsto q^{-1}$ — the substrate-level
[bar T-duality](#prop:bar-t-duality-substrate) at the trace level.
The duality is automatic from the disjoint-strand-pair
construction: each $\sigma_i^{2k}$ is bar-self-dual on its own
(`prop:even-twist-torus-link-psd-feasibility`),
and disjoint products preserve the duality.

The Plancherel-weighted form
$\mathcal{N}_{\rm sym}^{\rm Plancherel} = q^6 (1 + q^2 + q^4)/3$
from
[`prop:weak-symmetric-normalization`](#prop:weak-symmetric-normalization)
is **not** bar-self-dual and differs from $\mathrm{tr}_{\rm pure}$
by a factor of $\sim 22$ at $q_0$. It is retained only as a
legacy/degenerate reference; the cell-content trace is operative.

### Downstream consequence — the weak-scale crossing count

The weak-scale crossing count $N_v$ is conjecturally derivable
from the **bar-self-dual cell-content trace** over the EW
force-carrier sector. The structural ansatz takes the form

$$
  N_v \;\stackrel{?}{=}\;
  F\bigl( [2]_q,\, [4]_q,\, [6]_q,\, [8]_q,\,
  \mathrm{tr}_{\rm pure}(\sigma_1^4 \sigma_3^6 \sigma_5^8) \bigr)
$$

for some $R$-rational function $F$. The bar-self-duality of
$\mathrm{tr}_{\rm pure}$ is a strong structural constraint on
admissible $F$: any candidate must be invariant under
$\iota: q \mapsto q^{-1}$ (since $N_v$ is a $q$-independent
constant when evaluated at $q_0$, and the substrate-level
identity must hold at all generic $q$).

**PSLQ test.** The constrained basis is
$\{[2]_q, [4]_q, [6]_q, [8]_q, q^k, h^k,
\mathrm{tr}_{\rm pure}\}$ — strictly smaller than the
brute-force monomial basis used previously. The earlier
Plancherel-weight basis $\{[2k]_q^2/[2]_q, \mathcal{N}_{\rm sym}\}$
is **superseded**.
### Consequences

If this conjecture closes:
- **the weak-scale crossing count $N_v$**: pinned by constrained PSLQ on the
  extended basis
- **β-decay rates**: $G_F = 1/(\sqrt{2}\,N_v^2 E_\times^2 \mu_0^2)$
  becomes derivable from $(q_0, m_e)$ alone, closing every β-decay
  half-life prediction simultaneously.

**Archimedean specialisation.** What follows sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
