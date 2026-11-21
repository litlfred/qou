---
doc_id: arxiv-1205.4619v1
doc_title: "Quaternion-Octonion Unitary Symmetries and Analogous Casimir Operators"
section_id: sec-002-3-quaternions-and-dirac-spinors
section_title: "Quaternions and Dirac spinors"
section_number: 3
pages: 6-7
source_pdf: 1205.4619v1.pdf
source_sha256: 8c76e30a52dca571
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.984
doc_brief: "Quaternion-Octonion Unitary Symmetries and Analogous Casimir Operators — An attempt has been made to investigate the global SU(2) and SU(3) unitary ﬂavor symmetries systematically in terms of"
---
Let us define the free particle quaternion Dirac equation \cite{key-26}
for a particle of mass $m$ as 

\begin{align}
\left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi= & 0.\label{eq:26}
\end{align}
Here, we used the following quaternion valued Weyl representation
of $\gamma$ matrices as it is convenient for ultra relativistic problems
i.e

\begin{align}
\gamma^{0}=\left[\begin{array}{cc}
0 & e_{0}\\
e_{0} & 0
\end{array}\right],\equiv\left[\begin{array}{cc}
0 & \hat{1}_{2}\\
\hat{1}_{2} & 0
\end{array}\right],\,\,\,\,\,\, & \gamma^{j}=\left[\begin{array}{cc}
0 & -ie_{j}\\
ie_{j} & 0
\end{array}\right]\equiv\left[\begin{array}{cc}
0 & \tau^{j}\\
-\tau^{j} & 0
\end{array}\right](\forall j=1,2,3).\label{eq:27}
\end{align}
In Weyl representation, we have $\left(\gamma^{0}\right)^{\dagger}=\gamma^{0}$,
$\left(\gamma^{j}\right)^{\dagger}=-\gamma^{j}$ and $\left\{ \text{\textgreek{g}}^{\mu},\,\text{\textgreek{g}}^{\nu}\right\} =\text{\textgreek{g}}^{\mu}\text{\textgreek{g}}^{\nu}+\gamma^{\nu}\gamma^{\mu}=0\,(\forall\mu,\nu=0,1,2,3)$.
Rather, at sufficiently low energies \cite{key-27} the effect of
weak interactions dies away and the dominant contribution appears
due to the presence of electromagnetic and the strong interactions
both of which are Parity conserving interactions. So, we use the simplest
representation that closes under Parity $\mathbb{\hat{P}}$ for Dirac
spinor field $\psi$ in equation (\ref{eq:26}) as,

\begin{align}
\psi= & \left(\begin{array}{c}
\psi_{L}\\
\psi_{R}
\end{array}\right)\cong(\frac{1}{2},\,0)\,\oplus(0,\,\frac{1}{2})\label{eq:28}
\end{align}
where $(\frac{1}{2},\,0)$ and $(0,\,\frac{1}{2})$ are the simplest
representations of the Lorentz group $SL(2,C)$ so that an object
transforming in the $(\frac{1}{2},\,0)$ representation is called
a left-chiral $\psi_{L}$ Weyl spinor. Similarly, an object transforming
in the $(0,\,\frac{1}{2})$ representation of Lorentz group $SL(2,C)$,
is called a right-chiral Weyl spinor $\psi_{R}$. It is to be noted
that the meaning assigned to the technical word 'chiral' (or so called
chirality means handedness)) is associated with the matrix $\lyxmathsym{\textgreek{g}}^{5}$
which anti-commutes with all Dirac matrices (\ref{eq:27}) i.e.

\begin{align}
\left\{ \lyxmathsym{\textgreek{g}}^{5}\,,\,\lyxmathsym{\textgreek{g}}^{\mu}\right\} = & \text{\textgreek{g}}^{5}\lyxmathsym{\textgreek{g}}^{\mu}+\gamma^{\mu}\gamma^{5}=0\,\,(\forall\mu=0,1,2,3).\label{eq:29}
\end{align}
So, from the anti-commutation relation $\left\{ \text{\textgreek{g}}^{\mu},\,\lyxmathsym{\textgreek{g}}^{\nu}\right\} =\text{\textgreek{g}}^{\mu}\text{\textgreek{g}}^{\nu}+\gamma^{\nu}\gamma^{\mu}=0\,(\forall\mu,\nu=0,1,2,3)$
between the $\lyxmathsym{\textgreek{g}}$matrices (\ref{eq:27}),
it can be easily seen that the matrix

