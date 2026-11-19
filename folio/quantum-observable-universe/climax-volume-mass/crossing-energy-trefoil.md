The crossing energy ([crossing energy](#def:crossing-energy)) is evaluated first for the trefoil knot and then for composite hadron binding.

**Single crossing energy.**
Each crossing in a knot diagram carries Skein weight $q$ (positive crossing) or $-q^{-1}$ (negative crossing). For a positive crossing, the energy contribution is

$$
  \mathfrak{E}_{\mathrm{cross}}^{(+)} = q,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}^{(-)} = -q^{-1}.
$$

The net energy of a single positive crossing minus a single negative crossing is $q - q^{-1}$. This coefficient appears in the Skein relation $T - T^{-1} = q - q^{-1}$.

**Trefoil: three positive crossings.**
The standard diagram of the trefoil $\tau(2,3)$ has three positive crossings. Its total crossing energy is

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
  =  3q.
$$

At the aether parameter $q \approx 1.110$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
   \approx  3 \times 1.110
  =  3.330.
$$

This is positive. The trefoil is a single knot, not a composite, so there is no linking to provide negative binding energy.

**Binding in composites.**
A hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ is a composite. Its linking $\mathcal{L}$ introduces additional crossings between constituent knots. Mutual crossings between distinct components can contribute *negative* energy (via negative crossings in the linking braid word). The total crossing energy of a composite is

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\sum_{i} \mathfrak{E}_{\mathrm{cross}}(K_i)}_{\text{self-crossings (positive)}}
  + 
  \underbrace{\mathfrak{E}_{\mathrm{cross}}(\mathcal{L})}_{\text{mutual crossings (can be negative)}}.
$$

The composite is *bound* when the total is negative: $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) < 0$. The mutual linking energy overcomes the individual knot crossing costs. The composite is energetically favorable relative to the separated constituents.

**Proton binding.**
The proton ([proton as Borromean hadron](#ex:hadron-proton)) consists of three quarks linked in a Borromean configuration. The Borromean linking contributes enough negative mutual crossing energy to make $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. This explains why the proton is a stable bound state: disassembling it into free quarks demands adding energy equal to $|\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|$.
