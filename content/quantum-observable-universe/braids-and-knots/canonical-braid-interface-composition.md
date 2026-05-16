**Definition (canonical-braid interface composition).** *Let
$\beta(Z, N) \in H_{3A}(q)$ be the canonical atomic braid in the
standard pppnnn ordering (built by
[`mass_at_3A_proper.atom_braid_word_3A`](../../folio-assistant/computations/mass_at_3A_proper.py)).
The* $A - 1$ *inter-nucleon interface generators
$\sigma_{3k + 2}$ ($k = 0, \ldots, A - 2$) are classified by the
flavour pair $(\text{nuc}_k, \text{nuc}_{k+1})$ they bridge:*

| pair $(\mathrm{nuc}_k, \mathrm{nuc}_{k+1})$ | Hecke generator | content $(c, d)$ |
|---|---|---|
| $(\mathfrak{p}, \mathfrak{p})$ | $\sigma$ | $(1, 0)$ |
| $(\mathfrak{p}, \mathfrak{n})$ or $(\mathfrak{n}, \mathfrak{p})$ | $\Delta_I = \sigma - h/2$ | $(1, -h/2)$ |
| $(\mathfrak{n}, \mathfrak{n})$ | $\sigma^{-1}$ | $(1, -h)$ |

*The interface composition $(n_{pp}(Z, N), n_{pn}(Z, N), n_{nn}(Z, N))$
counts these three types. Under canonical pppnnn ordering, closed
forms are:*

$$
\boxed{\quad
n_{pp}(Z, N) = \max(0, Z - 1), \quad
n_{nn}(Z, N) = \max(0, N - 1), \quad
n_{pn}(Z, N) = \begin{cases} 1 & Z \geq 1, N \geq 1 \\ 0 & \text{else}\end{cases}
\quad}
$$

*with total count $n_{pp} + n_{pn} + n_{nn} = A - 1$.*

### Empirical table

| atom | $(Z, N)$ | $A$ | $n_{pp}$ | $n_{pn}$ | $n_{nn}$ | total |
|---|---|---:|---:|---:|---:|---:|
| D | $(1, 1)$ | 2 | 0 | 1 | 0 | 1 |
| T | $(1, 2)$ | 3 | 0 | 1 | 1 | 2 |
| ${}^3\mathrm{He}$ | $(2, 1)$ | 3 | 1 | 1 | 0 | 2 |
| ${}^4\mathrm{He}$ | $(2, 2)$ | 4 | 1 | 2 | 1 | 4 |
| ${}^5\mathrm{Li}$ | $(3, 2)$ | 5 | 2 | 1 | 1 | 4 |
| ${}^6\mathrm{He}$ | $(2, 4)$ | 6 | 1 | 1 | 3 | 5 |
| ${}^6\mathrm{Li}$ | $(3, 3)$ | 6 | 2 | 1 | 2 | 5 |
| ${}^6\mathrm{Be}$ | $(4, 2)$ | 6 | 3 | 1 | 1 | 5 |
| ${}^{16}\mathrm{O}$ | $(8, 8)$ | 16 | 7 | 1 | 7 | 15 |

### Z↔N asymmetry and ordering dependence

Under the pppnnn ordering the asymmetric counts $(n_{pp}, n_{nn})$
encode Z↔N asymmetry directly. **Alternative orderings** (e.g.\
alternating pnpnpn) would produce different interface compositions
for the same atom — at $(Z=2, N=2)$ ⁴He:

| ordering | $n_{pp}$ | $n_{pn}$ | $n_{nn}$ |
|---|---:|---:|---:|
| pppnnn (canonical) | 1 | 2 | 1 |
| pnpn (alternating) | 0 | 3 | 0 |
| ppnn (paired) | 1 | 1 | 1 |

The canonical pppnnn ordering is fixed by
[`atom_braid_word_3A`](../../folio-assistant/computations/mass_at_3A_proper.py);
this definition is **ordering-specific**. Generalising to arbitrary
orderings requires an additional `ordering: list[Nucleon]` argument,
captured in the
[`interface_composition.py`](../../folio-assistant/computations/interface_composition.py)
utility module's `interface_composition(ordering)` function.

### Role in substrate derivation

The Δ_coupling residual fit (PR #656 v6) localised the ³He
proton-heavy anomaly to the **pp interface asymmetry**: ³He has
$n_{pp} = 1$ (excess σ) while T has $n_{nn} = 1$ (excess σ⁻¹), and
the pp/nn interfaces contribute non-equivalently through the
hook's antisymmetric column. A linear fit

$$
\Delta_{\mathrm{coupling}}(Z, N)
\;\approx\;
[A - 2]_q \cdot E_0 \cdot \log(1/h)
\,+\, \alpha \, n_{pp}
\,+\, \beta \, n_{nn}
\,+\, \gamma
$$

with $\alpha \approx +0.224$ MeV, $\beta \approx +1.093$ MeV,
$\gamma \approx -1.295$ MeV closes the 4-atom probe set trivially
(3 free parameters, 3 non-trivial equations). The fit is **not
predictive** until extended to atoms with distinct $(n_{pp}, n_{nn})$
combinations beyond the $\{$D, T, ³He, ⁴He$\}$ set. See
[`docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md`](../../docs/audits/2026-05-15-a-minus-2-q-substrate-derivation.md)
§v6 for the open-question framing.
