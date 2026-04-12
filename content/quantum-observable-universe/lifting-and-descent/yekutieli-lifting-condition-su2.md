Continuing [SU(2) as a QOU](#ex:qou-su2), we verify the
[Yekutieli lifting condition](#def:yekutieli-lifting-condition) for
$G = \mathrm{SU}(2)$.

**The site.** Take $\mathcal{S} = \mathbb{CP}^1$ with the analytic
topology, where $\mathbb{CP}^1 \cong \mathrm{SU}(2)/\mathrm{U}(1)$ is
the flag variety (equivalently, the space of maximal tori in
$\mathrm{SU}(2)$).

**The gerbe.** The $\mathrm{SU}(2)$-principal bundle
$\pi \colon \mathrm{SU}(2) \to \mathbb{CP}^1$ defines a gerbe
$\mathfrak{G}$ on $\mathcal{S}$: objects over an open $U \subseteq \mathbb{CP}^1$ are local lifts of $\pi$, and morphisms are bundle
isomorphisms.  The banding sheaf is
$\mathcal{B} = \mathcal{O}_{\mathbb{CP}^1}^{\times}$, the sheaf of
nowhere-vanishing holomorphic functions.

**The obstruction class.** By the exponential sequence
$0 \to \mathbb{Z} \to \mathcal{O} \to \mathcal{O}^{\times} \to 0$
on $\mathbb{CP}^1$, the connecting homomorphism gives

$$
  H^1(\mathbb{CP}^1, \mathcal{O}^{\times})
  \xrightarrow{c_1}
  H^2(\mathbb{CP}^1, \mathbb{Z})  \cong  \mathbb{Z}.
$$

The obstruction to lifting a line bundle $L$ on $\mathbb{CP}^1$ to the
total space of the gerbe is its first Chern class
$\kappa(L) = c_1(L) \in H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$.

**Verification.** The lifting condition requires that $L$ admits a lift
if and only if $\kappa(L) = 0$.  For $\mathbb{CP}^1$:

- The tautological line bundle $\mathcal{O}(-1)$ has $c_1 = -1 \neq 0$,
  so it does *not* lift.
- The trivial bundle $\mathcal{O}$ has $c_1 = 0$, and it lifts via the
  constant section.

Since $H^2(\mathbb{CP}^1, \mathbb{Z}) \cong \mathbb{Z}$ is
torsion-free, the vanishing $\kappa(L) = 0$ is both necessary and
sufficient for a lift to exist, confirming the Yekutieli lifting
condition for $\mathrm{SU}(2)$.
