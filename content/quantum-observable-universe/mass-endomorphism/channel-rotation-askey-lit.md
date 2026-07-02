The bar-even (binding / $\cosh$) and bar-odd ($\mathfrak{Q}_\beta$ / $\sinh$) channels of the complex volume $\mathfrak{V}$ are not two special-function stories. They are **one Askey-scheme family read through a rotation**, and both the rotation and its limits are classical.

## Same eigenfunctions, rotated

The continuous $q$-Hermite polynomials $H_n(x \mid q)$ — the proved basis of the binding kernel (the Rogers–Szegő identification) — become, under the simultaneous variable rotation $x \mapsto ix$ and bar involution $q \mapsto q^{-1}$, the Ismail–Masson $q^{-1}$-Hermite polynomials:

$$
h_n(x \mid q) \;=\; i^{-n}\, H_n(ix \mid q^{-1}).
$$

The two channel recurrences are therefore the *same* three-term recurrence read through the rotation. This is formalized generically — over a commutative ring $R$ with bar involution $\sigma$ and a *formal* rotation element $\iota$ with $\iota^2 = -1$, no $\mathbb{C}$ and no $\mathbb{R}$ — as `rotation_step` in the Lean sibling of [`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume): a sequence satisfies the odd-channel step at $(q, x)$ iff its $\iota$-rotation satisfies the even-channel step at the bar-conjugated data $(\sigma q, \iota x)$. The archimedean $i$ appears only downstream of the functor $\tau$.

## Different orthogonality measures

The shared recurrence does **not** extend to a shared spectral measure, and this asymmetry is structural:

| | even channel (binding) | odd channel ($\mathfrak{Q}_\beta$) |
|---|---|---|
| polynomials | $H_n(x \mid q)$, $x = \cos\theta$ | $h_n(x \mid q)$, $x = \sinh t$ |
| locus | compact, $x \in [-1, 1]$ | non-compact, $x \in \mathbb{R}$ |
| measure | $q$-Plancherel weight (determinate) | **indeterminate** moment problem |
| at $q_0 > 1$ | does not exist archimedeanly | native regime |

At the substrate anchor $q_0 > 1$ the even-channel measure fails to exist as a probability law ([`prop:q-gaussian-obstruction-at-q0`](../mass-theory/q-gaussian-obstruction-at-q0.md), the Bożejko–Speicher positivity obstruction), so the rotation is irreducibly fibre-level — consistent with $\mathrm{Im}(q_0) = 0$ at the observable level. This measure asymmetry is also the structural reason the parity-*projection* probe left the binding error unchanged while the *recurrence* tie remains live: a three-term recurrence is measure-independent; a projection is not.

## Three literature homes for the rotation

1. **Askey and Ismail–Masson**: the $q > 1$ continuation of continuous $q$-Hermite \cite{askey1989qhermite} and the rotation identity above \cite{ismail-masson1994} — the eigenfunction-level statement.
2. **The modular double**: the non-compact channel pairs $q = e^{i\pi b^2}$ with $\tilde{q} = e^{-i\pi/b^2}$; the Ponsot–Teschner Racah–Wigner coefficients for $U_q(\mathfrak{sl}(2,\mathbb{R}))$ \cite{ponsot-teschner2001} are the non-compact Askey–Wilson level, with $b \leftrightarrow 1/b$ the 6j-level rotation. The corpus's context-sorting of $\Phi_q$ (Faddeev, non-compact) versus $\mathrm{Li}_2^q$ (Rogers, compact) is this same split.
3. **Quantum modularity**: the Andersen–Kashaev state integral of a knot factorizes as a $q$-series times a $\tilde{q}$-series with $\mathrm{Vol} + i\,\mathrm{CS}$ as leading asymptotics \cite{garoufalidis-zagier-2024} — one complex object, two channel factorizations, exactly the Neumann–Zagier shape \cite{neumann-zagier1985} that $\mathfrak{V}$ transports to binding and decay.

## The operator statement: Leonard pairs

Zhedanov's $AW(3)$ algebra \cite{zhedanov1991} packages the rotation as an operator identity: two operators, each tridiagonal in the other's eigenbasis, with the Askey–Wilson polynomials as the overlap ("rotation matrix") between the two eigenbases. The generically provable half — any eigencolumn of the channel tridiagonal operator has orthogonal-polynomial entries — is proved sorry-free as `eigencolumn_eq_overlap` (Lean sibling of the conjecture). The self-duality that would force the channel overlap into the Askey–Wilson family by Terwilliger's classification \cite{terwilliger2001} is carried as the conjecture class `ChannelLeonardDuality`.

## Vertex-algebra shadow

Under the bar involution the character side splits as a $\mathbb{Z}_2$-orbifold $V = V^+ \oplus V^-$, and the characters in play are false theta functions — $(1,p)$ singlet log-VOA characters \cite{creutzig-milas2014} — whose quantum modularity is again the disk-interior versus root-of-unity rotation, the same Lawrence–Zagier $\Psi$ already used at the $W_\lambda$ keystone. This is a lead for tying the lepton-tower $\Phi_q$ work to the binding/$\mathfrak{Q}_\beta$ program under one scheme, not a result.
