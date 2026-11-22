**Proposition (conditional on [Quarks as Borromean-linked unknots in the exceptional divisor](../predicted-spectra/borromean-quark.md)).**
*Let $h = q - q^{-1}$ and $\mathfrak{E}_0 = m_e/(q(q-1))$. Let $\mathrm{net}(p) = 1 - \tfrac{h}{2}$ and $\mathrm{net}(n) = 1 - \tfrac{3h}{2} + \tfrac{h^2}{2}$ be the single-wrap normal-form net coefficients of the proton $[u,u,d]$ and neutron $[u,d,d]$ in $H_3(q)$ (from [Quarks as Borromean-linked unknots in the exceptional divisor](../predicted-spectra/borromean-quark.md)). For any trace difference $\Delta\mathrm{tr}$,*

$$
\mathfrak{E}_0 \cdot \mathrm{net}(p) \cdot \Delta\mathrm{tr} \;=\; \mathfrak{Q}_\beta \cdot \frac{\Delta\mathrm{tr}}{h}.
$$

*The deuteron binding functional $\mathfrak{E}_0\,(1-\tfrac{h}{2})\,\Delta\mathrm{tr}$ dresses the energy scale $\mathfrak{E}_0$ by the proton net coefficient $\mathrm{net}(p)$. It is related to the $\beta$-decay $Q$-value $\mathfrak{Q}_\beta$ by the single Hecke factor $h$.*

Context. The trace-canonical deuteron binding on the $\mathfrak{E}_0$ route over-binds by $+11.99\%$. Dressing it by $(1-\tfrac{h}{2})$ corrects it to $+0.12\%$ of AME2020 without fitted constants. The term $(1-\tfrac{h}{2})$ is exactly $\mathrm{net}(p)$.

The derivation is exact in the field. The key identity is division-free:

$$
\Delta(\mathrm{net}) \;=\; \mathrm{net}(n) - \mathrm{net}(p) \;=\; -\,h \cdot \mathrm{net}(p),
$$

which holds since $(1 - \tfrac{3h}{2} + \tfrac{h^2}{2}) - (1 - \tfrac{h}{2}) = -h + \tfrac{h^2}{2} = -h(1-\tfrac{h}{2})$.
In the substrate regime $0 < h < 2$, the proton coefficient $\mathrm{net}(p) > 0$. Then $|\Delta(\mathrm{net})| = h\,\mathrm{net}(p)$. The $Q$-value ansatz $\mathfrak{Q}_\beta = |\Delta(\mathrm{net})|\,\mathfrak{E}_0$ from [Symbolic $Q$-value of free neutron decay](../nuclear-interactions/neutron-qvalue-symbolic.md) yields:

$$
\mathfrak{Q}_\beta \;=\; \mathfrak{E}_0 \, h \, \mathrm{net}(p).
$$

Dividing by $h \neq 0$ and multiplying by $\Delta\mathrm{tr}$ yields the proposition. The binding dressing $\mathrm{net}(p)$ and the $Q$-value differ by the factor $h = q - q^{-1}$, which is bar-odd. Neither side has a definite bar parity: the bar-involution sends $h$ to $-h$, hence $\mathrm{net}(p) = 1 - \tfrac{h}{2}$ to $1 + \tfrac{h}{2}$. The relation is therefore a factor of $h$, not an instance of the even/odd split conjectured in [The binding trace and the $\mathfrak{Q}_\beta$ residue are the bar-even and bar-odd parts of one fibre element](../mass-theory/bar-parity-split.md).

Scope. The identities are exact. The magnitude claim $B_D \approx \mathfrak{E}_0\,\mathrm{net}(p)\,\Delta\mathrm{tr}$ remains an observation. It accurately models the deuteron ($+0.12\%$), but does not extend to $A \geq 3$ because the extensive deficit acts as a separate mechanism. This isolates the origin of $(1-\tfrac{h}{2})$ to the proton normal-form net coefficient, linking it to the $\beta$-decay sector. The $\Delta_\lambda$ gate remains the general binding law.
