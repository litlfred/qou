---
doc_id: arxiv-1107.1559v1
doc_title: "Quaternion-Octonion SU (3) Flavor Symmetry"
section_id: sec-001-2-quaternionic-representation-of-isospin-su2-gro
section_title: "Quaternionic representation of isospin SU(2) group"
section_number: 2
pages: 2-7
source_pdf: 1107.1559.pdf
source_sha256: 90d63f2e18629b9d
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.956
---
Let us consider the standard Lie algebra in terms of the quaternions
by adopting the basic formula of the isotopic formalism for nucleons.
Accordingly we may write a spinors $\psi_{a}$ and $\psi_{b}$ as\begin{eqnarray}
\psi & = & \left(\begin{array}{c}
\psi_{a}\\
\psi_{b}\end{array}\right);\label{eq:1}\end{eqnarray}
whereas the adjoint spinor is described as

\begin{eqnarray}
\overline{\psi} & = & \left(\begin{array}{cc}
\overline{\psi_{a}} & \overline{\psi}_{b}\end{array}\right);\label{eq:2}\end{eqnarray}
where 

\begin{align}
\psi=( & \psi_{0}+e_{1}\psi_{1})+e_{2}(\psi_{2}-e_{1}\psi_{3})=\psi_{a}+e_{2}\psi_{b}.\label{eq:3}\end{align}
In equations (\ref{eq:1}) and (\ref{eq:2}), $\psi_{a}=(\psi_{0}+e_{1}\psi_{1})$
and $\psi_{b}=(\psi_{2}-e_{1}\psi_{3})$ are considered over the field
of a quaternion described in terms of the four dimensional representations
of real numbers and two dimensional representations of complex numbers.
Accordingly, under $SU(2)$ gauge symmetry, the quaternion spinor
transforms as \cite{key-15,key-16},

\begin{eqnarray}
\psi & \longmapsto\psi^{\shortmid}= & U\,\psi\label{eq:4}\end{eqnarray}
where $U$ is $2\times2$ unitary matrix and satisfies 

\begin{eqnarray}
U^{\dagger}U & =UU^{\dagger}=UU^{-1}=U^{-1}U= & 1.\label{eq:5}\end{eqnarray}
On the other hand, the quaternion conjugate spinor transforms as \begin{eqnarray}
\overline{\psi}\longmapsto\overline{\psi^{\shortmid}} & = & \overline{\psi}U^{-1}.\label{eq:6}\end{eqnarray}
Hence, the combination $\psi\overline{\psi}=\overline{\psi}\psi=\psi\overline{\psi^{\shortmid}}=\overline{\psi^{\shortmid}}\psi$
is an invariant quantity. So, any unitary matrix may then be written
as 

\begin{eqnarray}
U & = & \exp\left(i\,\hat{H}\right);\label{eq:7}\end{eqnarray}
where $\widehat{H}$ is Hermitian $\widehat{H}^{\dagger}=\widehat{H}$.
Thus, we may express the Hermitian $2\times2$ matrix in terms of
four real numbers, $a_{1},\, a_{2},\, a_{3},$ and $\theta$ as 

\begin{eqnarray}
\hat{H} & = & \theta\hat{1}+\tau_{j}a_{j}=\theta1+ie_{j}a_{j};\label{eq:8}\end{eqnarray}
where $\hat{1}$ is the $2\times2$ unit matrix, $\tau_{j}$ are well
known $2\times2$ Pauli - spin matrices and $e_{1},\, e_{2},\, e_{3}$
are the quaternion units related to Pauli - spin matrices as \begin{eqnarray}
e_{0}= & 1;\,\,\,\,\, & e_{j}=-i\tau_{j}.\label{eq:9}\end{eqnarray}
Here $e_{j}$ $\left(\forall\, j=1,2,3\right)$, the basis elements
of quaternion algebra, satisfy the following multiplication rule

\begin{eqnarray}
e_{j}e_{k}=-\delta_{jk}+ & \epsilon_{jkl} & e_{l}\,\,(\forall j,k,l=1,2,3).\label{eq:10}\end{eqnarray}
where $\delta_{jk}$ and $\epsilon_{jkl}$ are respectively known
as usual Kronecker delta and three index Levi - Civita symbols respectively.
We may now describe the $SU(2)$ isospin in terms of quaternions as

