The bar-even (binding, $\cosh$) and bar-odd ($\mathfrak{Q}_\beta$, $\sinh$) channels of the complex volume $\mathfrak{V}$ constitute a single Askey-scheme family evaluated through a rotation. Both the rotation and its limits are classical.

## Channel recurrences

The continuous $q$-Hermite polynomials $H_n(x \mid q)$ construct the proved basis of the binding kernel. Under simultaneous variable rotation $x \mapsto ix$ and bar involution $q \mapsto q^{-1}$, they yield the Ismail–Masson $q^{-1}$-Hermite polynomials:

$$
h_n(x \mid q) \;=\; i^{-n}\, H_n(ix \mid q^{-1}).
$$

The two channel recurrences are identical up to this rotation. This equivalence holds generically over a commutative ring $R$ equipped with a bar involution $\sigma$ and a formal rotation element $\iota$ satisfying $\iota^2 = -1$ ([complex-volume unification](#conj:binding-qbeta-complex-volume)): a sequence satisfies the odd-channel step at $(q, x)$ if and only if its $\iota$-rotation satisfies the even-channel step at $(\sigma q, \iota x)$. The archimedean $i$ emerges only downstream of the functor $\tau$.

## Orthogonality measures

The shared recurrence does not imply a shared spectral measure. The asymmetry remains structural:

| | even channel (binding) | odd channel ($\mathfrak{Q}_\beta$) |
|---|---|---|
| polynomials | $H_n(x \mid q)$, $x = \cos\theta$ | $h_n(x \mid q)$, $x = \sinh t$ |
| locus | compact, $x \in [-1, 1]$ | non-compact, $x \in \mathbb{R}$ |
| measure | $q$-Plancherel weight (determinate) | indeterminate moment problem |
| at $q_0 > 1$ | does not exist archimedeanly | native regime |

At the substrate anchor $q_0 > 1$, the even channel has no Bożejko–Speicher $q$-Fock realisation ([$q$-Gaussian obstruction at $q_0$](../mass-theory/q-gaussian-obstruction-at-q0.md)); its moment sequence is still positive definite, but no representing measure has a finite moment-generating function. The rotation is therefore irreducibly fibre-level, consistent with observable $\mathrm{Im}(q_0) = 0$. Measure asymmetry explains why parity projection left the binding error unchanged while the recurrence tie holds. A three-term recurrence is measure-independent, whereas a projection is not.

## Literature precedents

1. **Askey and Ismail–Masson**: The $q > 1$ continuation of continuous $q$-Hermite \cite{askey1989qhermite} provides the eigenfunction rotation \cite{ismail-masson1994}.
2. **The modular double**: The non-compact channel couples $q = e^{i\pi b^2}$ to $\tilde{q} = e^{-i\pi/b^2}$. Ponsot–Teschner Racah–Wigner coefficients for $U_q(\mathfrak{sl}(2,\mathbb{R}))$ \cite{ponsot-teschner2001} sit at the non-compact Askey–Wilson level. The map $b \leftrightarrow 1/b$ drives the $6j$-level rotation: the self-dual representations of $U_q$ are automatically $U_{\tilde q}$-representations \cite[\S2.1, \S2.3]{terashima-yamazaki2013}. That source writes $\tilde q = e^{+i\pi/b^2}$, the complex conjugate of the $\tilde q$ above. This divides $\Phi_q$ (Faddeev, non-compact) from $\mathrm{Li}_2^q$ (Rogers, compact).
3. **Quantum modularity**: The Andersen–Kashaev state integral of a knot factors into a $q$-series and a $\tilde{q}$-series. The leading asymptotics trace $\mathrm{Vol} + i\,\mathrm{CS}$ \cite{garoufalidis-zagier-2024}. One complex object dictates two channel factorizations, mirroring the Neumann–Zagier structure \cite{neumann-zagier1985} that $\mathfrak{V}$ transports to binding and decay.

## Leonard pairs

Zhedanov's $AW(3)$ algebra \cite{zhedanov1991} embeds the rotation as an operator identity. It pairs two operators, each tridiagonal in the other's eigenbasis, with Askey–Wilson polynomials forming the overlap matrix. Generically, any eigencolumn of the channel tridiagonal operator has orthogonal-polynomial entries. The self-duality that places the channel overlap into the Askey–Wilson family via Terwilliger's classification \cite{terwilliger2001} is carried as a Leonard-duality hypothesis.

## Vertex-algebra shadow

Under the bar involution, the character side splits as a $\mathbb{Z}_2$-orbifold $V = V^+ \oplus V^-$. The involved characters form false theta functions, appearing as $(1,p)$ singlet log-VOA characters \cite{creutzig-milas2014}. Their quantum modularity tracks the disk-interior versus root-of-unity rotation, using the Lawrence–Zagier $\Psi$ operation established for $W_\lambda$. This structure suggests a path to unify the lepton-tower $\Phi_q$ mechanism with the binding/decay model.
