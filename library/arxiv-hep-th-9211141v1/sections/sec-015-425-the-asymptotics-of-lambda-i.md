---
doc_id: arxiv-hep-th-9211141v1
doc_title: "arXiv:hep-th/9211141v1 1 Dec 1992"
section_id: sec-015-425-the-asymptotics-of-lambda-i
section_title: "The asymptotics of $\lambda_i$"
section_number: 4.2.5
pages: 25-34
source_pdf: 9211141v1.pdf
source_sha256: bd9fbd329884c26e
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.98
latex_coverage_ratio: 0.985
doc_brief: "arXiv:hep-th/9211141v1 1 Dec 1992 — 17 sections: Front matter; INTRODUCTION AND SUMMARY OF RESULT; The System of Partial Differential"
---
If we look at the asymptotics of $f_i(x)$ (the eigenfunction associated with the eigenvalue $\mu_i$ of $L$, normalized so that $f_i(0)=1$) given by ([\[appx1\]](#appx1){reference-type="ref" reference="appx1"}), ([\[appx3\]](#appx3){reference-type="ref" reference="appx3"}), ([\[appx5\]](#appx5){reference-type="ref" reference="appx5"}), and ([\[appx8\]](#appx8){reference-type="ref" reference="appx8"}) we see that the main contribution to $\int_0^\infty f_i(x)^2\,dx$ comes from any region $$t^{-1/4}\vert t-x \vert < \eta(t)$$ as long as $\eta(t)\rightarrow\infty$. For some such region we have, by ([\[appx7\]](#appx7){reference-type="ref" reference="appx7"}) and ([\[appx9\]](#appx9){reference-type="ref" reference="appx9"}), $$f_i(x) \sim {2^{-{5\over 2}i-2}\over\sqrt\pi} t^{-{3\over 4}i - {3\over 4}}
D_i\left(\sqrt{2} t^{-1/4}(t-x)\right) \, .$$ Using this, and the fact $\int_{-\infty}^\infty D_i(x)\, dx =\sqrt{2\pi} i!$, we deduce $$\int_0^\infty f_i(x)^2\, dx \sim {i!\over\sqrt\pi} 2^{-5i-4}
t^{-{3\over 2}i-{5\over 4}} \exp\left({8\over 3}t^{3/2}\right)\, .
\label{appx10}$$ This was the goal of all that went before.

Since $L$ has simple eigenvalues and commutes with our integral operator $K$ (translated to $(0,\infty)$) the set $\lbrace f_i\rbrace$ is the set of eigenfunctions of $K$ corresponding to its eigenvalues $\lbrace \lambda_i\rbrace$. However $f_i$ corresponds to $\mu_i$ and there is no assurance that the corresponding eigenvalue of $K$ is its $i^{\rm th}$ largest, which we have denoted by $\lambda_i$. We shall eventually show that this is actually the case. The first lemma of this section shows that the eigenvalues of $K$ are simple, and this is crucial for the argument we shall later use. (The proof of the corresponding result for the sine kernel is in [@slepian_pollak].)

::: lemma
If $f_1$ and $f_2$ are eigenfunctions of $L$ corresponding to distinct eigenvalues, then they are eigenfunctions of $K$ corresponding to distinct eigenvalues.
:::

Proof. The eigenvalues of $K$ are the squares of the eigenvalues of the operator on $(0,\infty)$ with kernel $A(x+y-2t)$. So we have to show that if for some $\nu$ we have either $$\int_0^\infty A(x+y-2t) f_i(y)\, dy = \nu f_i(x) \ \ \ (i=1,2)
\label{eig1}$$ or $$\int_0^\infty A(x+y-2t) f_1(y)=\nu f_1(x)\, , \ \ \int_0^\infty
A(x+y-2t) f_2(y)\, dy = -\nu f_2(x)
\label{eig2}$$ then $f_1=f_2$. (Recall that all eigenfunctions are normalized to satisfy $f(0)=1$.)

Assuming first that ([\[eig1\]](#eig1){reference-type="ref" reference="eig1"}) holds, apply $d^2/dx^2$ to both sides of the identity with $i=1$ and integrate the resulting integral by parts twice. What results is $$\nu f_1^{\prime\prime}(x)=-A^\prime(x-2t)+A(x-2t)f_1^\prime(0)+
\int_0^\infty A(x+y-2t) f_1^{\prime\prime}(y)\, dy\, .$$ If we multiply both sides by $f_2(x)$ and integrate we obtain, using ([\[eig1\]](#eig1){reference-type="ref" reference="eig1"}) with $i=2$ (and its differentiated version), $$\nu \int_0^\infty f_1^{\prime\prime}(x) f_2(x)\, dx =
-\nu f_2^\prime(0)+\nu f_1^\prime(0) +\nu\int_0^\infty f_2(y)
f_1^{\prime\prime}(y)\, dy\, .$$ Thus, since $\nu\neq 0$ (this follows easily from the fact that the Fourier transform of $A(x)$ is nonzero), we have $f_1^\prime(0)=f_2^\prime(0)$. But it is clear from ([\[eig_eqn1\]](#eig_eqn1){reference-type="ref" reference="eig_eqn1"}) that for any eigenfunction $f$ we have $f^\prime(0)=t^2-\mu$. Thus $f_1$ and $f_2$ correspond to the same eigenvalue of $L$ and so are equal.

The case when ([\[eig2\]](#eig2){reference-type="ref" reference="eig2"}) holds is even easier. Differentiating both sides of the first relation once and integrating by parts gives $$\nu f_1^\prime(x) = - A(x-2t)-\int_0^\infty A(x+y-2t) f_1^\prime(y)
\, dy\, .$$ Multiplying both sides of this by $f_2(x)$ and integrating, using the second relation of ([\[eig2\]](#eig2){reference-type="ref" reference="eig2"}), we obtain $$\nu \int_0^\infty f_1^\prime(x) f_2(x)\, dx =
-\nu+\nu \int_0^\infty f_2(y) f_1^\prime(y)\, dy\, ,$$ contradicting $\nu\neq 0$. 0◻

Since, as we now know, the eigenvalues of $K$ are simple, there is a permutation $\sigma$ of ${\rm{\bf N}}=\lbrace 0,1,2,\cdots\rbrace$ such that $f_i$ is the eigenfunction of $K$ corresponding to its $\sigma(i)^{th}$ largest eigenvalue $\lambda_{\sigma(i)}$; this permutation is independent of $t$ or else, by the continuity of the eigenvalues in $t$, there would be a multiple eigenvalue for some $t$.

Up to now our kernel $K$ corresponded to an arbitrary factor $\lambda$. Of course formula ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) refers to the case $\lambda=1$.

::: lemma
[]{#lemma:two label="lemma:two"} For each $i$ we have $\lambda_i\rightarrow 1$ as $s\rightarrow -\infty$.
:::

Proof. In this case $\lambda=1$ formula ([\[K_identity\]](#K_identity){reference-type="ref" reference="K_identity"}) reads $$K(x,y)=\int_0^\infty {\rm Ai}(x+z) {\rm Ai}(z+y) \, dz \, .
\label{K_identity2}$$ For the purposes of this proof we denote by $A$ (resp. $K$) the operator on $(-\infty,\infty)$ with kernel ${\rm Ai}(x+y)$ (resp. $K(x,y)$) and by $P_s$ the projection from $L_2(-\infty,\infty)$ to $L_2(s,\infty)$. So the $\lambda_i$ are the eigenvalues of $P_s K P_s$. Now it is known [@hastings_mcleod] that $A^2=I$, and ([\[K_identity2\]](#K_identity2){reference-type="ref" reference="K_identity2"}) says that $K=A P_0 A$. Thus $K^2=A P_0 A^2 P_0 A = A P_0 A = K$. In other words, $K$ is a projection operator. (This is not surprising since its kernel is a scaling limit of the kernels $K_N(x,y)$ of projection operators.)  Clearly it has infinite-dimensional range. It now follows easily from the minimax characterization of the eigenvalues that, for each $i$, the $i^{\rm th}$ largest eigenvalue of $P_s K P_s$ tends to $1$ as $s\rightarrow -\infty$. 0◻

We now state a lemma which is the basis of a trick used by Fuchs [@fuchs64] in his derivation of the asymptotics of the eigenvalues of the sine kernel.

::: lemma
Let $J(x,y)$ be a symmetric kernel, on a fixed interval, depending smoothly on a parameter $t$. Let $g$ be an eigenfunction normalized so that $\int g(x)^2\, dx = 1$ and let $\lambda$ be the corresponding eigenvalue. Then, with the subscript $t$ denoting $\partial/\partial t$, we have $$\lambda_t = \int\int J_t(x,y) g(y) g(x) \,dydx\, .$$
:::

Proof. From $$\int J(x,y) g(y)\, dy = \lambda g(x)
\label{J_eqn}$$ we get $$\int J_t(x,y) g(y)\, dy +\int J(x,y) g_t(y)\, dy =
\lambda_t g(x)+  \lambda g_t(x) \, .$$ Multiplying both sides by $g(x)$ and integrating over $x$, we obtain (using the normalization of $g$ and ([\[J_eqn\]](#J_eqn){reference-type="ref" reference="J_eqn"})) $$\begin{aligned}
\int\int J_t(x,y) g(y) g(x)\, dydx + \int\int J(x,y) g_t(y) g(x) \, dx dy
&=&\lambda_t + \lambda \int g_t(x) g(x)\, dx \\
&=&\lambda_t + \int\int J(x,y) g(y) g_t(x)\, dy dx\, .
\end{aligned}$$ By symmetry of $J$ the two double integrals involving it cancel, and we obtain the statement of the lemma. 0◻

We apply the lemma to the opertor with kernel $A(x+y-2t)$ on $(0,\infty)$ whose square is our Airy operator (translated to act on $(0,\infty)$). Thus we may write its eigenvalues as $\sqrt{\lambda_{\sigma(i)}}$, where the square roots might have either sign. The lemma gives $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} = -2 \int_0^\infty\int_0^\infty
A^\prime(x+y-2t) g_i(y) g_i(x)\, dy dx
\label{lambda_eqn}$$ where $$g_i(x) = f_i(x)\biggl/   \left\lbrace \int_0^\infty f_i(y)^2\, dy
\right\rbrace^{1/2}\, .$$ But from $$\int_0^\infty A(x+y-2t) g_i(y)\, dy = \sqrt{\lambda_{\sigma(i)}} g_i(x)$$ we obtain upon differentiation that $$\int_0^\infty A^\prime(x+y-2t) g_i(y)\, dy = \sqrt{\lambda_{\sigma(i)}} g_i^\prime(x)$$ so ([\[lambda_eqn\]](#lambda_eqn){reference-type="ref" reference="lambda_eqn"}) may be rewritten $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} = -2 \sqrt{\lambda_{\sigma(i)}}
\int_0^\infty g_i^\prime(x) g_i(x)\, dx\, .$$ The integral is of course $-{1\over 2} g_i(0)^2$. Recalling that $f_i(0)=1$ we see that we have established the relation $${\partial\over\partial t}\sqrt{\lambda_{\sigma(i)}} =\sqrt{\lambda_{\sigma(i)}}\biggl/ \left\lbrace
\int_0^\infty f_i(x)^2\, dx \right\rbrace \, ,$$ or $${\partial\over\partial t}\log\lambda_{\sigma(i)}= 2\biggl/ \left\lbrace
\int_0^\infty f_i(x)^2\, dx \right\rbrace \,$$

We now use ([\[appx10\]](#appx10){reference-type="ref" reference="appx10"}) and integrate the resulting relation with respect to $t$ from $t$ to $\infty$. Recalling Lemma [\[lemma:two\]](#lemma:two){reference-type="ref" reference="lemma:two"}, we deduce $$-\log\lambda_{\sigma(i)}\sim {\sqrt\pi\over i!} 2^{5i+3} t^{{3\over 2}i+{3\over 4}}
\exp\left(-{8\over 3} t^{3/2}\right)\, ,$$ precisely the right side of ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}).

All that remains now is to show that $\sigma(i)=i$ for all $i$. But it is clear from this asymptotic relation that $i<j$ implies $\lambda_{\sigma(i)}>\lambda_{\sigma(j)}$ for large $t$ (and so for all $t$), so that $\sigma(i)<\sigma(j)$. Thus $\sigma$ is order preserving, and since $\sigma:{\rm{\bf  N}}\rightarrow {\rm{\bf  N}}$ is onto we must have $\sigma(i)=i$ for all $i$.

This concludes the derivation of ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}). The deduction of ([\[r_asy\]](#r_asy){reference-type="ref" reference="r_asy"}) from ([\[eigs_asy\]](#eigs_asy){reference-type="ref" reference="eigs_asy"}) is completely analogous to the corresponding deduction for the sine kernel in ref. [@tw1], Sec. VIIB.

We wish to thank E. Brézin, P. J. Forrester, F. A. Grünbaum and J. Harnad for helpful comments. This work was supported in part by the National Science Foundation, DMS--9001794 and DMS--9216203, and this support is gratefully acknowledged.

::: references
M. J. Ablowitz and H. Segur, *Exact linearization of a Painlevé transcendent*, Phys. Rev. Letts. **38** (1977) 1103--1106.

E. L. Basor, C. A. Tracy, and H. Widom, *Asymptotics of level spacing distributions for random matrices*, Phys. Rev. Letts. **69** (1992) 5--8.

M. J. Bowick and E. Brézin, *Universal scaling of the tail of the density of eigenvalues in random matrix models*, Phys. Letts. **B268** (1991) 21--28.

A. Erdélyi (ed.), *Higher Transcendental Functions*, Vol. II (McGraw-Hill, New York, 1953).

P. A. Clarkson and J. B. McLeod, *A connection formula for the second Painlevé transcendent*, Arch. Rat. Mech. Anal. **103** (1988) 97--138.

P. A. Clarkson and J. B. McLeod, *Integral equations and connection formulae for the Painlevé equations*, in *Painlevé Transcendents: Their Asymptotics and Physical Applications*, eds. D. Levi and P. Winternitz (Plenum Press, New York, 1992), pgs. 1--31.

F. J. Dyson, *Statistical theory of energy levels of complex systems, I, II, and III*, J. Math. Phys. **3** (1962) 140--156; 157--165; 166--175.

F. J. Dyson, *Fredholm determinants and inverse scattering problems*, Commun. Math. Phys. **47** (1976) 171--183.

F. J. Dyson, *The Coulomb fluid and the fifth Painlevé transcendent*, IASSNSS-HEP-92/43 preprint, to appear in the proceedings of a conference in honor of C. N. Yang, ed. S.-T. Yau.

P. J. Forrester, *The spectrum edge of random matrix ensembles*, preprint.

W. H. J. Fuchs, *On the eigenvalues of an integral equation arising in the theory of band-limited signals*, J. Math. Anal. and Applic. **9** (1964) 317--330.

J. Harnad, C. A. Tracy, and H. Widom, *Hamiltonian structure of equations appearing in random matrices*, in preparation.

S. P. Hastings and J. B. McLeod, *A boundary value problem associated with the second Painlevé transcendent and the Korteweg-de Vries equation*, Arch. Rat. Mech. Anal. **73** (1980) 31--51.

E. L. Ince, *Ordinary Differential Equations*, (Dover, New York, 1956).

A. R. Its, A. G. Izergin, V. E. Korepin, and N. A. Slavnov, *Differential equations for quantum correlation functions*, Int. J. Mod. Physics B **4** (1990) 1003--1037.

K. Iwasaki, H. Kimura, S. Shimomura, and M. Yoshida, *From Gauss to Painlevé: A Modern Theory of Special Functions* (Vieweg, Braunschweig, 1991).

M. Jimbo, T. Miwa, Y. Môri, and M. Sato, *Density matrix of an impenetrable Bose gas and the fifth Painlevé transcendent*, Physica **1D** (1980) 80--158.

B. M. McCoy, C. A. Tracy, and T. T. Wu, *Connection between the KdV equation and the two-dimensional Ising model*, Phys. Letts. **61A** (1977) 283--284.

J. B. McLeod, private communication.

M. L. Mehta, *Random Matrices*, 2nd edition (Academic, San Diego, 1991).

M. L. Mehta, *A non-linear differential equation and a Fredholm determinant*, J. de Phys. I France, **2** (1992) 1721--1729.

M. L. Mehta and G. Mahoux, *Level spacing functions and non-linear differential equations*, preprint.

G. Moore, *Matrix models of 2D gravity and isomonodromic deformation*, Prog. Theor. Physics Suppl. No. **102** (1990) 255--285.

J. Moser, *Geometry of quadrics and spectral theory*, in *Chern Symposium 1979* (Springer, Berlin, 1980), 147--188.

P. Painlevé, *Sur les équations différentielles du second ordre et d'ordre supérieur dont l'intégrale générale est uniforme*, Acta Math. **25** (1902) 1--85.

C. E. Porter, *Statistical Theory of Spectra: Fluctuations* (Academic, New York, 1965).

D. Slepian and H. O. Pollak, *Prolate spheroidal wave functions, Fourier analysis and uncertainty-I*, Bell Systems Tech. J. **40** (1961) 43--64.

C. A. Tracy and H. Widom, *Introduction to random matrices*, to appear in the proceedings of the $8^{th}$ Scheveningen Conference, Springer Lecture Notes in Physics.

C. A. Tracy and H. Widom, *Level spacing distributions and the Airy kernel*, submitted to Phys. Letts. B.

H. Widom, *The strong Szegö limit theorem for circular arcs*, Indiana Univ. Math. J. **21** (1971) 277--283.

H. Widom, *The asymptotics of a continuous analogue of orthogonal polynomials*, to appear in J. Approx. Th.
:::
