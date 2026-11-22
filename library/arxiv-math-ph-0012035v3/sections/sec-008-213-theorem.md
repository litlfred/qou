---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action"
section_id: sec-008-213-theorem
section_title: "Theorem"
section_number: 2.1.3
pages: 11-16
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.976
latex_coverage_ratio: 0.976
doc_brief: "Non-Abelian Stokes theorem in action — In this short review main issues related to the non-Abelian Stokes theorem have been addressed."
---
The non-Abelian Stokes theorem in its original operator form roughly claims that the holonomy round a closed curve $C=\partial S$ equals a surface-ordered exponent of the *twisted* curvature, namely $${\rm P}\exp\left(i\oint_C A \right)
        ={\cal P}\exp\left(i\int_S {\cal F}\right),
    \label{op.NAST}$$ where $\cal F$ is the twisted curvature $${\cal F}\equiv U^{-1} F U.$$ A more precise form of the non-Abelian Stokes theorem as well as an exact meaning of the notions appearing in the theorem will be given in the course of the proof.

#### Proof

Following \[Are80\] and \[Men83\] we will present a short, direct proof of the non-Abelian Stokes theorem.

In our parametrization,

the first step consists of the decomposition of the initial loop (see, Fig.[\[fig:bigsq\]](#fig:bigsq){reference-type="ref" reference="fig:bigsq"}) into small lassos according to the rules given in the section [\[SECTION:calculusofPaths\]](#SECTION:calculusofPaths){reference-type="ref" reference="SECTION:calculusofPaths"} $${\rm P}\exp\left(i\oint_C A \right)
    =\lim_{N\rightarrow\infty}({\rm P}_{s,t})\prod_{m,n=1}^N U_{m,n}^{-1} W_{m,n} U_{m,n},$$ where the objects involved are defined as follows: parallel-transport operators from the reference point

($0,0$) to the point with coordinates $(\frac{m}{N},\frac{n}{N})$ consists of two segments (see, Fig.[\[fig:umn\]](#fig:umn){reference-type="ref" reference="fig:umn"}) $$U_{m,n}
    \stackrel{\rm def}{=}
    {\rm P}\exp\left(i\int_{(0,\frac{n}{N})}^
    {(\frac{m}{N},\frac{n}{N})}A\right)
    {\rm P}\exp\left(i\int_{(0,0)}^
    {(0,\frac{n}{N})}A\right),$$ parallel-transport operator round a small plaquette $S_{m,n}$

$$W_{m,n}
    \stackrel{\rm def}{=}
        {\rm Tr\,P}\exp\left(i\oint_{S_{m,n}} A \right),$$ where $S_{m,n}$ is a boundary of a (small) square with coordinates $$S_{m,n}:\quad\left\{
\left(\frac{m}{N},\frac{n}{N}\right), 
\left(\frac{m-1}{N},\frac{n}{N}\right), 
\left(\frac{m-1}{N},\frac{n-1}{N}\right), 
\left(\frac{m}{N},\frac{n-1}{N}\right) 
\right\}.$$ Now $$\begin{aligned}
    U_{m,n}^{-1} W_{m,n} U_{m,n}
    &=& U_{m,n}^{-1} \left[1+\frac{i}{N^2}F_{m,n}
    +O\left(\frac{1}{N^3}\right)\right] U_{m,n}    
    \nonumber \\
    &=& 1+\frac{i}{N^2} U_{m,n}^{-1} F_{m,n} U_{m,n}     
    +O\left(\frac{1}{N^3}\right)       
    \nonumber \\
    &=& 1+\frac{i}{N^2}{\cal F}_{m,n}
    +O\left(\frac{1}{N^3}\right)   
    \nonumber \\
    &=& {\cal W}_{m,n}+O\left(\frac{1}{N^3}\right),
\nonumber
\end{aligned}$$ where $W_{m,n}$ has been calculated in the Appendix to this section (see, Eq.[\[Wmn\]](#Wmn){reference-type="ref" reference="Wmn"}), $${\cal F}_{m,n}
    \stackrel{\rm def}{=}
     U_{m,n}^{-1} F_{m,n} U_{m,n},$$ and $${\cal W}_{m,n}
    \stackrel{\rm def}{=}
    \exp\left(\frac{i}{N^2}{\cal F}_{m,n}\right).$$ Then $$\begin{aligned}
    {\rm P}\exp\left(i\oint_C A \right)
    &=&
    \lim_{N\rightarrow\infty}({\rm P}_{s,t})\prod_{m,n=1}^N
    \left[{\cal W}_{m,n}+O\left(\frac{1}{N^3}\right)\right]
    \nonumber \\
    &=&
    \lim_{N\rightarrow\infty}({\rm P}_{s,t})\prod_{m,n=1}^N
    \exp\left[\frac{i}{N^2}{\cal F}_{m,n}
    +O\left(\frac{1}{N^3}\right)\right]\nonumber \\
    &=&
    \lim_{N\rightarrow\infty}({\rm P}_t)\prod_{m,n=1}^N
    \exp\left[\frac{i}{N^2}{\cal F}_{m,n}
    +O\left(\frac{1}{N^3}\right)\right].
    \nonumber
\end{aligned}$$ The last equality follows from the fact that operations corresponding to the change of the order of the operators yield the commutator $$\left[\frac{1}{N^2}{\cal F}_{m',n'},
    \frac{1}{N^2}{\cal F}_{m'',n''}\right]
    =O\left(\frac{1}{N^4}\right),$$ and there is maximum $N-1$ transpositions possible in the framework of $s$-ordering, so $$(N-1)\,O\left(\frac{1}{N^4}\right)
    =O\left(\frac{1}{N^3}\right).$$ Thus, we arive at the final form of the non-Abelian Stokes theorem, $${\rm P}\exp\left(i\oint_C A \right)
    =\lim_{N\rightarrow\infty}({\rm P}_t)\prod_{m,n=1}^N
    \exp\left[\frac{i}{N^2}{\cal F}_{m,n}\right]
    ={\cal P}\exp\left(i\int_S {\cal F}\right).$$

#### Appendix

In this paragraph we will perform a fairly standard calculus and derive the contribution coming from a small loop $W_{m,n}$. Namely, $$\begin{aligned}
        W_{m,n}
            &=&
            {\rm P}\exp\left(i\int
_{\left(\frac{m}{N},\frac{n-1}{N}\right)}
^{\left(\frac{m}{N},\frac{n}{N}\right)}
        A\right)
        
        {\rm P}\exp\left(i\int
_{\left(\frac{m-1}{N},\frac{n-1}{N}\right)}
^{\left(\frac{m}{N},\frac{n-1}{N}\right)}
        A\right)
        \nonumber
        \\
        &&\quad{\rm P}\exp\left(i\int
_{\left(\frac{m}{N},\frac{n-1}{N}\right)}
^{\left(\frac{m-1}{N},\frac{n-1}{N}\right)}
        A\right)
        
        {\rm P}\exp\left(i\int
_{\left(\frac{m}{N},\frac{n}{N}\right)}
^{\left(\frac{m}{N},\frac{n-1}{N}\right)}
        A\right)\nonumber\\          
    &=&
    \left[1+\frac{i}{N}A_{m,n}^y
    +\frac{1}{2}\left(\frac{i}{N}A_{m,n}^y\right)^2
    +O\left(\frac{1}{N^3}\right)\right]
    \nonumber\\
    &&\quad 
    \cdot\left[1+\frac{i}{N}A_{m,n-1}^x
    +\frac{1}{2}\left(\frac{i}{N}A_{m,n-1}^x\right)^2
    +O\left(\frac{1}{N^3}\right)\right]
    \nonumber\\
    &&\quad 
    \cdot\left[1-\frac{i}{N}A_{m-1,n}^y
    +\frac{1}{2}\left(\frac{i}{N}A_{m-1,n}^y\right)^2
    +O\left(\frac{1}{N^3}\right)\right]
    \nonumber\\
    &&\quad     
    \cdot\left[1-\frac{i}{N}A_{m,n}^x
    +\frac{1}{2}\left(\frac{i}{N}A_{m,n}^x\right)^2
    +O\left(\frac{1}{N^3}\right)\right] 
    \nonumber\\
    &=& 
    1+\frac{i}{N}\left(A_{m,n}^y - A_{m-1,n}^y\right)
    -\frac{i}{N}\left(A_{m,n}^x - A_{m,n-1}^x\right)
    \nonumber\\
    &&\quad
    +\left(\frac{i}{N}\right)^2 \left(A_{m,n}^y\right)^2
    +\left(\frac{i}{N}\right)^2 \left(A_{m,n}^x\right)^2
    +\left(\frac{i}{N}\right)^2 A_{m,n}^y A_{m,n}^x
    \nonumber\\
    &&\quad
    -\left(\frac{i}{N}\right)^2 \left(A_{m,n}^y\right)^2
    -\left(\frac{i}{N}\right)^2 A_{m,n}^y A_{m,n}^x
    -\left(\frac{i}{N}\right)^2 A_{m,n}^x A_{m,n}^y\nonumber\\
    &&\quad 
    -\left(\frac{i}{N}\right)^2 \left(A_{m,n}^x\right)^2
    +\left(-\frac{i}{N}\right)^2 A_{m,n}^y A_{m,n}^x
    +O\left(\frac{1}{N^3}\right)\nonumber\\
    &=&
    1+\frac{i}{N^2}\left(\partial_xA^y-\partial_yA^x\right)
    -\frac{i^2}{N^2}\left(A^xA^y-A^yA^x\right)
    +O\left(\frac{1}{N^3}\right)\nonumber\\
    &=&
    1+\frac{i}{N^2}F_{m,n}
    +O\left(\frac{1}{N^3}\right),\label{Wmn}
            
\end{aligned}$$ where $$F=\partial_xA_y-\partial_yA_x-i\left[A_x,A_y\right]$$ (ocassionally, we put $x$ and $y$ in the upper position), and $$A=A_{m,n}+O\left(\frac{1}{N}\right).$$ Then $$W_{m,n}=\exp\left[\frac{i}{N^2}F_{m,n}
    +O\left(\frac{1}{N^3}\right)\right].$$

#### Other approaches

There is a lot of other approaches to the (operator) non-Abelian Stokes theorem, more or less interrelated. The analytic approach advocated in \[Bra80\] and \[HM98\]. The approach using the, so-called, product integration \[KMR99\] and \[KMR00\]. And last, but not least, a (very interesting) coordinate-gauge approach \[SS98\], and \[Hal79\] as well as its lattice formulation \[Bat82\].
