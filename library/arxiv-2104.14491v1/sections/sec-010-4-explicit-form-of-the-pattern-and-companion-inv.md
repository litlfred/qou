---
doc_id: arxiv-2104.14491v1
doc_title: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Mo"
section_id: sec-010-4-explicit-form-of-the-pattern-and-companion-inv
section_title: "Explicit form of the pattern and companion invariants"
section_number: 4
pages: 8-9
source_pdf: 2104.14491v1.pdf
source_sha256: 1aea658f17283df1
doc_brief: "Khovanov polynomials for satellites and asymptotic adjoint polynomials A. Anokhinaa,∗ A. Morozova,b,c,† A. Popolitova,b,c,‡ a Institute for Theoretical and Experimental Physics, Moscow 117218, Russia"
text_source: latex
latex_prose_ratio: 0.788
latex_coverage_ratio: 0.931
---
Now we give an explicit form of the two basic ingredients in PPCD formulae from sec.[\[sec:PPCD\]](#sec:PPCD){reference-type="ref" reference="sec:PPCD"}. First, we describe the pattern invariant in sec.[\[sec:patt-pol\]](#sec:patt-pol){reference-type="ref" reference="sec:patt-pol"}. In fact, we recall the well known Khovanov polynomials of the two-strand torus and twist knots, bringing the expressions to a proper form. In next sec.[\[sec:AAK-rolf\]](#sec:AAK-rolf){reference-type="ref" reference="sec:AAK-rolf"},[\[sec:AAK-tor\]](#sec:AAK-tor){reference-type="ref" reference="sec:AAK-tor"},[\[sec:AAK-tw\]](#sec:AAK-tw){reference-type="ref" reference="sec:AAK-tw"}, we present the explicit expressions for the companion invariants extracted from PPCD. We call them an asymptotic adjoint Khovanov (AAK) polynomials, since we believe them to be "tails" of the true adjoint Khovanov polynomials that survive in the satellite polynomials. Although the exact relation of the two quantities is not yet established, the AAK may be interesting in itself, as an explicitly defined and readily computable Khovanov-like knot invariant.

## The pattern-defining polynomial[]{#sec:patt-pol label="sec:patt-pol"}

By definition, the $k$ in our $\mathcal{S}_{\mathtt{Tw}_k}$ and $\mathcal{S}_{\mathtt{Tor}_k}$, as well as in ([\[ppcd-tw-sat\]](#ppcd-tw-sat){reference-type="ref" reference="ppcd-tw-sat"},[\[ppcd-tor-sat\]](#ppcd-tor-sat){reference-type="ref" reference="ppcd-tor-sat"},[\[ppcd-u-tor-sat\]](#ppcd-u-tor-sat){reference-type="ref" reference="ppcd-u-tor-sat"}) is a satellite invariant independent of the companion knot. Hence $k$ and thus the knot $\mathtt{Tw}_k$ or $\mathtt{Tor}_k$ defines the pattern of the satellite (see sec.[\[sec:sat\]](#sec:sat){reference-type="ref" reference="sec:sat"}). The first term in the PPCD decomposition is just the respective Khovanov polynomial. Namely, the reduced polynomial for the twist knot is $$\begin{aligned}
\mathtt{Kh}^{\mathtt{Tw}_k}&=&-(-t)^{\Theta_{k}}\left(q^2t\right)^{-k-2}\!\cdot\!
\Bigg(1+q^2t\!\cdot\!\frac{\left(1+q^4t^2\right)\left(1-(q^2t)^{k-1}\right)}{1-q^2t}
\Bigg)\label{Kh-tw}\\\nonumber
&=&
(-t)^{\Theta_{k}}\left(q^2t\right)^{-k}\!\cdot\!
\Bigg(1+\left(q^2t\right)^{k-2}\!\cdot\!\frac{\left(1+q^4t^2\right)\left(1-(q^2t)^{-k}\right)}{1-q^2t}
\Bigg)=\\
&=&
(-t)^{\Theta_k}(q^2t)^{-2}\Bigg(\cfrac{1+q^4t^2}{1-q^2t}-(q^2t)^{-k}\cfrac{1+q^6t^3}{1-q^2t}
\Bigg),
\nonumber
\end{aligned}$$ while the reduced polynomial for the torus knot is $$\begin{aligned}
\mathtt{Kh}^{\mathtt{Tor}_k}&=&
-(-t)^{\Theta_{k}}t^{-1}q^{k-1}\Bigg(1+\left(q^2t\right)^2\!\cdot\!\frac{1-(q^2t)^{k-1}}{1-q^2t}
\Bigg)\label{Kh-tor}\\\nonumber&=&
(-t)^{\Theta_{k}}q^{k+1}\Bigg(1+\left(q^2t\right)^k\cdot\!\frac{1-(q^2t)^{-k-1}}{1-q^2t}
\Bigg)=\\
&=&(-t)^{\Theta_k}q(q^3t)^k\Bigg(\cfrac{1}{1-q^2t}-(q^2t)^{-k-1}\cfrac{1+q^6t^3}{1-q^4t^2}\Bigg),
\nonumber
\end{aligned}$$ and the unreduced polynomial for the torus knot is $$\begin{aligned}
{{}_u\mathtt{Kh}}^{\mathtt{Tor}_k}&=&
q^k\!\cdot\!\Bigg\{1-(-t)^{\Theta_{k}}\Bigg(\frac{1}{q^2t}+q^2t\!\cdot\!\frac{\left(1+q^4t\right)\left(1-(q^2t)^{k-1}\right)}{1-q^4t^2}\Bigg)\Bigg\}=\\&=&
q^k\!\cdot\!\Bigg\{1+(-t)^{\Theta_{k}}\Bigg(q^2+\left(q^2t\right)^k\!\cdot\!\frac{\left(1+q^4t\right)\left(1-(q^2t)^{-k-1}\right)}{1-q^4t^2}\Bigg)\Bigg\}.\nonumber
\end{aligned}$$ We give several equivalent expressions in all cases. The first and the second expressions for each of the polynomials are manifestly positive for $n>0$, and $n<0$, respectively. The third expression for each of the reduced polynomials is useful to rewrite our PPCD formulae ([\[ppcd-tor-sat\]](#ppcd-tor-sat){reference-type="ref" reference="ppcd-tor-sat"},[\[ppcd-tw-sat\]](#ppcd-tw-sat){reference-type="ref" reference="ppcd-tw-sat"}) like ([\[tor-cab-top\]](#tor-cab-top){reference-type="ref" reference="tor-cab-top"},[\[tw-cab-top\]](#tw-cab-top){reference-type="ref" reference="tw-cab-top"}) and ([\[Jcab\]](#Jcab){reference-type="ref" reference="Jcab"}).

## AAK for the simplest prime knots[]{#sec:AAK-rolf label="sec:AAK-rolf"}

We studied decompositions ([\[ppcd-tw-sat\]](#ppcd-tw-sat){reference-type="ref" reference="ppcd-tw-sat"}) for the simplest prime knots up to $8_9$. Below we present the explicit expressions for the corresponding AAK of the prime knots with no more than 6 crossings. $$\begin{aligned}
\begin{array}{cp{16cm}}
\mathcal{K}&${\mathfrak{K}}^{\mathcal{K}}(q,t)$\\
3_1&$1/q^2+1/(q^{10}t^5)+1/(q^8t^4)+t^2+q^4t^4$\\[2mm]
4_1&$1+1/q^2+1/(q^{12}t^7)+1/(q^{10}t^6)+1/(q^6t^3)+2/(q^4t^2)+1/(q^2t)+1/(q^4t)+2t+q^2t^2+q^6t^5+q^8t^6$\\[2mm]
5_1&$1/q^2+1/(q^{14}t^7)+1/(q^{12}t^6)+1/(q^{10}t^5)+1/(q^8t^4)+1/(q^8t^3)+1/(q^6t^2)+t/q^2+2t^2+q^4t^4+q^6t^6+q^8t^8+q^{12}t^{10}$\\[2mm]
5_2&$2/q^2+1/q^4+1/(q^{22}t^{13})+1/(q^{20}t^{12})+1/(q^{16}t^9)+2/(q^{14}t^8)+1/(q^{12}t^7)+1/(q^{14}t^7)+2/(q^{12}t^6)+2/(q^{10}t^5)+2/(q^8t^4)+1/(q^6t^3)+2/(q^6t^2)+3/(q^4t)+t+2t^2+q^2t^3+q^4t^4$
\\[2mm]
6_1&$1+2/q^2+1/(q^8t^3)+q^6t^5+q^2t^3+q^4t^4+2q^2t^2+1/(q^{24}t^{15})+1/(q^{22}t^{14})+1/(q^{18}t^{11})+2/(q^{16}t^{10})+1/(q^{14}t^9)+3/(q^4t)+1/(q^2t)+4/(q^6t^3)+1/(q^6t^2)+4/(q^4t^2)+q^8t^6+2/(q^{10}t^6)+1/(q^8t^5)+1/(q^{16}t^9)+2/(q^{14}t^8)+2/(q^{12}t^7)+1/(q^{10}t^5)+3/(q^8t^4)+3t$\\[2mm]
6_2&$1+5/q^2+2q^{10}t^8+3q^8t^7+2q^6t^5+q^6t^6+q^4t^5+4q^2t^3+5q^4t^4+2q^2t^2+q^{16}t^{12}+q^{14}t^{11}+5/(q^4t)+1/(q^2t)+4/(q^6t^3)+2/(q^6t^2)+3/(q^4t^2)+2q^8t^6+1/(q^{10}t^6)+1/(q^{12}t^6)+1/(q^{16}t^9)+2/(q^{14}t^8)+2/(q^{12}t^7)+3/(q^{10}t^5)+4/(q^8t^4)+2t^2+4t$\\[2mm]
6_3&$2+t^2+6q^2t^2+5q^6t^5+3q^8t^6+8/(q^4t^2)+q^2t^3+1/(q^{14}t^8)+2/(q^{16}t^{10})+q^{10}t^8+q^{14}t^{10}+q^{10}t^7+q^6t^4+1/(q^6t^4)+4q^4t^3+1/(q^4t^3)+2q^{12}t^9+5/(q^{10}t^6)+4/(q^8t^4)+3/(q^{12}t^7)+1/(q^{10}t^5)+6/(q^6t^3)+5/(q^2t)+2/(q^4t)+1/(q^{18}t^{11})+1/(q^{14}t^9)+4/(q^8t^5)+8t+5/q^2+4q^4t^4$
\end{array}
\label{RolfAAK}
\end{aligned}$$ The coloured Jones polynomials of the simplest knots are tabulated [@knbook] (see App.[\[app:data\]](#app:data){reference-type="ref" reference="app:data"}), and one can verify property ([\[AAKJcol\]](#AAKJcol){reference-type="ref" reference="AAKJcol"}). Namely, $$\begin{aligned}
\widehat{\mathtt{Kh}}^{\mathcal{K}}_k(q,t=-1)=
\left(-q^2\right)^{-\mathtt{Sh}_{\mathcal{K}}}\Big(1-\left(1-q^4\right){\mathfrak{K}}^{\mathcal{K}}(q,t=-1)\Big)=J_2(q),\label{AAKJcol}
\end{aligned}$$
