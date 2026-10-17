---
doc_id: arxiv-1202.4698v3
doc_title: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories"
section_id: sec-023-63-the-b-6j-symbols-as-a-partition-function
section_title: "The b-6j symbols as a partition function"
section_number: 6.3
pages: 20-21
source_pdf: 1202.4698.pdf
source_sha256: 54171c652161ca5b
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "6j symbols for the modular double, quantum hyperbolic geometry, and supersymmetric gauge theories — We revisit the deﬁnition of the 6j symbols from the modular double of Uq(sl(2, R)), referred to as"
---
Although expression (\ref{6j2}) for b-$6j$ symbol 
resembles the partition functions of 
$3d$ SYM theory with $U(1)$ gauge group, it cannot easily be interpreted 
as partition function for some three-dimensional 
gauge theory since the parameters 
entering its expression are subject to the condition that 
their sum equals $2Q$, 
while the parameters entering partitions functions are not restricted. 

In the course of the derivation of the new formula 
\rf{6j2} for the b-$6j$ symbols, as described in 
Appendix \ref{Cor}, we have found a few other 
integral representations
for these objects, including
\begin{align} \label{PF-6quarks}
 \mathcal{A}_1 \,I \bigg( 
\begin{array}{ccc}
\fr{Q-\alpha_t-\alpha_1-\alpha_4}{2} + \alpha_s & \fr{3Q-\alpha_t-\alpha_1-\alpha_4}{2}-\alpha_s & \fr{Q+\alpha_1-\alpha_4+\alpha_t}{2}-\alpha_3 \\  \fr{-Q-\alpha_1+\alpha_4+\alpha_t}{2}+\alpha_2 & \fr{Q-\alpha_1+\alpha_4+\alpha_t}{2} - \alpha_2& \fr{-Q+\alpha_1-\alpha_4+\alpha_t}{2}+\alpha_3
\end{array}\bigg)\,,
\end{align}
where we define the integral $I(\underline{\mu})$ as
\begin{equation}
I(\underline{\mu}) = \frac 12 \int_{- \textup{i} \infty}^{\textup{i} \infty} \frac{\prod_{i=1}^6 S_b(\mu_i\pm u)}{S_b(\pm 2u)} du\,,\qquad
[ \underline{\mu} ] = \bigg[  \begin{array}{ccc}
\mu_1 & \mu_2 & \mu_3 \\ \mu_4 & \mu_5 & \mu_6 \end{array}
\bigg]\,,
\end{equation}
and the prefactor in \rf{PF-6quarks} is explicitly given as
\beq \nonumber
\mathcal{A}_1 = \frac{S_b(\alpha_2+\alpha_3-\alpha_t) S_b(\alpha_1-\alpha_2+\alpha_s) S_b(-Q+\alpha_1+\alpha_4+\alpha_t)}{S_b(\alpha_2+\alpha_t-\alpha_3) S_b(\alpha_3+\alpha_t-\alpha_2) S_b(\alpha_3-\alpha_4+\alpha_s)}.
\eeq
We would like to point out that this expression, as opposed to \rf{6j2},
admits an interpretation as a partition 
function of the form (\ref{PF_def}) for a certain three-dimensional 
SYM theory. 
Namely, the expression \rf{PF-6quarks} without coefficient 
$\mathcal{A}_1$ can be interpreted as the partition function 
of three-dimensional $\mathcal{N}=2$ SYM theory defined on a 
squashed three-sphere with $SU(2)$ gauge group and $6$ quarks 
in the fundamental representation of the gauge group. The flavor symmetry 
group is $SU(6) \times U(1)_A \times U(1)_R$. The total axial mass is $m_A=\frac 16 \sum_{i=1}^6 \mu_6$ while the masses of 6 chiral multiplets then is $m_i = \mu_i - \frac 16 \sum_{k=1}^6 \mu_k,i=1,\ldots,6$ 
(constrained to $\sum_{i=1}^6 m_i=0$). We also 
take the $R$-charge in UV to be 0.
Considering \rf{PF-6quarks} 
as the partition function for $3d$ $\mathcal{N}=2$ SYM theory one obtains 
a whole series of Seiberg dualities which can be derived from \cite{DSV} 
by taking $N=1$ there. Keeping in mind the coefficient $\mathcal{A}_1$ 
in \rf{PF-6quarks} one sees that the corresponding theory has $8$ more 
singlet chiral fields and the flavor symmetry group is broken to 
$U(1)^5 \times U(1)_A \times U(1)_R$. 

We would also like to remark that the identification of the b-$6j$ symbols
as partition functions works straightforwardly 
only for the b-$6j$ symbol
$\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b^{\rm an}$. The square-roots
appearing in the expression for 
$\big\{\,{}^{\al_1}_{\al_3}\,{}^{\al_2}_{{\al}_4}\,|\,{}^{\al_s}_{\al_t}\big\}_b$ seem to prevent a similar interpretation.
