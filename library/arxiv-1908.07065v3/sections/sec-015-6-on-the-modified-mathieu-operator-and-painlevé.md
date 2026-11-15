---
doc_id: arxiv-1908.07065v3
doc_title: "Non-perturbative approaches to the quantum Seiberg–Witten curve"
section_id: sec-015-6-on-the-modified-mathieu-operator-and-painlevé
section_title: "On the modified Mathieu operator and Painlevé III3"
section_number: 6
pages: 36-37
source_pdf: 1908.07065v3.pdf
source_sha256: c43e413aed71aef1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.914
latex_coverage_ratio: 0.991
doc_brief: "Non-perturbative approaches to the quantum Seiberg–Witten curve — We study various non-perturbative approaches to the quantization of the Seiberg– Witten curve of N = 2, SU(2) super Yang–Mills"
---
\label{mathieu-painleve}

It was observed by many authors \cite{Lukyanov:2011wd, PCL, nok} that
the movable poles of Painlev\'e $\rm III_3$ are somehow related to
Mathieu functions. In particular in \cite{ sciarappa2}, based on
\cite{bgt}, it was observed that the zeros of the Painlev\'e
$\rm III_3$ $\tau$ function compute the spectrum of modified Mathieu
(with a suitable dictionary).  From the view point of the TS/ST
correspondence \cite{ghm} this connection comes naturally since both
systems arise as limiting cases of this duality.  In particular, the
modified Mathieu operator arises in the standard geometric engineering
limit \cite{hm,gm17,gm3}, while Painlev\'e $\rm III_3$ arises in the
dual geometric engineering limit considered in \cite{bgt}.


In this section we prove the connection between the zeros of the Painlev\'e $\rm III_3$ $\tau$ function and the spectrum of the modified Mathieu operator by using \cite{ggu}. 
From the CFT perspective this is a connection between Liouville conformal blocks at $c=1$ and $c=\infty$. We proceed as follows. 
First we  write the Painlev\'e $\rm III_3$ $\tau$ function as \cite{gil,ilt,Gavrylenko:2017lqz}

\be
 \label{GIL} \tau(\Lambda, a, \eta, \hbar)= \sum_{n \in \IZ}  \re^{4 \pi \ri n \eta} \exp\left(F^{\rm SD}(a+2\ri\hbar n, \hbar, \Lambda)\right)
 \ee
 
where

\be
\ba  \exp\left(F^{\rm SD}(a, \hbar, \Lambda)\right)= &\left(\frac{\Lambda }{\hbar }\right)^{-\frac{  a^2}{\hbar ^2}} {1 \over  G(1-\ri \frac{a}{\hbar })G(1+\ri \frac{a}{\hbar })}\\
&\times \left(1 -\frac{2\Lambda ^4}{ a^2 \hbar ^2}+\frac{\Lambda ^8 \left(2 a^2 -\hbar ^2\right)}{ a^2 \hbar ^2 \left( a^2+\hbar ^2\right)^2}+\mathcal{O}(\Lambda^{12})\right)\ea
\ee

is the so-called four dimensional Nekrasov partition function in the selfdual $\Omega$ background \cite{n} (namely, the equivariant parameters are $\epsilon_1=-\epsilon_2=\hbar$).

The parameters $(a, \eta)$ in \eqref{GIL} play the role of initial conditions while $\Lambda$ is the time.
We are interested in the case in which 

\be \eta=0.
\ee  

We now recall the result of
\cite{ggu}, where it was demonstrated that, in the NS limit, the
Nakajima--Yoshioka blowup equations for $SU(2)$ pure SYM
\cite{ny1,naga,nagalect} can be written as\footnote{Strictly speaking this
  is the four-dimensional limit of \cite{ggu}. This type of
  expressions first appeared in \cite{swh} as compatibility conditions
  between the exact quantization conditions of \cite{ghm,cgm} and
  those of \cite{wzh,fhm,hm}. A different connection between blowup and Painlev\'e equations was used in \cite{bes, Bershtein:2018zcz,ntalkbu} to prove the so-called Kiev formula \cite{gil,ilte} or its q-deformed version \cite{bsu, jns-qp}.
  }

\be\label{comp}
		\sum_{n\in\mathbb{Z} }
		\exp\left(\ri n  \pi+{F}^{\rm SD}\left(a+ 2\ri\hbar n+\ri\hbar, \hbar, \Lambda\right)
		 -2 \ri n\hbar^{-1}\frac{\partial }{\partial a}{F}_{\text{NS}}\left(a,\hbar\right)\right)=0.
\ee

Finally, we use the quantization condition for the modified Mathieu operator in the NS form (\ref{eqref}). It then follows from \eqref{comp} that, if a value of 
$a$ satisfies this exact quantization condition, one finds a vanishing condition for the tau function of
Painlev\'e $\rm III_3$, namely

\be\label{tau0}
 \tau\left(\Lambda, a+{\ri \hbar}, 0, \hbar \right)=\sum_{n\in\mathbb{Z} }
		\exp\left({F}^{\rm SD}\left(a+ 2\ri\hbar n+\ri\hbar, \hbar, \Lambda\right) \right)=0.\ee

Notice that we think of \eqref{eqref} and \eqref{tau0} as quantization conditions for the variable $a$. In order to obtain the spectrum of modified Mathieu one has to use the quantum Matone relation \eqref{mmap}.
