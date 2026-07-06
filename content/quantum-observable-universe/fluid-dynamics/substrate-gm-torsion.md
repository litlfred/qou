We identify the [substrate parameter](#def:substrate-parameter) as an element of $\mathrm{End}(\mathbf{1}) \cong k^\times$, serving as the fibre coordinate on a $\mathbb{G}_m$-family. This makes the $\mathbb{G}_m$-structure explicit and reformulates the not-root-of-unity axiom as torsion avoidance.

**The multiplicative group scheme.**
The substrate parameter acts as a section of $\mathbb{G}_m$: a map $q \colon M \to \mathbb{G}_m(k)$ where $\mathbb{G}_m(k) = k^\times$. The $\mathbb{G}_m$-family of operators

$$
  d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d
$$

is a universal deformation parametrised by the tautological coordinate on $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$.

The Lusztig integral form $\mathcal{U}^\mathbb{Z}_q(\mathfrak{su}(2))$ is a $\mathbb{Z}[q, q^{-1}]$-algebra. A ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ is a $k$-point of $\mathbb{G}_m$. Base change along $\iota$ specialises the universal family to the quantum group at $q_0 = \iota(q)$.

**Torsion points of the multiplicative group.**
The torsion subgroup of $\mathbb{G}_m$ consists of the roots of unity:

$$
  \mathbb{G}_m[n] = \mu_n = \{\zeta \in k^\times : \zeta^n = 1\},
  \qquad
  \mathbb{G}_m[\mathrm{tors}] = \mu_\infty = \bigcup_{n \geq 1} \mu_n.
$$

The not-root-of-unity axiom in the [substrate parameter](#def:substrate-parameter) states:

$$
  q(p) \notin \mu_\infty(k)
  \qquad\text{for all } p \in M.
$$

The section $q \colon M \to \mathbb{G}_m$ avoids the torsion subscheme. Its image lies in $\mathbb{G}_m \setminus \mu_\infty$.

**Necessity of torsion avoidance.**
At a torsion point $q_0 = e^{2\pi i m/n}$:

1. The quantum dimension $[n]_{q_0} = 0$ (the $n$-th quantum integer vanishes).
2. The Frobenius pairing degenerates on the representation $V_{(n-1)/2}$ (quantum dimension zero yields a null vector).
3. The non-degeneracy axiom (QOU axiom 1) fails.
4. The representation category truncates to finitely many simple objects, reducing to a modular tensor category (Chern--Simons TQFT at level $n$).

At $q_0 = 1$, we find the universal torsion point ($1^n = 1$ for all $n$). The quantum integer $[k]_1 = k$ remains non-zero for $k \geq 1$. However, the comultiplication becomes cocommutative ($R_1 = 1 \otimes 1$) and the braiding becomes symmetric. The braided structure collapses to a symmetric structure.

**The projective compactification.**
We embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via $k^\times \hookrightarrow k \cup \{\infty\}$. The two boundary points are:

- $q = 0$: the $d_q$ operator diverges due to the $q^{-1}$ pole. The spatial differential $d$ diverges.
- $q = \infty$: $d_q \to \pi_V \circ d$. The spatial components vanish, leaving only the pure vertical projection along the Reeb direction.

The torsion points $\mu_\infty$ are dense in $\mathbb{G}_m$ over $\mathbb{C}$. The substrate parameter avoids this dense set and lives in the non-torsion locus:

$$
  \mathbb{G}_m^{\mathrm{nt}}
  = \mathbb{G}_m \setminus \mu_\infty.
$$

For the archimedean realisation over $\mathbb{R}$, the torsion points in $\mathbb{R}^\times$ are $\{1, -1\}$. The condition $q > 1$ restricts $q$ to the torsion-free ray $(1, \infty) \subset \mathbb{R}^\times$.

**The $q = 1$ limit as torsion specialisation.**
The [NS regularity problem](#def:ns-regular-qou) examines the extension of the section $q \colon M \to \mathbb{G}_m^{\mathrm{nt}}$ to a section $\bar{q} \colon M \to \mathbb{G}_m$ that intersects the torsion point $q = 1$.

Extending a family across a torsion specialisation relies on the Neron model of the abelian scheme. The obstruction to extending the Frobenius--Hopf structure across $q = 1$ resides in the special fibre of the Neron model:

$$
  \mathrm{obs}(q \to 1)
   \in 
  \Phi_{q=1}(\mathbb{G}_m)
  = 
  \text{component group of the special fibre}.
$$

For $\mathbb{G}_m$ itself, the Neron model is trivial. The component group is trivial and the extension exists. However, the Frobenius--Hopf structure is a family of Hopf algebras parametrised by $\mathbb{G}_m$, not a $\mathbb{G}_m$-torsor. This makes the extension problem nontrivial.

**Connection to the NS obstruction.**
The [NS obstruction class](#prop:ns-obstruction-tower) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ resides in the cohomology with coefficients in the banding sheaf $\mathcal{B} = \mathcal{O}_M^\times$. The sheaf of units $\mathcal{O}_M^\times$ forms the sheaf of sections of $\mathbb{G}_m$. We identify:

$$
  \kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)
$$

The specialisation $q \to 1$ operates as the pullback along the inclusion $\{1\} \hookrightarrow \mathbb{G}_m$:

$$
  \kappa_n\big|_{q=1}
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{ \mathrm{sp}_{q=1}}
  H^2(\mathcal{S}, \mu_\infty).
$$

The specialisation map $\mathrm{sp}_{q=1}$ factors through the Kummer sequence:

$$
  1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n}
  \mathbb{G}_m \to 1
$$

The obstruction persists if and only if $\kappa_n$ is not divisible by $n$ in $H^2(\mathcal{S}, \mathbb{G}_m)$ for any $n$.

For the Descartes universe with $\chi(A) = -6$, this is a manifestation of the [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction). The class $\kappa_0$ is non-trivial at every finite place $p \nmid 6$. The specialisation $\kappa_0|_{q = \zeta_n}$ at every primitive $n$-th root of unity with $\gcd(n, 6) = 1$ is non-zero in $H^2(\mathcal{S}, \mu_n)$. The NS obstruction does not collapse. This provides the fluid-dynamics realization of the substrate's perpetual obstruction at every cyclotomic place.
