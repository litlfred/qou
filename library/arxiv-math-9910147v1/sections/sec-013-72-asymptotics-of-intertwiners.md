---
doc_id: arxiv-math-9910147v1
doc_title: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999"
section_id: sec-013-72-asymptotics-of-intertwiners
section_title: "Asymptotics of Intertwiners"
section_number: 7.2
pages: 28-29
source_pdf: 9910147v1.pdf
source_sha256: 1feefdb019e76ea7
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.986
doc_brief: "arXiv:math/9910147v1 [math.QA] 27 Oct 1999 — We study the tensor product of principal unitary representations of the quantum Lorentz Group, prove a decomposition theorem and compute the associated"
---
Our aim is to compute the behaviour of $\ElemRed{\!\!P+T}{\;\;P}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ (see ([\[form6jprol1\]](#form6jprol1){reference-type="ref" reference="form6jprol1"}) for the explicit expression) for $P=Y_0-Y_1\geq 0, T\rightarrow +\infty.$ The sum on $X_2$ being finite, we can work term by term.\
The asymptotics of $\sixjn{X_1}{X_0}{P+T}{T}{P}{\;\;X_2}{1}$ is very easy to obtain because, after a Racah-Wigner symetry ([\[symcont\]](#symcont){reference-type="ref" reference="symcont"}), the hypergeometric part of the result tends to one when $T$ is large. The behaviour is therefore given by: $$\begin{aligned}
&&\hskip -1cm\sixjn{X_1}{X_0}{P+T}{T}{P}{\;\;X_2}{1}\!\!\sim   
\frac{\varphi_{(X_0+X_2-T,P+X_2-X_1)}\nu_1(2X_2+1)\omega(P;X_1,X_2)}  
{q^{\frac{1}{2}(P-3X_2-X_1-1)(P+X_2-X_1)} \nu_{\infty}(2P+1)\nu_{\infty}(1)}\nonumber  
\end{aligned}$$ The behaviour of $\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}$ requires more attention, but can be achieved using the following computation.

By using first the Sears identity ([\[sears\]](#sears){reference-type="ref" reference="sears"}), and then taking the limit when $T$ goes to infinity, we easily conclude using Heine summation formula ([\[heine\]](#heine){reference-type="ref" reference="heine"}): $$\begin{aligned}
&&\hskip -0.5cm\frac{(Z_1\!+\!Y_0\!-\!X_0\!-\!T\!+\!1)_{\infty}{}_4\Phi_3\!\left[\!\!\begin{array}{cccc} \mbox{\it \small $Z_1\!-\!Z_0-\!$T} &\; \mbox{\it \small $Z_1\!+\!Z_0-\!$T$\;+1$} & \;\;\;\;\;\mbox{\it \small $X_2\!-\!X_0-\!$T} & \;\;\;\mbox{\it \small $-X_2\!-\!X_0\!-\!$T$-\!$1}\\ & \hskip -3.5cm\mbox{\it \small $-\!$2T} & \hskip -3.5cm\mbox{\it \small $\!-\!X_0\!-\!Y_0-\!$T$\;+\!Z_1$} & \hskip -1.8cm \mbox{\it \small $Z_1+Y_0\!-\!X_0\!-\!$T$\;+1$} \end{array} \!\!\right]}  
{(Z_0\!+\!Y_0\!-\!X_0\!+\!1,Y_0\!-\!X_0\!-\!Z_0,2Z_1\!+\!2)_{\infty}}=\nonumber 
\end{aligned}$$ $$\begin{aligned}
&&\hskip 0.5cm = \frac{(2T\!+\!1)_{\infty}{}_4\Phi_3\!\left[\!\!\begin{array}{cccc} \mbox{\it \small $Z_1\!-\!Z_0-\!$T} &\; \mbox{\it \small $Z_1\!+\!Z_0-\!$T$\;+$1} & \;\;\;\;\;\mbox{\it \small $Z_1\!-\!X_2-\!Y_0$} & \;\;\;\mbox{\it \small $X_2\!+\!Z_1\!-\!Y_0\!+\!1$}\\ & \hskip -3.5cm\mbox{\it \small $2Z_1\!+\!2$} & \hskip -3.5cm\mbox{\it \small $\!-\!X_0\!-\!Y_0-\!$T$\;+\!Z_1$} & \hskip -1.8cm \mbox{\it \small $Z_1+X_0\!-\!Y_0\!-\!$T$\;+1$} \end{array} \!\!\right]  
}  
{(T\!+\!Y_0\!-\!Z_1\!-\!X_0,T\!+\!Z_1\!+\!Z_0\!+\!2,Z_1\!+\!T\!-\!Z_0+1  
)_{\infty}}\!\!\nonumber\\  
&&\hskip 1.5cm{\sim}_{{}_{T \rightarrow +\infty}} \;\;{}_2\Phi_1\!\left[\!\!\begin{array}{lll} \mbox{\it \small $Z_1\!-\!X_2-\!Y_0$} & \;\;\;\mbox{\it \small $X_2\!+\!Z_1\!-\!Y_0\!+\!1$} &\\ &  
 \hskip -0.5cm\mbox{\it \small $2Z_1\!+\!2$} & \; ;2Y_0+1\end{array} \right]  
\nonumber\\  
&&\hskip 1.5cm{\sim}_{{}_{T \rightarrow +\infty}} \;\;\frac{(Z_1\!+\!Y_0\!+\!X_2\!+2,Z_1\!+\!Y_0\!-\!X_2\!+1)_{\infty}}{(2Y_0\!+\!1,2Z_1\!+\!2)_{\infty}}.\nonumber  
\end{aligned}$$ This gives us the following behaviour $$\begin{aligned}
&&\hskip -1cm\sixjn{Y_0}{X_0}{Z_0}{T}{Z_1}{X_2}{3}\!\!\!\sim e^{i \pi (T+X_0-X_2)}q^{-2TY_0}\frac{\varphi_{(X_0+X_2-T,-T)}\varphi_{(Z_0+Z_1-T,-T)}\omega(Y_0;X_2,Z_1)\omega(Y_0;X_0,Z_0)}{q^{(Z_1-Z_0)(X_0+Z_0-Y_0)+(X_2-X_0)(Z_1+X_0-Y_0+1)}(1,2Y_0\!+\!1)_{\infty}}\times\nonumber\\  
&&\hskip 1cm\times \frac{\nu_1(2X_2\!+\!1)\nu_1(2Z_0\!+\!1)(Y_0\!-\!X_0\!-\!Z_0,X_0\!+\!Z_0\!-\!Y_0\!+\!1)_{\infty}  
}{\nu_{\infty}(-\!X_0\!-\!X_2)\nu_{\infty}(X_0\!+\!X_2\!+\!1)\nu_{\infty}(-\!Z_0\!-\!Z_1)\nu_{\infty}(Z_0\!+\!Z_1\!+\!1)}\label{asymptotic6j3} 
\end{aligned}$$ The expression of $\sixjn{Z_1}{X_2}{Y_0}{P}{Y_1}{X_1}{3}$ being drastically simplified for $P=Y_0-Y_1,$ there is no problem anymore to obtain the behaviour of the whole expression, except that in order to have a simple answer, we have to take the sum over $X_2.$ Precisely, denoting $\alpha=2X_1\!+\!2Y_1\!-\!2Y_0\!+\!1, \;m=\!2Y_0\!-\!2Y_1\!, \;k=\!Y_0\!-\!Y_1\!+\!X_2\!-\!X_1$ we already have obtained the following behaviour when $T \rightarrow +\infty$ $$\begin{aligned}
&&\hskip -1.2cm\ElemRed{$\!\!\!T\!+\!Y_0\!\!-\!\!Y_1$}{$\!\!Y_0\!\!-\!\!Y_1$}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}  
\!\!{\sim}\;  
q^{-T(Y_0+Y_1)}\;e^{i \pi (\frac{X_0-X_1}{2})}   
q^{-Z_0Z_1}\!\!\times\nonumber\\  
&&\hskip -0.8cm\times \sqrt{\qd{Y_0-Y_1}}\nu_1(2X_1\!+\!1)\nu_1(2Z_0\!+\!1)  
\frac{\varphi_{(2X_0,P\!+\!T\!+\!X_0\!-\!X_1)}\varphi_{(Z_1\!+\!X_1\!-\!Y_1,Z_1\!-\!Z_0\!+\!X_1\!-\!X_0\!+\!Y_0\!-\!Y_1)}}{\varphi_{(Z_0\!+\!Z_1,T)}}  
\times\nonumber\\  
&&\hskip -0.8cm\times \;  
\frac{\nu_{\infty}(Y_0\!+\!X_0\!-\!Z_0\!+\!1)  
\nu_{\infty}(Y_0\!+\!X_0\!+\!Z_0\!+\!2)\nu_{\infty}(Y_0\!-\!X_0\!-\!Z_0)  
\nu_{\infty}(Y_0\!+\!Z_0\!-\!X_0\!+\!1)}{  
q^{\frac{3}{2}X_0^2+\onehalf X_0-\onehalf Z_0^2+\onehalf Z_0}  
(1)_{\infty}  
\nu_{\infty}(2Y_1\!+\!1)\nu_{\infty}(2Y_0\!+\!1)}\times\nonumber\\  
&&\hskip -0.8cm\times \;  
\frac{\nu_{\infty}(Y_1\!+\!X_1\!-\!Z_1\!+\!1)\nu_{\infty}(Y_1\!+\!X_1\!+\!Z_1\!+\!2)  
\nu_{\infty}(Y_1\!-\!X_1\!-\!Z_1)\nu_{\infty}(Y_1\!+\!Z_1\!-\!X_1\!+\!1)}{  
q^{-\frac{3}{2}X_1^2-\onehalf X_1-\onehalf Z_1^2 -\onehalf Z_1}  
\nu_{\infty}(2X_0\!+\!1)  
\nu_{\infty}(-\!2X_0)\nu_{\infty}(Z_0\!+\!Z_1+1)\nu_{\infty}(-\!Z_0\!-\!Z_1)}\times A\label{}  
\end{aligned}$$ where

$A=\frac{1}{(1+\alpha)_m}\sum_{k} \frac{(1-q^{2\alpha+4k})  
(\alpha)_k(-m)_k}{(1-q^{2\alpha})(1)_k(\alpha+m+1)_k} q^{2k^2+2k(m+\alpha)}.$

Using the formula ([\[phi65\]](#phi65){reference-type="ref" reference="phi65"}) and taking in it the limit where $\alpha_1, \alpha_2 \rightarrow -\infty,$ we obtain that $A=1.$ This gives the behaviour of $\ElemRed{$\!\!\!T\!+\!Y_0\!\!-\!\!Y_1$}{$\!\!Y_0\!\!-\!\!Y_1$}{T}{X_0X_1}{Y_0Y_1}{Z_0Z_1}$ when $T$ goes to infinity.
