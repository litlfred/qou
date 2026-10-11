---
doc_id: arxiv-1901.01312v1
doc_title: "Braided fermions from Hurwitz algebras"
section_id: sec-003-31-primitive-idempotents-and-orthogonal-subspace
section_title: "Primitive idempotents and orthogonal subspaces"
section_number: 3.1
pages: 3-4
source_pdf: 1901.01312v1.pdf
source_sha256: a480da38283622d6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.903
---
The extensive works of Dixon [@dixon2013division; @dixon1990derivation; @dixon2010division] focus on deriving the SM from tensor products of Hurwitz algebra. The approach is to reduce spinor spaces of Hurwitz algebras (as well as their associated action algebras) into sets of orthogonal subspaces. This is achieved by finding projection operators within the algebras, corresponding to primitive idempotents obtained from a resolution of the identity. In the case of $\mathbb{C}\otimes\mathbb{O}$ the projectors can be used to split the algebra into four orthogonal subspaces, each a $SU(3)$ multiplet. This is because the automorphism group that keeps $e_7$ fixed is $SU(3)$. Each spinor in $\mathbb{C}\otimes\mathbb{O}$ is resolved into $\mathbf{1}\oplus\mathbf{3}\oplus\mathbf{\overline{3}}\oplus\mathbf{\overline{1}}$ with respect to this chosen $SU(3)$ automorphism group[@dixon2013division]. The same algebra admits a $U(1)$ generator that produces the correct hypercharges.

## Minimal left ideals of $C\ell(6)$

The goal of identifying SM structure from tensor products of Hurwitz algebras is not unique to Dixon. More recently, Furey and Stoica have likewise looked at $\mathbb{C}\otimes\mathbb{O}$, and its associated left action algebra $C\ell(6)$, to identify unbroken SM symmetries [@furey2016standard; @stoica2018leptons]. However, in their works the implementation of $C\ell(6)$ is significantly different. In particular, the spinors representing fermions in this scheme correspond to basis states of the minimal left ideals of $C\ell(6)$.

Under a change of basis (induced by a projector), the generating space of the Clifford algebra $C\ell(2n)$ can be partitioned into two maximal totally isotropic subspaces (MTIS) from which two minimal ideals can be constructed. One can label the vectors of a split basis for $\mathbb{C}\otimes\mathbb{O}$ as $$\begin{aligned}
\alpha_1 &=&\frac{1}{2}(-e_5+ie_4),\qquad \alpha_2=\frac{1}{2}(-e_3+ie_1),\qquad \alpha_3=\frac{1}{2}(-e_6+ie_2),\\
\alpha_1^{\dagger}&=&\frac{1}{2}(e_5+ie_4),\qquad \alpha_2^{\dagger}=\frac{1}{2}(e_3+ie_1),\qquad \alpha_3^{\dagger}=\frac{1}{2}(e_6+ie_2),
\end{aligned}$$ which also serves as a basis for $C\ell(6)$. It is readily checked that $\alpha_i$ and $\alpha_i^{\dagger}$ are nilpotents, and furthermore behave as a set of fermionic creation and annihilation operators, satisfying $$\begin{aligned}
\lbrace \alpha_i,\alpha_j \rbrace=0,\; \lbrace \alpha_i^{\dagger},\alpha_j^{\dagger} \rbrace=0,\; \lbrace \alpha_i^{\dagger},\alpha_j \rbrace=\delta_{ij}.
\end{aligned}$$ The $\lbrace\alpha^{\dagger}_i\rbrace$ span one three complex-dimensional MTIS. It is readily checked that $\alpha_i\omega=0$. A minimal left ideal is then given by allowing $C\ell(6)$ to act on the primitive idempotent $\omega\omega^{\dagger}=\alpha_1\alpha_2\alpha_3\alpha_3^{\dagger}\alpha_2^{\dagger}\alpha_1^{\dagger}$. The first ideal is then $$\begin{aligned}
\label{ideal}
\nonumber S^u\equiv &{}&\\
\nonumber &{}&\;\;\nu \omega\omega^{\dagger}+\\
\nonumber \bar{d}^r\alpha_1^{\dagger}\omega\omega^{\dagger} &+& \bar{d}^g\alpha_2^{\dagger}\omega\omega^{\dagger} + \bar{d}^b\alpha_3^{\dagger}\omega\omega^{\dagger}\\
\nonumber u^r\alpha_3^{\dagger}\alpha_2^{\dagger}\omega\omega^{\dagger} &+& u^g\alpha_1^{\dagger}\alpha_3^{\dagger}\omega\omega^{\dagger} + u^b\alpha_2^{\dagger}\alpha_1^{\dagger}\omega\omega^{\dagger}\\
&+& e^{+}\alpha_3^{\dagger}\alpha_2^{\dagger}\alpha_1^{\dagger}\omega\omega^{\dagger},
\end{aligned}$$ where $\nu$, $\bar{d}^r$ etc. are suggestively labeled complex coefficients. The complex conjugate system analogously gives a second linearly independent minimal left ideal.
