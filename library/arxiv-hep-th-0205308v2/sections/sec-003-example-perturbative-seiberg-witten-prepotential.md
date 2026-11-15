---
doc_id: arxiv-hep-th-0205308v2
doc_title: "WDVV Equations as Functional Relations"
section_id: sec-003-example-perturbative-seiberg-witten-prepotential
section_title: "Example: perturbative Seiberg-Witten prepotentials"
section_number: null
pages: 7-8
source_pdf: 0205308v2.pdf
source_sha256: 2de5a4f40d80174c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.987
doc_brief: "WDVV Equations as Functional Relations — 6 sections: Front matter; Introduction; WDVV and dispersionless Hirota equ"
---
Here we shall consider one of the simplest examples of solutions to the WDVV equations coming from Seiberg-Witten theory. These are related to $SU(N+1)$ perturbative prepotentials [@MMM] and the corresponding Riemann surface is degenerate. With $a_{ij}\equiv a_i-a_j$ the perturbative prepotential is given by $$\label{pertpre}
{\cal F}= {1\over 2}\sum_{i<j}^N a_{ij}^2\log {a_{ij}\over\Lambda} +
{1\over 2}\sum_{i=1}^N a_i^2\log {a_i\over\Lambda}.$$ The second derivatives ([\[pematr\]](#pematr){reference-type="ref" reference="pematr"}) (for a special choice of $\Lambda$) are $$\label{pemape}
\begin{split}
 T_{ij} &= - \log a_{ij}, \ \ i<j; \qquad T_{ij} =
T_{ji},\ \ i>j;\\  T_{ii} &= \ln a_i+\sum_{i<j} \ln a_{ij}
+\sum_{j<i}\ln a_{ji} = \ln a_i - \sum_{j\ne i} T_{ij}.
\end{split}$$ Using ([\[pemape\]](#pemape){reference-type="ref" reference="pemape"}) one may reexpress all matrix elements $T_{ij}$ through a given row explicitly. For example, in the first nontrivial case corresponding to $SU(4)$ one finds $$\label{pemasu4}
\begin{split}
T &= \left(
\begin{array}{ccc}
  x & y & z \\
  y & \log\left(e^{x+y+z}-e^{-y}\right)\left(e^{-z}-e^{-y}\right)-y &
-\log\left(e^{-z}-e^{-y}\right) \\
  z & -\log\left(e^{-z}-e^{-y}\right) &
\log\left(e^{x+y+z}-e^{-z}\right)\left(e^{-z}-e^{-y}\right)-z
\end{array}\right)
\\
\\
&= \left(
\begin{array}{ccc}
 \log\left(e^{\tilde{x}+\tilde{y}+\tilde{z}}+e^{-\tilde x}\right)
\left(e^{-\tilde x}+e^{-\tilde z}\right)- \tilde{x}
& \tilde{x} & -\log\left(e^{-\tilde x}+e^{-\tilde z}\right) \\
  \tilde{x} & \tilde{y} & \tilde{z} \\
-\log\left(e^{-\tilde x}+e^{-\tilde z}\right)  & \tilde{z} &
\log\left(e^{\tilde{x}+\tilde{y}+\tilde{z}}+e^{-\tilde z}\right)
\left(e^{-\tilde x}+e^{-\tilde z}\right)- \tilde{z}
\end{array}\right)
\\
\\
&= \left(
\begin{array}{ccc}
 \log\left(e^{\hat{x}+\hat{y}+\hat{z}}+e^{-\hat x}\right)
\left(e^{-\hat x}-e^{-\hat y}\right)- \hat{x}
& -\log\left(e^{-\hat x}-e^{-\hat y}\right) & \hat{x} \\
-\log\left(e^{-\hat x}-e^{-\hat y}\right)  &
\log\left(e^{\hat{x}+\hat{y}+\hat{z}}+e^{-\hat y}\right)
\left(e^{-\hat x}-e^{-\hat y}\right)- \hat{y} &
\hat{y} \\
\hat{x} & \hat{y} & \hat{z}
\end{array}\right).
\end{split}$$ Here we have exhibited the different dependence on the rows which are taken as independent variables: $(x,y,z)=(T_{11},T_{12},T_{13})$, $(\tilde{x},\tilde{y},\tilde{z})=(T_{21},T_{22},T_{23})$ and $(\hat{x},\hat{y},\hat{z})=(T_{31},T_{32},T_{33})$.

In the $SU(4)$ perturbative Seiberg-Witten case equation ([\[cocycle\]](#cocycle){reference-type="ref" reference="cocycle"}) has essentially only the one nontrivial relation $$\label{cocsu4}
\sum_{i,k}\
\dfrac{\partial T_{2i}}{\partial T_{1j}}\dfrac{\partial T_{1k}}{\partial T_{3i}}
\dfrac{\partial T_{3l}}{\partial T_{2k}}
= \delta\sp{j} _l.$$ The corresponding matrices may be straightforwardly computed using ([\[pemape\]](#pemape){reference-type="ref" reference="pemape"}). It is easy to check, that ([\[cocsu4\]](#cocsu4){reference-type="ref" reference="cocsu4"}) holds provided the Hirota relations (cf. with [@ZaHi]) are satisfied: $$\label{h1}
{\rm sign}(j-i)e^{-T_{ij}} + {\rm sign}(k-j)e^{-T_{jk}} + {\rm sign}(i-k)e^{-T_{ki}} = 0,
\qquad
i \neq j \neq k,$$ (originating from $a_{ij} + {\rm cyclic}=0$) together with $$\label{h2}
e^{T_{11}+T_{12}+T_{13}-T_{23}} + e^{T_{13}+T_{23}+T_{33}-T_{12}} -
e^{T_{12}+T_{22}+T_{23}-T_{13}} = 0,$$ (coming from $a_ia_{jk} + {\rm cyclic}=0$) and $$\label{h3} e^{T_{12} + T_{22}+T_{23}} - e^{T_{13} + T_{33} +
T_{23}} = e^{-T_{23}}$$ (realizing $a_{ij}=a_i-a_j$). These may be seen to be satisfied upon utilising ([\[pemape\]](#pemape){reference-type="ref" reference="pemape"}).
