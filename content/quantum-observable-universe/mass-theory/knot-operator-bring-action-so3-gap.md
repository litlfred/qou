The six Gröbner-Shirshov knot operators of $H_3(q)$
([knot-operator action on the Bring surface](#rem:knot-operator-bring-action))
generate only the discrete group $S_3 \subset \mathrm{SO}(3)$; the
current pipeline therefore exploits the $\mathrm{SO}(3)$ structure
of the color-tube cross-section only partially.

## The $S_3 \subset \mathrm{SO}(3)$ gap

The six basis operators generate the **discrete** group
$S_3 \cong \mathrm{Dih}_3$ — the group of permutations of three
objects. This is a **subgroup** of $\mathrm{SO}(3)$:

$$
  S_3 \;\hookrightarrow\; \mathrm{SO}(3)
$$

embedded as the symmetry group of the equilateral triangle (the
three quark positions at $120°$ intervals on the color-tube
cross-section).

The **full** $\mathrm{SO}(3)$ acts by rotating the color-tube
cross-section continuously. This gives a continuous family of
crossing conventions parameterised by
$\mathrm{SO}(3) / S_3$ — a 3-dimensional manifold minus the
discrete quotient.

**Pipeline inputs:** only the $S_3$ subgroup — the six
discrete basis operators. The averaged crossing
$I = \sigma - (h/2) \cdot 1$ averages over the $S_3$ orbit.

**Pipeline exclusions:** the continuous
$\mathrm{SO}(3) / S_3$ rotations. These would give:

1. **Continuous families of Gram matrices** $G(\theta)$
   parameterised by rotation angle $\theta$. The LP shadow prices
   $y^*(\theta)$ would vary continuously, potentially identifying
   optimal orientations for the binding-energy prediction.

2. **Angular-momentum quantum numbers** from the
   $\mathrm{SO}(3)$ representation theory. The irreps of
   $\mathrm{SO}(3)$ are labelled by angular momentum $\ell$;
   restricting to $S_3$ gives the branching rule
   $V_\ell|_{S_3} = \bigoplus_\lambda n_{\ell,\lambda} V_\lambda$
   where the multiplicity $n_{\ell,\lambda}$ counts how many times
   each $S_3$ irrep appears in the $\ell$-th angular-momentum
   channel. These multiplicities are computable from character
   theory and may give the missing per-partition $\Delta_\lambda$
   values.

3. **Spherical harmonics on the Bring surface.** The Bring
   surface's genus-4 topology carries a natural Laplacian whose
   eigenfunctions are generalised spherical harmonics. The
   $\mathrm{SO}(3)$ action decomposes these into angular-momentum
   channels. The Markov trace, viewed as a function on the Bring
   surface, expands in these harmonics — giving a spectral
   decomposition of the mass formula in angular-momentum space.