\begin{align}
I_{a}= & \frac{ie_{a}}{2}\,\,\,(\forall\, a=1,2,3)\label{eq:11}\end{align}
and

\begin{align}
I_{\pm}= & \frac{i}{2}\left(e_{1}\pm ie_{2}\right).\label{eq:12}\end{align}
So, we may write the quaternion basis elements in terms of $SU(2)$
isospin as

\begin{align}
e_{1}=\frac{1}{i}\left(I_{+}+I_{-}\right);\,\,\,\,\,\,\, e_{2}=\frac{1}{i}\left(I_{+}-I_{-}\right);\,\,\,\,\,\,\, & e_{3}=\frac{1}{i}\left(I_{3}\right);\label{eq:13}\end{align}
which satisfy the following commutation relation

\begin{align}
\left[I_{+},I_{-}\right]=ie_{3};\,\,\,\quad & \left[I_{3},I_{\pm}\right]=\pm\frac{i}{2}\left(e_{1}\pm ie_{2}\right).\label{eq:14}\end{align}
 Here $SU(2)$ group acts upon the fundamental representation of $SU(2)$
doublets of up $\left(u\right)$ and down$\left(d\right)$ quark spinors 

\begin{align}
\left|u\right\rangle =\left(\begin{array}{c}
1\\
0\end{array}\right);\,\,\,\,\,\,\,\, & \left|d\right\rangle =\left(\begin{array}{c}
0\\
1\end{array}\right).\label{eq:15}\end{align}
So, we get for up quarks 

\begin{align}
I_{+}\left|u\right\rangle = & \frac{i\left(e_{1}+ie_{2}\right)}{2}\left|u\right\rangle =0;\,\,\,\,\,\,\, I_{-}\left|u\right\rangle =\frac{i\left(e_{1}-ie_{2}\right)}{2}\left|u\right\rangle =\frac{1}{2}\left|d\right\rangle ;\,\,\,\,\,\, I_{3}\left|u\right\rangle =\frac{ie_{3}}{2}\left|u\right\rangle =\frac{1}{2}u\left|u\right\rangle ;\label{eq:16}\end{align}
and for down quarks we have\begin{align}
I_{+}\left|d\right\rangle =\frac{i\left(e_{1}+ie_{2}\right)}{2}\left|d\right\rangle =\frac{1}{2}\left|u\right\rangle ;\,\,\,\,\, I_{-}\left|d\right\rangle =\frac{i\left(e_{1}-ie_{2}\right)}{2}\left|d\right\rangle =0;\,\,\,\,\,\,\, & I_{3}\left|d\right\rangle =\frac{ie_{3}}{2}\left|d\right\rangle =-\frac{1}{2}\left|d\right\rangle .\label{eq:17}\end{align}
Conjugates of equations$\left(\ref{eq:16}\right)$ and $\left(\ref{eq:17}\right)$
are now be described as

\begin{align}
\left\langle d\right|I_{+}=\left\langle d\right|\frac{i\left(e_{1}+ie_{2}\right)}{2}=0;\,\,\,\,\,\,\, & \left\langle d\right|I_{-}=\left\langle d\right|\frac{i\left(e_{1}-ie_{2}\right)}{2}=\frac{1}{2}\left\langle u\right|;\,\,\,\,\,\,\,\left\langle d\right|I=\left\langle d\right|\frac{ie_{3}}{2}=\frac{1}{2}\left\langle d\right|;\label{eq:18}\end{align}
and\begin{align}
\left\langle u\right|I_{+}=\left\langle u\right|\frac{i\left(e_{1}+ie_{2}\right)}{2}=\frac{1}{2}\left\langle d\right|;\,\,\,\,\,\,\left\langle u\right|I_{-}=\left\langle u\right|\frac{i\left(e_{1}-ie_{2}\right)}{2}=0;\,\,\,\:\,\,\,\, & \left\langle u\right|I_{3}=\left\langle u\right|\frac{ie_{3}}{2}=\frac{1}{2}\left\langle u\right|;\label{eq:19}\end{align}
where $e_{1}$, $e_{2}$ and $e_{3}$ are defined in $\left(\ref{eq:11}\right)$and
$\left(\ref{eq:12}\right).$ The effect of quaternion operator on
up $\left|u\right\rangle $ and down $\left|d\right\rangle $ quarks
states leads to