\begin{align}
\gamma^{5}=i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3} & =\left(\begin{array}{cc}
-e_{0} & 0\\
0 & e_{0}
\end{array}\right)\equiv\left(\begin{array}{cc}
-\widehat{1}_{2} & 0\\
0 & \hat{1}_{2}
\end{array}\right)\label{eq:30}
\end{align}
satisfi{}es Eq. (\ref{eq:29}) along with the following properties

\begin{align}
\left(\gamma^{5}\right)^{\dagger}=\gamma^{5};\,\,\,\,\,\,\, & \left(\gamma^{5}\right)^{2}=\hat{1}_{2}\equiv1.\label{eq:31}
\end{align}
As such, we may define the \textquotedblleft{}left-handed\textquotedblright{}
and \textquotedblleft{}right-handed\textquotedblright{} projection
operators (which are generally used as the terms \textquotedblleft{}left-chiral\textquotedblright{}
and \textquotedblleft{}right-chiral\textquotedblright{}) as

\begin{align}
\widehat{P}_{L}=\frac{1}{2}\left(1-\gamma^{5}\right);\,\,\,\,\,\,\,\, & \widehat{P}_{R}=\frac{1}{2}\left(1+\gamma^{5}\right);\label{eq:32}
\end{align}
which shows that the operators $\widehat{P}_{L/R}$ project onto the
left/right-chiral Weyl spinor as

\begin{align}
\widehat{P}_{L}\psi=\frac{1}{2}\left(1-\gamma^{5}\right)\psi=\left(\begin{array}{c}
\psi_{L}\\
0
\end{array}\right)\equiv\psi_{L};\,\,\,\,\,\,\,\, & \widehat{P}_{R}\psi=\frac{1}{2}\left(1+\gamma^{5}\right)\psi=\left(\begin{array}{c}
0\\
\psi_{R}
\end{array}\right)\equiv\psi_{R}.\label{eq:33}
\end{align}
Thus, we may write the suitable Dirac Lagrangian for left-right chiral
spinors as,

\begin{align}
\mathcal{L}_{D}= & \psi_{L}^{\dagger}\overline{e_{\mu}}\partial_{\mu}\psi_{L}+\psi_{R}^{\dagger}\overline{e_{\mu}}\partial_{\mu}\psi_{R}-m\left(\psi_{L}^{\dagger}\psi_{R}+\psi_{R}^{\dagger}\psi_{L}\right);\label{eq:34}
\end{align}
where $\mu=0,1,2,3.$ Here, the Euler-Lagrange equations are obtained
on considering $\psi_{L}$ and $\psi_{L}^{\star}$ independent (since
they are complex fields) and similarly for $\psi_{R}$, $\psi_{R}^{\star}$.
Then, performing the variations with respect to $\psi_{L}^{\star}$
and $\psi_{R}^{\star}$, we get that the Dirac equation (\ref{eq:26})
is equivalent to the pair of equations

\begin{align}
\overline{e_{\mu}}\partial_{\mu}\psi_{L}= & m\psi_{R};\nonumber \\
\overline{e_{\mu}}\partial_{\mu}\psi_{R}= & m\psi_{L}.\label{eq:35}
\end{align}
These two pairs of equations decouple for the $m=0$ (i.e for zero
mass) particles like neutrinos. We may also write the Lagrangian in
a compact form for which it is convenient to define the Dirac adjoint
spinor as $\overline{\psi}=\psi^{\dagger}\gamma^{0}\equiv\left(\psi_{R}^{\dagger},\psi_{L}^{\dagger}\right)$
in chiral representation. hence, the compact and consistent form of
the Dirac Lagrangian may be written as,

\begin{align}
L_{D}= & \overline{\psi}\left(i\gamma^{\mu}\partial_{\mu}-m\right)\psi.\label{eq:36}
\end{align}
