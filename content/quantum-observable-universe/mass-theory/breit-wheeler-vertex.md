The **Breit--Wheeler process** $\gamma\gamma \to e^-e^+$ is the
creation of an electron--positron pair from two real photons.
In the QOU the entire vertex is encoded in the Iwahori--Hecke algebra
$H_n(R, q)$ acting on the exceptional divisor
$\mathcal{S}_p \cong \mathbb{P}^1(\mathbb{C})$
([exceptional divisor](#def:exceptional-divisor)).

## The Breit--Wheeler vertex on the exceptional divisor

### Polarisation states as Hecke generators

The exceptional divisor $\mathcal{S}_p$ is the $\mathbb{P}^1(\mathbb{C})$
fibre of the state bundle $\mathcal{S}$ at a brane point $p$.  Its
homogeneous coordinates $[v_1 : v_2]$ parametrise the two
independent polarisation directions of a spin-$1$ field residing at
$p$.  The Reeb bundle $\mathcal{R}_p = (S^3 \xrightarrow{\pi_H} S^2,
\xi_q)$ ([Reeb bundle](#def:reeb-bundle)) is the Hopf fibration over
$\mathcal{S}_p$; its $U(1)$ holonomy $e^{2\pi i/[2]_q}$, with
$[2]_q = q + q^{-1}$, is the $q$-deformed phase acquired by a
photon completing one full rotation in the polarisation sphere.

The two Hecke generators act on $\mathcal{S}_p$ as follows:

| Generator | Coordinate patch | Polarisation mode | Eigenvalues of $\sigma_i$ |
|-----------|-----------------|-------------------|----------------------|
| $\sigma_0$ | $v_2 \neq 0$ (affine chart $z = v_1/v_2$) | horizontal ($\leftrightarrow$) | $+q$ (left), $-q^{-1}$ (right) |
| $\sigma_1$ | $v_1 \neq 0$ (affine chart $w = v_2/v_1$) | vertical ($\updownarrow$) | $+q$ (left), $-q^{-1}$ (right) |

The Hecke relation $(\sigma_i - q)(\sigma_i + q^{-1}) = 0$ is therefore the
**photon helicity equation**: its two roots $+q$ and $-q^{-1}$ are
the left- and right-circular polarisation eigenvalues.  A linearly
polarised photon is a superposition of these two eigenstates, with
the polarisation angle $\psi$ encoded in the ratio $v_1/v_2 \in
\mathcal{S}_p$.

### The pair-creation vertex

The two-photon state $\gamma_1 \otimes \gamma_2$ is a word in
$H_n(R, q)$.  Three cases arise depending on the relative polarisation:

**Same generator (parallel polarisation).**
$$
  \sigma_i \cdot \sigma_i
  =  (q - q^{-1})\sigma_i + \mathbf{1}.
$$
The Hecke relation reduces the word to a dressed photon plus the
vacuum $\mathbf{1}$ (neutrino).  No pair is created: the energy
$2E_\gamma$ does not exceed the pair threshold because the two
photons share the same polarisation degree of freedom and their
net helicity vanishes only modulo the Hecke reduction, leaving
a lower-energy residue.

**Orthogonal generators (perpendicular polarisation).**
$$
  \sigma_0 \cdot \sigma_1 =  L_+
  \qquad (\text{Hopf link intermediate state}).
$$
The product is already irreducible: it is the normal-form basis
element $L_+$ (Hopf link), a two-strand entangled state.  Applying
one further $\sigma_0$ from the substrate (the Reeb direction) completes
the trefoil:
$$
  L_+ \cdot \sigma_0
  =  \sigma_0\sigma_1\sigma_0
  =  e^-.
$$
The positron $e^+$ is supplied by the mirror process
$\sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ (all crossing signs
reversed, [antiparticle crossing reversal](#prop:antiparticle-crossing-reversal)).

The complete vertex is therefore:
$$
  \underbrace{\sigma_0}_{\gamma_1, \mathrm{horiz.}}
   \cdot 
  \underbrace{\sigma_1}_{\gamma_2, \mathrm{vert.}}
  \xrightarrow{\xi_q\text{-insertion}}
  \underbrace{\sigma_0\sigma_1\sigma_0}_{e^-}
  + 
  \underbrace{(\sigma_0\sigma_1\sigma_0)^\sigma}_{e^+}.
$$

The $\xi_q$-insertion is the action of the Reeb vector field
$\xi_q$ on the Reeb bundle $\mathcal{R}_p$: it supplies the third
crossing $\sigma_0$ from the contact structure of $S^3$, at a cost
of one unit of Reeb charge $1/[2]_q$.

### Polarisation selection rule

The vertex vanishes unless the two photons occupy **distinct**
polarisation patches of $\mathbb{P}^1(\mathbb{C})$:

$$
  \langle e^-e^+ | \sigma_i\sigma_i | 0 \rangle =  0,
  \qquad
  \langle e^-e^+ | \sigma_0\sigma_1 | 0 \rangle  \neq  0.
$$

This is the topological origin of the Breit--Wheeler polarisation
selection rule: parallel-polarised photons apply the Hecke
relation and return lower-energy states; only orthogonally
polarised photons produce the Hopf-link intermediate $L_+$ that
the substrate can complete into the $e^-e^+$ trefoil pair.
