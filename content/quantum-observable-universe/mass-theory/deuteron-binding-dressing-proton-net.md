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
