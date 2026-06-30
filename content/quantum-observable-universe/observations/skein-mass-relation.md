*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The mass functional $\mathcal{M}(\mathfrak{H})$ for a composite hadron $\mathfrak{H}$ is not additive but obeys the quantum Skein relation at every crossing in the color-exchange space:

$$
q \mathcal{M}(L_+) - q^{-1}\mathcal{M}(L_-) = (q^{1/2} - q^{-1/2})\mathcal{M}(L_0).
$$

Evaluation of the lepton mass ratio $m_{\mu}/m_{e}$ against **CODATA** recommended values yields a derivation of the local substrate parameter $q$ at leading order in the substrate-density truncation:

$$
\frac{m_{\mu}}{m_{e}} \;\stackrel{\text{LO}}{=}\; \frac{\mathrm{Vol}(4_1)}{\hbar_q^2}
  \approx \frac{:val[Vol_4_1]{precision=6}}{(1 - q^{-1})^2},
\qquad 206.7683 \implies q \approx 1.10998.
$$

> **Identification note (read before citing this formula).** The
> figure-eight $4_1$ here is the **Higgs** (mass mechanism), **not the
> muon**. The muon's own identity knot is the torus knot $T(2,5)$
> ([`prop:s5-equivariant-torus-knots`](s5-equivariant-torus-knots.md),
> [`lepton-meson-torus-knot-dictionary`](../particle-interactions/lepton-meson-torus-knot-dictionary.md));
> as a torus knot it has $\mathrm{Vol}_q = 0$ and **no intrinsic
> volume-mass**. So $\mathrm{Vol}(4_1)/\hbar_q^2$ is the **Higgs-coupling
> mass scale** — the figure-eight volume that *gives* the muon its mass —
> not the muon's own knot volume. Reading this as "muon $= 4_1$" is a
> category error (it confuses the muon with the Higgs that gives it
> mass); see
> [`docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md`](../../../docs/audits/2026-06-30-muon-knot-id-phi-q-evidence.md)
> (owner-ruled 2026-06-30). What this formula *derives* is $q_0$ — via
> the muon mass scale set by the Higgs volume — not a muon–$4_1$
> identification.
