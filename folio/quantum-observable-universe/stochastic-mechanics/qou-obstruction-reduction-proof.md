*What the axioms supply, and what they do not.* Three facts are relevant to the hypothesis of the Wigner axiom.

**Step 1: Observability kills $HH^0$.**
The QOU axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$
([observability](#def:quantum-observable-universe)) is the statement

$$
HH^0(\mathcal{U}_q, \mathrm{Ad}) = \mathrm{Ad}^G = 0.
$$

The adjoint representation of a semisimple group has no invariant vectors (equivalently: $\mathfrak{g}$ has trivial centre).

**Step 2: Duality is cohomology-to-homology, with a twist.**
For a Noetherian Hopf algebra $H$ that is Artin--Schelter Gorenstein of dimension $d$ — this covers $\mathcal{U}(\mathfrak{g})$, $\mathcal{O}(G)$, $\mathcal{U}_q(\mathfrak{g})$ and $\mathcal{O}_q(G)$ — Brown and Zhang \cite{brown-zhang-2008} prove the twisted Poincaré duality

$$
HH^{i}(H, M) \;\cong\; HH_{d-i}(H, {}_{\nu}M),
$$

where $\nu$ is the Nakayama automorphism of $H$: trivial up to an inner automorphism for $\mathcal{U}(\mathfrak{g})$ and $\mathcal{O}(G)$, and non-trivial for the quantum groups. The untwisted form fails at $q \neq 1$: the Hochschild homology of $\mathcal{O}_q(\mathrm{SL}_2)$ drops in top degree \cite{feng-tsygan-1991}, and the one-dimensional top group reappears only in the twisted theory \cite{hadfield-krahmer-2005}. With $d = \dim G = 3$ the relevant identification is $HH^2(H, \mathrm{Ad}) \cong HH_1(H, {}_{\nu}\mathrm{Ad})$ — first Hochschild *homology* with twisted coefficients, not the dual of $HH^1$.

**Step 3: At the classical point the space is zero.**
For $H = \mathcal{U}(\mathfrak{g})$ one has $HH^n(\mathcal{U}(\mathfrak{g}), M) \cong H^n(\mathfrak{g}, M)$ with $M$ carrying the adjoint action, and Whitehead's lemmas \cite{weibel1994} give $H^1(\mathfrak{g}, M) = H^2(\mathfrak{g}, M) = 0$ for $\mathfrak{g}$ semisimple in characteristic $0$ and $M$ finite-dimensional, hence for the locally finite $\mathrm{Ad}(A)$. So $\mathrm{Obs} = 0$ at $q = 1$. The one-dimensionality of the obstruction space at $q \neq 1$ is therefore not a consequence of the axioms; it is the first clause of the Wigner axiom, and the identification of its generator with the Euler class is the second.

*Proof of (a).* By the second clause the generator $w(A)$ maps to $e(\xi) = e(TM_0) \in H^2(M_0; \mathbb{Z})$. The Euler class of the tangent bundle of a closed oriented surface integrates to its Euler characteristic (Poincaré–Hopf), so $\langle e(TM_0), [M_0] \rangle = \chi_{\mathrm{eu}}(M_0) = 2 - 2g(M_0)$. Since the obstruction space is one-dimensional by the first clause, the class is determined by this integer. No Hochschild--Kostant--Rosenberg identification is used. $\square$

*Proof of (b).*
This is the Kummer specialisation
([Kummer](#prop:ns-kummer-specialisation)): $\kappa_0 \bmod n = 0$
in $H^2(\mathcal{S}, \mathbb{G}_m) / nH^2(\mathcal{S}, \mathbb{G}_m)$
iff $n$ divides $\chi_{\mathrm{eu}}(M_0)$. Equivalently, the motivic
Galois character $\chi^{\mathrm{mot}}_A$ is non-trivial at every
finite place $p \nmid \chi_{\mathrm{eu}}(M_0)$
([motivic perpetual obstruction](#thm:motivic-perpetual-obstruction), proved via Route A: prime-ideal collapse, $C = a_0(-1) + 2 \cdot a_1(-1)$). $\square$
