> **Superseded.** The scalar substrate density $\rho_q = 1/\hbar_q^2$ used
> below is the structurally-wrong leading-order ansatz; the operator-valued
> form supersedes it ([`mass-endomorphism-tower`](mass-endomorphism-tower.md));
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [graded expansion of $\rho_K$](rho-k-graded-expansion.md).

The **Kashaev volume conjecture (KVC)** asserts that, for every
hyperbolic knot $K \subseteq S^3$, the Kashaev limit of the colored
Jones polynomial computes the hyperbolic volume of the complement,

$$
  \mathrm{Vol}_{\mathrm{hyp}}(S^3 \setminus K)
  \;=\;
  2\pi \cdot \lim_{N \to \infty}
  \frac{\log \lvert J_N(K)\rvert}{N},
  \qquad
  J_N(K)\big\vert_{q = \exp(2\pi i / N)},
$$

with the convention that the right-hand side vanishes when $K$ is not
hyperbolic. KVC was conjectured by Kashaev [`kashaev1997`] and reformulated
in terms of the colored Jones polynomial by Murakami–Murakami
[`murakami-murakami2001`]. It is **open in general** (proved only for
specific families: the figure-eight knot, certain torus and pretzel
knots, etc.).

Inside QOU, KVC is the consistency statement that the archimedean
realisation functor $\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$
([archimedean realization functor](#def:archimedean-realization-functor))
applied to the algebraic quantum volume
([algebraic quantum volume](#def:algebraic-quantum-volume))
recovers the hyperbolic volume; this is the content of the per-block
[Kashaev as archimedean realization](#rem:kashaev-as-archimedean-realization)
remark.

### KVC as an explicit hypothesis

KVC is used throughout as an explicit hypothesis. Every downstream
result that depends on it is conditional on KVC — and only on KVC
restricted to the knots involved: a bridge statement of the form
$\Phi_q(V_S) = \rho_q \cdot \mathrm{Vol}(K_S)$ depends only on KVC
for $K_S$. Such a result becomes unconditional for a knot family
(figure-eight, torus, etc.) exactly where KVC is actually proved.

The conjecture itself remains open at the level of $\pi_0$ —
no claim of proof is made by stating it as a hypothesis.

### Motivic perspective

KVC is, in motivic language, a **regulator statement**: the
hyperbolic volume of $S^3 \setminus K$ is the image of a class in
the Bloch group $\mathcal{B}(\mathbb{C})$ under the Borel/Beilinson
regulator $r_\infty$, and the colored Jones polynomial at
$q = \exp(2\pi i / N)$ is the $q$-deformed avatar of that class
[`zagier1986`, `neumann-zagier1985`]. The QOU recasting frames
$\tau_{\mathrm{arch}} = \pi_\infty \circ \tau$ as the archimedean
realisation functor on the algebraic data $\Phi_q(\lvert V_S\rvert)$
— a class in the quantum Bloch group
([quantum Bloch group](#def:quantum-bloch-group)) — landing in
$\mathbb{R}$ as the hyperbolic volume of the corresponding
Φ$_q$-piece. KVC, in this presentation, is the assertion that the
$q$-deformed regulator agrees with the classical one in the Kashaev
limit.

### Two published neighbours of the statement

Gukov's generalised volume conjecture is a one-parameter family that contains this statement. It predicts the limit of $\log J_N(K, e^{2\pi i/k})/k$ as $N, k \to \infty$ with $N/k$ fixed, as $\tfrac{1}{2\pi}\big(\mathrm{Vol}(l,m) + i\,2\pi^2\,\mathrm{CS}(l,m)\big)$ evaluated on the zero locus of the A-polynomial, and it reduces to the volume conjecture at $m = 1$ \cite[\S5.2, eqs.~(5.12)--(5.13)]{arxiv-hep-th-0306165v1}. For $4_1$ the source checks the real part of the family \cite[\S5.3]{arxiv-hep-th-0306165v1}. The figure-eight case of the conjecture above is therefore the $m = 1$ member of that family.

Baseilhac and Ben Aribi prove a volume-conjecture statement for the quantum hyperbolic invariants $H_N(M,\rho,h_\rho,k_c)$ of the figure-eight complement $M$, for odd $N \ge 3$. For every character $\rho$ on the geometric component and every charge weight, $\lim_{N\to\infty} \tfrac{2\pi}{N}\,\mathrm{Log}\,\lvert H_N\rvert$ equals $\mathrm{Vol}(M)$ when $h_\rho(\lambda_K) \in 2\pi i(2\mathbb{Z}+1)$ and equals $0$ when $h_\rho(\lambda_K) \in 4\pi i\,\mathbb{Z}$, where $\lambda_K$ is the canonical longitude \cite[\S1.1, Thm.~1.1]{baseilhac2026}. The limit does not depend on $\rho$. These invariants of the cusped manifold are not the Kashaev invariant of the conjecture: the Kashaev invariant $\langle L\rangle_N$ coincides with the quantum hyperbolic invariant of the pair $(S^3, L)$, and the source relates the invariant of $S^3 \setminus 4_1$ to $\langle 4_1\rangle_N$ only through a discrete Laplace-transform type formula \cite[\S1.1 and App.~A]{baseilhac2026}. The theorem is therefore a statement about a neighbouring sequence, and it does not supply an instance of the conjecture as stated; whether the parity case (a) holds at a given choice of longitude logarithm is a separate check.
