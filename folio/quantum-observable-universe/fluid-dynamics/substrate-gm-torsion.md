The [substrate parameter](#def:substrate-parameter) operates as an element of $\mathrm{End}(\mathbf{1}) \cong k^\times$, establishing the fibre coordinate on a $\mathbb{G}_m$-family. This parameter must strictly avoid the torsion subgroup of $\mathbb{G}_m$.

**The multiplicative group scheme.**
The substrate parameter evaluates as a section $q \colon M \to \mathbb{G}_m(k)$ where $\mathbb{G}_m(k) = k^\times$. The $\mathbb{G}_m$-family of operators

$$
  d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d
$$

defines a universal deformation scaling under the tautological coordinate on $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$. A base change along a ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ specialises this family rigidly to the quantum group stationed at $q_0 = \iota(q)$.

**Torsion points of the multiplicative group.**
Roots of unity form the torsion subgroup:

$$
  \mathbb{G}_m[n] = \mu_n = \{\zeta \in k^\times : \zeta^n = 1\},
  \qquad
  \mathbb{G}_m[\mathrm{tors}] = \mu_\infty = \bigcup_{n \geq 1} \mu_n.
$$

The rigid axiom controlling the [substrate parameter](#def:substrate-parameter) dictates:

$$
  q(p) \notin \mu_\infty(k)
  \qquad\text{for all } p \in M.
$$

The section $q$ must remain anchored entirely within the non-torsion locus $\mathbb{G}_m \setminus \mu_\infty$.

**Necessity of torsion avoidance.**
At a strict torsion point $q_0 = e^{2\pi i m/n}$:

1. The quantum dimension $[n]_{q_0} = 0$ zeroes out.
2. The Frobenius pairing degenerates entirely on $V_{(n-1)/2}$.
3. The fundamental QOU non-degeneracy axiom collapses.
4. The representation category abruptly truncates into a modular tensor category (matching a Chern--Simons TQFT).

The anchor $q_0 = 1$ constitutes the **universal torsion point**. While quantum integers $[k]_1 = k$ avoid vanishing, the comultiplication turns cocommutative and the braiding degrades into symmetric swapping.

**The projective compactification.**
Embedding $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ defines two absolute boundaries. At $q = 0$, the operator $d_q$ hits an undefined $q^{-1}$ pole; the spatial differential diverges. At $q = \infty$, $d_q \to \pi_V \circ d$; spatial mechanics vanish entirely, isolating purely the vertical Reeb dynamic. Under $\mathbb{C}$, torsion points blanket $\mathbb{G}_m$ densely. Under $\mathbb{R}$, torsion points limit to $\{1, -1\}$; the physical substrate $q > 1$ cleanly occupies the torsion-free ray $(1, \infty)$.

**The $q = 1$ limit as torsion specialisation.**
The [NS regularity problem](#def:ns-regular-qou) effectively tests the extension of a valid non-torsion section $q \colon M \to \mathbb{G}_m^{\mathrm{nt}}$ directly into the universal torsion point $q = 1$. The Neron model of the abelian scheme controls this exact extension. Because the Frobenius--Hopf architecture operates as a parameterised family of Hopf algebras, not a simple $\mathbb{G}_m$-torsor, the obstruction directly populates the special fibre:

$$
  \mathrm{obs}(q \to 1)
   \in 
  \Phi_{q=1}(\mathbb{G}_m).
$$

**Connection to the NS obstruction.**
The [NS obstruction class](#prop:ns-obstruction-tower) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ is bound to the banding sheaf $\mathcal{B} = \mathcal{O}_M^\times$. Consequently,

$$
  \kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m).
$$

The specialisation $q \to 1$ applies exactly as a pullback:

$$
  \kappa_n\big|_{q=1}
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{ \mathrm{sp}_{q=1}}
  H^2(\mathcal{S}, \mu_\infty).
$$

The specialisation map factors precisely through the Kummer sequence. The obstruction definitively persists if and only if $\kappa_n$ remains **not** divisible by $n$ in $H^2(\mathcal{S}, \mathbb{G}_m)$ for any finite $n$.

On the Descartes universe ($\chi_{\mathrm{eu}}(M_0) = -6$), the [motivic perpetual obstruction theorem](#thm:motivic-perpetual-obstruction) commands that the specialisation $\kappa_0|_{q = \zeta_n}$ registers as non-zero at every primitive root avoiding $\gcd(n, 6) = 1$. The NS obstruction categorically cannot collapse.

*Scope.* On a closed surface $H^2(\mathcal{S}, \mathbb{G}_m) = 0$, so the class cannot live there. The Kummer obstruction is the image of the Reeb bundle's class $[\xi] \in H^1(\mathcal{S}, \mathbb{G}_m)$ under the connecting map to $H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n$, namely $\chi(A) \bmod n$ ([Kummer specialisation](#prop:ns-kummer-specialisation); [QU-to-QOU](#thm:qu-to-qou), item 3). It is non-zero for $n \nmid 6$. It is a global class and does not by itself determine the NS verdict.
