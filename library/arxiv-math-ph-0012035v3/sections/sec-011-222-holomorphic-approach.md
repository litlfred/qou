---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-011-222-holomorphic-approach
section_title: "Holomorphic approach"
section_number: 2.2.2
pages: 21-28
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.996
latex_coverage_ratio: 0.931
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
#### Quantum-mechanics background

For our further convenience let us formulate an auxiliary "Schrödinger problem" governing the parallel-transport operator [\[par.trans.\]](#par.trans.){reference-type="ref" reference="par.trans."} for the Abelian gauge potential $A$, $$i\frac {d z}{dt }=-\dot{x}^i A_i  z,
    \label{ab.Schr.eq.}$$ which expresses the fact that the "wave function" $z$ should be covariantly constant along the line $L$, i.e. $$D_t   z
\stackrel{\rm def}{=}
 \left( \frac {d}{dt } -i\dot{x}^i A_i
\right)  z =0,$$ where $D_t$ is the absolute covariant derivative.

First of all, let us derive the path-integral expression for the parallel-transport operator $U$ along $L$. To this end, we should consider the non-Abelian formula (differential equation) analogous to Eq.[\[ab.Schr.eq.\]](#ab.Schr.eq.){reference-type="ref" reference="ab.Schr.eq."}, $$i\frac{d z_{k}}{dt }=-\dot{x}^i(t  ) A_i^a
    [x(t )] T^a_{kl} z_l,
    \label{nab.Schr.eq.}$$ or $$(D_t   z)_k
\stackrel{\rm def}{=}
 \left\{\delta_{kl}\frac{d}{dt} -i\dot{x}^i
 A_i^a[x(t)] T^a_{kl}
\right\}  z_l =0,$$ where $z$ is an auxiliary "wave function" in an irreducible representation $R$ of the gauge Lie group $G$, which is to be parallelly transported along $L$ parametrized by $x^i(t  )$, $t  '\le t  \le t  ''$. Formally, Eq.[\[nab.Schr.eq.\]](#nab.Schr.eq.){reference-type="ref" reference="nab.Schr.eq."} can be instantaneously integrated out yielding $$z_k (x'')=U_{kl}(x'',x') z_l (x') ,$$ where $x''=x(t  '')$, $x'=x(t  ')$, and $$U(x'',x')\equiv U(t  '', t  ')=
{\rm P} \exp \left( i\int_{t  '}^{t  ''}
\!\!\dot{x}^i (t  ) A_i[x(t  )]\, dt  \right),$$ as expected.

Let us now consider the following auxiliary classical-mechanics problem with the classical Lagrangian $$L\left(\bar{ z},  z \right)=i \bar{ z} D_t   z.
    \label{clas.L}$$ The equation of motion for $z$ following from Eq.[\[clas.L\]](#clas.L){reference-type="ref" reference="clas.L"} reproduces Eq.[\[nab.Schr.eq.\]](#nab.Schr.eq.){reference-type="ref" reference="nab.Schr.eq."}, and yields the classical Hamiltonian

$$H=i\dot{x}^i(t)A_i^a[x(t)] 
    T_{kl}^a \pi_k  z_l
    =-\dot{x}^i (t)A_i^a[x(t)]T_{kl}^a
    \bar{ z}_k z_l .
    \label{clas.H}$$ The corresponding auxiliary quantum-mechanics problem is given, according to Eq.[\[clas.H\]](#clas.H){reference-type="ref" reference="clas.H"}, by the Schrödinger equation $$i\frac {d}{dt } | \Phi \rangle =\hat{H}(t )|\Phi
    \rangle,
    \label{Schr.eq.}$$ with $$\hat{H}(t)
=-\hat{A}(t)
=-\dot{x}^i (t)A_i^a [x(t)]\hat{T}^a
=-\dot{x}^i(t) A_i^a[x(t)]T_{kl}^a\hat{a}_k^+\hat{a}_l 
\equiv H_{kl}(t  )
\hat{a}_k^+ \hat{a}_l,$$ where the creation and anihilation operators satisfy the standard commutation ($-$) or anticommutation ($+$) relations $$[\hat{a}_k ,\hat{a}_l^+]_{\mp}= \delta_{kl} ,\quad
[\hat{a}_k^+ ,\hat{a}_l^+ ]_{\mp}
=[\hat{a}_k ,\hat{a}_l ]_{\mp} =0 .$$ It can be easily checked by direct computation that we have really obtained a realization of the Lie algebra $\bf g$ in a Hilbert (Fock) space, $$[ \hat{T}^a,\hat{T}^b ]_-
=i f^{abc}\hat{T}^c ,$$ in accordance with [\[Liealg.com.\]](#Liealg.com.){reference-type="ref" reference="Liealg.com."}, where $\hat{T}^a=T_{kl}^a \hat{a}_k^+\hat{a}_l$. For an irreducible representation $R$ the second-order Casimir operator $C_2$ is proportional to the identity operator $I$, which in turn, is equal to the number operator $\hat{N}$ in our Fock representation, i.e. if $T^a\rightarrow \hat{T}^a$, then $I\rightarrow \hat{N} 
=\delta_{kl} \hat{a}_k^+ \hat{a}_l$. Thus, we obtain an important for our further considerations constant of motion $\hat{N}$, $$_- =0 .
    \label{[N,H]}$$ It is interesting to note that this approach works equally well for commutation relations as well as for anticommutation relations.

#### Path integral

Let us now derive the holomorphic path-integral representation for the kernel of the parallel-transport operator, $$\begin{aligned}
    \lefteqn{
    \left<\bar{z}''\left|{\rm P}\exp
    \left[i\int_{t'}^{t''}\!\!\!\hat{A}(t)\,dt\right]
    \right|z'\right>}
    \nonumber\\
    &=&
    \lim_{N\rightarrow\infty}\int\ldots\int\
    \left<\bar{z}_N\left|\left(1
    +i\epsilon \hat{A}_N\right)\right|z_{N-1}\right>
    e^{-\bar{z}_{N-1}z_{N-1}} 
    \frac{d\bar{z}_{N-1}\,dz_{N-1}}{2\pi i}
    \nonumber\\
    &&\quad\left<\bar{z}_{N-1}\left|\left(1
    +i\epsilon \hat{A}_{N-1}\right)\right|z_{N-2}\right>
    e^{-\bar{z}_{N-2}z_{N-2}} 
    \frac{d\bar{z}_{N-2}\,dz_{N-2}}{2\pi i}
    \nonumber\\
    &&\quad\ldots e^{-\bar{z}_1 z_1} 
    \frac{d\bar{z}_1\,dz_1}{2\pi i}
    \left<\bar{z}_1\left|\left(1
    +i\epsilon \hat{A}_1\right)\right|z_0\right>.
    \label{hol.amp.}
    
\end{aligned}$$ Now we should calculate the single expectation value $$\left<\bar{z}_n\left|\left(1
    +i\epsilon \hat{A}_n\right)\right|z_{n-1}\right>
    =\left<\bar{z}_n\left|z_{n-1}\right.\right>
    +i\left<\bar{z}_n\left|\hat{A}_n
    \right|z_{n-1}\right>\epsilon.$$ Here $$\left<\bar{z}_n\left|z_{n-1}\right.\right>
    =e^{\bar{z}_n z_{n-1}},$$ whereas $$\begin{aligned}
    i\left<\bar{z}_n\left|\hat{A}_n
    \right|z_{n-1}\right>\epsilon
    &=&
    i\left<\bar{z}_n\left|\bar{z}_n A_n z_{n-1}
    \right|z_{n-1}\right>\epsilon   \nonumber \\
    &=&
    i\epsilon\bar{z}_n A_n z_{n-1}
    \left<\bar{z}_n\left|\right.z_{n-1}\right>.
    \nonumber
\end{aligned}$$ Thus $$\begin{aligned}
    \left<\bar{z}_n\left|\left(1
    +i\epsilon \hat{A}_n\right)\right|z_{n-1}\right>
    &=&e^{\bar{z}_n z_{n-1}}
    +i\epsilon\bar{z}_n A_n z_{n-1}
    e^{\bar{z}_n z_{n-1}}  \nonumber \\
    &=&
    e^{\bar{z}_n z_{n-1}}\left[1
    +i\epsilon\bar{z}_n A_n z_n
    +O\left(\epsilon^2\right)\right]   \nonumber \\
    &=&
    e^{\bar{z}_n z_{n-1}}
    e^{+i\epsilon\bar{z}_n A_n z_n
    +O\left(\epsilon^2\right)}.
    \nonumber
\end{aligned}$$ Combining this expression with the exponent in [\[hol.amp.\]](#hol.amp.){reference-type="ref" reference="hol.amp."} we obtain $$\begin{aligned}
    e^{-\bar{z}_n z_n} e^{\bar{z}_n z_{n-1}
    +i\epsilon\bar{z}_n A_n z_n
    +O\left(\epsilon^2\right)}
    &=&
    e^{-\bar{z}_n \left(z_n-z_{n-1}\right)
    +i\epsilon\bar{z}_n A_n z_n
    +O\left(\epsilon^2\right)}   \nonumber \\
    &=&
    \exp{\left[\left(-\bar{z}_n \dot{z}_n
    +\epsilon\bar{z}_n A_n z_n\right)\epsilon
    +O\left(\epsilon^2\right)\right]}.\nonumber
\end{aligned}$$ Finally, $$\begin{aligned}
    U(\bar{z}'',z';t'',t')
    &=&
    \left< \bar{z}'' \left| {\rm P} 
    \exp \left[-i\int_{t'}^{t''}\!\!\! 
    \hat{H}(t) dt  \right] \right| z' \right>
    \nonumber
    \\
    &\equiv&
    \left<\bar{z}''\left|{\rm P}\exp
    \left[i\int_{t'}^{t''}\!\!\!\hat{A}(t)\,dt\right]
    \right|z'\right>
    \nonumber
    \\
    &=&
    \int\left[D^2z\right]\exp\left\{\bar{z}(t'')z(t'')
    +i\int_{t'}^{t''}\!\left[i\bar{z}(t)\dot{z}(t)
    \right.\right.
    \nonumber
    \\
    &&\qquad
    \left.\left.
    +\bar{z}(t)A(t)z(t)\right]dt\right\},
    \nonumber
    \\
    &\equiv&
    \int\left[D^2z\right]\exp{\left[\bar{z}(t'')z(t'')
    +i\int_{t'}^{t''}\!\!\!L\,dt\right]},
    \nonumber
\end{aligned}$$ where $$\left[D^2z\right]
    =\prod_{t'<t<t''} \frac{d\bar{z}(t)\,dz(t)}{2\pi i},$$ and $L$ is of "classical" form [\[clas.L\]](#clas.L){reference-type="ref" reference="clas.L"}.

Let us confine our attention to the one-particle subspace of the Fock space. As the number operator $\hat{N}$ is conserved by virtue of Eq.[\[\[N,H\]\]](#[N,H]){reference-type="ref" reference="[N,H]"}, if we start from the one-particle subspace of the Fock space, we shall remain in this subspace during all the evolution. The transition amplitude $U_{kl}(t '',t ')$ between the one-particle states $|1_k\rangle =\hat{a}_k^+ | 0\rangle$ and $| 1_l\rangle = \hat{a}_l^+| 0\rangle$ is given by the following scalar product in the holomorphic representation $$\begin{aligned}
    U_{kl}
    &=&
    \left<1_k\left|{\rm P}\exp  \left[i\int_{t'}^{t''}\!\!\!
    \hat{A}(t)\,dt\right]\right|1_l\right>
    \nonumber \\
    &=&
    \int\left<1_k\left|z''\right.\right>
    \left<\bar{z}''\left|{\rm P}
    \exp{\left[i\int_{t'}^{t''}\hat{A}(t)\,dt\right]}
    \right|z'\right>
    \left<\bar{z}'\left|1_l\right.\right>
    \nonumber \\
    &&\qquad
    e^{-\bar{z}''z''-\bar{z}'z'}
    \frac{d\bar{z}''\,dz''\,d\bar{z}'\,dz'}
    {\left(2\pi i\right)^2} \nonumber  \\
    &=&\int D^2z\,z_k(t'')\bar{z}_l(t')
    \exp{\left[-\bar{z}(t')z(t')
    +i\int_{t'}^{t''}\!\!\!L\,dt\right]},
    \label{hol.par.tr.}
\end{aligned}$$ where now $$D^2z
    =\prod_{t'\leq t\leq t''}
    \frac{d\bar{z}(t)\,dz(t)}{2\pi i}.$$ Depending on the statistics, there are the two ($\mp$) possibilities (fermionic and bosonic) $$z_k\bar{z}_l \mp \bar{z}_l z_k
=\bar{z}_k \bar{z}_l \mp \bar{z}_l \bar{z}_k
=z_k z_l\mp z_l z_k =0 ,$$ equivalent as far as one-particle subspace of the Fock space is concerned, which takes place in our further considerations.

One can easily check that Eq.[\[hol.par.tr.\]](#hol.par.tr.){reference-type="ref" reference="hol.par.tr."} represents the object we are looking for. Namely, from the Schrödinger equation (Eq.[\[Schr.eq.\]](#Schr.eq.){reference-type="ref" reference="Schr.eq."}) it follows that for the general one-particle state $\alpha_k\hat{a}_k^+ | 0\rangle$ (summation after repeating indices) we have $$i\frac{d}{dt} (\alpha_m \hat{a}_m^+| 0\rangle )
    =H_{kl}(t)\hat{a}_k^+ \hat{a}_l \alpha_m \hat{a}_m^+
    | 0\rangle
    =H_{kl}(t  )\alpha_l (\hat{a}_k^+ | 0\rangle ).
    \label{Schr.1p}$$ Using the property of linear independence of Fock-space vectors in Eq.[\[Schr.1p\]](#Schr.1p){reference-type="ref" reference="Schr.1p"}, and comparing Eq.[\[Schr.1p\]](#Schr.1p){reference-type="ref" reference="Schr.1p"} to Eq.[\[nab.Schr.eq.\]](#nab.Schr.eq.){reference-type="ref" reference="nab.Schr.eq."}, we can see that Eq.[\[hol.par.tr.\]](#hol.par.tr.){reference-type="ref" reference="hol.par.tr."} really represents the matrix elements of the parallel-transport operator. For closed paths, $x(t')=x(t'')=x$, Eq.[\[hol.par.tr.\]](#hol.par.tr.){reference-type="ref" reference="hol.par.tr."} gives the holonomy operator $U_{kl}(x)$ and $U_{kk}$ is the Wilson loop. Interestingly enough, the Wilson loop, which is supposed to describe a quark-antiquark interaction, is represented by a "true" quark and antiquark field, $z$ and $\bar{z}$, respectively. So, the mathematical trick can be interpreted "physically".

Obviously, the "full" trace of the kernel in Eq. 3.9 is obtained by imposing appropriate boundary conditions, and integrating with respect to all the variables without the boundary term. Analogously, one can also derive the parallel-transport operator (a generalization of the one just considered) for symmetric $n$-tensors (bosonic $n$-particle states) and for $n$-forms (fermionic $n$-particle states).

#### The non-Abelian Stokes theorem

Let us now define a (bosonic or fermionic) Euclidean two-dimensional "topological" quantum field theory of multicomponent fields $\bar z, z$ transforming in an irreducible representation $R$ of the Lie algebra $\bf g$ on the compact surface $S$, $\mbox{dim} S=2, \partial S=C$, $S\subset M$, $\dim{M}=d$, in an external non-Abelian gauge field $A$, by the classical action $$S_{\rm{cl}}=\int_S \left( iD_i \bar{ z}D_j z +\frac{1}{2}
    \bar{ z} F_{ij} z \right) dx^i\wedge dx^j,
    \qquad i,j=1,\ldots ,d,
    \label{top.act.}$$ or in a parametrization $x^i(\sigma^1,\sigma^2)$, by the action $$\begin{aligned}
    S_{\rm{cl}}
    &=&
    \int_{S}{\cal L}_{\rm{cl}}(\bar{z},z)d^2\sigma
    \label{clas.eL}
    \\
    &=&
    \int_{S} \varepsilon^{AB}
    \left( i D_A\bar{ z} D_B z +\frac{1}{2} \bar{ z}
    F_{AB}z \right) d^2\sigma ,\qquad A,B=1,2,
    \nonumber
\end{aligned}$$ where $$D_A=\partial_A x^iD_i,
\qquad
D_i\stackrel{\rm def}{=}\partial_i-iA_i,
\qquad
F_{AB}=\partial_A x^i
\partial_B x^j F_{ij}.$$

At present, we are prepared to formulate a holomorphic path-integral version of the non-Abelian Stokes theorem, $$\begin{aligned}
    \lefteqn{\int\! D^2z\,z_k''\bar{z}_k' 
    \exp{\left(-\bar{z}'z'
    +i\oint_C i\bar{z}\,Dz\right)}}
    \label{np.hol.NAST}
    \\
    &=&  
    \int D^2z\,z_k''\bar{z}_k'
    \exp{\left(-\bar{z}'z'
    +iS_{\rm cl}\right)},
    \nonumber
    
\end{aligned}$$ or in the polar parametrization $x^i(\sigma^1,\sigma^2)$ $t  '\le \sigma^1 \equiv t  \le t  ''$, $0\le \sigma^2\equiv s\le 1$, $$\begin{aligned}
    \lefteqn{\int D^2z\,z_k(t'')\bar{z}_k(t') 
    \exp{\left\{-\bar{ z}(t') z(t')
    +i\int_{t'}^{t''}\!\!\!L[\bar{z}(t),z(t)]dt 
    \right\}}}
    \label{pp.hol.NAST}
    \\
    &=&  
    \int D^2z\,z_k(t'',1)\bar{z}_k(t',1)
    \exp{\left[-\bar{z}(t',1)z(t',1)
    +i\int_0^1\!\!\!\int_{t'}^{t''}\!\!\!
    {\cal L}_{\rm{cl}}\,dt\,ds\right]},
    \nonumber
    
\end{aligned}$$ where $L(z,\bar{z})$ and ${\cal L}_{\rm{cl}}(\bar{z},z)$ are defined by Eq.[\[clas.L\]](#clas.L){reference-type="ref" reference="clas.L"} and Eq.[\[clas.eL\]](#clas.eL){reference-type="ref" reference="clas.eL"}, respectively. The measure on both sides of Eqs.[\[np.hol.NAST\]](#np.hol.NAST){reference-type="ref" reference="np.hol.NAST"} and [\[pp.hol.NAST\]](#pp.hol.NAST){reference-type="ref" reference="pp.hol.NAST"} is the same, i.e. it is concentrated on the boundary $\partial S$, and the imposed boundary conditions are free.

It should be noted that the surface integral on the RHS of Eqs.[\[np.hol.NAST\]](#np.hol.NAST){reference-type="ref" reference="np.hol.NAST"} and [\[pp.hol.NAST\]](#pp.hol.NAST){reference-type="ref" reference="pp.hol.NAST"} depends on the curvature $F$ as well as on the connection $A$ entering the covariant derivatives, which is reminiscent of the path dependence of the curvature $\cal F$ in the operator approach.

A quite different formulation of the holomorphic approach to the non-Abelian Stokes theorem has been proposed in \[Lun97\].

#### Appendix

For completness of our derivations, we will remind the reader a few standard facts being used above. First of all, we assume the following (non-quite standard, but convinient) definition $$\begin{aligned}
    \left.\left|z\right.\right>
    &\stackrel{\rm def}{=}&
    e^{za^++\bar{z}a+\frac{1}{2}|z|^2}
    \left.\left|0\right.\right>
    =e^{za^+} e^{\bar{z}a} \left.\left|0\right.\right>   \nonumber \\
    &=&e^{za^+} \left.\left|0\right.\right>
    =\sum_{k=0}^\infty \frac{\left(z^na^+\right)^n}{n!}
    \left.\left|0\right.\right>
    =\sum_{k=0}^\infty \frac{z^n}{\sqrt{n!}}
    \left.\left|n\right.\right>,
    \nonumber
\end{aligned}$$ where $\left.\left|0\right.\right>$ is the Fock vacuum, i.e. $\hat{a}\left.\left|0\right.\right>=0$, and the Baker-Campbell-Hausdorff formula has been applied in the first line. We could also treat $\left.\left|z\right.\right>$ as a coherent state for the Heisenberg group. We can easily calculate $$\left<\bar{z}\left|\right.z\right>
    =\sum_{m,n=0}^\infty \frac{\bar{z}^mz^n}{\sqrt{m!\,n!}}
    \left<m\left|\right.n\right>
    =\sum_{n=0}^\infty 
    \frac{\left(\bar{z}z\right)^n}{n!}
    =e^{\bar{z}z}.$$ The identity operator is of the form $$I=\int\left.\left|z\right.\right>
    \left.\left<\bar{z}\right.\right|
    e^{-\bar{z}z} \frac{d\bar{z}\,dz}{2\pi i}.$$ Really, $$\begin{aligned}
    I\left.\left|z'\right.\right>
    &=&\int\left.\left|z\right.\right>
    \left<\left.\bar{z}\right|z'\right>
    e^{-\bar{z}z} \frac{d\bar{z}\,dz}{2\pi i}
    =
    \int\left.\left|z\right.\right>
    e^{\bar{z}z'-\bar{z}z} \frac{d\bar{z}\,dz}{2\pi i}   \nonumber \\
    &=&
    \int\left.\left|z\right.\right>
    \delta(z'-z)\,dz=\left.\left|z'\right.\right>.
    \nonumber   
\end{aligned}$$ All these formulas for a single pair of creation and annihilation operators obviously apply to a more general situation of $\dim{R}$ pairs. The matrix elements are $$\begin{aligned}
    \left<\bar{z}\left|\hat{A}\right|z\right>
    &=&
    \Big<0\Big|e^{\sum_k\bar{z}_k\hat{a}_k}
    \sum_a A^a \sum_{k,l} T_{kl}^a
    \hat{a}_k^+ \hat{a}_l e^{\sum_k z_k\hat{a}_k^+}
    \Big|0\Big>   \nonumber \\
    &=&
    \Big<0\Big|e^{\sum_k\bar{z}_k\hat{a}_k}
    \sum_a A^a \sum_{k,l} T_{kl}^a
    \bar{z}_k z_l e^{\sum_k z_k\hat{a}_k^+}
    \Big|0\Big>   \nonumber \\
    &=&
    \Big<\bar{z}\Big|
    \sum_a A^a \sum_{k,l} T_{kl}^a
    \bar{z}_k z_l \Big|z\Big>   \nonumber \\
    &=&\left<\bar{z}\left|\bar{z}Az\right|z\right>,
    \nonumber
\end{aligned}$$ where we have used the formula $$\left[\hat{a},e^{z\hat{a}^+}\right]_\mp
    =ze^{z\hat{a}^+}.$$ Now $$\begin{aligned}
    \left<1_k\left|\left(1+i\epsilon\hat{A}
    \right)\right|1_l\right>
    &=&
    \delta_{kl}+i\epsilon
    \left<0\left|\hat{a}_k\sum_a A^a \sum_{i,j} T_{ij}^a 
    \hat{a}_i^+ \hat{a}_j \hat{a}_l^+\right|0\right>   \nonumber \\
    &=&
    \delta_{kl}+i\epsilon\sum_a A^a T_{kl}^a
    =(1+i\epsilon A)_{kl}.
    \nonumber
\end{aligned}$$ Also, $$\left<1_k\right|z\left.\right>=z_k.$$
