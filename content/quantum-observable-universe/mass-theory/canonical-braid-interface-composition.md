**Definition (canonical-braid interface composition).** *Let
$\beta(Z, N) \in H_{3A}(q)$ be the canonical atomic braid in the
standard pppnnn ordering (built by
[`mass_at_3A_proper.atom_braid_word_3A`](../../computations/mass_at_3A_proper.py)).
The* $A - 1$ *inter-nucleon interface generators
$\sigma_{3k + 2}$ ($k = 0, \ldots, A - 2$) are classified by the
flavour pair $(\text{nuc}_k, \text{nuc}_{k+1})$ they bridge:*

See [Table 1](#tbl:canonical-braid-interface-composition-table1-data).

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

See [Table 2](#tbl:canonical-braid-interface-composition-table2-data).

### Z$\leftrightarrow$N asymmetry and ordering dependence

Under the pppnnn ordering the asymmetric counts $(n_{pp}, n_{nn})$
encode Z$\leftrightarrow$N asymmetry directly. **Alternative orderings** (e.g.,
alternating pnpnpn) would produce different interface compositions
for the same atom — at $(Z=2, N=2)$ ${}^{4}$He:

See [Table 3](#tbl:canonical-braid-interface-composition-table3-data).

The canonical pppnnn ordering is fixed by
[`atom_braid_word_3A`](../../computations/mass_at_3A_proper.py);
this definition is **ordering-specific**. Generalising to arbitrary
orderings requires an additional `ordering: list[Nucleon]` argument,
captured in the
[`interface_composition.py`](../../computations/interface_composition.py)
utility module's `interface_composition(ordering)` function.

### Role in substrate derivation

The Δ_coupling residual fit localised the ${}^{3}$He
proton-heavy anomaly to the **pp interface asymmetry**: ${}^{3}$He has
$n_{pp} = 1$ (excess $\sigma$) while T has $n_{nn} = 1$ (excess $\sigma^{-1}$), and
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
$\gamma \approx -1.295$ MeV closes the 4-atom probe set by definition
(3 free parameters, 3 non-trivial equations). The fit is **not
predictive** until extended to atoms with distinct $(n_{pp}, n_{nn})$
combinations beyond the $\{$D, T, ${}^{3}$He, ${}^{4}$He$\}$ set. See
[`docs/audits/-a-minus-2-q-substrate-derivation.md`](../../docs/audits/-a-minus-2-q-substrate-derivation.md)
§v6 for the open-question framing.
