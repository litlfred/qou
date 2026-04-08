We evaluate the crossing energy
([crossing energy](#def:crossing-energy)) for the trefoil knot and
then explain how binding arises in hadrons.

**Single crossing energy.**
Each crossing in a knot diagram carries Skein weight $q$ (positive
crossing) or $-q^{-1}$ (negative crossing).  For a positive crossing,
the energy contribution is

$$
  \mathbf{E}_{\mathrm{cross}}^{(+)} = q,
  \qquad
  \mathbf{E}_{\mathrm{cross}}^{(-)} = -q^{-1}.
$$

The net energy of a single positive crossing minus a single negative
crossing is $q - q^{-1}$, which is the coefficient appearing in the
Skein relation $T - T^{-1} = q - q^{-1}$.

**Trefoil: three positive crossings.**
The standard diagram of the trefoil $\tau(2,3)$ has three positive
crossings.  Its total crossing energy is

$$
  \mathbf{E}_{\mathrm{cross}}(\tau(2,3))
  =  3q.
$$

At the substrate parameter $q \approx 1.110$:

$$
  \mathbf{E}_{\mathrm{cross}}(\tau(2,3))
   \approx  3 \times 1.110
  =  3.330.
$$

This is positive, reflecting the fact that the trefoil is a single
knot (not a composite) — there is no linking to provide negative
binding energy.

**Binding in composites.**
A hadron $\mathfrak{H} = [K_1, \ldots, K_n]_p \bowtie \mathcal{L}$ is a
composite whose linking $\mathcal{L}$ introduces additional crossings
between constituent knots.  Mutual crossings between distinct
components can contribute *negative* energy (from negative crossings
in the linking braid word), so the total crossing energy of a
composite is

$$
  \mathbf{E}_{\mathrm{cross}}(\mathfrak{H})
  = 
  \underbrace{\sum_{i} \mathbf{E}_{\mathrm{cross}}(K_i)}_{\text{self-crossings (positive)}}
  + 
  \underbrace{\mathbf{E}_{\mathrm{cross}}(\mathcal{L})}_{\text{mutual crossings (can be negative)}}.
$$

The composite is *bound* when the total is negative:
$\mathbf{E}_{\mathrm{cross}}(\mathfrak{H}) < 0$.  This means the mutual linking
energy overcomes the individual knot crossing costs — the composite
is energetically favorable relative to the separated constituents.

**Proton binding.**
The proton ([proton as Borromean hadron](#ex:hadron-proton)) consists
of three quarks linked in a Borromean configuration.  The Borromean
linking contributes enough negative mutual crossing energy to make
$\mathbf{E}_{\mathrm{cross}}(\mathfrak{p}) < 0$, which is why the
proton is a stable bound state: disassembling it into free quarks
would require adding energy equal to
$|\mathbf{E}_{\mathrm{cross}}(\mathfrak{p})|$.
