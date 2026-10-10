---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
text_source: latex
latex_prose_ratio: 0.975
latex_coverage_ratio: 0.977
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
One of the most fruitful applications of supersymmetry to geometry is the possibility to define and compute enumerative invariants 
based on the counting of BPS states. This idea goes back to Witten's index \cite{witten-index} and has led to many important developments, 
like the Gopakumar--Vafa invariants of Calabi--Yau threefolds \cite{gv} or the DGG index of three-dimensional 
manifolds \cite{dgg-index}. More recently, through the study of their wall-crossing properties \cite{KS-wall}, 
it has been understood that BPS invariants can be formulated in a more analytic framework, based e.g. on the 
solution to a Riemann--Hilbert problem \cite{cecotti-vafa, gmn}, and closely related to WKB analysis \cite{gmn2}. A general mathematical construction 
encapsulating this idea has been put forward in \cite{bridgeland}, in which a given set of BPS invariants (or ``BPS structure") is reformulated 
in terms of a Riemann--Hilbert problem. 

In \cite{mm-s2019,grassi-gm, ggm1,ggm2} it has been advocated that the connection between BPS invariants and analytic
 problems can be formulated more generally by using the theory of resurgence (see \cite{ks-analytic} for similar ideas). 
 In this approach, the starting analytic data are 
 asymptotic, perturbative series obtained in an 
appropriate quantum theory. Under some mild assumptions, the theory 
of resurgence associates to these series a set of complex numbers called Stokes constants. It turns out that, in some cases, 
the Stokes constants are integers which can be interpreted in terms of BPS counting. 

Two important examples of this situation have been considered so far. The first and simpler example arises in the counting of 
BPS states in 4d, $\CN=2$ supersymmetric gauge theories. In this case, 
the appropriate quantum theory is obtained by putting the $\CN=2$ theory in the Nekrasov--Shatashvili (NS) limit \cite{ns} of the 
Omega-background \cite{n}. This is equivalent to quantizing the Seiberg--Witten curve \cite{mirmor}. The asymptotic series obtained in this way are 
called quantum periods, and, as shown in \cite{grassi-gm}, the corresponding Stokes constants 
are essentially the BPS invariants studied with the WKB method in \cite{gmn2}. 

Another example is provided by complex Chern--Simons (CS) theory on the complement of a hyperbolic knot. 
In this case, the asymptotic series are defined by saddle-point expansions of the quantum invariants around classical solutions, 
and lead to a very rich resurgent structure. By combining different 
techniques, the Stokes constants associated to these series could be determined numerically in \cite{ggm1,ggm2}, and 
then conjectured analytically in closed form in many examples. Surprisingly, these Stokes constants are integers, and they turn out to be 
closely related to the DGG index of the three-manifold. In both types of examples ($\CN=2$ theories and complex CS theory), the Stokes 
constants are associated to singularities in the Borel plane which form infinite towers. In \cite{ggm1,ggm2} we called these arrangements, 
leading to infinitely many integer invariants, ``peacock patterns."

In this paper we use these ideas to introduce new invariants for
topological string theory on a Calabi--Yau threefold. In this case one
has to address an additional difficulty which is not present in the
previous examples. The natural series appearing in topological string
theory are asymptotic expansions in the string coupling constant, but
their coefficients are highly non-trivial functions of the moduli of
the Calabi--Yau threefold. We then have to face a problem of
``parametric" resurgence, similar to what happens when one studies
resurgence in the large $N$ expansion of gauge theories (see
e.g. \cite{mmlargen}). In this case, the coefficients of the series in
$1/N$ are non-trivial functions of the 't Hooft parameter. This
observation suggests that a more manageable problem can be found if
one considers, in topological string theory, the analogue of working
at finite, fixed $N$ in gauge theory. From the point of view of the
gauge/string duality, this means working in the small radius regime,
or tensionless limit of string theory. In topological string theory,
this corresponds to an expansion around the {\it conifold} point.

Folllowing this logic, the invariants we define are based on
perturbative series in a single parameter, obtained by ``quantizing"
the CY moduli near the conifold point. For example, in the case of a
CY with a single modulus, we obtain in this way an infinite family of
perturbative series $\Phi_N(g_s)$, labeled by an integer
$N=1,2, \cdots$. One should think about $N$ as the rank of the gauge
group in a large $N$ duality (in general, each CY modulus gives an
integer label).  The resulting asymptotic series lead to peacock
patterns, and by applying the theory of resurgence, we associate to
them a (generally infinite) set of Stokes constants, which we
conjecture to be integers.

Let us note that, in contrast to the usual Gopakumar--Vafa invariants, 
which can be obtained by rearranging the perturbative topological string expansion at large radius, the invariants we 
define are intrinsically non-perturbative. They encode information about the large order behavior of the perturbative series and 
about non-perturbative sectors which are invisible in conventional perturbation theory. 

Once these invariants are defined, one should ask whether they can be effectively computed, 
and what is their interpretation. We show in this paper that, in the case 
of {\it toric} CY manifolds, the invariants can be calculated efficiently in many cases, and in some examples 
one can even obtain conjectural 
expressions for them in terms of $q$-series. This is done by appealing to the TS/ST correspondence, which is a 
conjectural equivalence between topological string theory on toric CY threefolds and spectral theory.  
The TS/ST correspondence was formulated in the form we need here in \cite{ghm,cgm}, 
based on previous insights in \cite{mp,hmo2,hmo3,hmmo,km,hw}. It provides in particular 
a non-perturbative definition of the perturbative series $\Phi_N(g_s)$ in terms of the spectral trace $Z_N(g_s)$ of a trace class operator. 
We stress that our definition of the integer invariants only involves the resurgent structure of the asymptotic series and 
does {\it not} depend on the existence of a non-perturbative 
definition for them. However, the existence of the analytic functions $Z_N(g_s)$ makes the task of computing the invariants much easier.  

In the toric case, the structure we unveil has many similarities to complex CS theory on hyperbolic knot complements. 
In this theory, for each complex gauge group and each hyperbolic knot 
one obtains a collection of perturbative series, associated to different flat complex connections in the complement of the knot. The 
non-perturbative object underlying these series is the state integral, or Andersen--Kashaev invariant \cite{hikami, dglz, ak}. The counterpart of these 
invariants in the topological string are precisely the spectral traces appearing in the TS/ST correspondence. However, and in contrast to CS theory, the conventional topological 
string theory provides a {\it single} perturbative series. A resurgent analysis, like the one we will perform in this paper, 
unveils additional asymptotic series which are invisible in perturbation theory, and should be regarded as the ``hidden" sectors of topological string theory (a similar resurgent analysis of topological string theory, albeit with very different tools, was performed in \cite{cesv1,cesv2}). The set of asymptotic series obtained in this way in the topological string should correspond to the collection of series appearing in complex CS theory.  


The analogy with complex CS theory and the 3d/3d correspondence \cite{DGG1} is a good starting point to address the geometric and 
physical interpretation of the integer invariants we define. It suggests that there should be some sort of field theory dual to 
topological string theory, in which the integer invariants we define have a direct enumerative meaning. Another route to interpret our invariants 
is the rich structure of BPS/DT invariants of the underlying CY threefold. The results of \cite{bridgeland} and the work on 
exponential networks in \cite{esw,blr1,blr2, blr3, longhi} suggests that one could use 
resurgent tools to compute these invariants, and we believe that the invariants we define here are simpler versions of the full 
BPS/DT invariants of the CY. These analogies are however not fully precise, and more work is needed to obtain a direct BPS interpretation of our invariants. 

The paper is organized as follows. In section \ref{sec-definition} we define the new integer invariants as Stokes constants of appropriate 
series arising in topological string theory, and we provide the necessary background from the theory of resurgence. In section \ref{sec-ex}, after 
a short summary of the TS/ST correspondence of \cite{ghm,cgm}, we perform detailed analysis and computations in two well-known examples of toric CY threefolds: local $\IP^2$ and local $\IF_0$. In section \ref{sec-conclude} we conclude and list various problems opened by this investigation. 
There are three Appendices. The first one summarizes properties of Faddeev's quantum dilogarithm and of $q$-series which we use repeatedly in the paper. The second one explains how to obtain efficiently one of the relevant perturbative series in local $\IP^2$. Finally, the third Appendix summarizes the Hunter--Guerrieri algorithm, which makes it possible to extract trans-series from the large order behavior of a Gevrey-1 
series in the oscillatory case, where usual Richardson extrapolation cannot be applied.
