Interactive visualization of beta decay as a $T_{3,5}$ braid insertion on the nuclear braid word.

## The $T_{3,5}$ weak vertex

The weak interaction is carried by the torus knot $T_{3,5}$ ([force identification](#rem:force-knot-identification)). Its braid word $\beta_{T_{3,5}} = (\sigma_1 \sigma_2)^5$ has $10$ crossings. This simulator draws the full braid left-to-right. It shows strands flowing from the parent nucleon through the $T_{3,5}$ insertion to the daughter nucleon plus lepton pair.

## Panels

1. **Braid flow diagram** --- The $10$-crossing $T_{3,5}$ braid inserted at the converting $\mathfrak{d}$-quark crossing. Input strands (left) carry the parent quark content. Output strands (right) carry the daughter quark content plus the emitted electron ($T_{2,3}$, $3$ crossings) and antineutrino ($K_{0_1}$, $0$ crossings). Toggle between $\beta^-$ ($\mathfrak{d} \to \mathfrak{u}$) and $\beta^+$ ($\mathfrak{u} \to \mathfrak{d}$).
2. **Transfer matrix crossings** --- The three nuclear crossing types $T_{pp}$, $T_{nn}$, $T_{\mathrm{mix}}$ drawn as individual braid crossings, with their $2 \times 2$ matrix entries evaluated at the substrate parameter $q$.
3. **Hecke and Skein relations** --- The Hecke relation $T^2 = (q - q^{-1})T + 1$ and the Skein relation $q[L_+] - q^{-1}[L_-] = (q^{1/2} - q^{-1/2})[L_0]$ illustrated as braid crossing reductions.
4. **Universal decay matrix** --- The equally-spaced property $\Delta_\beta = T_{\mathrm{mix}} - T_{nn} = T_{pp} - T_{\mathrm{mix}}$ with explicit polynomial entries.

## Strand conventions

Strands follow the pointed-knot convention from the building-block table ([building blocks](#rem:building-block-knots)):

- **Solid** ($\bullet$) = particle (positive time orientation, $T_{2,3}$).
- **Outlined** ($\circ$) = antiparticle (negative time / mirror, $\overline{T_{2,3}}$).
- **Basepoint** marked on each strand.

The $\mathfrak{u}$-quark strands are drawn in blue (solid), and $\mathfrak{d}$-quark strands in red (outlined). This matches the crossing-chirality convention where positive crossings are $\mathfrak{u}\text{-}\mathfrak{u}$ and negative crossings are $\mathfrak{d}\text{-}\mathfrak{d}$.

## The $10$-crossing budget

$$
  \underbrace{10}_{\text{total}} = 
  \underbrace{3}_{e^- (T_{2,3})} + 
  \underbrace{0}_{\bar{\nu}_e (K_{0_1})} + 
  \underbrace{7}_{\text{R2 re-reduction}}
$$

The $7$ re-reduction crossings modify inter-nucleon crossing types at the converting quark's strand. These produce the dominant contribution to the $Q$-value.
