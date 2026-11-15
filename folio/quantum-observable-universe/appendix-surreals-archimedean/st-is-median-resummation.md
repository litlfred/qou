The standard-part map $\mathrm{st}$
([standard-part functor](#def:standard-part-functor)) and the median
resummation $\mathcal{L}^{\mathrm{med}}$ of
[Écalle–Borel resummation](#def:ecalle-borel-resummation) compute the
same value wherever both are defined. This remark records the
identification once, at block level; elsewhere it appears only in
passing inside the [surreal Kashaev reformulation](#conj:kashaev-surreal).

Concretely: let $\tilde f$ be a Gevrey-1 transseries whose Borel
transform admits lateral Laplace sums along a Stokes ray. The two
lateral sums $\mathcal{L}^{\theta^\pm}\tilde f$ disagree by exponentially
small terms; the median sum $\mathcal{L}^{\mathrm{med}}\tilde f$ is the
unique real single-valued average. On the surreal side, the same
$\tilde f$ is a transseries in the sense of Berarducci–Mantova
\cite{berarducci-mantova2018}, hence evaluates at a positive infinitesimal
(or, for asymptotic-in-$n$ series, at $n = \omega$) to a finite element
of $\mathbf{No}$, and $\mathrm{st}$ projects that element to
$\mathbb{R}$. Selecting the real single-valued representative is
precisely what $\mathrm{st}$ does to the finite surreal value:

$$
  \mathrm{st}\bigl(\tilde f\,\big|_{\,\varepsilon}\bigr)
  \;=\; \mathcal{L}^{\mathrm{med}}\tilde f ,
$$

read as an identity of the two selection rules, not as a new theorem:
each side is the unique real, single-valued value compatible with the
asymptotics of $\tilde f$ (Watson/Nevanlinna–Sokal uniqueness supplies
the analytic half; the valuation quotient
$\mathcal{O}/\mathfrak{m} \cong \mathbb{R}$ supplies the surreal half). A concrete class on which median resummation is proved to exist: for elements of the Habiro ring that arise from partial theta series through strange identities, the Borel transform of the associated series is resurgent, and its median resummation is analytic on $\mathrm{Re}(x) > 0$ with radial limits at the points $\tfrac{1}{2\pi i}\mathbb{Q}$ of its natural boundary \cite[Thm.~1.2]{crew2023}.

Three consequences:

1. **Directionality of the citation graph.** Resurgence-side blocks and
   witnesses (the alien datum, Borel-singularity probes, saddle
   transseries) may cite this result when they take a real value of a
   resummed series; the surreal appendix no longer needs to restate the
   analytic machinery.
2. **The Kashaev application.** In the
   [surreal Kashaev statement](#conj:kashaev-surreal) the map
   $\mathrm{st}$ applied to
   $2\pi \log |J_K(\zeta_\omega, \omega)| / \omega$ is the median
   resummation of the Kashaev transseries at the root of unity — the
   asymptotic-limit content of the volume conjecture in resummation
   form.
3. **Scope.** The identification is language-level: it names one
   operation consistently across the two vocabularies. It does not
   enlarge the class of summable series and does not touch the genuinely
   geometric inputs (hyperbolic volume).
