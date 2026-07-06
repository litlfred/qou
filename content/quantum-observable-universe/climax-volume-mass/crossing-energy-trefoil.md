We evaluate the crossing energy ([crossing energy](#def:crossing-energy)) for the trefoil knot to illustrate hadron binding.

**Single crossing energy.**
Each crossing in a knot diagram carries a Skein weight: $q$ for a positive crossing and $-q^{-1}$ for a negative crossing. The single-crossing energy contributions are

$$
  \mathfrak{E}_{\mathrm{cross}}^{(+)} = q,
  \qquad
  \mathfrak{E}_{\mathrm{cross}}^{(-)} = -q^{-1}.
$$

The net energy of one positive crossing minus one negative crossing is $q - q^{-1}$, exactly the coefficient of the Skein relation $T - T^{-1} = q - q^{-1}$.

**Trefoil: three positive crossings.**
The standard diagram of the trefoil $\tau(2,3)$ contains three positive crossings. Its total crossing energy is

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
  =  3q.
$$

Evaluated at the substrate parameter $q \approx 1.110$:

$$
  \mathfrak{E}_{\mathrm{cross}}(\tau(2,3))
   \approx  3 \times 1.110
  =  3.330.
$$

This positive value confirms that the trefoil acts as a single knot (not a composite). It lacks the inter-component linking required to supply negative binding energy.

**Binding in composites.**
A hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ is a composite whose linking $\mathcal{L}$ forces additional crossings between constituent knots. These mutual crossings can carry negative energy. The total crossing energy of a composite separates as

$$
  \mathfrak{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\sum_{i} \mathfrak{E}_{\mathrm{cross}}(K_i)}_{\text{self-crossings (positive)}}
  + 
  \underbrace{\mathfrak{E}_{\mathrm{cross}}(\mathcal{L})}_{\text{mutual crossings (can be negative)}}.
$$

A composite is bound when the total energy is negative: $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{H}) < 0$. The mutual linking energy must overcome the individual knot crossing costs, making the composite energetically favourable over its separated constituents.

**Proton binding.**
The proton ([proton as Borromean hadron](#ex:hadron-proton)) consists of three quarks locked in a Borromean configuration. This linking contributes sufficient negative mutual crossing energy to enforce $\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$. The proton thus forms a stable bound state. Disassembling it requires adding energy equal to $|\mathfrak{E}_{\mathrm{cross}}(\mathfrak{p})|$.
