---
doc_id: arxiv-0903.2472v1
doc_title: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group"
section_id: sec-005-24-brane-quantization
section_title: "Brane quantization"
section_number: 2.4
pages: 25-27
source_pdf: 0903.2472v1.pdf
source_sha256: 637cfd1d4d833c02
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.953
doc_brief: "Exact Results for Perturbative Chern-Simons Theory with Complex Gauge Group — We develop several methods that allow us to compute all-loop partition functions in perturbative Chern-Simons theory with"
---
Now, let us briefly describe how the problem of quantizing the moduli space of flat connections, ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$, would look in the new approach [@gukov-2008] based on the topological A-model and D-branes. Although it can be useful for a better understanding of Chern-Simons theory with complex gauge group, this discussion is not crucial for the rest of the paper and the reader not interested in this approach may skip directly to Section [\[sec:statesum\]](#sec:statesum){reference-type="ref" reference="sec:statesum"}.

In the approach of [@gukov-2008], the problem of quantizing a symplectic manifold $N$ with symplectic structure $\omega$ is solved by complexifying $(N,\omega)$ into $(Y,\Omega)$ and studying the A-model of $Y$ with symplectic structure $\omega_Y = {\rm Im}\,\Omega$. Here, $Y$ is a complexification of $N$, *i.e.* a complex manifold with complex structure ${\cal I}$ and an antiholomorphic involution $$\tau: Y \to Y \,,$$ such that $N$ is contained in the fixed point set of $\tau$ and $\tau^* {\cal I}= - {\cal I}$. The 2-form $\Omega$ on $Y$ is holomorphic in complex structure ${\cal I}$ and obeys $$\tau^* \Omega = \overline{\Omega}
\label{omtau}$$ and $$\Omega \vert_N = \omega\,.
\label{omrestr}$$ In addition, one needs to pick a unitary line bundle $\frak L \to Y$ (extending the "prequantum line bundle" $\frak L \to N$) with a connection of curvature ${\rm Re}\,\Omega$. This choice needs to be consistent with the action of the involution $\tau$, meaning that $\tau: Y \to Y$ lifts to an action on $\frak L$, such that $\tau|_N = {\rm id}$. To summarize, in brane quantization the starting point involves the choice of $Y$, $\Omega$, $\frak L$, and $\tau$.

In our problem, the space $N = {{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$ that we wish to quantize is already a complex manifold. Indeed, as we noted earlier, it comes equipped with the complex structure $J$ (that does not depend on the complex structure on $\Sigma$). Therefore, its complexification[^1] is $Y = N \times \overline{N}$ with the complex structure on $\overline{N}$ being prescribed by $-J$ and the complex structure on $Y$ being ${\cal I}=(J, -J)$. The tangent bundle $TY=TN\oplus T\overline{N}$ is identified with the complexified tangent bundle of $N$, which has the usual decomposition ${\mathbb{C}}TN=T^{1,0}N\oplus T^{0,1} N$.

Then, the "real slice" $N$ is embedded in $Y$ as the diagonal $$N \ni x \mapsto (x, x) \in N \times \overline{N}\,.
\label{ndiag}$$ In particular, $N$ is the fixed point set of the antiholomorphic involution $\tau : Y \to Y$ which acts on $(x,y) \in Y$ as $\tau: (x,y) \mapsto (y, x)$.

Our next goal is to describe the holomorphic 2-form $\Omega$ that obeys [\[omtau\]](#omtau){reference-type="eqref" reference="omtau"} and [\[omrestr\]](#omrestr){reference-type="eqref" reference="omrestr"} with[^2] $$\omega = \frac{t}{2\pi i} (\omega_K + i \omega_I) - \frac{\bar t}{2\pi i} (\omega_K - i \omega_I)$$ Note, that $(\omega_K + i \omega_I)$ is holomorphic on $N = {{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$ and $(\omega_K - i \omega_I)$ is holomorphic on $\overline{N}$. Moreover, if we take $\bar t$ to be a complex conjugate of $t$, the antiholomorphic involution $\tau$ maps $t (\omega_K + i \omega_I)$ to $\bar t (\omega_K - i \omega_I)$, so that $\tau^* \omega = \omega$. Therefore, we can simply take $$\Omega = \frac{t}{2\pi i} (\omega_K^{(1)} + i \omega_I^{(1)}) - \frac{\bar t}{2\pi i} (\omega_K^{(2)} - i \omega_I^{(2)})$$ where the superscript $i=1,2$ refers to the first (resp. second) factor in $Y = N \times \overline{N}$. It is easy to verify that the 2-form $\Omega$ defined in this way indeed obeys $({\rm Im}\,\Omega)^{-1} {\rm Re}\,\Omega = {\cal I}$. Moreover, one can also check that if $\bar t$ is a complex conjugate of $t$ then the restriction of $\omega_Y = {\rm Im}\,\Omega$ to the diagonal [\[ndiag\]](#ndiag){reference-type="eqref" reference="ndiag"} vanishes, so that the "real slice" $N \subset Y$, as expected, is a Lagrangian submanifold in $(Y,\omega_Y)$.

Now, the quantization problem can be realized in the A-model of $Y$ with symplectic structure $\omega_Y = {\rm Im}\,\Omega$. In particular, the Hilbert space ${\cal H}_{\Sigma}$ is obtained as the space of $({\cal B}_{cc},{\cal B}')$ strings, $${\cal H}_{\Sigma} = {\rm ~space~of~} ({\cal B}_{cc},{\cal B}') {\rm ~strings}$$ where ${\cal B}_{cc}$ and ${\cal B}'$ are A-branes on $Y$ (with respect to the symplectic structure $\omega_Y$). The brane ${\cal B}'$ is the ordinary Lagrangian brane supported on the "real slice" $N \subset Y$. The other A-brane, ${\cal B}_{cc}$, is the so-called canonical coisotropic brane supported on all of $Y$. It carries a Chan-Paton line bundle of curvature $F = {\rm Re}\,\Omega$. Note that for $[F]$ to be an integral cohomology class we need ${\rm Re}\,(t) \in {\mathbb{Z}}$. Since in the present case the involution $\tau$ fixes the "real slice" pointwise, it defines a hermitian inner product on ${\cal H}_{\Sigma}$ which is positive definite.

[^1]: Notice, since in our problem we start with a hyper-Kähler manifold ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$, its complexification $Y$ admits many complex structures. In fact, $Y$ has holonomy group $Sp(n) \times Sp(n)$, where $n$ is the quaternionic dimension of ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$.

[^2]: Notice, while in the rest of the paper we consider only the "holomorphic" sector of the theory (which is sufficient in the perturbative approach), here we write the complete symplectic form on ${{\cal M}}_{{\rm flat}}(G_{{\mathbb{C}}},\Sigma)$ that follows from the classical Chern-Simons action [\[csaction\]](#csaction){reference-type="eqref" reference="csaction"}, including the contributions of both fields ${\cal A}$ and $\bar {\cal A}$.