\begin{align}
ie_{1}\left|u\right\rangle =\left|d\right\rangle ;\,\,\,\,\,\,\, & ie_{1}\left|d\right\rangle =\left|u\right\rangle ;\nonumber \\
e_{2}\left|u\right\rangle =\left|d\right\rangle ;\,\,\,\,\,\,\, & e_{2}\left|d\right\rangle =-\left|u\right\rangle \nonumber \\
ie_{3}\left|u\right\rangle =\left|u\right\rangle ;\,\,\,\,\,\,\, & ie_{3}\left|d\right\rangle =-\left|d\right\rangle .\label{eq:20}\end{align}
So, we may write

\begin{align}
e_{1}\left(\begin{array}{c}
u\\
d\end{array}\right)= & i\left(\begin{array}{c}
u\\
d\end{array}\right);\label{eq:21}\end{align}


\begin{align}
e_{2}\left(\begin{array}{c}
u\\
d\end{array}\right)= & \left(\begin{array}{c}
d\\
-u\end{array}\right);\label{eq:22}\end{align}
\begin{align}
e_{3}\left(\begin{array}{c}
u\\
d\end{array}\right)= & i\left(\begin{array}{c}
u\\
-d\end{array}\right);\label{eq:23}\end{align}
transform a neutron (down quark) state into a proton ( up quark) state
or vice versa. Only $e_{2}$ gives real doublets of up and down quarks.



\section{Octonions and Gelmann $\lambda$ Matrices}

Octonions describe the widest normed algebra after the algebra of
real numbers, complex numbers and quaternions. The octonions are non
associative and non commutative normed division algebra over the algebra
of real numbers. A set of octets $(e_{0},\, e_{1},\, e_{2},\, e_{3},\, e_{4},\, e_{5},\, e_{6},\, e_{7})$
are known as the octonion basis elements and satisfy the following
multiplication rules

\begin{align}
e_{0}=1;\,\, e_{0}e_{A}=e_{A}e_{0}= & e_{A};\nonumber \\
e_{A}e_{B}=-\delta_{AB}e_{0}+f_{ABC}e_{C}.\,\,(\forall\, A,\, B,\, C=1,\,2,.....,\,7) & .\label{eq:24}\end{align}
The structure constants $f_{ABC}$ is completely antisymmetric and
takes the value $\mbox{\ensuremath{1}}$ for the following combinations,

\begin{eqnarray}
f_{ABC} & = & +1;\nonumber \\
\forall & (ABC) & =(123),\,(471),\,(257),\,(165),\,(624),\,(543),\,(736).\label{eq:25}\end{eqnarray}
The relation between Gell - Mann $\lambda$ matrices and octonion
units are given as \cite{key-15}

\begin{equation}
\frac{\left[e_{a+3},\, e_{7}\right]}{\left[\lambda_{a+3},\,\lambda_{7}\right]}=\frac{e_{a}}{2i\lambda_{a}};\label{eq:26}\end{equation}


\begin{equation}
\frac{\left[e_{7},\, e_{a}\right]}{\left[\lambda_{7},\,\lambda_{a}\right]}=\frac{e_{a+3}}{2i\lambda_{a+3}};\label{eq:27}\end{equation}


\begin{equation}
\frac{\left[e_{a},\, e_{a+3}\right]}{\left[\lambda_{a},\,\lambda_{a+3}\right]}=\frac{e_{7}}{2i\lambda_{7}};\label{eq:28}\end{equation}
where $a=1,\,2,\,3$. So, we have may describe \cite{key-15} the
following relationship between Gell - Mann $\lambda$ matrices and
octonion units as , 

\begin{align}
\lambda_{1}=-ie_{1}\, k_{1};\,\lambda_{2}=-ie_{2}\, k_{2};\,\lambda_{3}=-ie_{3}\, k_{3}; & \,\lambda_{4}=-ie_{4\,}k_{4};\nonumber \\
\lambda_{5}=-ie_{5\,}k_{5};\,\lambda_{6}=-ie_{6\,}k_{6}; & \,\lambda_{7}=-ie_{7}\, k_{7};\label{eq:29}\end{align}
and $\lambda_{8}$ are also related with $e_{3}$ as

\begin{equation}
\lambda_{8}=-ik_{8}e_{3}\,\,\, where\,\,\, k_{8}=\frac{8}{\sqrt{3}};\label{eq:30}\end{equation}
where $k_{a}=-1\,\,\,(\forall a=1,2,3,.....,7)$ are proportionality
constants.
